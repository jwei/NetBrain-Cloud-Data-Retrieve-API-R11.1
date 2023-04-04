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

> **Content**: The Azure API Response of Virtual Network.  
:exclamation:**Todo**:exclamation: @Xun: vnet比较简单。这里重点想解释，有些config是由多个API拼接而成。比如vng的描述可能类似于 The Azure API Response of Azure Virtual Network Gateway, with the full API response data of associated resources: 
* "self.properties.ipConfigurations.publicIPAddress"
* "self.properties.ipConfigurations.subnet"
* "self.properties.remoteVirtualNetworkPeerings". 
@Xun 这种多个API conbination的情况，需要再下面的Azure API Doc & Azure API Version部分，做成3 columns tbl "Resource" (Virtual Networks - Get), "API Doc" (xx), "API Version Used" (xx).

|**Type**|**Associated Resource**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Virtual Networks - Get | | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/virtual-networks/get?tabs=HTTP | 
| Network Security Groups – Get （Optional）| test | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/virtual-networks/get?tabs=HTTP |

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
