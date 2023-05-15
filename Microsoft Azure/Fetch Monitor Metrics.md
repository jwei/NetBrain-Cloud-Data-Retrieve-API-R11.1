# Table of Contents
- [Introduction](#introduction)
- [API Definition](#api_def)
    - [Input Parameters](#input)
    - [Output](#output)    
- [Sample](#sample)   

# Introduction <a name="introduction"></a>
The `GetMonitorMetrics` function is a static method defined in the `NBAzureAPILibrary` class. It leverages the Azure Monitor solution to fetch metrics of Azure resources via the Azure RESTful API.
For a complete list of available metrics for each Azure resource, please reference to Microsoft document: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/metrics-supported

# API Definition <a name="api_def"></a>
```python
class NBAzureAPILibrary:
    @staticmethod
    def GetMonitorMetrics(
            api_server_id: str,
            azure_resource_uri: str,
            params: object = None,
            api_version: str = '2018-01-01'
    ) -> object:
        # implementation
        # ...
```

# Input Parameters <a name="input"></a>
 - `api_server_id`(str) - The Azure Tenant API Server Instance ID saved in Device.
 - `azure_resource_uri`(str) - The resource identifier for the Azure resource whose metrics are to be fetched.
 - `params`(dic) - A dictionary containing additional URL parameters to use when calling the Azure monitor metrics API. For a complete list of available metrics for each Azure resource, please reference to Microsoft document: https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/metrics-supported
 - `api_version[optional]`(str) - The API version to use for the Azure monitor metrics API. This is a string value. This parameter is optional and defaults to None. 

# Output <a name="output"></a>
> resp_body_json: The JSON response body of the HTTP request to the Azure monitor metrics API. This is a dictionary with string keys and values.

# Sample <a name="sample"></a>

```python
'''
Begin Declare Input Parameters
[
]
End Declare
'''

metric_name = 'ExpressRouteGatewayCpuUtilization'  # metric name
 
def BuildParameters(context, device_name, params):
    nb_node = GetDeviceProperties(
            context, 
            device_name, 
            {'techName': 'Microsoft Azure', 'paramType': 'SDN', 'params' : ['*']})
    return nb_node
     
def RetrieveData(params):    
    rtn_res = NBAzureAPILibrary.GetMonitorMetrics(
        api_server_id=params['apiServerId'], 
        azure_resource_uri=params['params']['id'], 
        params={'metricnames': metric_name}
    )
    return json.dumps(rtn_res, indent=4)   
 ```

