# Usage
To retrieve the configuration data for a resource, you can utilize NetBrain's built-in configuration file function, which does not require coding. This function enables you to quickly obtain the resource configuration.


# Table of Contents
* [Azure Virtual Network Distributed Router](#azure-virtual-network-distributed-router)
* [Azure Virtual Network Gateway](#azure-virtual-network-gateway)
* [Azure Virtual Machine](#azure-virtual-machine)
* [Azure VPN Gateway](#azure-vpn-gateway)
* [Azure ExpressRoute Gateway](#azure-expressroute-gateway)
* [Azure MSEE](#azure-msee)
* [Azure NAT Gateway](#azure-nat-gateway)
* [Azure Firewall](#azure-firewall)
* [Azure Virtual Hub](#azure-virtual-hub)
* [Azure Load Balancer](#azure-load-balancer)
* [Azure Application Gateway](#azure-application-gateway)
* [Azure Private Endpoint](#azure-private-endpoint)
* [Azure Private Link Service](#azure-private-link-service)
* [Azure Service Endpoint](#azure-service-endpoint)


## Azure Virtual Network Distributed Router

### Introduction
The configuration of the Azure virtual network distributed router relies solely on the corresponding Azure API of the virtual network. The Azure API provides detailed information regarding the configuration of the virtual network, including its connectivity, security, etc.

### Content
Below are the Azure APIs used to generate this configuration.
|**Resource/Action**|**Relationship**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Virtual Networks - Get | self | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/virtual-networks/get | 


### Sample
<details><summary>Configuration File</summary>

```json
{
  "netbrainNotes": "This config file is generated via API",
  "netbrainHostName": "test-vnet(<ResourceGroup>)(<Subscription_ID_Prefix>)(VirtualNetworkDistributedRouter)",
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
    "virtualNetworkPeerings": [
      {
        "id": "/subscriptions/subid/resourceGroups/peerTest/providers/Microsoft.Network/virtualNetworks/vnet1/virtualNetworkPeerings/peer2",
        "name": "peer",
        "properties": {
          "allowVirtualNetworkAccess": true,
          "allowForwardedTraffic": false,
          "allowGatewayTransit": false,
          "useRemoteGateways": false,
          "remoteVirtualNetwork": {
            "id": "/subscriptions/subid/resourceGroups/peerTest/providers/Microsoft.Network/virtualNetworks/vnet3"
          },
          "remoteAddressSpace": {
            "addressPrefixes": [
              "13.0.0.0/8"
            ]
          },
          "remoteVirtualNetworkAddressSpace": {
            "addressPrefixes": [
              "13.0.0.0/8"
            ]
          },
          "remoteBgpCommunities": {
            "virtualNetworkCommunity": "12076:20003",
            "regionalCommunity": "12076:50004"
          },
          "peeringState": "Initiated",
          "peeringSyncLevel": "FullyInSync",
          "provisioningState": "Succeeded"
        }
      }
    ]
  }
}
```

</details>
<br />


## Azure Virtual Network Gateway

### Introduction
The configuration of the Azure virtual network gateway is dependent on the Azure API response of the Azure Virtual Network Gateway as the primary response. The full resource configuration consists of some associated resources' API data, including `publicIPAddress`, `subnet`, and `remoteVirtualNetworkPeerings`.

### Content
Below are the Azure APIs used to generate this configuration.
|**Resource/Action**|**Relationship**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Virtual Network Gateways - Get | vnetGateway | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/network-gateway/virtual-network-gateways/get | 
| Public IP Addresses - Get | vnetGateway.properties.ipConfigurations.publicIPAddress | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/public-ip-addresses/get |
| Subnets - Get | vnetGateway.properties.ipConfigurations.subnet | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/subnets/get |
| Virtual Network Peerings - Get | vnetGateway.properties.remoteVirtualNetworkPeerings | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/virtual-networks/get?source=recommendations |

### Sample
<details><summary>Configuration File</summary>

```json
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "East-VPN-GW(<ResourceGroup>)(<Subscription_ID_Prefix>)(VirtualNetworkGateway)",
    "name": "East-VPN-GW",
    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-VPN-GW",
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
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-VPN-GW/ipConfigurations/default",
                "etag": "W/\"c29b2eef-4bf8-4826-94fa-cc3a4e468bee\"",
                "type": "Microsoft.Network/virtualNetworkGateways/ipConfigurations",
                "properties": {
                    "provisioningState": "Succeeded",
                    "privateIPAllocationMethod": "Dynamic",
                    # Public IP Addresses: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/public-ip-addresses/get?tabs=HTTP
                    "publicIPAddress": {
                        "name": "East-VNET1-VNG-IP",
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/publicIPAddresses/East-VNET1-VNG-IP",
                        "etag": "W/\"5bbd76c7-0fff-40c5-adac-ad14c81e5b80\"",
                        "location": "eastus",
                        "properties": {
                            "provisioningState": "Succeeded",
                            "resourceGuid": "239090b6-9758-4bda-846f-553fcbffb698",
                            "ipAddress": "40.85.154.247",
                            "publicIPAddressVersion": "IPv4",
                            "publicIPAllocationMethod": "Dynamic",
                            "idleTimeoutInMinutes": 4,
                            "ipTags": [],
                            "ipConfiguration": {
                                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-VPN-GW/ipConfigurations/default"
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
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworks/East-VNET1/subnets/GatewaySubnet",
                        "etag": "W/\"4ec86895-3aad-471e-84de-177ff56b4442\"",
                        "properties": {
                            "provisioningState": "Succeeded",
                            "addressPrefix": "172.17.11.128/26",
                            "routeTable": {
                                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/routeTables/East-GW-RT"
                            },
                            "ipConfigurations": [
                                {
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-Express-GW/ipConfigurations/default"
                                },
                                {
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-VPN-GW/ipConfigurations/default"
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
                    "ipconfigurationId": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-VPN-GW/ipConfigurations/default",
                    "defaultBgpIpAddresses": [
                        "172.17.11.190"
                    ],
                    "customBgpIpAddresses": [],
                    "tunnelIpAddresses": [
                        "40.85.154.247"
                    ]
                }
            ]
        },
        # Virtual Network Peerings: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/virtual-networks/get?source=recommendations&tabs=HTTP
        "remoteVirtualNetworkPeerings": [
            {
                "name": "Spoke-VNET1-To-Hub-VNET",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/virtualNetworks/Spoke-VNET-1/virtualNetworkPeerings/Spoke-VNET1-To-Hub-VNET",
                "etag": "W/\"b53d457b-780d-48de-b8c9-80bc76113d08\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "resourceGuid": "561b78a8-76ca-08e1-0369-e0ba1169bf1e",
                    "peeringState": "Connected",
                    "peeringSyncLevel": "FullyInSync",
                    "remoteVirtualNetwork": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworks/East-VNET1"
                    },
                    "allowVirtualNetworkAccess": true,
                    "allowForwardedTraffic": true,
                    "allowGatewayTransit": false,
                    "useRemoteGateways": true,
                    "doNotVerifyRemoteGateways": false,
                    "peerCompleteVnets": true,
                    "remoteGateways": [
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-Express-GW"
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
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/US-West-RG/providers/Microsoft.Network/virtualNetworks/Spoke-VNET3/virtualNetworkPeerings/Spoke-VNET3-To-Hub-VNET",
                "etag": "W/\"68bb885e-a9e7-42dd-94c2-8966f3f4e693\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "resourceGuid": "a8eb3ef9-5804-05f0-0124-ef526570f25d",
                    "peeringState": "Connected",
                    "peeringSyncLevel": "FullyInSync",
                    "remoteVirtualNetwork": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworks/East-VNET1"
                    },
                    "allowVirtualNetworkAccess": true,
                    "allowForwardedTraffic": true,
                    "allowGatewayTransit": false,
                    "useRemoteGateways": true,
                    "doNotVerifyRemoteGateways": false,
                    "peerCompleteVnets": true,
                    "remoteGateways": [
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-Express-GW"
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
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-2/providers/Microsoft.Network/virtualNetworks/Spoke-VNET-2/virtualNetworkPeerings/Spoke-VNET2-To-Hub-VNET",
                "etag": "W/\"67383cf6-e0af-4102-b54d-6dab5693a6f9\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "resourceGuid": "b5fa35a0-4544-0b61-26e2-cda7eb9f0fe9",
                    "peeringState": "Connected",
                    "peeringSyncLevel": "FullyInSync",
                    "remoteVirtualNetwork": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworks/East-VNET1"
                    },
                    "allowVirtualNetworkAccess": true,
                    "allowForwardedTraffic": true,
                    "allowGatewayTransit": false,
                    "useRemoteGateways": true,
                    "doNotVerifyRemoteGateways": false,
                    "peerCompleteVnets": true,
                    "remoteGateways": [
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworkGateways/East-Express-GW"
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

</details>
<br />


## Azure Virtual Machine

### Introduction
Configuration feature is not supported for Azure Virtual Machine yet. Please send API to get the resource data instead. Reference: https://github.com/jwei/NetBrain-Cloud-Data-Retrieve-API-R11.1/blob/main/Microsoft%20Azure/Fetch%20Resource%20Simple%20Data.md


## Azure VPN Gateway

### Introduction
The configuration of the Azure VPN gateway is dependent on the Azure API response of the Azure VPN gateway as the primary response. The full resource configuration consists of some associated resources' API data, including `remoteVpnSite`, `vpnSiteLink`.

### Content
Below are the Azure APIs used to generate this configuration.
|**Resource/Action**|**Relationship**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Virtual Networks - Get | self | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/virtual-networks/get | 
| Vpn Sites - Get | properties.connections.properties.remoteVpnSite | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualwan/vpn-sites/get | 
| Vpn Site Links - Get | properties.connections.properties.vpnLinkConnections.properties.vpnSiteLink | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualwan/vpn-site-links/get | 


### Sample
<details><summary>Configuration File</summary>

```json
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "e53bd582834840239c034dae44bfacc1-westus-gw(<ResourceGroup>)(<Subscription_ID_Prefix>)(VpnGateway)",
    "name": "e53bd582834840239c034dae44bfacc1-westus-gw",
    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/vpnGateways/e53bd582834840239c034dae44bfacc1-westus-gw",
    "etag": "W/\"597fb38a-3155-4d30-9b73-061035052cf4\"",
    "type": "Microsoft.Network/vpnGateways",
    "location": "westus",
    "properties": {
        "provisioningState": "Succeeded",
        "connections": [
            {
                "name": "Connection-VPNSite-NoBGP-Test",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/vpnGateways/e53bd582834840239c034dae44bfacc1-westus-gw/vpnConnections/Connection-VPNSite-NoBGP-Test",
                "etag": "W/\"597fb38a-3155-4d30-9b73-061035052cf4\"",
                "type": "Microsoft.Network/vpnGateways/vpnConnections",
                "properties": {
                    "provisioningState": "Succeeded",
                    "routingConfiguration": {
                        "associatedRouteTable": {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualHubs/West-VHUB/hubRouteTables/defaultRouteTable"
                        },
                        "propagatedRouteTables": {
                            "labels": [
                                "none"
                            ],
                            "ids": [
                                {
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualHubs/West-VHUB/hubRouteTables/noneRouteTable"
                                }
                            ]
                        },
                        "vnetRoutes": {
                            "staticRoutes": []
                        }
                    },
                    "enableInternetSecurity": false,
                    # Vpn Sites: https://learn.microsoft.com/en-us/rest/api/virtualwan/vpn-sites/get
                    "remoteVpnSite": {
                        "name": "VPNSite-NoBGP-Test",
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/vpnSites/VPNSite-NoBGP-Test",
                        "etag": "W/\"6ce821df-7a86-482b-99b7-9dace1ecbb46\"",
                        "type": "Microsoft.Network/vpnSites",
                        "location": "westus",
                        "properties": {
                            "provisioningState": "Succeeded",
                            "addressSpace": {
                                "addressPrefixes": [
                                    "172.17.37.0/24"
                                ]
                            },
                            "deviceProperties": {
                                "deviceVendor": "NetBrain",
                                "linkSpeedInMbps": 0
                            },
                            "virtualWan": {
                                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualWans/VWAN-TO-BUR"
                            },
                            "isSecuritySite": false,
                            "o365Policy": {
                                "breakOutCategories": {
                                    "optimize": false,
                                    "allow": false,
                                    "default": false
                                }
                            },
                            # VPN Site Links: https://learn.microsoft.com/en-us/rest/api/virtualwan/vpn-site-links/get  
                            "vpnSiteLinks": [
                                {
                                    "name": "Burlington-Fortigate",
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/vpnSites/VPNSite-NoBGP-Test/vpnSiteLinks/Burlington-Fortigate",
                                    "etag": "W/\"6ce821df-7a86-482b-99b7-9dace1ecbb46\"",
                                    "properties": {
                                        "provisioningState": "Succeeded",
                                        "ipAddress": "40.85.154.247",
                                        "linkProperties": {
                                            "linkProviderName": "NetBrain",
                                            "linkSpeedInMbps": 50
                                        }
                                    },
                                    "type": "Microsoft.Network/vpnSites/vpnSiteLinks"
                                },
                                {
                                    "name": "Burlington-ASA",
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/vpnSites/VPNSite-NoBGP-Test/vpnSiteLinks/Burlington-ASA",
                                    "etag": "W/\"6ce821df-7a86-482b-99b7-9dace1ecbb46\"",
                                    "properties": {
                                        "provisioningState": "Succeeded",
                                        "ipAddress": "40.85.154.247",
                                        "linkProperties": {
                                            "linkProviderName": "NetBrain",
                                            "linkSpeedInMbps": 50
                                        }
                                    },
                                    "type": "Microsoft.Network/vpnSites/vpnSiteLinks"
                                }
                            ]
                        }
                    },
                    "vpnLinkConnections": [
                        {
                            "name": "Burlington-Fortigate",
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/vpnGateways/e53bd582834840239c034dae44bfacc1-westus-gw/vpnConnections/Connection-VPNSite-NoBGP-Test/vpnLinkConnections/Burlington-Fortigate",
                            "etag": "W/\"597fb38a-3155-4d30-9b73-061035052cf4\"",
                            "properties": {
                                "provisioningState": "Succeeded",
                                "vpnSiteLink": {
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/vpnSites/VPNSite-NoBGP-Test/vpnSiteLinks/Burlington-Fortigate"
                                },
                                "connectionBandwidth": 10,
                                "ipsecPolicies": [],
                                "vpnConnectionProtocolType": "IKEv2",
                                "sharedKey": "Netbrain123!",
                                "ingressBytesTransferred": 0,
                                "egressBytesTransferred": 0,
                                "packetCaptureDiagnosticState": "None",
                                "connectionStatusDetails": [],
                                "enableBgp": false,
                                "enableRateLimiting": false,
                                "useLocalAzureIpAddress": false,
                                "usePolicyBasedTrafficSelectors": false,
                                "routingWeight": 0,
                                "dpdTimeoutSeconds": 0,
                                "vpnLinkConnectionMode": "Default",
                                "vpnGatewayCustomBgpAddresses": []
                            },
                            "type": "Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections"
                        },
                        {
                            "name": "Burlington-ASA",
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/vpnGateways/e53bd582834840239c034dae44bfacc1-westus-gw/vpnConnections/Connection-VPNSite-NoBGP-Test/vpnLinkConnections/Burlington-ASA",
                            "etag": "W/\"597fb38a-3155-4d30-9b73-061035052cf4\"",
                            "properties": {
                                "provisioningState": "Succeeded",
                                "vpnSiteLink": {
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/vpnSites/VPNSite-NoBGP-Test/vpnSiteLinks/Burlington-ASA"
                                },
                                "connectionBandwidth": 10,
                                "ipsecPolicies": [],
                                "vpnConnectionProtocolType": "IKEv2",
                                "sharedKey": "Netbrain123!",
                                "ingressBytesTransferred": 0,
                                "egressBytesTransferred": 0,
                                "packetCaptureDiagnosticState": "None",
                                "connectionStatusDetails": [],
                                "enableBgp": false,
                                "enableRateLimiting": false,
                                "useLocalAzureIpAddress": false,
                                "usePolicyBasedTrafficSelectors": false,
                                "routingWeight": 0,
                                "dpdTimeoutSeconds": 0,
                                "vpnLinkConnectionMode": "Default",
                                "vpnGatewayCustomBgpAddresses": []
                            },
                            "type": "Microsoft.Network/vpnGateways/vpnConnections/vpnLinkConnections"
                        }
                    ],
                    "ingressBytesTransferred": 0,
                    "egressBytesTransferred": 0
                }
            }
        ],
        "virtualHub": {
            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualHubs/West-VHUB"
        },
        "bgpSettings": {
            "asn": 65515,
            "peerWeight": 0,
            "bgpPeeringAddresses": [
                {
                    "ipconfigurationId": "Instance0",
                    "defaultBgpIpAddresses": [
                        "172.17.25.14"
                    ],
                    "customBgpIpAddresses": [],
                    "tunnelIpAddresses": [
                        "20.157.87.52",
                        "172.17.25.6"
                    ]
                },
                {
                    "ipconfigurationId": "Instance1",
                    "defaultBgpIpAddresses": [
                        "172.17.25.15"
                    ],
                    "customBgpIpAddresses": [],
                    "tunnelIpAddresses": [
                        "20.157.87.54",
                        "172.17.25.7"
                    ]
                }
            ]
        },
        "vpnGatewayScaleUnit": 1,
        "packetCaptureDiagnosticState": "Failed",
        "ipConfigurations": [
            {
                "id": "Instance0",
                "publicIpAddress": "20.157.87.52",
                "privateIpAddress": "172.17.25.6"
            },
            {
                "id": "Instance1",
                "publicIpAddress": "20.157.87.54",
                "privateIpAddress": "172.17.25.7"
            }
        ],
        "natRules": [],
        "enableBgpRouteTranslationForNat": false,
        "isRoutingPreferenceInternet": true
    }
}
```

</details>
<br />

## Azure ExpressRoute Gateway

### Introduction
The configuration of the Azure express route gateway is dependent on the Azure API response of the Azure express route gateway as the primary response. The full resource configuration consists of some associated resources' API data, including `expressRouteCircuitPeering`.

### Content
Below are the Azure APIs used to generate this configuration.
|**Resource/Action**|**Relationship**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Express Route Gateways - Get | self | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/expressroute/express-route-gateways/get | 
| Express Route Circuits - Get | properties.expressRouteConnections.properties.expressRouteCircuitPeering | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/expressroute/express-route-circuits/get | 


### Sample
<details><summary>Configuration File</summary>

```json
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "947de39baaf54512b65930c2300c7ded-eastus-er-gw(<ResourceGroup>)(<Subscription_ID_Prefix>)(ExpressRouteGateway)",
    "name": "947de39baaf54512b65930c2300c7ded-eastus-er-gw",
    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/expressRouteGateways/947de39baaf54512b65930c2300c7ded-eastus-er-gw",
    "etag": "W/\"ea450342-3433-4929-a9b0-c6041a799704\"",
    "type": "Microsoft.Network/expressRouteGateways",
    "location": "eastus",
    "properties": {
        "provisioningState": "Succeeded",
        "resourceGuid": "211f05d4-17c0-4eab-953f-5ffe3ec13db3",
        "virtualHub": {
            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualHubs/East-VHUB"
        },
        "expressRouteConnections": [
            {
                "name": "ExRConnection-eastus-1596986809931",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/expressRouteGateways/947de39baaf54512b65930c2300c7ded-eastus-er-gw/expressRouteConnections/ExRConnection-eastus-1596986809931",
                "etag": "W/\"ea450342-3433-4929-a9b0-c6041a799704\"",
                "type": "Microsoft.Network/expressRouteGateways/expressRouteConnections",
                "properties": {
                    "provisioningState": "Succeeded",
                    "resourceGuid": "225f6ef1-4c33-425c-a038-06ae813678ae",
                    "routingConfiguration": {
                        "associatedRouteTable": {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualHubs/East-VHUB/hubRouteTables/defaultRouteTable"
                        },
                        "propagatedRouteTables": {
                            "labels": [
                                "default"
                            ],
                            "ids": [
                                {
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualHubs/East-VHUB/hubRouteTables/defaultRouteTable"
                                },
                                {
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualHubs/East-VHUB/hubRouteTables/DefaultRouteTable"
                                }
                            ]
                        },
                        "vnetRoutes": {
                            "staticRoutes": []
                        }
                    },
                    # Express Route Circuits: https://learn.microsoft.com/en-us/rest/api/expressroute/express-route-circuits/get
                    "expressRouteCircuitPeering": {
                        "name": "AzurePrivatePeering",
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/expressRouteCircuits/Bur-Netbond/peerings/AzurePrivatePeering",
                        "etag": "W/\"292809ed-199b-4b54-b3ea-33dae90bfd4a\"",
                        "properties": {
                            "provisioningState": "Succeeded",
                            "peeringType": "AzurePrivatePeering",
                            "azureASN": 12076,
                            "peerASN": 8030,
                            "primaryPeerAddressPrefix": "172.17.254.8/30",
                            "secondaryPeerAddressPrefix": "172.17.254.12/30",
                            "primaryAzurePort": "<primaryAzurePort>",
                            "secondaryAzurePort": "<secondaryAzurePort>",
                            "state": "Enabled",
                            "vlanId": 1,
                            "gatewayManagerEtag": "7",
                            "lastModifiedBy": "Customer",
                            "microsoftPeeringConfig": {
                                "advertisedPublicPrefixes": [],
                                "advertisedCommunities": [],
                                "advertisedPublicPrefixesState": "NotConfigured",
                                "customerASN": 0,
                                "legacyMode": 0,
                                "routingRegistryName": "NONE"
                            },
                            "connections": [],
                            "peeredConnections": []
                        },
                        "type": "Microsoft.Network/expressRouteCircuits/peerings"
                    },
                    "routingWeight": 0,
                    "enableInternetSecurity": false
                }
            }
        ],
        "autoScaleConfiguration": {
            "bounds": {
                "min": 1
            }
        }
    }
}
```

</details>
<br />

## Azure MSEE

### Introduction
The configuration of the Azure MSEE relies solely on the corresponding Azure API response of the Azure express route circuit.

### Content
Below are the Azure APIs used to generate this configuration.
|**Resource/Action**|**Relationship**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Express Route Circuits - Get | self | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/expressroute/express-route-circuits/get | 


### Sample
<details><summary>Configuration File</summary>

```json
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "Bur-Netbond(Primary)(<ResourceGroup>)(<Subscription_ID_Prefix>)(MSEE)",
    "name": "Bur-Netbond",
    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/expressRouteCircuits/Bur-Netbond",
    "etag": "W/\"292809ed-199b-4b54-b3ea-33dae90bfd4a\"",
    "type": "Microsoft.Network/expressRouteCircuits",
    "location": "eastus",
    "properties": {
        "provisioningState": "Succeeded",
        "resourceGuid": "4bdbc638-ac36-49c9-a053-66a2a385a5c7",
        "peerings": [
            {
                "name": "AzurePrivatePeering",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/expressRouteCircuits/Bur-Netbond/peerings/AzurePrivatePeering",
                "etag": "W/\"292809ed-199b-4b54-b3ea-33dae90bfd4a\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "peeringType": "AzurePrivatePeering",
                    "azureASN": 12076,
                    "peerASN": 8030,
                    "primaryPeerAddressPrefix": "172.17.254.8/30",
                    "secondaryPeerAddressPrefix": "172.17.254.12/30",
                    "primaryAzurePort": "",
                    "secondaryAzurePort": "",
                    "state": "Enabled",
                    "vlanId": 1,
                    "gatewayManagerEtag": "7",
                    "lastModifiedBy": "Customer",
                    "microsoftPeeringConfig": {
                        "advertisedPublicPrefixes": [],
                        "advertisedCommunities": [],
                        "advertisedPublicPrefixesState": "NotConfigured",
                        "customerASN": 0,
                        "legacyMode": 0,
                        "routingRegistryName": "NONE"
                    },
                    "connections": [],
                    "peeredConnections": []
                },
                "type": "Microsoft.Network/expressRouteCircuits/peerings"
            }
        ],
        "authorizations": [
            {
                "name": "MyAuthorization2",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/expressRouteCircuits/Bur-Netbond/authorizations/MyAuthorization2",
                "etag": "W/\"292809ed-199b-4b54-b3ea-33dae90bfd4a\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "authorizationKey": "58ad0e96-938d-48d1-9f74-8087f5b7f19b",
                    "authorizationUseStatus": "Available"
                },
                "type": "Microsoft.Network/expressRouteCircuits/authorizations"
            },
            {
                "name": "MyAuthorization3",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/expressRouteCircuits/Bur-Netbond/authorizations/MyAuthorization3",
                "etag": "W/\"292809ed-199b-4b54-b3ea-33dae90bfd4a\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "authorizationKey": "28ea8385-ad29-4413-810f-4d1709c5df7d",
                    "authorizationUseStatus": "Used"
                },
                "type": "Microsoft.Network/expressRouteCircuits/authorizations"
            },
            {
                "name": "MyAuthorization4",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/expressRouteCircuits/Bur-Netbond/authorizations/MyAuthorization4",
                "etag": "W/\"292809ed-199b-4b54-b3ea-33dae90bfd4a\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "authorizationKey": "5fe58c3e-72c0-4310-8993-9b8168b7636b",
                    "authorizationUseStatus": "Used"
                },
                "type": "Microsoft.Network/expressRouteCircuits/authorizations"
            },
            {
                "name": "2ed-AD-Auth",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/expressRouteCircuits/Bur-Netbond/authorizations/2ed-AD-Auth",
                "etag": "W/\"292809ed-199b-4b54-b3ea-33dae90bfd4a\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "authorizationKey": "f84ace51-d05d-4bdd-a053-8b659cc8dcc3",
                    "authorizationUseStatus": "Available"
                },
                "type": "Microsoft.Network/expressRouteCircuits/authorizations"
            },
            {
                "name": "publi",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/expressRouteCircuits/Bur-Netbond/authorizations/publi",
                "etag": "W/\"292809ed-199b-4b54-b3ea-33dae90bfd4a\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "authorizationKey": "29c5ae03-af13-4a1a-925d-db29f759499a",
                    "authorizationUseStatus": "Available"
                },
                "type": "Microsoft.Network/expressRouteCircuits/authorizations"
            },
            {
                "name": "2ed-AD-Auth-Canada-Central",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/expressRouteCircuits/Bur-Netbond/authorizations/2ed-AD-Auth-Canada-Central",
                "etag": "W/\"292809ed-199b-4b54-b3ea-33dae90bfd4a\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "authorizationKey": "eb4c073f-df57-4e20-ba8d-2dd2045aa873",
                    "authorizationUseStatus": "Available"
                },
                "type": "Microsoft.Network/expressRouteCircuits/authorizations"
            },
            {
                "name": "2ed-AD-VWAN",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/expressRouteCircuits/Bur-Netbond/authorizations/2ed-AD-VWAN",
                "etag": "W/\"292809ed-199b-4b54-b3ea-33dae90bfd4a\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "authorizationKey": "dec6f56c-9223-4456-8c6d-3977b329bff6",
                    "authorizationUseStatus": "Used"
                },
                "type": "Microsoft.Network/expressRouteCircuits/authorizations"
            },
            {
                "name": "to-West-VHUB",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/expressRouteCircuits/Bur-Netbond/authorizations/to-West-VHUB",
                "etag": "W/\"292809ed-199b-4b54-b3ea-33dae90bfd4a\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "authorizationKey": "2821adf4-0cd9-4a62-95d5-ccee110d7daf",
                    "authorizationUseStatus": "Available"
                },
                "type": "Microsoft.Network/expressRouteCircuits/authorizations"
            }
        ],
        "serviceProviderProperties": {
            "serviceProviderName": "AT&T Netbond",
            "peeringLocation": "Chicago",
            "bandwidthInMbps": 50
        },
        "circuitProvisioningState": "Enabled",
        "allowClassicOperations": false,
        "gatewayManagerEtag": "7",
        "serviceKey": "7db0a77d-97cc-4040-aab7-99e3f37ac5b0",
        "serviceProviderProvisioningState": "Provisioned",
        "allowGlobalReach": false,
        "globalReachEnabled": false,
        "stag": 8
    },
    "sku": {
        "name": "Standard_MeteredData",
        "tier": "Premium",
        "family": "MeteredData"
    }
}
```

</details>
<br />

## Azure NAT Gateway

### Introduction
The configuration of the Azure NAT gateway is dependent on the Azure API response of the Azure NAT gateway as the primary response. The full resource configuration consists of some associated resources' API data, including `expressRouteCircuitPeering`, `publicIpAddresses` and `subnets`.

### Content
Below are the Azure APIs used to generate this configuration.
|**Resource/Action**|**Relationship**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Nat Gateways - Get | self | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/nat-gateways/get | 
| Public IP Addresses - Get | properties.publicIpAddresses | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/public-ip-addresses/get | 
| Subnets - Get | properties.subnets | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/subnets/get | 


### Sample
<details><summary>Configuration File</summary>

```json
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "Spoke-VNET-2-NAT-Gateway(<ResourceGroup>)(<Subscription_ID_Prefix>)(NatGateway)",
    "name": "Spoke-VNET-2-NAT-Gateway",
    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-2/providers/Microsoft.Network/natGateways/Spoke-VNET-2-NAT-Gateway",
    "etag": "W/\"e3d27ab0-77c0-4593-9599-afa06a4fa589\"",
    "type": "Microsoft.Network/natGateways",
    "location": "eastus2",
    "tags": {},
    "zones": [
        "1"
    ],
    "properties": {
        "provisioningState": "Succeeded",
        "resourceGuid": "844eadf7-7b17-4db8-a5cd-632a0b16ff51",
        "idleTimeoutInMinutes": 10,
        # Public IP Addresses: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/public-ip-addresses/get
        "publicIpAddresses": [
            {
                "name": "NAT-Public-IP",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-2/providers/Microsoft.Network/publicIPAddresses/NAT-Public-IP",
                "etag": "W/\"d4d9e43a-2ea7-4534-a6d3-63b3d8a79099\"",
                "location": "eastus2",
                "zones": [
                    "1"
                ],
                "properties": {
                    "provisioningState": "Succeeded",
                    "resourceGuid": "a28a34ab-c9c4-4d56-a49e-644868e7b9b8",
                    "natGateway": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-2/providers/Microsoft.Network/natGateways/Spoke-VNET-2-NAT-Gateway"
                    },
                    "ipAddress": "20.186.58.35",
                    "publicIPAddressVersion": "IPv4",
                    "publicIPAllocationMethod": "Static",
                    "idleTimeoutInMinutes": 4,
                    "ipTags": []
                },
                "type": "Microsoft.Network/publicIPAddresses",
                "sku": {
                    "name": "Standard",
                    "tier": "Regional"
                }
            }
        ],
        "publicIpPrefixes": [
            {
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-2/providers/Microsoft.Network/publicIPPrefixes/20.186.58.30"
            }
        ],
        # Subnets: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/subnets/get
        "subnets": [
            {
                "name": "AzureFirewallSubnet",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/US-West-RG/providers/Microsoft.Network/virtualNetworks/Spoke-VNET3/subnets/AzureFirewallSubnet",
                "etag": "W/\"e88d699c-7496-499c-b1d4-2c6bebe9a91d\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "addressPrefix": "172.17.16.64/26",
                    "ipConfigurations": [
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/US-West-RG/providers/Microsoft.Network/azureFirewalls/Spoke-3-Firewall/azureFirewallIpConfigurations/Spoke-3-Firewall"
                        }
                    ],
                    "serviceEndpoints": [
                        {
                            "provisioningState": "Succeeded",
                            "service": "Microsoft.Storage",
                            "locations": [
                                "westus",
                                "eastus"
                            ]
                        }
                    ],
                    "delegations": [],
                    "privateEndpointNetworkPolicies": "Enabled",
                    "privateLinkServiceNetworkPolicies": "Enabled"
                },
                "type": "Microsoft.Network/virtualNetworks/subnets"
            }
        ]
    },
    "sku": {
        "name": "Standard",
        "tier": "Regional"
    }
}
```

</details>
<br />

## Azure Firewall

### Introduction
The configuration of the Azure firewall is dependent on the Azure API response of the Azure firewall as the primary response. The full resource configuration consists of some associated resources' API data, including `publicIPAddress`, `subnet`.

### Content
Below are the Azure APIs used to generate this configuration.
|**Resource/Action**|**Relationship**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Azure Firewalls - Get | self | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/firewall/azure-firewalls/get | 
| Public IP Addresses - Get | properties.ipConfigurations.properties.publicIPAddress | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/public-ip-addresses/get | 
| Subnets - Get | properties.ipConfigurations.properties.subnet | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/subnets/get | 


### Sample
<details><summary>Configuration File</summary>

```json
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "Spoke-3-Firewall(<ResourceGroup>)(<Subscription_ID_Prefix>)(AzureFirewall)",
    "name": "Spoke-3-Firewall",
    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/US-West-RG/providers/Microsoft.Network/azureFirewalls/Spoke-3-Firewall",
    "etag": "W/\"8347fd01-ac03-4648-8c0d-6c6189c7bbeb\"",
    "type": "Microsoft.Network/azureFirewalls",
    "location": "westus",
    "properties": {
        "provisioningState": "Succeeded",
        "sku": {
            "name": "AZFW_VNet",
            "tier": "Standard"
        },
        "threatIntelMode": "Alert",
        "additionalProperties": {},
        "ipConfigurations": [
            {
                "name": "Spoke-3-Firewall",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/US-West-RG/providers/Microsoft.Network/azureFirewalls/Spoke-3-Firewall/azureFirewallIpConfigurations/Spoke-3-Firewall",
                "etag": "W/\"8347fd01-ac03-4648-8c0d-6c6189c7bbeb\"",
                "type": "Microsoft.Network/azureFirewalls/azureFirewallIpConfigurations",
                "properties": {
                    "provisioningState": "Succeeded",
                    "privateIPAddress": "172.17.16.68",
                    "privateIPAllocationMethod": "Dynamic",
                    # Public IP Addresses: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/public-ip-addresses/get
                    "publicIPAddress": {
                        "name": "Spoke-3-Firewall",
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/US-West-RG/providers/Microsoft.Network/publicIPAddresses/Spoke-3-Firewall",
                        "etag": "W/\"800ab353-201f-4115-a096-278422739076\"",
                        "location": "westus",
                        "tags": {},
                        "properties": {
                            "provisioningState": "Succeeded",
                            "resourceGuid": "cacc4e88-23b2-43ad-a06a-c165bbccc5d6",
                            "ipAddress": "40.85.154.247",
                            "publicIPAddressVersion": "IPv4",
                            "publicIPAllocationMethod": "Static",
                            "idleTimeoutInMinutes": 4,
                            "ipTags": [],
                            "ipConfiguration": {
                                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/US-West-RG/providers/Microsoft.Network/azureFirewalls/Spoke-3-Firewall/azureFirewallIpConfigurations/Spoke-3-Firewall"
                            }
                        },
                        "type": "Microsoft.Network/publicIPAddresses",
                        "sku": {
                            "name": "Standard",
                            "tier": "Regional"
                        }
                    },
                    # Subnets: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/subnets/get
                    "subnet": {
                        "name": "AzureFirewallSubnet",
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/US-West-RG/providers/Microsoft.Network/virtualNetworks/Spoke-VNET3/subnets/AzureFirewallSubnet",
                        "etag": "W/\"e88d699c-7496-499c-b1d4-2c6bebe9a91d\"",
                        "properties": {
                            "provisioningState": "Succeeded",
                            "addressPrefix": "172.17.16.64/26",
                            "ipConfigurations": [
                                {
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/US-West-RG/providers/Microsoft.Network/azureFirewalls/Spoke-3-Firewall/azureFirewallIpConfigurations/Spoke-3-Firewall"
                                }
                            ],
                            "serviceEndpoints": [
                                {
                                    "provisioningState": "Succeeded",
                                    "service": "Microsoft.Storage",
                                    "locations": [
                                        "westus",
                                        "eastus"
                                    ]
                                }
                            ],
                            "delegations": [],
                            "privateEndpointNetworkPolicies": "Enabled",
                            "privateLinkServiceNetworkPolicies": "Enabled"
                        },
                        "type": "Microsoft.Network/virtualNetworks/subnets"
                    }
                }
            }
        ],
        "networkRuleCollections": [],
        "applicationRuleCollections": [],
        "natRuleCollections": [],
        "firewallPolicy": {
            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourcegroups/US-West-RG/providers/Microsoft.Network/firewallPolicies/AzurePathTest-FW"
        }
    }
}
```

</details>
<br />

## Azure Virtual Hub

### Introduction
The configuration of the Azure virtual hub is dependent on the Azure API response of the Azure virtual hub as the primary response. The full resource configuration consists of some associated resources' API data, including `virtualWan`, `vpnSites`.

### Content
Below are the Azure APIs used to generate this configuration.
|**Resource/Action**|**Relationship**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Virtual Hubs - Get | self | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualwan/virtual-hubs/get | 
| Virtual Wans - Get | properties.virtualWan | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualwan/virtual-wans/get |
| Vpn Sites - Get | properties.virtualWan.properties.vpnSites | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualwan/vpn-sites/get |


### Sample
<details><summary>Configuration File</summary>

```json
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "East-VHUB(<ResourceGroup>)(<Subscription_ID_Prefix>)(VirtualHub)",
    "name": "East-VHUB",
    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualHubs/East-VHUB",
    "etag": "W/\"729f33a3-a3a3-4377-bb14-715b592740c2\"",
    "type": "Microsoft.Network/virtualHubs",
    "location": "eastus",
    "properties": {
        "provisioningState": "Succeeded",
        "virtualHubRouteTableV2s": [],
        "addressPrefix": "172.17.253.0/24",
        "virtualRouterAsn": 65515,
        "virtualRouterIps": [
            "172.17.253.104",
            "172.17.253.105"
        ],
        "routeTable": {
            "routes": []
        },
        "virtualRouterAutoScaleConfiguration": {
            "minCapacity": 2
        },
        # Virtual Wans: https://learn.microsoft.com/en-us/rest/api/virtualwan/virtual-wans/get
        "virtualWan": {
            "name": "VWAN-TO-BUR",
            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualWans/VWAN-TO-BUR",
            "etag": "W/\"f6e2942d-c798-43ab-9f76-9295a61ce2e0\"",
            "type": "Microsoft.Network/virtualWans",
            "location": "eastus",
            "tags": {
                "DEMO-LAB": "NO CHANGE"
            },
            "properties": {
                "provisioningState": "Succeeded",
                "disableVpnEncryption": false,
                "allowBranchToBranchTraffic": true,
                "office365LocalBreakoutCategory": "None",
                "type": "Standard",
                "virtualHubs": [
                    {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualHubs/East-VHUB"
                    },
                    {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualHubs/West-VHUB"
                    }
                ],
                # Vpn Sites: https://learn.microsoft.com/en-us/rest/api/virtualwan/vpn-sites/get
                "vpnSites": [
                    {
                        "name": "Burlington",
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/vpnSites/Burlington",
                        "etag": "W/\"d5398329-a48a-4c0f-8d54-8095f55b445d\"",
                        "type": "Microsoft.Network/vpnSites",
                        "location": "eastus",
                        "properties": {
                            "provisioningState": "Succeeded",
                            "addressSpace": {
                                "addressPrefixes": [
                                    "172.17.251.0/30",
                                    "172.17.251.4/30"
                                ]
                            },
                            "deviceProperties": {
                                "deviceVendor": "Cisco",
                                "linkSpeedInMbps": 0
                            },
                            "virtualWan": {
                                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualWans/VWAN-TO-BUR"
                            },
                            "isSecuritySite": false,
                            "o365Policy": {
                                "breakOutCategories": {
                                    "optimize": false,
                                    "allow": false,
                                    "default": false
                                }
                            },
                            "vpnSiteLinks": [
                                {
                                    "name": "To-Lab-ASA",
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/vpnSites/Burlington/vpnSiteLinks/To-Lab-ASA",
                                    "etag": "W/\"d5398329-a48a-4c0f-8d54-8095f55b445d\"",
                                    "properties": {
                                        "provisioningState": "Succeeded",
                                        "ipAddress": "40.85.154.247",
                                        "bgpProperties": {
                                            "asn": 64666,
                                            "bgpPeeringAddress": "172.17.251.1"
                                        },
                                        "linkProperties": {
                                            "linkProviderName": "Crown Castle",
                                            "linkSpeedInMbps": 1
                                        }
                                    },
                                    "type": "Microsoft.Network/vpnSites/vpnSiteLinks"
                                },
                                {
                                    "name": "To-Bur-Fortigate",
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/vpnSites/Burlington/vpnSiteLinks/To-Bur-Fortigate",
                                    "etag": "W/\"d5398329-a48a-4c0f-8d54-8095f55b445d\"",
                                    "properties": {
                                        "provisioningState": "Succeeded",
                                        "ipAddress": "40.85.154.247",
                                        "bgpProperties": {
                                            "asn": 64665,
                                            "bgpPeeringAddress": "172.17.251.5"
                                        },
                                        "linkProperties": {
                                            "linkProviderName": "Crown Castle",
                                            "linkSpeedInMbps": 1
                                        }
                                    },
                                    "type": "Microsoft.Network/vpnSites/vpnSiteLinks"
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "vpnGateway": {
            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/vpnGateways/a139004e542a42b9a685e94e4401e7ed-eastus-gw"
        },
        "expressRouteGateway": {
            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/expressRouteGateways/947de39baaf54512b65930c2300c7ded-eastus-er-gw"
        },
        "networkVirtualAppliances": [],
        "routingState": "Provisioned",
        "allowBranchToBranchTraffic": false,
        "preferredRoutingGateway": "ExpressRoute",
        "hubRoutingPreference": "ExpressRoute"
    }
}
```

</details>
<br />

## Azure Load Balancer

### Introduction
The configuration of the Azure load balancer is dependent on the Azure API response of the Azure load balancer as the primary response. The full resource configuration consists of some associated resources' API data, including `virtualWan`, `vpnSites`.

### Content
Below are the Azure APIs used to generate this configuration.
|**Resource/Action**|**Relationship**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Load Balancers - Get | self | 2021-08-01 | https://docs.microsoft.com/en-us/rest/api/load-balancer/load-balancers/get | 
| Public IP Addresses - Get | properties.frontendIPConfigurations.properties.publicIPAddress | 2021-08-01 | https://docs.microsoft.com/en-us/rest/api/virtualnetwork/public-ip-addresses/get | 
| Network Interface IP Configurations - Get | properties.backendAddressPools.properties.backendIPConfigurations | 2021-08-01 | https://docs.microsoft.com/en-us/rest/api/virtualnetwork/network-interface-ip-configurations/get | 
| Network Interface IP Configurations - Get | properties.backendAddressPools.properties.loadBalancerBackendAddresses.properties.networkInterfaceIPConfiguration | 2021-08-01 | https://docs.microsoft.com/en-us/rest/api/virtualnetwork/network-interface-ip-configurations/get | 


### Sample
<details><summary>Configuration File</summary>

```json
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "VNET-1-Private-Load-Balancer(<ResourceGroup>)(<Subscription_ID_Prefix>)(LoadBalancer)",
    "name": "VNET-1-Private-Load-Balancer",
    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer",
    "etag": "W/\"7f1ec08b-d06a-4c25-88d0-d29f847904b1\"",
    "type": "Microsoft.Network/loadBalancers",
    "location": "westus2",
    "tags": {},
    "properties": {
        "provisioningState": "Succeeded",
        "resourceGuid": "cdd67be5-2871-430c-9693-6a142ea3ca15",
        "frontendIPConfigurations": [
            {
                "name": "LoadBalancerFrontEnd",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/frontendIPConfigurations/LoadBalancerFrontEnd",
                "etag": "W/\"7f1ec08b-d06a-4c25-88d0-d29f847904b1\"",
                "type": "Microsoft.Network/loadBalancers/frontendIPConfigurations",
                "properties": {
                    "provisioningState": "Succeeded",
                    "privateIPAddress": "172.17.12.20",
                    "privateIPAllocationMethod": "Static",
                    "subnet": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/virtualNetworks/Spoke-VNET-1/subnets/172.17.12.16-31"
                    },
                    "loadBalancingRules": [
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/loadBalancingRules/TestHAPorts"
                        }
                    ],
                    "privateIPAddressVersion": "IPv4"
                },
                "zones": [
                    "2"
                ]
            }
        ],
        "backendAddressPools": [
            {
                "name": "VNET-1-Private-Load-Balancer-Backend-Pool",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/backendAddressPools/VNET-1-Private-Load-Balancer-Backend-Pool",
                "etag": "W/\"7f1ec08b-d06a-4c25-88d0-d29f847904b1\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "loadBalancerBackendAddresses": [
                        {
                            "name": "Spoke-VNET-1_vnet-1-private-endpo278ipconfig1",
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/backendAddressPools/VNET-1-Private-Load-Balancer-Backend-Pool/loadBalancerBackendAddresses/Spoke-VNET-1_vnet-1-private-endpo278ipconfig1",
                            "etag": "W/\"7f1ec08b-d06a-4c25-88d0-d29f847904b1\"",
                            "properties": {
                                "provisioningState": "Succeeded",
                                # Network Interface IP Configurations: https://docs.microsoft.com/en-us/rest/api/virtualnetwork/network-interface-ip-configurations/get
                                "networkInterfaceIPConfiguration": {
                                    "name": "ipconfig1",
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/networkInterfaces/vnet-1-private-endpo278/ipConfigurations/ipconfig1",
                                    "etag": "W/\"b5540360-3c53-4b77-a8b0-01fa28561f8d\"",
                                    "type": "Microsoft.Network/networkInterfaces/ipConfigurations",
                                    "properties": {
                                        "provisioningState": "Succeeded",
                                        "privateIPAddress": "172.17.12.22",
                                        "privateIPAllocationMethod": "Dynamic",
                                        "subnet": {
                                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/virtualNetworks/Spoke-VNET-1/subnets/172.17.12.16-31"
                                        },
                                        "primary": true,
                                        "privateIPAddressVersion": "IPv4",
                                        "loadBalancerBackendAddressPools": [
                                            {
                                                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/backendAddressPools/VNET-1-Private-Load-Balancer-Backend-Pool"
                                            }
                                        ]
                                    }
                                }
                            },
                            "type": "Microsoft.Network/loadBalancers/backendAddressPools/loadBalancerBackendAddresses"
                        },
                        {
                            "name": "Spoke-VNET-1_vnet-1-private-endpo158ipconfig1",
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/backendAddressPools/VNET-1-Private-Load-Balancer-Backend-Pool/loadBalancerBackendAddresses/Spoke-VNET-1_vnet-1-private-endpo158ipconfig1",
                            "etag": "W/\"7f1ec08b-d06a-4c25-88d0-d29f847904b1\"",
                            "properties": {
                                "provisioningState": "Succeeded",
                                "networkInterfaceIPConfiguration": {
                                    "name": "ipconfig1",
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/networkInterfaces/vnet-1-private-endpo158/ipConfigurations/ipconfig1",
                                    "etag": "W/\"3dc3fed7-49e1-4db2-abe4-1e48389bf2fd\"",
                                    "type": "Microsoft.Network/networkInterfaces/ipConfigurations",
                                    "properties": {
                                        "provisioningState": "Succeeded",
                                        "privateIPAddress": "172.17.12.21",
                                        "privateIPAllocationMethod": "Dynamic",
                                        "subnet": {
                                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/virtualNetworks/Spoke-VNET-1/subnets/172.17.12.16-31"
                                        },
                                        "primary": true,
                                        "privateIPAddressVersion": "IPv4",
                                        "loadBalancerBackendAddressPools": [
                                            {
                                                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/backendAddressPools/VNET-1-Private-Load-Balancer-Backend-Pool"
                                            }
                                        ]
                                    }
                                }
                            },
                            "type": "Microsoft.Network/loadBalancers/backendAddressPools/loadBalancerBackendAddresses"
                        }
                    ],
                    # Network Interface IP Configurations: https://docs.microsoft.com/en-us/rest/api/virtualnetwork/network-interface-ip-configurations/get
                    "backendIPConfigurations": [
                        {
                            "name": "ipconfig1",
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/networkInterfaces/vnet-1-private-endpo278/ipConfigurations/ipconfig1",
                            "etag": "W/\"b5540360-3c53-4b77-a8b0-01fa28561f8d\"",
                            "type": "Microsoft.Network/networkInterfaces/ipConfigurations",
                            "properties": {
                                "provisioningState": "Succeeded",
                                "privateIPAddress": "172.17.12.22",
                                "privateIPAllocationMethod": "Dynamic",
                                "subnet": {
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/virtualNetworks/Spoke-VNET-1/subnets/172.17.12.16-31"
                                },
                                "primary": true,
                                "privateIPAddressVersion": "IPv4",
                                "loadBalancerBackendAddressPools": [
                                    {
                                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/backendAddressPools/VNET-1-Private-Load-Balancer-Backend-Pool"
                                    }
                                ]
                            }
                        },
                        {
                            "name": "ipconfig1",
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/networkInterfaces/vnet-1-private-endpo158/ipConfigurations/ipconfig1",
                            "etag": "W/\"3dc3fed7-49e1-4db2-abe4-1e48389bf2fd\"",
                            "type": "Microsoft.Network/networkInterfaces/ipConfigurations",
                            "properties": {
                                "provisioningState": "Succeeded",
                                "privateIPAddress": "172.17.12.21",
                                "privateIPAllocationMethod": "Dynamic",
                                "subnet": {
                                    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/virtualNetworks/Spoke-VNET-1/subnets/172.17.12.16-31"
                                },
                                "primary": true,
                                "privateIPAddressVersion": "IPv4",
                                "loadBalancerBackendAddressPools": [
                                    {
                                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/backendAddressPools/VNET-1-Private-Load-Balancer-Backend-Pool"
                                    }
                                ]
                            }
                        }
                    ],
                    "loadBalancingRules": [
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/loadBalancingRules/TestHAPorts"
                        }
                    ]
                },
                "type": "Microsoft.Network/loadBalancers/backendAddressPools"
            }
        ],
        "loadBalancingRules": [
            {
                "name": "TestHAPorts",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/loadBalancingRules/TestHAPorts",
                "etag": "W/\"7f1ec08b-d06a-4c25-88d0-d29f847904b1\"",
                "type": "Microsoft.Network/loadBalancers/loadBalancingRules",
                "properties": {
                    "provisioningState": "Succeeded",
                    "frontendIPConfiguration": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/frontendIPConfigurations/LoadBalancerFrontEnd"
                    },
                    "frontendPort": 0,
                    "backendPort": 0,
                    "enableFloatingIP": false,
                    "idleTimeoutInMinutes": 4,
                    "protocol": "All",
                    "enableDestinationServiceEndpoint": false,
                    "enableTcpReset": false,
                    "allowBackendPortConflict": false,
                    "loadDistribution": "Default",
                    "disableOutboundSnat": false,
                    "backendAddressPool": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/backendAddressPools/VNET-1-Private-Load-Balancer-Backend-Pool"
                    },
                    "backendAddressPools": [
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/backendAddressPools/VNET-1-Private-Load-Balancer-Backend-Pool"
                        }
                    ],
                    "probe": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/probes/HTTP"
                    }
                }
            }
        ],
        "probes": [
            {
                "name": "HTTP",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/probes/HTTP",
                "etag": "W/\"7f1ec08b-d06a-4c25-88d0-d29f847904b1\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "protocol": "Http",
                    "port": 80,
                    "requestPath": "/",
                    "intervalInSeconds": 15,
                    "numberOfProbes": 2,
                    "loadBalancingRules": [
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/loadBalancingRules/TestHAPorts"
                        },
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/loadBalancingRules/AzurePathTest-NoHA"
                        },
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/loadBalancingRules/to-firewall-virtual-appliance-HA"
                        },
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/loadBalancingRules/to-firewall-virtual-appliance-NoHA"
                        }
                    ]
                },
                "type": "Microsoft.Network/loadBalancers/probes"
            }
        ],
        "inboundNatRules": [
            {
                "name": "AzurePathTest_INNat",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/inboundNatRules/AzurePathTest_INNat",
                "etag": "W/\"7f1ec08b-d06a-4c25-88d0-d29f847904b1\"",
                "type": "Microsoft.Network/loadBalancers/inboundNatRules",
                "properties": {
                    "provisioningState": "Succeeded",
                    "frontendIPConfiguration": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/Spoke-VNET-1/providers/Microsoft.Network/loadBalancers/VNET-1-Private-Load-Balancer/frontendIPConfigurations/AzurePathTest"
                    },
                    "frontendPort": 3389,
                    "backendPort": 3389,
                    "enableFloatingIP": false,
                    "idleTimeoutInMinutes": 4,
                    "protocol": "Tcp",
                    "enableDestinationServiceEndpoint": false,
                    "enableTcpReset": false,
                    "allowBackendPortConflict": false,
                    "backendIPConfiguration": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/AzurePathTest/providers/Microsoft.Network/networkInterfaces/vnet-1-private-endpo650/ipConfigurations/ipconfig1"
                    }
                }
            }
        ],
        "outboundRules": [],
        "inboundNatPools": []
    },
    "sku": {
        "name": "Standard",
        "tier": "Regional"
    }
}
```

</details>
<br />


## Azure Application Gateway

### Introduction
The configuration of the Azure application gateway relies solely on the corresponding Azure API of the azure application gateway. The Azure API provides detailed information regarding the configuration of the application gateway, including its connectivity, configuration, etc.

### Content
Below are the Azure APIs used to generate this configuration.
|**Resource/Action**|**Relationship**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Application Gateways - Get | self | 2021-08-01 | https://docs.microsoft.com/en-us/rest/api/application-gateway/application-gateways/get | 


### Sample
<details><summary>Configuration File</summary>

```json
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "appgw_aks_test_2(<ResourceGroup>)(<Subscription_ID_Prefix>)(ApplicationGateway)",
    "name": "appgw_aks_test_2",
    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2",
    "etag": "W/\"5687248c-3700-412c-b211-750ad368e9ba\"",
    "type": "Microsoft.Network/applicationGateways",
    "location": "westus2",
    "tags": {
        "managed-by-k8s-ingress": "1.5.3/94b2b229/2023-02-03-21:42T+0000"
    },
    "zones": [
        "1",
        "2",
        "3"
    ],
    "properties": {
        "provisioningState": "Succeeded",
        "resourceGuid": "99a132df-e2fb-43f5-ad0b-11fab7baad1b",
        "sku": {
            "name": "Standard_v2",
            "tier": "Standard_v2"
        },
        "operationalState": "Running",
        "gatewayIPConfigurations": [
            {
                "name": "appGatewayIpConfig",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/gatewayIPConfigurations/appGatewayIpConfig",
                "etag": "W/\"5687248c-3700-412c-b211-750ad368e9ba\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "subnet": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/virtualNetworks/aks-vnet-39472610/subnets/appgw-subnet"
                    }
                },
                "type": "Microsoft.Network/applicationGateways/gatewayIPConfigurations"
            }
        ],
        "sslCertificates": [],
        "trustedRootCertificates": [],
        "trustedClientCertificates": [],
        "sslProfiles": [],
        "frontendIPConfigurations": [
            {
                "name": "appGwPublicFrontendIp",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/frontendIPConfigurations/appGwPublicFrontendIp",
                "etag": "W/\"5687248c-3700-412c-b211-750ad368e9ba\"",
                "type": "Microsoft.Network/applicationGateways/frontendIPConfigurations",
                "properties": {
                    "provisioningState": "Succeeded",
                    "privateIPAllocationMethod": "Dynamic",
                    "publicIPAddress": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/publicIPAddresses/public_IP_aks_test2_appgw"
                    },
                    "httpListeners": [
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/httpListeners/fl-e1903c8aa3446b7b3207aec6d6ecba8a"
                        }
                    ]
                }
            }
        ],
        "frontendPorts": [
            {
                "name": "port_80",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/frontendPorts/port_80",
                "etag": "W/\"5687248c-3700-412c-b211-750ad368e9ba\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "port": 80,
                    "httpListeners": [
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/httpListeners/fl-e1903c8aa3446b7b3207aec6d6ecba8a"
                        }
                    ]
                },
                "type": "Microsoft.Network/applicationGateways/frontendPorts"
            }
        ],
        "backendAddressPools": [
            {
                "name": "defaultaddresspool",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/backendAddressPools/defaultaddresspool",
                "etag": "W/\"5687248c-3700-412c-b211-750ad368e9ba\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "backendAddresses": []
                },
                "type": "Microsoft.Network/applicationGateways/backendAddressPools"
            },
            {
                "name": "pool-default-aspnetapp-80-bp-80",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/backendAddressPools/pool-default-aspnetapp-80-bp-80",
                "etag": "W/\"5687248c-3700-412c-b211-750ad368e9ba\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "backendAddresses": [
                        {
                            "ipAddress": "10.244.0.14"
                        }
                    ],
                    "requestRoutingRules": [
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/requestRoutingRules/rr-e1903c8aa3446b7b3207aec6d6ecba8a"
                        }
                    ]
                },
                "type": "Microsoft.Network/applicationGateways/backendAddressPools"
            }
        ],
        "loadDistributionPolicies": [],
        "backendHttpSettingsCollection": [
            {
                "name": "bp-default-aspnetapp-80-80-aspnetapp",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/backendHttpSettingsCollection/bp-default-aspnetapp-80-80-aspnetapp",
                "etag": "W/\"5687248c-3700-412c-b211-750ad368e9ba\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "port": 80,
                    "protocol": "Http",
                    "cookieBasedAffinity": "Disabled",
                    "pickHostNameFromBackendAddress": false,
                    "requestTimeout": 30,
                    "probe": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/probes/pb-default-aspnetapp-80-aspnetapp"
                    },
                    "requestRoutingRules": [
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/requestRoutingRules/rr-e1903c8aa3446b7b3207aec6d6ecba8a"
                        }
                    ]
                },
                "type": "Microsoft.Network/applicationGateways/backendHttpSettingsCollection"
            },
            {
                "name": "defaulthttpsetting",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/backendHttpSettingsCollection/defaulthttpsetting",
                "etag": "W/\"5687248c-3700-412c-b211-750ad368e9ba\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "port": 80,
                    "protocol": "Http",
                    "cookieBasedAffinity": "Disabled",
                    "pickHostNameFromBackendAddress": false,
                    "requestTimeout": 30,
                    "probe": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/probes/defaultprobe-Http"
                    }
                },
                "type": "Microsoft.Network/applicationGateways/backendHttpSettingsCollection"
            }
        ],
        "backendSettingsCollection": [],
        "httpListeners": [
            {
                "name": "fl-e1903c8aa3446b7b3207aec6d6ecba8a",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/httpListeners/fl-e1903c8aa3446b7b3207aec6d6ecba8a",
                "etag": "W/\"5687248c-3700-412c-b211-750ad368e9ba\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "frontendIPConfiguration": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/frontendIPConfigurations/appGwPublicFrontendIp"
                    },
                    "frontendPort": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/frontendPorts/port_80"
                    },
                    "protocol": "Http",
                    "hostNames": [],
                    "requireServerNameIndication": false,
                    "requestRoutingRules": [
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/requestRoutingRules/rr-e1903c8aa3446b7b3207aec6d6ecba8a"
                        }
                    ]
                },
                "type": "Microsoft.Network/applicationGateways/httpListeners"
            }
        ],
        "listeners": [],
        "urlPathMaps": [],
        "requestRoutingRules": [
            {
                "name": "rr-e1903c8aa3446b7b3207aec6d6ecba8a",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/requestRoutingRules/rr-e1903c8aa3446b7b3207aec6d6ecba8a",
                "etag": "W/\"5687248c-3700-412c-b211-750ad368e9ba\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "ruleType": "Basic",
                    "priority": 19500,
                    "httpListener": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/httpListeners/fl-e1903c8aa3446b7b3207aec6d6ecba8a"
                    },
                    "backendAddressPool": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/backendAddressPools/pool-default-aspnetapp-80-bp-80"
                    },
                    "backendHttpSettings": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/backendHttpSettingsCollection/bp-default-aspnetapp-80-80-aspnetapp"
                    }
                },
                "type": "Microsoft.Network/applicationGateways/requestRoutingRules"
            }
        ],
        "routingRules": [],
        "probes": [
            {
                "name": "defaultprobe-Http",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/probes/defaultprobe-Http",
                "etag": "W/\"5687248c-3700-412c-b211-750ad368e9ba\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "protocol": "Http",
                    "host": "localhost",
                    "path": "/",
                    "interval": 30,
                    "timeout": 30,
                    "unhealthyThreshold": 3,
                    "pickHostNameFromBackendHttpSettings": false,
                    "minServers": 0,
                    "match": {},
                    "backendHttpSettings": [
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/backendHttpSettingsCollection/defaulthttpsetting"
                        }
                    ]
                },
                "type": "Microsoft.Network/applicationGateways/probes"
            },
            {
                "name": "defaultprobe-Https",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/probes/defaultprobe-Https",
                "etag": "W/\"5687248c-3700-412c-b211-750ad368e9ba\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "protocol": "Https",
                    "host": "localhost",
                    "path": "/",
                    "interval": 30,
                    "timeout": 30,
                    "unhealthyThreshold": 3,
                    "pickHostNameFromBackendHttpSettings": false,
                    "minServers": 0,
                    "match": {}
                },
                "type": "Microsoft.Network/applicationGateways/probes"
            },
            {
                "name": "pb-default-aspnetapp-80-aspnetapp",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/probes/pb-default-aspnetapp-80-aspnetapp",
                "etag": "W/\"5687248c-3700-412c-b211-750ad368e9ba\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "protocol": "Http",
                    "host": "localhost",
                    "path": "/",
                    "interval": 30,
                    "timeout": 30,
                    "unhealthyThreshold": 3,
                    "pickHostNameFromBackendHttpSettings": false,
                    "minServers": 0,
                    "match": {},
                    "backendHttpSettings": [
                        {
                            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/MC_aks_test_2_aks-test-2-public_westus2/providers/Microsoft.Network/applicationGateways/appgw_aks_test_2/backendHttpSettingsCollection/bp-default-aspnetapp-80-80-aspnetapp"
                        }
                    ]
                },
                "type": "Microsoft.Network/applicationGateways/probes"
            }
        ],
        "rewriteRuleSets": [],
        "redirectConfigurations": [],
        "privateLinkConfigurations": [],
        "privateEndpointConnections": [],
        "enableHttp2": false,
        "autoscaleConfiguration": {
            "minCapacity": 0,
            "maxCapacity": 3
        }
    }
}
```

</details>
<br />


## Azure Private Endpoint

### Introduction
The configuration of the Azure private endpoint relies solely on the corresponding Azure API of the private endpoint. The Azure API provides detailed information regarding the configuration of this private endpoint, including its connectivity, status, etc.

### Content
Below are the Azure APIs used to generate this configuration.
|**Resource/Action**|**Relationship**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Private Endpoints - Get | self | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/private-endpoints/get | 


### Sample
<details><summary>Configuration File</summary>

```json
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "1stsub-private-endpoint(<ResourceGroup>)(<Subscription_ID_Prefix>)(PrivateEndpoint)",
    "name": "1stsub-private-endpoint",
    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/public-service-test/providers/Microsoft.Network/privateEndpoints/1stsub-private-endpoint",
    "etag": "W/\"17898344-69e0-41df-b9a2-7179d9f062b0\"",
    "type": "Microsoft.Network/privateEndpoints",
    "location": "eastus",
    "tags": {},
    "properties": {
        "provisioningState": "Succeeded",
        "resourceGuid": "b36d12ae-86b8-4639-8b30-27214474de12",
        "privateLinkServiceConnections": [
            {
                "name": "1stsub-private-endpoint",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/public-service-test/providers/Microsoft.Network/privateEndpoints/1stsub-private-endpoint/privateLinkServiceConnections/1stsub-private-endpoint",
                "etag": "W/\"17898344-69e0-41df-b9a2-7179d9f062b0\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "privateLinkServiceId": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/paastestgroup/providers/Microsoft.Storage/storageAccounts/2edsub4storageaccount",
                    "groupIds": [
                        "file"
                    ],
                    "privateLinkServiceConnectionState": {
                        "status": "Approved",
                        "description": "Auto-Approved",
                        "actionsRequired": "None"
                    }
                },
                "type": "Microsoft.Network/privateEndpoints/privateLinkServiceConnections"
            }
        ],
        "manualPrivateLinkServiceConnections": [],
        "customNetworkInterfaceName": "1stsub-private-endpoint-nic",
        "subnet": {
            "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworks/East-VNET1/subnets/ASAv-Subnet2"
        },
        "ipConfigurations": [],
        "networkInterfaces": [
            {
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/public-service-test/providers/Microsoft.Network/networkInterfaces/1stsub-private-endpoint-nic"
            }
        ],
        "customDnsConfigs": []
    }
}
```

</details>
<br />

## Azure Private Link Service

### Introduction
The configuration of the Azure private link service relies solely on the corresponding Azure API of the private link service. The Azure API provides detailed information regarding the configuration of the azure private link service, including its connectivity, status, etc.

### Content
Below are the Azure APIs used to generate this configuration.
|**Resource/Action**|**Relationship**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Private Link Services - Get | self | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/private-link-services/get | 


### Sample
<details><summary>Configuration File</summary>

```json
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "public_service_test_privatelinkservice(<ResourceGroup>)(<Subscription_ID_Prefix>)(PrivateLinkService)",
    "name": "public_service_test_privatelinkservice",
    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/public-service-test/providers/Microsoft.Network/privateLinkServices/public_service_test_privatelinkservice",
    "etag": "W/\"058d64b8-fd86-48e4-b1cb-61b629934556\"",
    "type": "Microsoft.Network/privateLinkServices",
    "location": "eastus",
    "tags": {
        "type": "dev"
    },
    "properties": {
        "provisioningState": "Succeeded",
        "resourceGuid": "bfd8925e-0c2e-448a-b215-1c42121cd572",
        "fqdns": [],
        "alias": "public_service_test_privatelinkservice.acb1b37c-fb58-47a8-bbbe-4137bd3064f2.eastus.azure.privatelinkservice",
        "visibility": {
            "subscriptions": []
        },
        "autoApproval": {
            "subscriptions": []
        },
        "enableProxyProtocol": false,
        "loadBalancerFrontendIpConfigurations": [
            {
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/loadBalancers/TestLBStandard/frontendIPConfigurations/LoadBalancerFrontEnd"
            }
        ],
        "ipConfigurations": [
            {
                "name": "Subnet1-1",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/public-service-test/providers/Microsoft.Network/privateLinkServices/public_service_test_privatelinkservice/ipConfigurations/Subnet1-1",
                "etag": "W/\"058d64b8-fd86-48e4-b1cb-61b629934556\"",
                "type": "Microsoft.Network/privateLinkServices/ipConfigurations",
                "properties": {
                    "provisioningState": "Succeeded",
                    "privateIPAllocationMethod": "Dynamic",
                    "subnet": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworks/East-VNET1/subnets/Subnet1"
                    },
                    "primary": false,
                    "privateIPAddressVersion": "IPv4"
                }
            },
            {
                "name": "Subnet1-2",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/public-service-test/providers/Microsoft.Network/privateLinkServices/public_service_test_privatelinkservice/ipConfigurations/Subnet1-2",
                "etag": "W/\"058d64b8-fd86-48e4-b1cb-61b629934556\"",
                "type": "Microsoft.Network/privateLinkServices/ipConfigurations",
                "properties": {
                    "provisioningState": "Succeeded",
                    "privateIPAddress": "172.17.11.12",
                    "privateIPAllocationMethod": "Static",
                    "subnet": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworks/East-VNET1/subnets/Subnet1"
                    },
                    "primary": true,
                    "privateIPAddressVersion": "IPv4"
                }
            }
        ],
        "privateEndpointConnections": [
            {
                "name": "publicservicetest_privateendpoint_1.0e476d97-89ac-4dea-8771-23087d1294aa",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/public-service-test/providers/Microsoft.Network/privateLinkServices/public_service_test_privatelinkservice/privateEndpointConnections/publicservicetest_privateendpoint_1.0e476d97-89ac-4dea-8771-23087d1294aa",
                "etag": "W/\"058d64b8-fd86-48e4-b1cb-61b629934556\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "privateEndpoint": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/public-service-test/providers/Microsoft.Network/privateEndpoints/publicservicetest_privateendpoint_1"
                    },
                    "privateLinkServiceConnectionState": {
                        "status": "Approved",
                        "description": "Auto Approved",
                        "actionsRequired": "None"
                    },
                    "linkIdentifier": "184561670"
                },
                "type": "Microsoft.Network/privateLinkServices/privateEndpointConnections"
            },
            {
                "name": "2edSub-private-endpoint-pls.60e3456e-2c5c-4031-af30-08a12da52acc",
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/public-service-test/providers/Microsoft.Network/privateLinkServices/public_service_test_privatelinkservice/privateEndpointConnections/2edSub-private-endpoint-pls.60e3456e-2c5c-4031-af30-08a12da52acc",
                "etag": "W/\"058d64b8-fd86-48e4-b1cb-61b629934556\"",
                "properties": {
                    "provisioningState": "Succeeded",
                    "privateEndpoint": {
                        "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/paastestgroup/providers/Microsoft.Network/privateEndpoints/2edSub-private-endpoint-pls"
                    },
                    "privateLinkServiceConnectionState": {
                        "status": "Approved",
                        "description": "Auto Approved",
                        "actionsRequired": "None"
                    },
                    "linkIdentifier": "536904747"
                },
                "type": "Microsoft.Network/privateLinkServices/privateEndpointConnections"
            }
        ],
        "networkInterfaces": [
            {
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/public-service-test/providers/Microsoft.Network/networkInterfaces/public_service_test_privatelinkservice.nic.280a7b6f-4ef7-43ef-9a47-1b49c27127bf"
            }
        ]
    }
}
```

</details>
<br />


## Azure Service Endpoint

### Introduction
The configuration of the Azure service endpoint relies solely on the corresponding Azure API of the subnet. The Azure API provides detailed information regarding the configuration of the subnet, including its connectivity, accessibility, etc.

### Content
Below are the Azure APIs used to generate this configuration.
|**Resource/Action**|**Relationship**|**Azure API Version**|**Azure API document**|
|------|------|------|------|
| Subnets - Get | self | 2021-08-01 | https://learn.microsoft.com/en-us/rest/api/virtualnetwork/subnets/get | 


### Sample
<details><summary>Configuration File</summary>

```json
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "AzureFirewallSubnet_in_East-Test-VNET(<ResourceGroup>)(<Subscription_ID_Prefix>)(ServiceEndpoint)",
    "name": "AzureFirewallSubnet",
    "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/virtualNetworks/East-Test-VNET/subnets/AzureFirewallSubnet",
    "etag": "W/\"a2970964-5e0b-4f76-beb4-eddf5d573c6f\"",
    "properties": {
        "provisioningState": "Succeeded",
        "addressPrefix": "172.17.19.64/26",
        "serviceEndpointPolicies": [
            {
                "id": "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx/resourceGroups/East-RG1/providers/Microsoft.Network/serviceEndpointPolicies/XunServiceEndpoint1"
            }
        ],
        "serviceEndpoints": [
            {
                "provisioningState": "Succeeded",
                "service": "Microsoft.Storage",
                "locations": [
                    "*"
                ]
            }
        ],
        "delegations": [],
        "privateEndpointNetworkPolicies": "Enabled",
        "privateLinkServiceNetworkPolicies": "Enabled"
    },
    "type": "Microsoft.Network/virtualNetworks/subnets"
}
```

</details>
<br />
