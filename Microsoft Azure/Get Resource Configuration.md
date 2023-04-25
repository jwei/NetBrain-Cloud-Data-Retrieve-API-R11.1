# Usage
To retrieve the configuration data for a resource, you can utilize NetBrain's built-in configuration file function, which does not require coding. This function enables you to quickly obtain the resource configuration.


# Table of Contents
* [Azure Virtual Network Distributed Router](#azure-virtual-network-distributed-router)
* [Azure Virtual Network Gateway](#azure-virtual-network-gateway)
* [Azure Virtual Machine](#azure-virtual-machine)


## Azure Virtual Network Distributed Router

### Introduction
The configuration of the Azure virtual network distributed router relies solely on the corresponding Azure API of the virtual network. The Azure API provides detailed information regarding the configuration of the virtual network, including its connectivity, security, etc.

### Content
Below are the Azure APIs used to generate this configuration.
|**Resource/Action**|**Relationship**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Virtual Networks - Get | self | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/virtual-networks/get?tabs=HTTP | 


### Sample
```json
{
  "netbrainNotes": "This config file is generated via API",
  "netbrainHostName": "test-vnet(rg1)(subscription_id_prefix)(VirtualNetworkDistributedRouter)",
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

### Introduction
The configuration of the Azure virtual network gateway is dependent on the Azure API response of the Azure Virtual Network Gateway as the primary response. The full resource configuration consists of some associated resources' API data, including `publicIPAddress`, `subnet`, and `remoteVirtualNetworkPeerings`.

### Content
Below are the Azure APIs used to generate this configuration.
|**Resource/Action**|**Relationship**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Virtual Network Gateways - Get | vnetGateway | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/network-gateway/virtual-network-gateways/get?tabs=HTTP | 
| Public IP Addresses - Get | vnetGateway.properties.ipConfigurations.publicIPAddress | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/public-ip-addresses/get?tabs=HTTP |
| Subnets - Get | vnetGateway.properties.ipConfigurations.subnet | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/subnets/get?tabs=HTTP |
| Virtual Network Peerings - Get | vnetGateway.properties.remoteVirtualNetworkPeerings | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/virtual-networks/get?source=recommendations&tabs=HTTP |

### Sample
```json
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "East-VPN-GW(East-RG1)(073e6f45)(VirtualNetworkGateway)",
    "name": "East-VPN-GW",
    "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-VPN-GW",
    "etag": "W/\"c29b2eef-4bf8-4826-94fa-cc3a4e468bee\"",
    "type": "Microsoft.Network/virtualNetworkGateways",
    "location": "eastus",
    "properties": {
        "provisioningState": "Succeeded",
        "resourceGuid": "2514e288-f3e1-4ac9-adac-e5bc03c7fe79",
        "packetCaptureDiagnosticState": "None",
        "enablePrivateIpAddress": false,
        "isMigrateToCSES": false,
        "ipConfigurations": [
            {
                "name": "default",
                "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-VPN-GW/ipConfigurations/default",
                "etag": "W/\"c29b2eef-4bf8-4826-94fa-cc3a4e468bee\"",
                "type": "Microsoft.Network/virtualNetworkGateways/ipConfigurations",
                "properties": {
                    "provisioningState": "Succeeded",
                    "privateIPAllocationMethod": "Dynamic",
                    # Public IP Addresses: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/public-ip-addresses/get?tabs=HTTP
                    "publicIPAddress": {
                        "name": "East-VNET1-VNG-IP",
                        "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/East-RG1/providers/Microsoft.Network/publicIPAddresses/East-VNET1-VNG-IP",
                        "etag": "W/\"5bbd76c7-0fff-40c5-adac-ad14c81e5b80\"",
                        "location": "eastus",
                        "properties": {
                            "provisioningState": "Succeeded",
                            "resourceGuid": "239090b6-9758-4bda-846f-553fcbffb698",
                            "ipAddress": "52.179.98.177",
                            "publicIPAddressVersion": "IPv4",
                            "publicIPAllocationMethod": "Dynamic",
                            "idleTimeoutInMinutes": 4,
                            "ipTags": [],
                            "ipConfiguration": {
                                "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-VPN-GW/ipConfigurations/default"
                            }
                        },
                        "type": "Microsoft.Network/publicIPAddresses",
                        "sku": {
                            "name": "Basic",
                            "tier": "Regional"
                        }
                    },
                    # Subnet: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/subnets/get?tabs=HTTP
                    "subnet": {
                        "name": "GatewaySubnet",
                        "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworks/East-VNET1/subnets/GatewaySubnet",
                        "etag": "W/\"4ec86895-3aad-471e-84de-177ff56b4442\"",
                        "properties": {
                            "provisioningState": "Succeeded",
                            "addressPrefix": "172.17.11.128/26",
                            "routeTable": {
                                "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/East-RG1/providers/Microsoft.Network/routeTables/East-GW-RT"
                            },
                            "ipConfigurations": [
                                {
                                    "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-Express-GW/ipConfigurations/default"
                                },
                                {
                                    "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-VPN-GW/ipConfigurations/default"
                                }
                            ],
                            "serviceEndpoints": [],
                            "delegations": [],
                            "privateEndpointNetworkPolicies": "Enabled",
                            "privateLinkServiceNetworkPolicies": "Enabled"
                        },
                        "type": "Microsoft.Network/virtualNetworks/subnets"
                    }
                }
            }
        ],
        "natRules": [],
        "virtualNetworkGatewayPolicyGroups": [],
        "enableBgpRouteTranslationForNat": false,
        "disableIPSecReplayProtection": false,
        "sku": {
            "name": "VpnGw1",
            "tier": "VpnGw1",
            "capacity": 2
        },
        "gatewayType": "Vpn",
        "vpnType": "RouteBased",
        "enableBgp": true,
        "activeActive": false,
        "bgpSettings": {
            "asn": 65516,
            "bgpPeeringAddress": "172.17.11.190",
            "peerWeight": 0,
            "bgpPeeringAddresses": [
                {
                    "ipconfigurationId": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-VPN-GW/ipConfigurations/default",
                    "defaultBgpIpAddresses": [
                        "172.17.11.190"
                    ],
                    "customBgpIpAddresses": [],
                    "tunnelIpAddresses": [
                        "52.179.98.177"
                    ]
                }
            ]
        },
        # Virtual Network Peerings: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/virtual-networks/get?source=recommendations&tabs=HTTP
        "remoteVirtualNetworkPeerings": [
            {
                "name": "Spoke-VNET1-To-Hub-VNET",
                "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/virtualNetworks/Spoke-VNET-1/virtualNetworkPeerings/Spoke-VNET1-To-Hub-VNET",
                "etag": "W/\"b53d457b-780d-48de-b8c9-80bc76113d08\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "resourceGuid": "561b78a8-76ca-08e1-0369-e0ba1169bf1e",
                    "peeringState": "Connected",
                    "peeringSyncLevel": "FullyInSync",
                    "remoteVirtualNetwork": {
                        "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworks/East-VNET1"
                    },
                    "allowVirtualNetworkAccess": true,
                    "allowForwardedTraffic": true,
                    "allowGatewayTransit": false,
                    "useRemoteGateways": true,
                    "doNotVerifyRemoteGateways": false,
                    "peerCompleteVnets": true,
                    "remoteGateways": [
                        {
                            "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-Express-GW"
                        }
                    ],
                    "remoteAddressSpace": {
                        "addressPrefixes": [
                            "172.17.11.0/24",
                            "172.17.15.0/24"
                        ]
                    },
                    "remoteVirtualNetworkAddressSpace": {
                        "addressPrefixes": [
                            "172.17.11.0/24",
                            "172.17.15.0/24"
                        ]
                    },
                    "routeServiceVips": {}
                },
                "type": "Microsoft.Network/virtualNetworks/virtualNetworkPeerings"
            },
            {
                "name": "Spoke-VNET3-To-Hub-VNET",
                "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/US-West-RG/providers/Microsoft.Network/virtualNetworks/Spoke-VNET3/virtualNetworkPeerings/Spoke-VNET3-To-Hub-VNET",
                "etag": "W/\"68bb885e-a9e7-42dd-94c2-8966f3f4e693\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "resourceGuid": "a8eb3ef9-5804-05f0-0124-ef526570f25d",
                    "peeringState": "Connected",
                    "peeringSyncLevel": "FullyInSync",
                    "remoteVirtualNetwork": {
                        "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworks/East-VNET1"
                    },
                    "allowVirtualNetworkAccess": true,
                    "allowForwardedTraffic": true,
                    "allowGatewayTransit": false,
                    "useRemoteGateways": true,
                    "doNotVerifyRemoteGateways": false,
                    "peerCompleteVnets": true,
                    "remoteGateways": [
                        {
                            "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-Express-GW"
                        }
                    ],
                    "remoteAddressSpace": {
                        "addressPrefixes": [
                            "172.17.11.0/24",
                            "172.17.15.0/24"
                        ]
                    },
                    "remoteVirtualNetworkAddressSpace": {
                        "addressPrefixes": [
                            "172.17.11.0/24",
                            "172.17.15.0/24"
                        ]
                    },
                    "routeServiceVips": {}
                },
                "type": "Microsoft.Network/virtualNetworks/virtualNetworkPeerings"
            },
            {
                "name": "Spoke-VNET2-To-Hub-VNET",
                "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/Spoke-VNET-2/providers/Microsoft.Network/virtualNetworks/Spoke-VNET-2/virtualNetworkPeerings/Spoke-VNET2-To-Hub-VNET",
                "etag": "W/\"67383cf6-e0af-4102-b54d-6dab5693a6f9\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "resourceGuid": "b5fa35a0-4544-0b61-26e2-cda7eb9f0fe9",
                    "peeringState": "Connected",
                    "peeringSyncLevel": "FullyInSync",
                    "remoteVirtualNetwork": {
                        "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworks/East-VNET1"
                    },
                    "allowVirtualNetworkAccess": true,
                    "allowForwardedTraffic": true,
                    "allowGatewayTransit": false,
                    "useRemoteGateways": true,
                    "doNotVerifyRemoteGateways": false,
                    "peerCompleteVnets": true,
                    "remoteGateways": [
                        {
                            "id": "/subscriptions/073e6f45-d1ae-40fe-93af-88231d2377bd/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-Express-GW"
                        }
                    ],
                    "remoteAddressSpace": {
                        "addressPrefixes": [
                            "172.17.11.0/24",
                            "172.17.15.0/24"
                        ]
                    },
                    "remoteVirtualNetworkAddressSpace": {
                        "addressPrefixes": [
                            "172.17.11.0/24",
                            "172.17.15.0/24"
                        ]
                    },
                    "routeServiceVips": {}
                },
                "type": "Microsoft.Network/virtualNetworks/virtualNetworkPeerings"
            }
        ],
        "vpnGatewayGeneration": "Generation1"
    }
}
```

## Azure Virtual Machine

### Introduction
Configuration feature is not supported for Azure Virtual Machine yet. Please send API to get the resource data instead. Reference: https://github.com/jwei/NetBrain-Cloud-Data-Retrieve-API-R11.1/blob/main/Microsoft%20Azure/Fetch%20Resource%20Simple%20Data.md

