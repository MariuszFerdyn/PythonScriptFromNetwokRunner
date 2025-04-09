# Python Script From Netwok Runner

## Project Overview

This sample project downloads Python scripts from network sources and executes them using Docker. It can also be deployed to various Azure services such as Azure App Service, Azure Container Apps (Container App Job), and more.

## Description

This project creates a workflow that:

1. Downloads Python scripts from a network such as a URL
2. Executes these scripts in isolated Docker environments
3. Can be deployed across various Azure cloud services

## Key Features

- **Isolation**: Runs scripts in containerized environments for security and dependency management
- **Cloud-ready**: Compatible with multiple Azure deployment options
- **Automation**: Can be scheduled or triggered as needed
- **Flexibility**: Works with any Python script accessible over a network

## Use Cases

- Running scheduled data processing jobs
- Executing maintenance scripts across distributed systems
- Deploying algorithm updates without rebuilding entire applications
- Creating serverless function-like capabilities with custom Python logic

## Docker Command Example

```bash
docker run -it --rm --name mypython-script python:3.12-alpine /bin/sh -c "wget -O /opt/pi_digit_calculator.py https://raw.githubusercontent.com/MariuszFerdyn/PythonScriptFromNetwokRunner/main/python/pi_digit_calculator.py && cd /opt && python pi_digit_calculator.py"
```

