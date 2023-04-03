# Usage
Please retrieve the resource configuration data through NetBrain's built-in config file function. NO API is needed.


# Table of Contents
* [Azure Virtual Network Distributed Router](#azure-virtual-network-distributed-router)
* [Azure Virtual Machine](#azure-virtual-machine)


## Azure Virtual Network Distributed Router

> **Content**: The Azure API Response of Virtual Network.  
:exclamation:**Todo**:exclamation: @Xun: vnet比较简单。这里重点想解释，有些config是由多个API拼接而成。比如vng的描述可能类似于 The Azure API Response of Azure Virtual Network Gateway, with the full API response data of associated resources: 
* "self.properties.ipConfigurations.publicIPAddress"
* "self.properties.ipConfigurations.subnet"
* "self.properties.remoteVirtualNetworkPeerings". 
@Xun 这种多个API conbination的情况，需要再下面的Azure API Doc & Azure API Version部分，做成3 columns tbl "Resource" (Virtual Networks - Get), "API Doc" (xx), "API Version Used" (xx).

> **Azure API documentation** : https://learn.microsoft.com/en-us/rest/api/virtualnetwork/virtual-networks/get?tabs=HTTP

> **Azure API Version**: 2021-08-01

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



# Azure Virtual Machine


> **Title** : Get virtual machine

> **API documentation** : https://learn.microsoft.com/en-us/rest/api/compute/virtual-machines/get

> **Version** : 2022-03-01

> **API Response** : 
```json
{
  "name": "myVM",
  "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM",
  "type": "Microsoft.Compute/virtualMachines",
  "location": "West US",
  "tags": {
    "myTag1": "tagValue1"
  },
  "properties": {
    "vmId": "0f47b100-583c-48e3-a4c0-aefc2c9bbcc1",
    "hostGroup": {
      "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/hostGroups/myHostGroup"
    },
    "hardwareProfile": {
      "vmSize": "Standard_D2s_v3"
    },
    "storageProfile": {
      "imageReference": {
        "publisher": "MicrosoftWindowsServer",
        "offer": "WindowsServer",
        "sku": "2016-Datacenter",
        "version": "latest"
      },
      "osDisk": {
        "osType": "Windows",
        "name": "myOsDisk",
        "createOption": "FromImage",
        "caching": "ReadWrite",
        "managedDisk": {
          "storageAccountType": "Premium_LRS",
          "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myOsDisk"
        },
        "diskSizeGB": 30
      },
      "dataDisks": []
    },
    "osProfile": {
      "computerName": "myVM",
      "adminUsername": "admin",
      "windowsConfiguration": {
        "provisionVMAgent": true,
        "enableAutomaticUpdates": false
      },
      "secrets": []
    },
    "networkProfile": {
      "networkInterfaces": [  // The full data structure of Network Interface resource is enriched by NetBrain.
        {
          "id": "/subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{myNIC}"
        }
      ]
    },
    "provisioningState": "Succeeded"
  }
}
```

> **Title** : Get network interface

> **API documentation** : https://learn.microsoft.com/en-us/rest/api/virtualnetwork/network-interfaces/get

> **Version** : 2021-08-01

> **API Response** : 
```json
{
  "name": "test-nic",
  "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/networkInterfaces/test-nic",
  "location": "eastus",
  "properties": {
    "provisioningState": "Succeeded",
    "ipConfigurations": [
      {
        "name": "ipconfig1",
        "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/networkInterfaces/test-nic/ipConfigurations/ipconfig1",
        "properties": {
          "provisioningState": "Succeeded",
          "privateIPAddress": "172.20.2.4",
          "privateIPAllocationMethod": "Dynamic",
          "publicIPAddress": {
            "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/publicIPAddresses/test-ip"
          },
          "subnet": {
            "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/rg1-vnet/subnets/default"
          },
          "primary": true,
          "privateIPAddressVersion": "IPv4"
        }
      }
    ],
    "dnsSettings": {
      "dnsServers": [],
      "appliedDnsServers": [],
      "internalDomainNameSuffix": "test.bx.internal.cloudapp.net"
    },
    "macAddress": "00-0D-3A-1B-C7-21",
    "enableAcceleratedNetworking": true,
    "disableTcpStateTracking": true,
    "enableIPForwarding": false,
    "networkSecurityGroup": {
      "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/networkSecurityGroups/nsg"
    },
    "primary": true,
    "virtualMachine": {
      "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Compute/virtualMachines/vm1"
    },
    "dscpConfiguration": {
      "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Compute/dscpConfiguration/mydscpconfiguration"
    },
    "vnetEncryptionSupported": false
  },
  "type": "Microsoft.Network/networkInterfaces"
}
```
