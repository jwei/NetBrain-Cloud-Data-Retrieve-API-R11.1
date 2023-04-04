# Introduction

The `GetResourceData` function is a static method defined in the `NBAzureAPILibrary` class. It leverages the Azure Monitor solution to fetch metrics of Azure resources via the Azure RESTful API.

# API Definition
```python
class NBAzureAPILibrary:
    @staticmethod
    def GetResourceData(api_server_id: str,
                        b_resource_data: object,
                        data_type: str, 
                        sub_resource_uri: str
                        ) -> object:
    # implementation
        # ...
```

# Input Parameters:
 - `api_server_id`(str) - The external API Server ID of this technology instance. It is used to identify the target Azure API server. The user should be able to get it in the API script context. The usage reference can be found in the Sample Azure API Parser in NetBrain Parser Library.
 - `nb_resource_data`(object) - The entire resource data structure in NetBrain. It is retrieved by calling the `GetDeviceProperties` API method, passing in the device name and some parameters.
 - `data_type`(str) - The available data type for the current resource. This can be found in the Azure API documentation.
 - `sub_resource_uri`(str) - An optional parameter in case the customer just wants to fetch one sub-table of data. For example, if an Azure Load Balancer has multiple Backend Address Pools, the user can specify which one they want to fetch.

# Output:
> resp_body_json: The JSON response body of the HTTP request to the Azure monitor metrics API. This is a dictionary with string keys and values.

# Raises:
> This function does not raise any exceptions.

# Example

```python
'''
Begin Declare Input Parameters
[
]
End Declare
'''
  
def BuildParameters(context, device_name, params):
    node_props = GetDeviceProperties(context, device_name, {'techName': 'Microsoft Azure', 'paramType': 'SDN', 'params' : ['id', 'vNetId']})
    arn =  node_props['params']['id']
  
    rtn_params = [{ 'devName' : device_name, 'arn': arn}]
    return rtn_params
      
def RetrieveData(rtn_params):
    if isinstance(rtn_params, str):
        rtn_params = json.loads(rtn_params)
    param = rtn_params
  
    api_server_id = param['apiServerId']
    # refer to link below for supported metrics and url parameters
    # https://docs.microsoft.com/en-us/rest/api/network-gateway/virtualnetworkgateways/get#code-try-0
    resourceUri = param['arn']
    url_params = {'metricnames': 'ComputeUnits'}
    
    rtn_res = NBAzureAPILibrary.GetMonitorMetrics(api_server_id, resourceUri, url_params)  # call Azure Insight Monitoring Service to get Metrics data
  
    return json.dumps(rtn_res, indent=4)
 ```
