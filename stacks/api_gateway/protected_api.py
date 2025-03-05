import json

from aws_cdk import (
    aws_apigateway as apigw,
    aws_logs as logs,
    Stack,
)
from constructs import Construct

from stacks import ressource_id


class ProtectedApiStack(Stack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        api_stack,
        **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        log_group = logs.LogGroup(
            self,
            ressource_id('LambdaEndpointLogGroup'),
            log_group_name=f'{scope.team}-api-gateway',
        )

        log_format = apigw.AccessLogFormat.custom(
            json.dumps({
                'time': apigw.AccessLogField.context_request_time(),
                'request_id': apigw.AccessLogField.context_request_id(),
                'source_ip': apigw.AccessLogField.context_identity_source_ip(),
                'user_agent': apigw.AccessLogField.context_identity_user_agent(),
                'http_method': apigw.AccessLogField.context_http_method(),
                'protocol': apigw.AccessLogField.context_protocol(),
                'domain_name': apigw.AccessLogField.context_domain_name(),
                'path': apigw.AccessLogField.context_path(),
                'status': apigw.AccessLogField.context_status(),
                'latency': apigw.AccessLogField.context_response_latency(),
                'payload_length': apigw.AccessLogField.context_response_length()
            })
        )

        deploy_options = apigw.StageOptions(
            access_log_destination=apigw.LogGroupLogDestination(log_group),
            access_log_format=log_format,
            stage_name=scope.stage,
            tracing_enabled=True
        )

        self.api_gateway = apigw.LambdaRestApi(
            self,
            ressource_id('LambdaEndpoint'),
            cloud_watch_role=True,
            default_cors_preflight_options=apigw.CorsOptions(
                allow_credentials=True,
                allow_headers=[
                    '*'
                ],
                allow_methods=[
                    '*'
                ],
                allow_origins=[
                    '*'
                ],
                expose_headers=[
                    '*'
                ]
            ),
            disable_execute_api_endpoint=False,
            deploy_options=deploy_options,
            handler=api_stack.lambda_api,
            rest_api_name=f'{scope.team}-lambda-endpoint'
        )

        apigw.GatewayResponse(
            self,
            ressource_id('ProtectedApiDefault5XXApiGatewayResponse'),
            rest_api=self.api_gateway,
            type=apigw.ResponseType.DEFAULT_5_XX,
            response_headers={
                'Access-Control-Allow-Origin': "'*'",
                'Access-Control-Allow-Methods': "'*'",
                'Access-Control-Allow-Headers': "'*'"
            },
        )

        apigw.GatewayResponse(
            self,
            ressource_id('ProtectedApiDefault4XXApiGatewayResponse'),
            rest_api=self.api_gateway,
            type=apigw.ResponseType.DEFAULT_4_XX,
            response_headers={
                'Access-Control-Allow-Origin': "'*'",
                'Access-Control-Allow-Methods': "'*'",
                'Access-Control-Allow-Headers': "'*'"
            },
        )
