from os import environ

import aws_cdk as cdk

from stacks import ressource_id
from stacks.lambdas.api import ApiStack
from stacks.api_gateway.protected_api import ProtectedApiStack
from stacks.oidc_provider import OidcProviderStack


env = cdk.Environment(
    region='eu-central-2' # Zurich
)

app = cdk.App()

app.stage = environ.get('STAGE', 'dev')
app.team = environ.get('TEAM', 'alpha')

if app.team == 'main':
    OidcProviderStack(
        app,
        ressource_id('OidcProviderStack'),
        env=env
    )

api_stack = ApiStack(
    app,
    ressource_id('ApiStack'),
    env=env
)

protected_api_stack = ProtectedApiStack(
    app,
    ressource_id('ProtectedApiStack'),
    api_stack=api_stack,
    env=env
)

app.synth()
