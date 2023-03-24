Azure VNet Router

Get virtual network
https://learn.microsoft.com/en-us/rest/api/virtualnetwork/virtual-networks/get?tabs=HTTP#code-try-0
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

Get network security group
https://learn.microsoft.com/en-us/rest/api/virtualnetwork/network-security-groups/get?tabs=HTTP#code-try-0
```
{
  "name": "testnsg",
  "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/networkSecurityGroups/testnsg",
  "type": "Microsoft.Network/networkSecurityGroups",
  "location": "westus",
  "properties": {
    "provisioningState": "Succeeded",
    "securityRules": [
      {
        "name": "rule1",
        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/networkSecurityGroups/testnsg/securityRules/rule1",
        "properties": {
          "provisioningState": "Succeeded",
          "protocol": "*",
          "sourcePortRange": "*",
          "destinationPortRange": "80",
          "sourceAddressPrefix": "*",
          "destinationAddressPrefix": "*",
          "access": "Allow",
          "priority": 130,
          "direction": "Inbound"
        }
      }
    ],
    "defaultSecurityRules": [
      {
        "name": "AllowVnetInBound",
        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/networkSecurityGroups/testnsg/defaultSecurityRules/AllowVnetInBound",
        "properties": {
          "provisioningState": "Succeeded",
          "description": "Allow inbound traffic from all VMs in VNET",
          "protocol": "*",
          "sourcePortRange": "*",
          "destinationPortRange": "*",
          "sourceAddressPrefix": "VirtualNetwork",
          "destinationAddressPrefix": "VirtualNetwork",
          "access": "Allow",
          "priority": 65000,
          "direction": "Inbound"
        }
      },
      {
        "name": "AllowAzureLoadBalancerInBound",
        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/networkSecurityGroups/testnsg/defaultSecurityRules/AllowAzureLoadBalancerInBound",
        "properties": {
          "provisioningState": "Succeeded",
          "description": "Allow inbound traffic from azure load balancer",
          "protocol": "*",
          "sourcePortRange": "*",
          "destinationPortRange": "*",
          "sourceAddressPrefix": "AzureLoadBalancer",
          "destinationAddressPrefix": "*",
          "access": "Allow",
          "priority": 65001,
          "direction": "Inbound"
        }
      },
      {
        "name": "DenyAllInBound",
        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/networkSecurityGroups/testnsg/defaultSecurityRules/DenyAllInBound",
        "properties": {
          "provisioningState": "Succeeded",
          "description": "Deny all inbound traffic",
          "protocol": "*",
          "sourcePortRange": "*",
          "destinationPortRange": "*",
          "sourceAddressPrefix": "*",
          "destinationAddressPrefix": "*",
          "access": "Deny",
          "priority": 65500,
          "direction": "Inbound"
        }
      }
    ]
  }
}
```
