# Usage
To retrieve the configuration data for a resource, you can utilize NetBrain's built-in configuration file function, which does not require coding. This function enables you to quickly obtain the resource configuration.


# Table of Contents
* [AWS VPC Router](#aws-vpc-router)
* [AWS VPC Endpoint](#aws-vpc-endpoint)
* [AWS VPN Gateway](#aws-vpn-gateway)
* [AWS Transit Gateway](#aws-transit-gateway)
* [AWS Egress Internet Gateway](#aws-egress-internet-gateway)
* [AWS Internet Gateway](#aws-internet-gateway)
* [AWS Load Balancer](#aws-load-balancer)
* [AWS Load Balancer v2](#aws-load-balancer-v2)
* [AWS Direct Connect Router](#aws-direct-connect-router)
* [AWS Direct Connect Gateway](#aws-direct-connect-gateway)
* [AWS NAT Gateway](#aws-nat-gateway)
* [AWS Firewall](#aws-firewall)


## AWS VPC Router

### Introduction
The configuration of the AWS VPC Router is dependent on the AWS SDK response of the AWS virtual private cloud (VPC) as the primary response. The full resource configuration consists of some associated resources' data, including `vpc classic link`, `subnet`, and `vpc peering connections`.

### Content
Below are the AWS SDK used to generate this configuration.
|**Resource/Action**|**Relationship**|**AWS SDK document**|
|------|------|------|
| describe_vpcs | self | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_vpcs.html|
| describe_vpc_classic_link | VpcClassicLinks | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_vpc_classic_link.html |
| describe_subnets | Subnets | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_subnets.html | 
| describe_vpc_peering_connections | VpcPeeringConnections | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_vpc_peering_connections.html |


### Sample
<details><summary>Configuration File</summary>

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


## AWS VPC Endpoint

### Introduction
The configuration of the AWS VPC Endpoint is dependent on the AWS SDK response of the VPC Endpoint as the primary response. The full resource configuration consists of some associated resources' data, including `Vpc Endpoint Connections`.

### Content
Below are the AWS SDK used to generate this configuration.
|**Resource/Action**|**Relationship**|**AWS SDK document**|
|------|------|------|
| describe_vpc_endpoints | self | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_vpc_endpoints.html|
| describe_vpc_endpoint_connections | VpcEndpointConnections | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_vpc_endpoint_connections.html |

### Sample
<details><summary>Configuration File</summary>

```json
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "East-VPN-GW(East-RG1)(073e6f45)(VirtualNetworkGateway)",
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
                            "ipAddress": "52.179.98.177",
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
                        "52.179.98.177"
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


## AWS VPN Gateway

### Introduction
The configuration of the AWS VPN Gateway is dependent on the AWS SDK response of the AWS VPN Gateway as the primary response. The full resource configuration consists of some associated resources' data, including `Vpc Endpoint Connections`, `Vpn Connections`, and `Customer Gateways`.

### Content
Below are the AWS SDK used to generate this configuration.
|**Resource/Action**|**Relationship**|**AWS SDK document**|
|------|------|------|
| describe_vpn_gateways | self | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_vpn_gateways.html|
| describe_vpn_connections | VpnConnections | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_vpn_connections.html |
| describe_customer_gateways | CustomerGateways | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_customer_gateways.html |


### Sample
<details><summary>Configuration File</summary>

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

  
## AWS Transit Gateway

### Introduction
The configuration of the AWS Transit Gateway is dependent on the AWS SDK response of the AWS Transit Gateway as the primary response. The full resource configuration consists of some associated resources' data, including `transit gateway connects`, ` transit gateway vpc attachments`.

### Content
Below are the AWS SDK used to generate this configuration.
|**Resource/Action**|**Relationship**|**AWS SDK document**|
|------|------|------|
| describe_transit_gateways | self | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_transit_gateways.html|
| describe_transit_gateway_connects | TransitGatewayConnects | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_transit_gateway_connects.html |
| describe_transit_gateway_vpc_attachments | TransitGatewayVpcAttachments | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_transit_gateway_vpc_attachments.html |


### Sample
<details><summary>Configuration File</summary>

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

## AWS Internet Gateway

### Introduction
The configuration of the Azure Internet Gateway relies solely on the corresponding AWS SDK of the internet gateway. The AWS SDK provides detailed information regarding the configuration of the internet gateway, including its connectivity, security, etc.

### Content
Below are the AWS SDK used to generate this configuration.
|**Resource/Action**|**Relationship**|**AWS SDK document**|
|------|------|------|
| describe_internet_gateways | self | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_internet_gateways.html|


### Sample
<details><summary>Configuration File</summary>

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
  

## AWS Egress Internet Gateway

### Introduction
The configuration of the Azure Egress Internet Gateway relies solely on the corresponding AWS SDK of the egress internet gateway. The AWS SDK provides detailed information regarding the configuration of the egress internet gateway, including its connectivity, security, etc.

### Content
Below are the AWS SDK used to generate this configuration.
|**Resource/Action**|**Relationship**|**AWS SDK document**|
|------|------|------|
| describe_egress_only_internet_gateways | self | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_egress_only_internet_gateways.html|


### Sample
<details><summary>Configuration File</summary>

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
  

## AWS Load Balancer

### Introduction
The configuration of the AWS Load Balancer is dependent on the AWS SDK response of the Load Balancer as the primary response. The full resource configuration consists of some associated resources' data, including `load balancer policies`, `instance health`.

### Content
Below are the AWS SDK used to generate this configuration.
|**Resource/Action**|**Relationship**|**AWS SDK document**|
|------|------|------|
| describe_load_balancers | self | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_load_balancers.html |
| describe_load_balancer_policies | PolicyDescriptions | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_load_balancer_policies.html |
| describe_instance_health | InstanceStates | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_instance_health.html |

### Sample
<details><summary>Configuration File</summary>

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
  

## AWS Load Balancer v2

### Introduction
The configuration of the AWS Load Balancer v2 is dependent on the AWS SDK response of the Load Balancer v2 as the primary response. The full resource configuration consists of some associated resources' data, including `load balancer policies`, `instance health`.

### Content
Below are the AWS SDK used to generate this configuration.
|**Resource/Action**|**Relationship**|**AWS SDK document**|
|------|------|------|
| describe_load_balancers | self | https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html |


### Sample
<details><summary>Configuration File</summary>

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
  

## AWS Direct Connect Router

### Introduction
The configuration of the AWS direct connect router is dependent on the AWS SDK response of the virtual interface as the primary response. The full resource configuration consists of some associated resources' data, including `connections`.

### Content
Below are the AWS SDK used to generate this configuration.
|**Resource/Action**|**Relationship**|**AWS SDK document**|
|------|------|------|
| describe_virtual_interfaces | self | https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/client/describe_virtual_interfaces.html |
| describe_connections | connections | https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/client/describe_connections.html |

### Sample
<details><summary>Configuration File</summary>

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
  

## AWS Direct Connect Gateway

### Introduction
The configuration of the AWS direct connect gateway is dependent on the AWS SDK response of the direct connect gateway as the primary response. The full resource configuration consists of some associated resources' data, including `attachments`, `associations`, and `association proposals`.

### Content
Below are the AWS SDK used to generate this configuration.
|**Resource/Action**|**Relationship**|**AWS SDK document**|
|------|------|------|
| describe_direct_connect_gateways | self | https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/client/describe_virtual_interfaces.html |
| describe_direct_connect_gateway_attachments | directConnectGatewayAttachments | https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/client/describe_direct_connect_gateway_attachments.html |
| describe_direct_connect_gateway_associations | directConnectGatewayAssociations | https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/client/describe_direct_connect_gateway_associations.html |
| describe_direct_connect_gateway_association_proposals | directConnectGatewayAssociationProposals | https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/client/describe_direct_connect_gateway_association_proposals.html |

### Sample
<details><summary>Configuration File</summary>

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
  

## AWS NAT Gateway

### Introduction
The configuration of the AWS NAT gateway is dependent on the AWS SDK response of the NAT gateway as the primary response. The full resource configuration consists of some associated resources' data, including `subnets` as well.

### Content
Below are the AWS SDK used to generate this configuration.
|**Resource/Action**|**Relationship**|**AWS SDK document**|
|------|------|------|
| describe_nat_gateways | self | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_nat_gateways.html |
| describe_subnets | Subnet | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_subnets.html |

### Sample
<details><summary>Configuration File</summary>

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


## AWS Firewall

### Introduction
The configuration of the Azure Firewall relies solely on the corresponding AWS SDK of the AWS network firewall. The AWS SDK provides detailed information regarding the configuration of the network firewall, including its connectivity, security, etc.

### Content
Below are the AWS SDK used to generate this configuration.
|**Resource/Action**|**Relationship**|**AWS SDK document**|
|------|------|------|
| describe_firewall | self | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/network-firewall/client/describe_firewall.html |

### Sample
<details><summary>Configuration File</summary>

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
  

