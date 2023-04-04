# Usage
To retrieve the configuration data for a resource, you can utilize NetBrain's built-in configuration file function, which does not require the use of an API. This function enables you to quickly obtain the necessary configuration information for your resources.


# Table of Contents
* [Azure Virtual Network Distributed Router](#azure-virtual-network-distributed-router)
* [Azure Virtual Network Gateway](#azure-virtual-network-gateway)


## Azure Virtual Network Distributed Router

> **Content**: The configuration of the Azure virtual network distributed router relies solely on the corresponding Azure API for its virtual network. The Azure API provides detailed information regarding the configuration of the virtual network, including its connectivity, security, and other relevant parameters.

Please find below the detailed information regarding the Azure API used for configuring the virtual network distributed router.

|**Type**|**Associated Resource**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Virtual Networks - Get |  | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/virtual-networks/get?tabs=HTTP | 


> **Sample** :
```json
{
  "name": "test-vnet",
  "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/test-vnet",
  "type": "Microsoft.Network/virtualNetworks",
  "location": "westus",
  "properties": {
    "provisioningState": "Succeeded",
    "addressSpace": {
      "addressPrefixes": [
        "10.0.0.0/16"
      ]
    },
    "subnets": [
      {
        "name": "subnet1",
        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/test-vnet/subnets/subnet1",
        "properties": {
          "provisioningState": "Succeeded",
          "addressPrefix": "10.0.1.0/24",
          "ipConfigurations": [
            {
              "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/loadBalancers/lb/frontendIPConfigurations/fe"
            }
          ]
        }
      }
    ],
    "virtualNetworkPeerings": []
  }
}
```



## Azure Virtual Network Gateway

> **Content**: The configuration of the Azure virtual network gateway is dependent on the Azure API response of the Azure Virtual Network Gateway as the primary response. The full API response data of associated resources, including `publicIPAddress`, `subnet`, and `remoteVirtualNetworkPeerings`, is required for the configuration process.

|**Type**|**Associated Resource**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Virtual Network Gateways - Get | | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/network-gateway/virtual-network-gateways/get?tabs=HTTP | 
| Public IP Addresses - Get | self.properties.ipConfigurations.publicIPAddress | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/public-ip-addresses/get?tabs=HTTP |
| Subnets - Get | self.properties.ipConfigurations.subnet | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/subnets/get?tabs=HTTP |
| Virtual Network Peerings - Get | self.properties.remoteVirtualNetworkPeerings | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/virtual-networks/get?source=recommendations&tabs=HTTP |

> **Sample** : 
:exclamation:**Todo**:exclamation: @Xun: 
1. try to use placehodler to display some variable (as in Azure doc) like id field below. But some variable can be real samples, e.g. private IP (range), region, etc. Maybe you can just copy paste from Azure doc.
2. put some content in each of the key part, e.g. for vnet: subnet, peering, etc.
```json
{
  "netbrainNotes": "This config file is generated via API",
  "netbrainHostName": "test-vnet(rg1)(subscription_id_prefix)(VirtualNetworkDistributedRouter)",
  "name": "{virtualNetworkAzureName}",
  "id": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}",
  "type": "Microsoft.Network/virtualNetworks",
  "location": "westus",
  "properties": {
    "provisioningState": "Succeeded",
    "addressSpace": {
      "addressPrefixes": [
        "10.0.0.0/16"
      ]
    },
    "subnets": [
      {
        "name": "subnet1",
        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/test-vnet/subnets/subnet1",
        "properties": {
          "provisioningState": "Succeeded",
          "addressPrefix": "10.0.1.0/24",
          "ipConfigurations": [
            {
              "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/loadBalancers/lb/frontendIPConfigurations/fe"
            }
          ]
        }
      }
    ],
    "virtualNetworkPeerings": []
  }
}
```
