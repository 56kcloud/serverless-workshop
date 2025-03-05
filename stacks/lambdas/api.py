from aws_cdk import (
    aws_lambda as lambda_,
    Stack,
    Duration
)

from constructs import Construct

from stacks import ressource_id


class ApiStack(Stack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        self.lambda_api = lambda_.Function(
            self,
            ressource_id('ApiFunction'),
            code=lambda_.Code.from_asset('lambdas/api'),
            handler='handler.handle',
            function_name=f'{scope.team}-api',
            runtime=lambda_.Runtime.PYTHON_3_9,
            environment={
                'TEAM': scope.team
            },
            memory_size=256,
            timeout=Duration.seconds(30),
            tracing=lambda_.Tracing.ACTIVE
        )
