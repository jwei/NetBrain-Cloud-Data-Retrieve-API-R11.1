# Introduction

The `GetMonitorMetrics` function is a static method defined in the `NBAzureAPILibrary` class that leverages Azure Monitor solution that fetches metrics of Azure resources via Azure RESTful API. The function takes four parameters:

# API Definition
```python
class NBAzureAPILibrary:
    @staticmethod
    def GetMonitorMetrics(api_server_id: str, azure_resource_uri: str, api_version: str, url_params: Dict[str, str]) -> Dict[str, Any]:
        # implementation
        # ...
 ```

# Input Parameters:
 - `api_server_id`(str) - The Azure Tenant API Server Instance ID saved in Device.
 - `azure_resource_uri`(str) - The resource identifier for the Azure resource whose metrics are to be fetched.
 - `api_version`(str)(optional) - The API version to use for the Azure monitor metrics API. This is a string value. This parameter is optional and defaults to None.
 - `url_params`(dic)(optional) - A dictionary containing additional URL parameters to use when calling the Azure monitor metrics API. This parameter is optional and defaults to '2018-01-01'.

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

