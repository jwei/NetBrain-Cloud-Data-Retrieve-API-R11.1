## Description

The get_azure_data_2steps function supports two steps (i.e., POST + GET) methods to get data tables of Azure resources. This function performs the following two steps to retrieve the data:

1. It sends a POST request which returns a table URL in the HTTP response location header.
2. It sends a subsequent GET request to get the table data from the returned URL.

Note that it takes time for the Azure REST server to generate the table resource. The function will retry if the resource is not ready, with a maximum timeout of 30 seconds.

Please refer to the Microsoft API documentation for URL format and parameters. For example, please refer to https://docs.microsoft.com/en-us/rest/api/network-gateway/virtualnetworkgateways/getlearnedroutes#code-try-0

## Usage

### Arguments
 - `api_server_id` (str): Azure Tenant API Server Instance ID saved in the device.
 - `url` (str): HTTP request URL of the POST method. For example, https://management.azure.com/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/Central-RG1/providers/Microsoft.Network/virtualNetworkGateways/West-VPN-GW/getLearnedRoutes?api-version=2020-06-01
 - `json_body` (dict): The JSON body of the POST request. For example, {'sample_field1': value1}

### Returns
 - `dict` or `list`: The JSON output of the table result.
 - `None`: In case of POST URL format error or GET request timeout.

### Example

```python
def RetrieveData(rtn_params):
    if isinstance(rtn_params, str):
        rtn_params = json.loads(rtn_params)

    resource_id = rtn_params['id']
    api_server_id = rtn_params['apiServerId']
    base_url = 'https://management.azure.com/'

    url = '{base_url}{resource_url_path}?api-version={version}'.format(
        base_url=base_url,
        resource_url_path=resource_id,
        version='2021-05-01'
    )
    front_end_ip_conf_res_list = get_azure_api_data(api_server_id, url)
 ```

#### Parameters

- `rtn_params`: A dictionary or JSON string containing the parameters for the API call. The dictionary must contain the following keys:
  - `'id'`: The ID of the resource.
  - `'apiServerId'`: The ID of the API server.

In the `RetrieveData` function, the `url` variable is constructed using the `base_url`, `resource_id`, and `version` variables. The `base_url` is set to `'https://management.azure.com/'`, which is the base URL for the Azure Management API. The `resource_id` is obtained from the `rtn_params` dictionary passed to the function. The `version` is set to `'2021-05-01'`, which specifies the version of the Azure API to use.

The `url` variable is then constructed using Python's string formatting method `.format()`. The resulting URL is a combination of the `base_url`, the `resource_id`, and the `version`, and it specifies the function `get_azure_api_data` to call.
