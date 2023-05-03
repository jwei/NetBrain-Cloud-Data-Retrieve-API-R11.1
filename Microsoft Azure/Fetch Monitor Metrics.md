# Introduction

The `GetMonitorMetrics` function is a static method defined in the `NBAzureAPILibrary` class. It leverages the Azure Monitor solution to fetch metrics of Azure resources via the Azure RESTful API.
@Jia -- add merics doc ref

@Jia -- Finalize API Def
# API Definition
```python
class NBAzureAPILibrary:
    @staticmethod
    def GetMonitorMetrics(api_server_id: str,
                          azure_resource_uri: str,
                          api_version: str, 
                          url_params: Dict[str, str]
                          ) -> Dict[str, Any]:
        # implementation
        # ...
```

# Input Parameters:
 - `api_server_id`(str) - The Azure Tenant API Server Instance ID saved in Device.
 - `azure_resource_uri`(str) - The resource identifier for the Azure resource whose metrics are to be fetched.
 - `api_version[optional]`(str) - The API version to use for the Azure monitor metrics API. This is a string value. This parameter is optional and defaults to None.
 - `url_params[optional]`(dic) - A dictionary containing additional URL parameters to use when calling the Azure monitor metrics API. For a complete list of available metrics for each Azure resource, please reference to Microsoft document: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/metrics-supported

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

metric_name = 'ExpressRouteGatewayCpuUtilization'  # metric name
 
def BuildParameters(context, device_name, params):
    node_props = GetDeviceProperties(context, device_name, 
            {'techName': 'Microsoft Azure', 'paramType': 'SDN', 'params' : ['*']})
    return node_props
     
def RetrieveData(param):
    resourceUri = param['params']['id']
    url_params = {'metricnames': metric_name}
    rtn_res = NBAzureAPILibrary.GetMonitorMetrics(param['apiServerId'], resourceUri, url_params)
    return json.dumps(rtn_res, indent=4)
    
 ```

