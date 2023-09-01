# Table of Contents
- [Introduction](#introduction)
- [API Definition](#api_def)
    - [Input Parameters](#input)
    - [Output](#output)    
- [Samples](#sample)
    - [Sample 1 -- Get Resource API DataMethod](#sample_1) 

# Introduction <a id="introduction"></a>
The `GetResourceDataByAPI` function is a static method of the `NBGoogleAPILibrary` class that retrieves Google resource data via the Google REST API.


# Supported devices -> TBD
  - Google VPC Router
  - Google VPN Gateway
  - Google Cloud Router
  - Google Internal Load Balancer
  - Google External Load Balancer
  - Google Firewall
  - Google Cloud NAT Gateway
  - Google Virtual Machine
  - Google Cloud Internet Gateway
  - Google Partner Interconnect
  - Google Dedicated Interconnect
  - Google Cloud Private Service Connect Endpoint


# API Definition <a id="api_def"></a>
```python
  def GetResourceDataByAPI(
            params: dict
    ) -> object:
    # implementation
    # ...
```

## Input Parameters <a id="input"></a>
The function takes in several arguments, including:
 - `params` (str) A dictionary containing additional parameters to use when calling the Google Resource API. 

## Output <a id="output"></a>
> The JSON response body of the HTTP request to the Google RESTful API, which can be found in Azure API Document (e.g. https://cloud.google.com/compute/docs/reference/rest/v1)
> This is a dictionary with string keys and values.

# Samples <a id="sample"></a>
## Sample 1 -- Get Resource API Data <a id="sample_1"></a>
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

def RetrieveData(nb_node):
    # Get Live Data
    data = NBGoogleAPILibrary.GetResourceDataByAPI(
        nb_node
    )
    return data
```
