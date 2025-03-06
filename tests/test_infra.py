from os import environ

import pytest

import aws_cdk as cdk
from aws_cdk.assertions import Template

from stacks import ressource_id
from stacks.lambdas.api import ApiStack
from stacks.api_gateway.protected_api import ProtectedApiStack
from stacks.oidc_provider import OidcProviderStack


@pytest.fixture(autouse=True)
def environment():
    environ['TEAM'] = 'main'
    environ['STAGE'] = 'test'

@pytest.fixture
def env():
    return cdk.Environment(region='eu-central-2')

@pytest.fixture
def app():
    app = cdk.App(context={'stage': 'test'})
    app.stage = environ['STAGE']
    app.team = environ['TEAM']
    return app


@pytest.fixture
def api_stack(app, env):
    return ApiStack(
        app,
        ressource_id('ApiStack'),
        env=env
    )


@pytest.fixture
def protected_api_stack(app, env, api_stack):
    return ProtectedApiStack(
        app,
        ressource_id('ProtectedApiStack'),
        api_stack=api_stack,
        env=env
    )


@pytest.fixture
def oidc_provider_stack(app, env):
    return OidcProviderStack(
        app,
        ressource_id('OidcProviderStack'),
        env=env
    )


def test_api_stack(app, api_stack):
    template = Template.from_stack(api_stack)

    r = {
        'FunctionName': f'{app.team}-api',
        'MemorySize': 256,
        'Runtime': 'python',
        'TracingConfig': {
            'Mode': 'Active'
        }
    }
    template.has_resource_properties('AWS::Lambda::Function', r)


def test_protected_api_stack(app, protected_api_stack):
    template = Template.from_stack(protected_api_stack)

    r = {
        'LogGroupName': f'{app.team}-api-gateway',
    }
    template.has_resource_properties('AWS::Logs::LogGroup', r)

    r = {
        'DisableExecuteApiEndpoint': False,
        'Name': f'{app.team}-lambda-endpoint'
    }
    template.has_resource_properties('AWS::ApiGateway::RestApi', r)

    r = {
        'StageName': app.stage
    }
    template.has_resource_properties('AWS::ApiGateway::Stage', r)

    r = {
        'ResponseType': 'DEFAULT_5XX'
    }
    template.has_resource_properties('AWS::ApiGateway::GatewayResponse', r)

    r = {
        'ResponseType': 'DEFAULT_4XX'
    }
    template.has_resource_properties('AWS::ApiGateway::GatewayResponse', r)


def test_oidc_provider_stack(app, oidc_provider_stack):
    template = Template.from_stack(oidc_provider_stack)

    r = {
        'Url': 'https://token.actions.githubusercontent.com',
        'ClientIDList': ['sts.amazonaws.com']
    }
    template.has_resource_properties('Custom::AWSCDKOpenIdConnectProvider', r)
