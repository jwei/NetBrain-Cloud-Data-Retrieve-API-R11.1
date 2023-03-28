The get_azure_monitor_metrics function is a Python function used to retrieve Azure monitor metrics. It is executed in the FrontServer and takes the Azure Tenant API Server Instance ID, resource ARN, API version, and URL parameters as input. The function returns the JSON response body of the HTTP request to the Azure monitor metrics API.

# Function Signature

> def get_azure_monitor_metrics(api_server_id: str, resource_arn: str, api_version: str, url_params: Dict[str, str]) -> Dict[str, Any]:

### Input Parameters:
 - `api_server_id` - The Azure Tenant API Server Instance ID saved in Device. This is a string value.
 - `resource_arn` - The resource ARN of the Azure resource whose metrics you want to retrieve. This is a string value.
 - `api_version` - The API version to use for the Azure monitor metrics API. This is a string value.
 - `url_params` - A dictionary containing additional URL parameters to use when calling the Azure monitor metrics API. This is a dictionary with string keys and values.

### Output:
> resp_body_json: The JSON response body of the HTTP request to the Azure monitor metrics API. This is a dictionary with string keys and values.

### Raises:
> This function does not raise any exceptions.

### Example:
```python
url_params = {'metricnames': 'TunnelIngressBytes,TunnelEgressBytes'}
resp_body_json = get_azure_monitor_metrics(api_server_id, resource_arn, api_version, url_params)
print(resp_body_json)
```

### Usages through `RetrieveData(rtn_params)`

This function retrieves data from the Azure API using the provided parameters.

### Example

```python
def RetrieveData(rtn_params):
    if isinstance(rtn_params, str):
        rtn_params = json.loads(rtn_params)
    param = rtn_params
 
    api_server_id = param['apiServerId']
    resourceUri = param['arn']
    api_version = '2018-01-01'
    url_params = {'metricnames': 'AvgRequestCountPerHealthyHost'}   
    rtn_res = get_azure_monitor_metrics(api_server_id, resourceUri, api_version, url_params) 
    return rtn_res
 ```

