
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
