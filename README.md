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

## Azure Container App 

```bash
# Login to Azure
az login 
        
# Set the subscription context
az account set --subscription $subscriptionId
        
# Create a new resource group for the gallery if it doesn't exist
az group create --name $ResourceGroup --location $location
        
# Prepare env
az extension add --name containerapp --upgrade --allow-preview true
az provider register --namespace Microsoft.App
az provider register --namespace Microsoft.OperationalInsights

# Create Container App Enviorment
az containerapp env create --name $Enviorment --resource-group $ResourceGroup --location $location

# Create a container app by explicitly passing in a Compose configuration file.
az containerapp job create --name pi-calculator-job --resource-group $ResourceGroup --environment $Enviorment --trigger-type Manual --replica-timeout 1800 --replica-retry-limit 1 --replica-completion-count 1 --image python:3.12-alpine --command-line "/bin/sh -c 'wget -O /opt/pi_digit_calculator.py https://raw.githubusercontent.com/MariuszFerdyn/PythonScriptFromNetwokRunner/main/python/pi_digit_calculator.py && cd /opt && python pi_digit_calculator.py'" --cpu 0.5 --memory 1.0Gi
```     
---

### Storing the Script in Azure Storage Account

The script can be stored in an Azure Storage Account as a blob. To provide secure access, you can generate a Shared Access Signature (SAS) token with the following features:
- **Read-Only Access**: Grant access with permissions limited to reading the blob.
- **Time-Based Access**: Specify a time window during which the token is valid, ensuring temporary access.
- **IP Address Restrictions**: Restrict access to specific IP addresses for added security.

For more information on generating SAS tokens, refer to the [Azure Documentation on Shared Access Signatures](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview).
