# Table of Contents
- [Introduction](#introduction)
- [API Definition](#api_def)
    - [Input Parameters](#input)
    - [Output](#output)    
- [Samples](#sample)
    - [Sample 1 -- Get Resource API DataMethod](#sample_1) 

# Introduction <a id="introduction"></a>
The `GetResourceDataByAPI` function is a static method of the `NBGoogleAPILibrary` class that retrieves Google resource data via the Google REST API.


# Supported devices
  - Google VPC Router
  - Google VPN Gateway
  - Google Cloud Router
  - Google Partner Interconnect
  - Google Dedicated Interconnect
  - Google Cloud Private Service Connect Endpoint


# API Definition <a id="api_def"></a>
```python
class NBGoogleAPILibrary:
    @staticmethod
    def GetResourceDataByAPI(
            api_server_id: str,
            resource_uri: str,
            http_method: str = 'GET',
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
 - `json_body[optional]` (object) API request body

## Output <a id="output"></a>
> The JSON response body of the HTTP request to the Google RESTful API, which can be found in Azure API Document (e.g. https://cloud.google.com/compute/docs/reference/rest/v1)
> This is a dictionary with string keys and values.

# Samples <a id="sample"></a>
## Sample 1 -- Get General Resource API Data <a id="sample_1"></a>
- Supported Resources: VPC Router, VPN Gateway, Cloud Router, Private Service Connect, Partner Interconnect
- Virtual Nodes: Internet Gateway,Global Internet Gateway
- Unsupported Resources: Firewall, LoadBalancer, Cloud Nat
- Unknow: Dedicated Interconnect

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
    # Unsupported Devices
    if 'selfLink' not in params['params']:
        raise Exception("Error: Not support device '{}'".format(params['params']['name']))

    # Get Live Data
    data = NBGoogleAPILibrary.GetResourceDataByAPI(
        api_server_id=params['apiServerId'],
        resource_uri=params['params']['selfLink']
    )
    return data
```
