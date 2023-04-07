# Introduction
The `GetResourceData` function is a static method defined in the `NBAzureAPILibrary` class. It is used to retrieve data (tables) of Azure resources.

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
]
End Declare
'''
  
def BuildParameters(context, device_name, params):
    node_props = GetDeviceProperties(
        context,
        device_name,
        {'techName': 'Microsoft Azure', 'paramType': 'SDN', 'params' : ['*'] }
    )
    return node_props
      
def RetrieveData(param):   
    nb_node = param['params']
    data = NBAzureAPILibrary.GetResourceData(
        api_server_id=param['apiServerId'],
        nb_resource_data=nb_node,
        data_type='load_balancing_rules'
    )
      
    return data
 ```
