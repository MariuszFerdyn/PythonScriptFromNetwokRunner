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

---

### Storing the Script in Azure Storage Account

The script can be stored in an Azure Storage Account as a blob. To provide secure access, you can generate a Shared Access Signature (SAS) token with the following features:
- **Read-Only Access**: Grant access with permissions limited to reading the blob.
- **Time-Based Access**: Specify a time window during which the token is valid, ensuring temporary access.
- **IP Address Restrictions**: Restrict access to specific IP addresses for added security.

For more information on generating SAS tokens, refer to the [Azure Documentation on Shared Access Signatures](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview).
