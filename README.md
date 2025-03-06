![Test Suite](https://github.com/56kcloud/serverless-workshop/workflows/test/badge.svg)
[![GitHub Super-Linter](https://github.com/56kcloud/serverless-workshop/actions/workflows/linter.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![Code Coverage](https://codecov.io/gh/56kcloud/serverless-workshop/branch/main/graph/badge.svg?token=aoWqkGkVXX)](https://codecov.io/gh/56kcloud/serverless-workshop)

# Serverless Workshop Infrastructure

## Overview

This repository contains the infrastructure for the Serverless Workshop, which aims to provide a hands-on experience with serverless architecture using AWS services. The project utilizes AWS CDK (Cloud Development Kit) to define cloud infrastructure as code.

## Prerequisites

Ensure that your development environment is set up with the following tools:

- [Docker](https://docs.docker.com/get-docker/)
- [Node.js 22](https://nodejs.org/en/download/)
- [Python 3.9](https://www.python.org/downloads/)
- [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)
- [AWS Command Line Interface](https://aws.amazon.com/cli/)

In addition to these, your system must be properly configured with AWS credentials, possessing necessary permissions to deploy the service. For a seamless AWS credential management experience, we recommend using [aws-vault](https://github.com/99designs/aws-vault).

## Setting Up the Local Development Environment

1. Start by cloning this repository:

    ```bash
    git clone git@github.com:56kcloud/serverless-workshop.git
    ```

2. Create a virtual Python environment and install dependencies:

    ```bash
    cd serverless-workshop
    python3.9 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements-dev.txt
    ```

## Testing

Run Python tests to ensure everything is functioning correctly:

```bash
python -m pytest -v tests/test_infra.py --cov=stacks --cov-report=html
python -m unittest tests/test_handler.py --cov=stacks --cov-report=html
```

## Deployment

### Bootstrapping

To deploy AWS CDK apps into an AWS [environment](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html), you will need to provision the necessary resources. Run the following command:

```bash
aws-vault exec shared-services-full-access -- cdk bootstrap
```

### Live Infrastructure Deployment

Please note that the deployment process is automatically triggered via a GitHub action when changes are pushed to the `serverless-workshop` repository.

## Contributing

We welcome contributions to this project! Please fork the repository and submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
