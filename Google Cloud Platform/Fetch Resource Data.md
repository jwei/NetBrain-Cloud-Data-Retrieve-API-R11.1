# Table of Contents
- [Introduction](#introduction)
- [API Definition](#api_def)
    - [Input Parameters](#input)
    - [Output](#output)
- [Special Notes](#special-notes)
  - [Resource Support Status](#resource-support-status)
- [Samples](#sample)
    - [Sample 1: Get Resource API Data of General Resource](#sample1)
    - [Sample 2: Get Resource API Data of Google Cloud NAT](#sample2)
    - [Sample 3: Get Resource API Data of Google Firewall](#sample3)
    - [Sample 4: Get Resource API Data of Load Balancer](#sample4)

# Introduction <a id="introduction"></a>
The `GetResourceDataByAPI` function is a static method of the `NBGoogleAPILibrary` class that retrieves Google resource data via the Google REST API.


# API Definition <a id="api_def"></a>
```python
class NBGoogleAPILibrary:
    @staticmethod
    def GetResourceDataByAPI(
            api_server_id: str,
            resource_uri: str,
            http_method: str = 'GET',
            url_params: dict = None,
            json_body: object = None,
    ) -> object:
        # implementation
        # ...
```

## Input Parameters <a id="input"></a>
The function takes in several arguments, including:
 - `api_server_id` (str) The external API Server ID of this technology instance. User should be able to get it in API Script context. Check Sample Google API Parser in NetBrain Parser Library for usage reference.
 - `resource_uri` (str) The resource identifier
 - `http_method[optional]` (str) GET or POST. The default method is "GET". 
 - `url_params[optional]` (dict) API request params for GET request
 - `json_body[optional]` (object) API request body

## Output <a id="output"></a>
> The JSON response body of the HTTP request to the Google RESTful API, which can be found in Azure API Document (e.g. https://cloud.google.com/compute/docs/reference/rest/v1)
> This is a dictionary with string keys and values.

# Special Notes <a id="special-notes"></a>
## Resource Support Status
- Supported Resources: 
  - Google Cloud NAT
  - Google Cloud Router
  - Google Firewall (Special case)
  - Google LoadBalancer (Special case)
  - Google Private Service Connect
  - Google Partner Interconnect
  - Google VPC Router
  - Google VPN Gateway
- Unsupported Resources: 
  - Google Internet Gateway (Virtual Node)
  - Google Global Internet Gateway  (Virtual Node)
  - Dedicated Interconnect


# Samples <a id="sample"></a>
## Sample 1: Get Resource API Data of General Resource <a id="sample1"></a>


```python
'''
Begin Declare Input Parameters
[
]
End Declare

For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''
from datetime import datetime, timedelta


def BuildParameters(context, device_name, params):
    nb_node = GetDeviceProperties(
        context, device_name,
        {
            'techName': 'Google Cloud',
            'paramType': 'SDN',
            'params': ['*']
        }
    )
    return nb_node


def RetrieveData(params):
    # Common used variable: nb_node, resource_uri, project_id, network_name
    nb_node = params['params']
    resource_uri = nb_node['selfLink'] if 'selfLink' in params['params'] else None
    project_id = nb_node["projectId"]
    network_name = nb_node["networkName"] if 'network_name' in params['params'] else None

    # Unsupported Devices
    if resource_uri == None:
        raise Exception("Error: Not support device '{}'".format(params['params']['name']))

    # Setup api server id
    api_server_id = params['apiServerId']


    # Get Live Data
    data = NBGoogleAPILibrary.GetResourceDataByAPI(
        api_server_id=api_server_id,
        resource_uri=resource_uri
    )
    return data
```


## Sample 2: Get Resource API Data of Google Cloud NAT <a id="sample2"></a>

```python
'''
Begin Declare Input Parameters
[
]
End Declare

For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''
from datetime import datetime, timedelta


def BuildParameters(context, device_name, params):
    nb_node = GetDeviceProperties(
        context, device_name,
        {
            'techName': 'Google Cloud',
            'paramType': 'SDN',
            'params': ['*']
        }
    )
    return nb_node


def RetrieveData(params):
    # Common used variable: nb_node, resource_uri, project_id,
    nb_node = params['params']
    resource_uri = nb_node['cloudRouterLink'] if 'cloudRouterLink' in params['params'] else None
    project_id = nb_node["projectId"]
    network_name = nb_node["networkName"] if 'network_name' in params['params'] else None

    # Unsupported Devices
    if resource_uri == None:
        raise Exception("Error: Not support device '{}'".format(params['params']['name']))

    # Setup api server id
    api_server_id = params['apiServerId']

    # Get Live Data
    data = NBGoogleAPILibrary.GetResourceDataByAPI(
        api_server_id=api_server_id,
        resource_uri=resource_uri
    )
    return data
```


## Sample 3: Get Resource API Data of Google Firewall <a id="sample3"></a>

```python
'''
Begin Declare Input Parameters
[
]
End Declare

For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''
from datetime import datetime, timedelta


def BuildParameters(context, device_name, params):
    nb_node = GetDeviceProperties(
        context, device_name,
        {
            'techName': 'Google Cloud',
            'paramType': 'SDN',
            'params': ['*']
        }
    )
    return nb_node


def RetrieveData(params):
    # Common used variable: nb_node, resource_uri, project_id,
    nb_node = params['params']
    resource_uri = nb_node['selfLink'] if 'selfLink' in params['params'] else None
    project_id = nb_node["projectId"]
    network_name = nb_node["networkName"]

    # Setup api server id
    api_server_id = params['apiServerId']

    url = f"https://compute.googleapis.com/compute/v1/projects/{project_id}/global/firewalls"
    url_params = {
        # Doc: https://cloud.google.com/compute/docs/reference/rest/v1/firewalls/list'
        "filter": f'(network="https://www.googleapis.com/compute/v1/projects/{project_id}/global/networks/{network_name}")'
    }

    # Get Live Data
    data = NBGoogleAPILibrary.GetResourceDataByAPI(
        api_server_id=api_server_id,
        resource_uri=url,
        url_params=url_params
    )
    return data
```

## Sample 4: Get Resource API Data of Load Balancer <a id="sample4"></a>

```python
'''
Begin Declare Input Parameters
[
]
End Declare

For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''
from datetime import datetime, timedelta


def BuildParameters(context, device_name, params):
    nb_node = GetDeviceProperties(
        context, device_name,
        {
            'techName': 'Google Cloud',
            'paramType': 'SDN',
            'params': ['*']
        }
    )
    return nb_node


def RetrieveData(params):
    # raise Exception(params)
    # Common used variable: nb_node, resource_uri, project_id,
    nb_node = params['params']
    project_id = nb_node["projectId"]  if 'projectId' in params['params'] else None
    network_name = nb_node["networkName"] if 'network_name' in params['params'] else None

    # Get resource_uri
    #   Might have attributes below, but all these are included at result of forwardingRules
    #       nbProperties.backendServices / nbProperties.subnetwork / nbProperties.targetPool
    resource_uri = nb_node['nbProperties']['forwardingRules'][0]


    # Unsupported Devices
    if resource_uri == None:
        raise Exception("Error: Not support device '{}'".format(params['params']['name']))

    # Setup api server id
    api_server_id = params['apiServerId']

    # Get Live Data
    data = NBGoogleAPILibrary.GetResourceDataByAPI(
        api_server_id=api_server_id,
        resource_uri=resource_uri
    )

    # Add details of backendService for internal-tcp-ldb
    if "backendService" in data:
        backend_url = data["backendService"]
        backendService = NBGoogleAPILibrary.GetResourceDataByAPI(
            api_server_id=api_server_id,
            resource_uri=backend_url
        )
        data["backendService"] = backendService

    return data
```