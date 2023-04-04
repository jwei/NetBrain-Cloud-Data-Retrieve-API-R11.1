# Introduction
The `GetResourceDataByAPI` function is a static method of the `NBAzureAPILibrary` class that retrieves Azure resource data via the Azure Management REST API. It supports both GET and POST methods to download resource data, where GET is used to download the resource data, and POST is used to download large or complex data sets asynchronously.

# API Definition
```python
class NBAzureAPILibrary:
    @staticmethod
    def GetResourceDataByAPI(
            api_server_id: str,
            azure_resource_uri: str,
            action: str = None,
            is_async_method: bool = False,
            api_method: str = "GET",
            api_version: str = '2022-09-01',
            json_body: object = None
    ) -> object:
    # implementation
        # ...
```

# Input Parameters:
The function takes in several arguments, including:


 - `api_server_id` (str) The external API Server ID of this technology instance. User should be able to get it in API Script context. Check Sample Azure API Parser in NetBrain Parser Library for usage reference.

 - `azure_resource_uri` (str) e.g. The resource identifier, e.g. /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}

 - `action[optional]` (str) in case that you want to download some specific data from the resource. e.g. pass in "getLearnedRoutes" when you want to download vnet gateway learned routes. Ref: https://learn.microsoft.com/en-us/rest/api/network-gateway/virtual-network-gateways/get-learned-routes?tabs=HTTP

 - `api_method[optional]` (str) GET or POST. Note that async methods like downloading large data set would need a POST method. (e.g. download vnet gateway learned routes, vnic effective routes, etc.) please check Microsoft Azure API document for reference.

 - `api_version[optional]` (str) API Version of the Azure Rest API. e.g. '2022-09-01'

 - `json_body[optional]` (object) API request body

 - `is_async_method[optional]` (bool) True if it is async API to download large data set from Azure.

# Output:
> The JSON response body of the HTTP request to the Azure RESTful API. This is a dictionary with string keys and values.

# Raises:
> This function does not raise any exceptions.

# Example

```python
'''
Begin Declare Input Parameters
 [
    {"name": "$backend_pool_id"}
 ]
End Declare

For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''

def BuildParameters(context, device_name, params):
    backend_pool_id = params['backend_pool_id']
    # backend_pool_id = '/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/backendAddressPools/AzurePathTest'
    self_node = GetDeviceProperties(context, device_name,
                                    {'techName': 'Microsoft Azure', 'paramType': 'SDN',
                                     'params': ['*']})  # query DB, get required property of the node data model
    return [{
        'nbNode': self_node['params'],
        'backend_pool_id': backend_pool_id
    }]


def RetrieveData(rtn_params):
    if isinstance(rtn_params, str):
        rtn_params = json.loads(rtn_params)

    nb_node = rtn_params['nbNode']
    backend_pool_id = rtn_params['backend_pool_id']
    api_server_id = rtn_params['apiServerId']

    res = NBAzureAPILibrary.GetResourceData(api_server_id, nb_resource_data=nb_node, data_type='backend_pools', sub_resource_uri=backend_pool_id)
    return res
 ```
