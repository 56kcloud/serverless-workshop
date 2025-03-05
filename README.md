![Test Suite](https://github.com/56kcloud/serverless-workshop/workflows/test/badge.svg)
[![GitHub Super-Linter](https://github.com/56kcloud/serverless-workshop/actions/workflows/linter.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![Code Coverage](https://codecov.io/gh/56kcloud/serverless-workshop/branch/main/graph/badge.svg?token=aoWqkGkVXX)](https://codecov.io/gh/56kcloud/serverless-workshop)

# Serverless Workshop Infrastructure

## Overview

This repository contains the infrastructure for the Serverless Workshop.

## Prerequisites

Ensure that your development environment is set up with the following tools:

- [Docker](https://docs.docker.com/get-docker/)
- [Node.js 22](https://nodejs.org/en/download/)
- [Python 3.9](https://www.python.org/downloads/)
- [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)
- [AWS Command Line Interface](https://aws.amazon.com/cli/)

In addition to these, your system must be properly configured with AWS credentials, possessing necessary permissions to deploy the service. For a seamless AWS credential management experience, we recommend using [aws-vault](https://github.com/99designs/aws-vault).

### Setup the local development environment

Start by cloning this repository:

    $ git clone git@github.com:56kcloud/serverless-workshop.git

Create a virtual Python envrionement and install dependencies:

    $ cd serverless-workshop
    $ python3.9 -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements-dev.txt


### Testing

Run Python tests:

    $ python -m pytest -v test.py --cov=stacks --cov-report=html


## Deployment


**Bootstrapping**

To deploy AWS CDK apps into an AWS [environment](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html), you will need to provision the necessary resources.

```bash
aws-vault exec shared-services-full-access -- cdk bootstrap
```

### Live Infrastructure Deployment

Please note that the deployment process is automatically triggered via a Github action when `serverless-workshop` is pushed.
