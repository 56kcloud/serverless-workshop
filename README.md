![Test Suite](https://github.com/56kcloud/serverless-workshop/workflows/test/badge.svg)
[![GitHub Super-Linter](https://github.com/56kcloud/serverless-workshop/actions/workflows/linter.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![Code Coverage](https://codecov.io/gh/56kcloud/serverless-workshop/branch/main/graph/badge.svg?token=aoWqkGkVXX)](https://codecov.io/gh/56kcloud/serverless-workshop)

# Serverless Workshop Infrastructure

## Overview

This repository contains infrastructure-as-code and the application code for the Serverless Workshop, which aims to provide a hands-on experience with serverless architecture using AWS services. The project utilizes AWS CDK (Cloud Development Kit) to define cloud infrastructure as code.

## Prerequisites

You will need a GitHub account. If you haven't got one, it's time to [sign up](https://github.com/signup).

If you are working on a Windows machine, we recommend using [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install).

Then ensure you have a Python interpreter installed and the Git Command Line Interface:

- [Python 3.9 or higher](https://www.python.org/downloads/)
- [Git](https://github.com/git-guides/install-git)

## Lab #1

1. Start by cloning this repository:
    
    ```bash
    git clone git@github.com:56kcloud/serverless-workshop.git
    cd serverless-workshop
    ```

2. Create a new branch with your UNIQUE team name:

    ```bash
    git checkout -b <your-unique-team-name>
    ```

3. Define an environment variable with your team name:

    ```bash
    export TEAM=$(git rev-parse --abbrev-ref HEAD)
    ```

4. Create a virtual Python environment and install dependencies:

    ```bash
    python3.9 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements-dev.txt
    ```

5. Run application unit tests:

    ```bash
    python -m unittest tests/test_handler.py 
    ```

    Fix the failing tests if any.

6. Commit

    ```bash
    git commit -a -m "Fixed unit tests"

7. Push

    ```bash
    git push -u origin <your-unique-team-name>
    ```

8. Deploy

Open a browser and navigate to GitHub Actions to see the deployment progress.    

    https://github.com/56kcloud/serverless-workshop/actions


When the deployment completes, find the URL of the API you just deployed and copy/paste it in a new browser windows. You should see:



## Contributing

We welcome contributions to this project! Please fork the repository and submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
