from aws_cdk import (
    aws_iam as iam,
    Stack,
    Duration,
)
from constructs import Construct

class OidcProviderStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.oidc_provider = iam.OpenIdConnectProvider(
            self,
            "GitHubOIDCProvider",
            url="https://token.actions.githubusercontent.com",
            client_ids=["sts.amazonaws.com"],
        )

        self.role = iam.Role(
            self,
            "GitHubActionsRole",
            role_name="GitHubActionsRole",
            assumed_by=iam.WebIdentityPrincipal(
                identity_provider=self.oidc_provider.open_id_connect_provider_arn,
                conditions={
                    "StringLike": {
                        "token.actions.githubusercontent.com:sub": "repo:56kcloud/serverless-workshop:*"
                    }
                }
            ),
            max_session_duration=Duration.hours(1),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess")
            ]
        )
