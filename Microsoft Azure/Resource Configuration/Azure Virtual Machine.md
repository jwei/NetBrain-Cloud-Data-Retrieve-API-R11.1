# Azure Virtual Machine Configuration File Structure


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
      "networkInterfaces": [
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
