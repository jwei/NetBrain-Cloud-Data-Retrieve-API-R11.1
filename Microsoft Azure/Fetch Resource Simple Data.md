# Table of Contents
1. [Introduction](#introduction)
2. [API Definition](#api_def)
- [Input Parameters](#input)
- [Output](#output)
- [Raises](#exception)
3. [Sample](#sample)
4. [Default Azure API Versions](#default_api_version)

# Introduction <a name="introduction"></a>
The `GetResourceDataByAPI` function is a static method of the `NBAzureAPILibrary` class that retrieves Azure resource data via the Azure Management REST API. It supports both GET and POST methods to download resource data, where GET is used to download the resource data, and POST is used to download large or complex data sets asynchronously.

# API Definition  <a name="api_def"></a>
```python
class NBAzureAPILibrary:
    @staticmethod
    def GetResourceDataByAPI(api_server_id: str,
                             azure_resource_uri: str,
                             resource_action: str = None,
                             async_request: bool = False,  # Todo @Jia -- remove
                             api_method: str = "GET",  # Todo @Jia -- rename: http_method
                             api_version: str = '',
                             json_body: object = None) -> object:
    # implementation
        # ...
```

## Input Parameters <a name="input"></a>
The function takes in several arguments, including:
 - `api_server_id` (str) The external API Server ID of this technology instance. User should be able to get it in API Script context. Check Sample Azure API Parser in NetBrain Parser Library for usage reference.
 - `azure_resource_uri` (str) e.g. The resource identifier, e.g. /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}
 - `action[optional]` (str) in case that you want to download some specific data from the resource. e.g. pass in "getLearnedRoutes" when you want to download vnet gateway learned routes. Ref: https://learn.microsoft.com/en-us/rest/api/network-gateway/virtual-network-gateways/get-learned-routes?tabs=HTTP
 - `http_method[optional]` (str) GET or POST. Note that async methods like downloading large data set would need a POST method. (e.g. download vnet gateway learned routes, vnic effective routes, etc.) please check Microsoft Azure API document for reference.
 - `api_version[optional]` (str) API Version of the Azure Rest API, e.g. '2022-09-01', which can be found in Azure API document. If not provided, then a default API version is assigned for each resource provider. The mapping can be found at the end of this document.
 - `json_body[optional]` (object) API request body
 - `is_async_method[optional]` (bool) True if it is async API to download large data set from Azure.

## Output <a name="output"></a>
> The JSON response body of the HTTP request to the Azure RESTful API. This is a dictionary with string keys and values.

## Raises <a name="exception"></a>
> This function does not raise any exceptions.

# Sample <a name="sample"></a>
## Synchronized Example -- Get Resource API Data
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

def BuildParameters(context, device_name, params):
    # query DB, get required property of the node data model
    self_node = GetDeviceProperties(context, device_name, {'techName': 'Microsoft Azure', 'paramType': 'SDN', 'params': ['*']})
    return self_node
	
def RetrieveData(rtn_params):
    nb_node = rtn_params['params']
    api_server_id = rtn_params['apiServerId']
    resource = NBAzureAPILibrary.GetResourceDataByAPI(api_server_id, nb_node['id'])    
    return json.dumps(resource, indent=4)
 ```
 
 
## Asynchronized Example -- Get Virtual Network Gateway BGP Learned Routes
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

def BuildParameters(context, device_name, params):
    self_node = GetDeviceProperties(context, device_name, 
			{'techName': 'Microsoft Azure', 'paramType': 'SDN', 'params': ['*']})
    return {
        'nbNode': self_node['params']
    }
	
def RetrieveData(rtn_params):
    id = rtn_params['nbNode']['id']
    api_server_id = rtn_params['apiServerId']
    
    data = NBAzureAPILibrary.GetResourceDataByAPI(api_server_id, id, "getBgpPeerStatus", is_async_method=True)
    
    return json.dumps(data, indent=4)
 ```

# Default Azure API Versions <a name="default_api_version"></a>
Below are the default API versions for different Azure provider.
|**Azure Provider**|**Default API Version**|
|------|------|
| Microsoft.Network | 2022-09-01 |
| Microsoft.Compute | 2022-11-01 |
| Microsoft.Sql | 2021-11-01 |
| Microsoft.DBforMySQL | 2017-12-01 |
| Microsoft.DBforPostgreSQL | 2017-12-01 |
| Microsoft.DBforMariaDB | 2018-06-01 |
| Microsoft.Storage | 2022-09-01 |
| Microsoft.DocumentDB | 2022-05-01 |
