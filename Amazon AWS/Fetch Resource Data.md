# Introduction
The `GetResourceData` function is a static method defined in the `NBAWSAPILibrary` class. It is used to retrieve data (tables) of AWS resources.
# Supported Devices
Below are supported device by built-in mapping function. Please use `customized_func_mapping` for more devices based AWS boto3 document.
* AWS VPC router
* AWS Transit Gateways
* AWS Network Firewall
* AWS Elastic Load Balancer
* AWS Application Load Balancer
* AWS Gateway Load Balancer

# API Definition
The `GetResourceData` function is used to retrieve data from AWS resources using AWS SDK methods. It takes various parameters such as params which contain the standard parameters for the AWS SDK method.
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
 - `func_name` (string): A string that specifies the name of the AWS function that will be called to retrieve the desired resources. For example, `describe_transit_gateway_route_tables`.
 - `filter_keys` (list): A list of strings representing keys for filters to be applied to the AWS function call. Filters provided in this parameter have the second highest priority, and will be used if there are no filters provided in `customized_filters` for the same key. For example, `['transit-gateway-route-table-id']`.

    | Resource Type | Device Type | func_name | filter_keys |
    | --- | --- | --- | --- |
    | ec2 | VPC router | describe_route_tables | vpc-id |
    | ec2 | VPC router | describe_security_groups | vpc-id |
    | ec2 | VPC router | describe_network_acls | vpc-id |
    | ec2 | VPC router | describe_vpc_peering_connections | requester-vpc-info.vpc-id |
    | ec2 | VPC router | describe_vpc_peering_connections | accepter-vpc-info.vpc-id |
    | ec2 | VPC router | describe_network_interfaces | vpc-id |
    | ec2 | Transit Gateway | describe_transit_gateway_route_tables | transit-gateway-route-table-id |
    | ec2 | Transit Gateway | describe_transit_gateway_route_tables | transit-gateway-id |
    | ec2 | Transit Gateway | describe_transit_gateway_attachments | transit-gateway-route-table-id |
    | ec2 | Transit Gateway | describe_transit_gateway_attachments | transit-gateway-id |
    | elbv2 | Application Load Balancer | describe_listeners | LoadBalancerArn |
    | elbv2 | Network Load Balancer | describe_listeners | LoadBalancerArn |
    | elbv2 | Gateway Load Balancer | describe_listeners | LoadBalancerArn |
    | network-firewall | Network Firewall | describe_firewall_policy | FirewallPolicyArn |

 - `customized_filters` (list, optional): Customized_filters only supports `EC2` resource. Supposing customer want to create their own customized filters according to AWS boto3 SDK. A list of dictionaries representing customized filters to be applied to the AWS function call. Filters provided in this parameter have the highest priority and will override any other filters defined later in the code for the same key. For example, `[{'Name': 'transit-gateway-id', 'Values': ['tgw-0cf091f03edf14349']}]`. Please use EC2 boto3 document as reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html

 - `customized_func_mapping` (dict, optional): A dictionary object that specifies how to fetch resources through the context of a specific device. Each key represents the name of an AWS function, and its value is another dictionary containing the following fields: `resource_type`, `field_name` and so on. Please check below for format and example.
 
    ```python
    # Format
    {
        func_name:
        {
            'resource_type': resource_type,
            'field_name': field_name,
            filter_key1: device_property,
            filter_key2: device_property,
        }
    }
    # Example
    {
      "describe_transit_gateway_route_tables": {
        "resource_type": "ec2",
        "field_name": "TransitGatewayRouteTables",
        "transit-gateway-route-table-id": "Options.AssociationDefaultRouteTableId",
        "transit-gateway-id": "TransitGatewayId"
      }
    }
    ```
   - `Resource Type` (string): Refers to the type of digital asset or service that is being managed or tracked. It could be `ec2`, `elbc2` or `network-firewall`.
   - `func_name` (string): A string that specifies the name of the AWS function that will be called to retrieve the desired resources. For example, `'describe_transit_gateway_route_tables'`.
   - `filed_name` (string): Refers to the specific attribute or property of the resource that is being accessed or modified..
   - `filter_keys` (string): A list of strings representing keys for filters to be applied to the AWS function call.
   - `device_property` (string): Refers to the specific property keys in device. The value of properties will be used filter values. For example, `'Options.AssociationDefaultRouteTableId'`




# Output:
> The JSON response body of the request to the AWS SDK. This is a dictionary with string keys and values.

# Raises:
- If the function name specified in the `func_name` parameter is not found in either `built_in_func_mapping` or `customized_func_mapping`, the code raises an `Exception` with an error message.
- If a filter key specified in either `filter_keys` or `customized_filters` is not defined in the function mapping specified in `config` or `customized_func_mapping`, respectively, the code raises an `Exception` with an error message.
- If a customized filter is not in the correct format (i.e., it does not have a `Name` and `Values` field), the code raises an `Exception` with an error message.
- If the `resource_type` specified in config is not one of the supported types (`ec2`, `elbv2`, or `network-firewall`), the code raises a `Warning` with an error message. However, this warning is treated the same as an exception, and the code immediately raises an `Exception` with the same error message.

# Example 1 -- Using filter keys
```python
'''
Begin Declare Input Parameters
[
]
End Declare
 
For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''
import json
  
def BuildParameters(context, device_name, params):
    self_node = GetDeviceProperties(context, device_name, {'techName': 'Amazon AWS', 'paramType': 'SDN', 'params': ['*']})
    return self_node['params']
      
def RetrieveData(params):
    data = NBAWSAPILibrary.GetResourceData(params, func_name='describe_transit_gateway_route_tables', filter_keys=['transit-gateway-id'])
    return json.dumps(data, indent=4, default=str)
 ```
 
 # Example 2 -- Using customized filters
```python
'''
Begin Declare Input Parameters
[
]
End Declare
 
For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''
import json
  
def BuildParameters(context, device_name, params):
    self_node = GetDeviceProperties(context, device_name, {'techName': 'Amazon AWS', 'paramType': 'SDN', 'params': ['*']})
    return self_node['params']
      
def RetrieveData(params):
    # customized_filters is optional   
    customized_filters = [{'Name': 'transit-gateway-id', 'Values': ['tgw-0cf091f03edf14349']}]
    data = NBAWSAPILibrary.GetResourceData(params, func_name='describe_transit_gateway_route_tables', customized_filters=customized_filters)
    return json.dumps(data, indent=4, default=str)
 ```
 
 # Example 3 -- Using customized function mapping
```python
'''
Begin Declare Input Parameters
[
]
End Declare
 
For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''
import json
  
def BuildParameters(context, device_name, params):
    self_node = GetDeviceProperties(context, device_name, {'techName': 'Amazon AWS', 'paramType': 'SDN', 'params': ['*']})
    return self_node['params']
      
def RetrieveData(params):
    # customized_func_mapping is optional 
    customized_func_mapping = {
        'describe_transit_gateway_route_tables':
        {
            'resource_type': 'ec2',
            'field_name': 'TransitGatewayRouteTables',
            'transit-gateway-route-table-id': 'Options.AssociationDefaultRouteTableId',
            'transit-gateway-id': 'TransitGatewayId'
        }
    }
    data = NBAWSAPILibrary.GetResourceData(params, func_name='describe_transit_gateway_route_tables', filter_keys=['transit-gateway-id'], customized_func_mapping=customized_func_mapping)
    return json.dumps(data, indent=4, default=str)
 ```
