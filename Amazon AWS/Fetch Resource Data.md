# Introduction
The `GetResourceData` function is a static method defined in the `NBAWSAPILibrary` class. It is used to retrieve data (tables) of AWS resources.
# Supported devices
Below are supported device by built-in mapping function. Please use `customized_func_mapping` for more devices based AWS boto3 document.
* AWS VPC router
* AWS Transit Gateways
* AWS Network Firewall
* AWS Elastic Load Balancer
* AWS Application Load Balancer
* AWS Gateway Load Balancer

# API Definition
The `GetResourceData` function is used to retrieve data from AWS resources using AWS SDK methods. It takes various parameters such as params which contain the standard parameters for the AWS SDK method,
```python
class NBAWSAPILibrary:
    @staticmethod
    def GetResourceData(param, func_name, filter_keys=[], customized_filters=[], customized_func_mapping={}):
        """Simulate the functionality of NCT and get Azure resource complex data (tables).
 
        Args:
            param (dict): e.g., {'apiServerId': 'b737cc5a-75a4-4663-97d6-eb2c6b576880', 'RegionName': 'ca-central-1', ...}
            func_name (string): This parameter specifies the name of the AWS function that will be called to retrieve the desired resources. E.g., 'describe_transit_gateway_route_tables'
            filter_keys (list): The filters provided in this parameter have the second highest priority. They will be used if there are no filters provided in customized_filters for the same key. E.g., ['transit-gateway-route-table-id']
            customized_filters (list): The filters provided in this parameter have the highest priority. They will override any other filters defined later in the code for the same key. E.g., [{'Name': 'transit-gateway-id', 'Values': ['tgw-0cf091f03edf14349']}]
            customized_func_mapping (dict): Specifies how to fetch resources through the context of a specific device. E.g., {'describe_transit_gateway_route_tables': {'resource_type': 'ec2', 'field_name': 'TransitGatewayRouteTables', 'transit-gateway-route-table-id': 'Options.AssociationDefaultRouteTableId', 'transit-gateway-id': 'TransitGatewayId'}}
 
        Returns:
            (object) list of objects
 
        Raises:
        """
  
        # implementation
        # ...
```

# Input Parameters:
 - `param` (dict): A dictionary object that contains key-value pairs representing parameters to be passed to the AWS function being called. For example, `{'apiServerId': 'b737cc5a-75a4-4663-97d6-eb2c6b576880', 'RegionName': 'ca-central-1', ...}`.

 - `func_name` (string): A string that specifies the name of the AWS function that will be called to retrieve the desired resources. For example, `'describe_transit_gateway_route_tables'`.

 - `filter_keys` (list): A list of strings representing keys for filters to be applied to the AWS function call. Filters provided in this parameter have the second highest priority, and will be used if there are no filters provided in `customized_filters` for the same key. For example, `['transit-gateway-route-table-id']`.

 - `customized_filters` (list): A list of dictionaries representing customized filters to be applied to the AWS function call. Filters provided in this parameter have the highest priority and will override any other filters defined later in the code for the same key. For example, `[{'Name': 'transit-gateway-id', 'Values': ['tgw-0cf091f03edf14349']}]`.

 - `customized_func_mapping` (dict): A dictionary object that specifies how to fetch resources through the context of a specific device. Each key represents the name of an AWS function, and its value is another dictionary containing the following fields: `resource_type`, `field_name` and so on. For example, `{'describe_transit_gateway_route_tables': {'resource_type': 'ec2', 'field_name': 'TransitGatewayRouteTables', 'transit-gateway-route-table-id': 'Options.AssociationDefaultRouteTableId', 'transit-gateway-id': 'TransitGatewayId'}}`.

| Resource Type | Device Type | func_name | filed_name | filter_keys | customer_filters |
| --- | --- | --- | --- | --- | --- |
| ec2 | VPC router | describe_route_tables | RouteTables | vpc-id | |
| ec2 | VPC router | describe_security_groups | SecurityGroups | vpc-id | |
| ec2 | VPC router | describe_network_acls | NetworkAcls | vpc-id | |
| ec2 | VPC router | describe_vpc_peering_connections | VpcPeeringConnections | requester-vpc-info.vpc-id | |
| ec2 | VPC router | describe_vpc_peering_connections | VpcPeeringConnections | accepter-vpc-info.vpc-id | |
| ec2 | VPC router | describe_network_interfaces | NetworkInterfaces | vpc-id | |
| ec2 | Transit Gateway | describe_transit_gateway_route_tables | TransitGatewayRouteTables | transit-gateway-route-table-id | |
| ec2 | Transit Gateway | describe_transit_gateway_route_tables | TransitGatewayRouteTables | transit-gateway-id | |
| ec2 | Transit Gateway | describe_transit_gateway_attachments | TransitGatewayAttachments | transit-gateway-route-table-id | |
| ec2 | Transit Gateway | describe_transit_gateway_attachments | TransitGatewayAttachments | transit-gateway-id | |
| elbv2 | Application Load Balancer | describe_listeners | Listeners | LoadBalancerArn | N/A |
| elbv2 | Network Load Balancer | describe_listeners | Listeners | LoadBalancerArn | N/A |
| elbv2 | Gateway Load Balancer | describe_listeners | Listeners | LoadBalancerArn | N/A |
| network-firewall | Network Firewall | describe_firewall_policy | None| FirewallPolicyArn | N/A |

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
      
    return json.dumps(data, indent=4)
 ```
