# Introduction

The `GetResourceData` function is a static method defined in the `NBAzureAPILibrary` class. It leverages the Azure Monitor solution to fetch metrics of Azure resources via the Azure RESTful API.

# API Definition
```python
class NBAzureAPILibrary:
    @staticmethod
    def GetResourceData(api_server_id: str,
                        nb_resource_data: object,
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

| Resource Type | data_type | sub_resource_uri | Notes |
| --- | --- | --- | --- |
| Virtual Network (Distributed Router) | vnet_route_tables | route_table_azure_uri | |
| | vnet_peerings | - | |
| | private_endpoints | - | |
| | network_security_groups | subnet_id or vnic_id | |
| | vnic_effective_routes | vnic_id | |
| Virtual Machine | vnics | - | |
| | vnic_nsg | - | |
| Load Balancer | load_balancing_rules | - | |
| | inbound_nat_rules | - | |
| | outbound_rules | - | |
| | backend_pools | backend_address_pool_uri | |
| Firewall 	| dnat_rule_collections	| -	| |
| 	| network_rule_collections | -	| |
| 	| application_rule_collections	| -	| |
| Application Gateway | app_gw_rules | -	| |
| 	| http_settings	| -	| |
| 	| translation_tables	|- 	||
| 	| listeners	|- 	||
| 	| backend_pools	| backend_address_pool_uri ||
| ExpressRoute Circuit | arp_table	| -	| |
| 	| route_table | -	| |
| 	| route_summary_table |- 	||
| Virtual Hub | route_tables	| -	| |
| 	| effective_routes	| -	| |
| NAT Gateway | nat_table | -	| |
| Virtual Network Gateway | bgp_learned_routes	| -	| |
| 	| bgp_advertised_routes	| -	| |
| 	| bgp_peerings	|- 	||
| VPN Gateway | bgp_learned_routes	| -	| |
| 	| bgp_advertised_routes	| -	| |
| 	| bgp_peerings	|- 	||

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
