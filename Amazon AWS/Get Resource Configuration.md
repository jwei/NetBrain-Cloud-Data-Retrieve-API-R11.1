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
    "netbrainHostName": "Spoke1(vpc-03bf7347a44aea79a)",
    "CidrBlock": "172.16.101.0/24",
    "DhcpOptionsId": "dopt-bfa3bbc4",
    "State": "available",
    "VpcId": "vpc-03bf7347a44aea79a",
    "OwnerId": "747895045325",
    "InstanceTenancy": "default",
    "CidrBlockAssociationSet": [
        {
            "AssociationId": "vpc-cidr-assoc-011a9a86b67277b6d",
            "CidrBlock": "172.16.101.0/24",
            "CidrBlockState": {
                "State": "associated"
            }
        }
    ],
    "IsDefault": false,
    "Tags": [
        {
            "Key": "Name",
            "Value": "Spoke1"
        }
    ],
    # VPC Classic Links: https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_vpc_classic_link.html
    "VpcClassicLinks": [],
    # Subnets: https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_subnets.html
    "Subnets": [
        {
            "AvailabilityZone": "us-east-1a",
            "AvailabilityZoneId": "use1-az1",
            "AvailableIpAddressCount": 10,
            "CidrBlock": "172.16.101.144/28",
            "DefaultForAz": false,
            "MapPublicIpOnLaunch": false,
            "MapCustomerOwnedIpOnLaunch": false,
            "State": "available",
            "SubnetId": "subnet-01f62fa49059b2723",
            "VpcId": "vpc-03bf7347a44aea79a",
            "OwnerId": "747895045325",
            "AssignIpv6AddressOnCreation": false,
            "Ipv6CidrBlockAssociationSet": [],
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "BMC-Subnet"
                }
            ],
            "SubnetArn": "arn:aws:ec2:us-east-1:747895045325:subnet/subnet-01f62fa49059b2723",
            "EnableDns64": false,
            "Ipv6Native": false,
            "PrivateDnsNameOptionsOnLaunch": {
                "HostnameType": "ip-name",
                "EnableResourceNameDnsARecord": false,
                "EnableResourceNameDnsAAAARecord": false
            }
        }
    ],
    # VPC Peering Connections: https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_vpc_peering_connections.html
    "VpcPeeringConnections": [
        {
            "AccepterVpcInfo": {
                "CidrBlock": "172.16.102.0/24",
                "CidrBlockSet": [
                    {
                        "CidrBlock": "172.16.102.0/24"
                    },
                    {
                        "CidrBlock": "172.16.103.0/24"
                    },
                    {
                        "CidrBlock": "172.16.104.0/24"
                    }
                ],
                "OwnerId": "747895045325",
                "PeeringOptions": {
                    "AllowDnsResolutionFromRemoteVpc": false,
                    "AllowEgressFromLocalClassicLinkToRemoteVpc": false,
                    "AllowEgressFromLocalVpcToRemoteClassicLink": false
                },
                "VpcId": "vpc-0797a80cf72fdc101",
                "Region": "us-east-1"
            },
            "RequesterVpcInfo": {
                "CidrBlock": "172.16.101.0/24",
                "CidrBlockSet": [
                    {
                        "CidrBlock": "172.16.101.0/24"
                    }
                ],
                "OwnerId": "747895045325",
                "PeeringOptions": {
                    "AllowDnsResolutionFromRemoteVpc": false,
                    "AllowEgressFromLocalClassicLinkToRemoteVpc": false,
                    "AllowEgressFromLocalVpcToRemoteClassicLink": false
                },
                "VpcId": "vpc-03bf7347a44aea79a",
                "Region": "us-east-1"
            },
            "Status": {
                "Code": "active",
                "Message": "Active"
            },
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "fourth"
                }
            ],
            "VpcPeeringConnectionId": "pcx-09852bb044bec839f"
        },
        {
            "AccepterVpcInfo": {
                "CidrBlock": "172.26.1.0/24",
                "CidrBlockSet": [
                    {
                        "CidrBlock": "172.26.1.0/24"
                    },
                    {
                        "CidrBlock": "172.26.150.0/24"
                    }
                ],
                "OwnerId": "747895045325",
                "PeeringOptions": {
                    "AllowDnsResolutionFromRemoteVpc": false,
                    "AllowEgressFromLocalClassicLinkToRemoteVpc": false,
                    "AllowEgressFromLocalVpcToRemoteClassicLink": false
                },
                "VpcId": "vpc-00a3b35e314056695",
                "Region": "us-east-2"
            },
            "RequesterVpcInfo": {
                "CidrBlock": "172.16.101.0/24",
                "CidrBlockSet": [
                    {
                        "CidrBlock": "172.16.101.0/24"
                    }
                ],
                "OwnerId": "747895045325",
                "PeeringOptions": {
                    "AllowDnsResolutionFromRemoteVpc": false,
                    "AllowEgressFromLocalClassicLinkToRemoteVpc": false,
                    "AllowEgressFromLocalVpcToRemoteClassicLink": false
                },
                "VpcId": "vpc-03bf7347a44aea79a",
                "Region": "us-east-1"
            },
            "Status": {
                "Code": "active",
                "Message": "Active"
            },
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "third"
                }
            ],
            "VpcPeeringConnectionId": "pcx-0ae7dccf7496c9115"
        },
        {
            "AccepterVpcInfo": {
                "CidrBlock": "10.55.0.0/22",
                "Ipv6CidrBlockSet": [
                    {
                        "Ipv6CidrBlock": "2600:1f11:164:3e00::/56"
                    }
                ],
                "CidrBlockSet": [
                    {
                        "CidrBlock": "10.55.0.0/22"
                    },
                    {
                        "CidrBlock": "10.57.0.0/22"
                    }
                ],
                "OwnerId": "747895045325",
                "PeeringOptions": {
                    "AllowDnsResolutionFromRemoteVpc": false,
                    "AllowEgressFromLocalClassicLinkToRemoteVpc": false,
                    "AllowEgressFromLocalVpcToRemoteClassicLink": false
                },
                "VpcId": "vpc-08a97e073f7f21698",
                "Region": "ca-central-1"
            },
            "RequesterVpcInfo": {
                "CidrBlock": "172.16.101.0/24",
                "CidrBlockSet": [
                    {
                        "CidrBlock": "172.16.101.0/24"
                    }
                ],
                "OwnerId": "747895045325",
                "PeeringOptions": {
                    "AllowDnsResolutionFromRemoteVpc": false,
                    "AllowEgressFromLocalClassicLinkToRemoteVpc": false,
                    "AllowEgressFromLocalVpcToRemoteClassicLink": false
                },
                "VpcId": "vpc-03bf7347a44aea79a",
                "Region": "us-east-1"
            },
            "Status": {
                "Code": "active",
                "Message": "Active"
            },
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "to-5325-huans-vpc-central"
                }
            ],
            "VpcPeeringConnectionId": "pcx-0fac6bae1a2a747e6"
        }
    ]
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
    "netbrainHostName": "spoke2-s3-vpcgwe(vpce-0baf3c939d32e6fa3)",
    "VpcEndpointId": "vpce-0baf3c939d32e6fa3",
    "VpcEndpointType": "Gateway",
    "VpcId": "vpc-0797a80cf72fdc101",
    "ServiceName": "com.amazonaws.us-east-1.s3",
    "State": "available",
    "PolicyDocument": "{\"Version\":\"2008-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"*\",\"Resource\":\"*\"}]}",
    "RouteTableIds": [
        "rtb-02194d2b37347310a"
    ],
    "SubnetIds": [],
    "Groups": [],
    "PrivateDnsEnabled": false,
    "RequesterManaged": false,
    "NetworkInterfaceIds": [],
    "DnsEntries": [],
    "CreationTimestamp": "2020-08-20 20:55:19+00:00",
    "Tags": [
        {
            "Key": "Name",
            "Value": "spoke2-s3-vpcgwe"
        }
    ],
    "OwnerId": "747895045325",
    # VPC Endpoint Connections: https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_vpc_endpoint_connections.html
    "VpcEndpointConnections": []
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
| describe_customer_gateways | VpnConnections.CustomerGateways | https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_customer_gateways.html |


### Sample
<details><summary>Configuration File</summary>

```json
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "spoke-vpc-3-vgw(vgw-0ff076c24c4932e4a)",
    "State": "available",
    "Type": "ipsec.1",

    "VpcAttachments": [
        {
            "State": "attached",
            "VpcId": "vpc-059b96a14ccfef687"
        }
    ],
    "VpnGatewayId": "vgw-0ff076c24c4932e4a",
    "AmazonSideAsn": 64512,
    "Tags": [
        {
            "Key": "Name",
            "Value": "spoke-vpc-3-vgw"
        }
    ],
    # VPN Connections https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_vpn_connections.html
    "VpnConnections": [
        {
            "CustomerGatewayConfiguration": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<vpn_connection id=\"vpn-0ecb2a2698b33f4ee\">\n  <customer_gateway_id>cgw-03cf0ff0c8d3727f9</customer_gateway_id>\n  <vpn_gateway_id>vgw-0ff076c24c4932e4a</vpn_gateway_id>\n  <vpn_connection_type>ipsec.1</vpn_connection_type>\n  <ipsec_tunnel>\n    <customer_gateway>\n      <tunnel_outside_address>\n        <ip_address>3.15.245.169</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.225.10</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64513</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </customer_gateway>\n    <vpn_gateway>\n      <tunnel_outside_address>\n        <ip_address>3.18.239.122</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.225.9</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64512</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </vpn_gateway>\n    <ike>\n      <authentication_protocol>sha1</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>28800</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>main</mode>\n      <pre_shared_key>xlk6lMNzd4CNRP8YUX4PlRLVL4pV1FWS</pre_shared_key>\n    </ike>\n    <ipsec>\n      <protocol>esp</protocol>\n      <authentication_protocol>hmac-sha1-96</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>3600</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>tunnel</mode>\n      <clear_df_bit>true</clear_df_bit>\n      <fragmentation_before_encryption>true</fragmentation_before_encryption>\n      <tcp_mss_adjustment>1379</tcp_mss_adjustment>\n      <dead_peer_detection>\n        <interval>10</interval>\n        <retries>3</retries>\n      </dead_peer_detection>\n    </ipsec>\n  </ipsec_tunnel>\n  <ipsec_tunnel>\n    <customer_gateway>\n      <tunnel_outside_address>\n        <ip_address>3.15.245.169</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.68.26</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64513</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </customer_gateway>\n    <vpn_gateway>\n      <tunnel_outside_address>\n        <ip_address>52.15.217.142</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.68.25</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64512</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </vpn_gateway>\n    <ike>\n      <authentication_protocol>sha1</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>28800</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>main</mode>\n      <pre_shared_key>KMA_6TXDeJzOJAnrn6gnMEtCO0jbE655</pre_shared_key>\n    </ike>\n    <ipsec>\n      <protocol>esp</protocol>\n      <authentication_protocol>hmac-sha1-96</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>3600</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>tunnel</mode>\n      <clear_df_bit>true</clear_df_bit>\n      <fragmentation_before_encryption>true</fragmentation_before_encryption>\n      <tcp_mss_adjustment>1379</tcp_mss_adjustment>\n      <dead_peer_detection>\n        <interval>10</interval>\n        <retries>3</retries>\n      </dead_peer_detection>\n    </ipsec>\n  </ipsec_tunnel>\n</vpn_connection>",
            "CustomerGatewayId": "cgw-03cf0ff0c8d3727f9",
            "Category": "VPN",
            "State": "available",
            "Type": "ipsec.1",
            "VpnConnectionId": "vpn-0ecb2a2698b33f4ee",
            "VpnGatewayId": "vgw-0ff076c24c4932e4a",
            "GatewayAssociationState": "associated",
            "Options": {
                "EnableAcceleration": false,
                "StaticRoutesOnly": false,
                "LocalIpv4NetworkCidr": "0.0.0.0/0",
                "RemoteIpv4NetworkCidr": "0.0.0.0/0",
                "OutsideIpAddressType": "PublicIpv4",
                "TunnelInsideIpVersion": "ipv4"
            },
            "Routes": [],
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "CSR1000V2-TO-SPOKE3"
                }
            ],
            "VgwTelemetry": [
                {
                    "AcceptedRouteCount": 0,
                    "LastStatusChange": "2023-05-02 10:47:58+00:00",
                    "OutsideIpAddress": "3.18.239.122",
                    "Status": "UP",
                    "StatusMessage": "0 BGP ROUTES"
                },
                {
                    "AcceptedRouteCount": 0,
                    "LastStatusChange": "2023-04-29 01:09:41+00:00",
                    "OutsideIpAddress": "52.15.217.142",
                    "Status": "UP",
                    "StatusMessage": "0 BGP ROUTES"
                }
            ],
            # Customer Gateways https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_customer_gateways.html
            "CustomerGateways": [
                {
                    "BgpAsn": "64513",
                    "CustomerGatewayId": "cgw-03cf0ff0c8d3727f9",
                    "IpAddress": "3.15.245.169",
                    "State": "available",
                    "Type": "ipsec.1",
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "Csr1000v-2-to-spoke"
                        }
                    ]
                }
            ]
        },
        {
            "CustomerGatewayConfiguration": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<vpn_connection id=\"vpn-0b953fd90796f7c2d\">\n  <customer_gateway_id>cgw-0171e5b81d042c2a3</customer_gateway_id>\n  <vpn_gateway_id>vgw-0ff076c24c4932e4a</vpn_gateway_id>\n  <vpn_connection_type>ipsec.1</vpn_connection_type>\n  <ipsec_tunnel>\n    <customer_gateway>\n      <tunnel_outside_address>\n        <ip_address>3.18.73.221</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.14.138</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64513</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </customer_gateway>\n    <vpn_gateway>\n      <tunnel_outside_address>\n        <ip_address>3.19.204.36</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.14.137</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64512</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </vpn_gateway>\n    <ike>\n      <authentication_protocol>sha1</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>28800</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>main</mode>\n      <pre_shared_key>W.1xFZ9TAtwgIn5g5vxKikxaIVFDH56i</pre_shared_key>\n    </ike>\n    <ipsec>\n      <protocol>esp</protocol>\n      <authentication_protocol>hmac-sha1-96</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>3600</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>tunnel</mode>\n      <clear_df_bit>true</clear_df_bit>\n      <fragmentation_before_encryption>true</fragmentation_before_encryption>\n      <tcp_mss_adjustment>1379</tcp_mss_adjustment>\n      <dead_peer_detection>\n        <interval>10</interval>\n        <retries>3</retries>\n      </dead_peer_detection>\n    </ipsec>\n  </ipsec_tunnel>\n  <ipsec_tunnel>\n    <customer_gateway>\n      <tunnel_outside_address>\n        <ip_address>3.18.73.221</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.10.6</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64513</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </customer_gateway>\n    <vpn_gateway>\n      <tunnel_outside_address>\n        <ip_address>18.216.245.201</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.10.5</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64512</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </vpn_gateway>\n    <ike>\n      <authentication_protocol>sha1</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>28800</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>main</mode>\n      <pre_shared_key>yrPRMk7SGQyo.es7ywU38qHAucXH8E8Q</pre_shared_key>\n    </ike>\n    <ipsec>\n      <protocol>esp</protocol>\n      <authentication_protocol>hmac-sha1-96</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>3600</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>tunnel</mode>\n      <clear_df_bit>true</clear_df_bit>\n      <fragmentation_before_encryption>true</fragmentation_before_encryption>\n      <tcp_mss_adjustment>1379</tcp_mss_adjustment>\n      <dead_peer_detection>\n        <interval>10</interval>\n        <retries>3</retries>\n      </dead_peer_detection>\n    </ipsec>\n  </ipsec_tunnel>\n</vpn_connection>",
            "CustomerGatewayId": "cgw-0171e5b81d042c2a3",
            "Category": "VPN",
            "State": "available",
            "Type": "ipsec.1",
            "VpnConnectionId": "vpn-0b953fd90796f7c2d",
            "VpnGatewayId": "vgw-0ff076c24c4932e4a",
            "GatewayAssociationState": "associated",
            "Options": {
                "EnableAcceleration": false,
                "StaticRoutesOnly": false,
                "LocalIpv4NetworkCidr": "0.0.0.0/0",
                "RemoteIpv4NetworkCidr": "0.0.0.0/0",
                "OutsideIpAddressType": "PublicIpv4",
                "TunnelInsideIpVersion": "ipv4"
            },
            "Routes": [],
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "CSR1000V1-TO-SPOKE3"
                }
            ],
            "VgwTelemetry": [
                {
                    "AcceptedRouteCount": 3,
                    "LastStatusChange": "2023-04-11 12:31:37+00:00",
                    "OutsideIpAddress": "3.19.204.36",
                    "Status": "UP",
                    "StatusMessage": "3 BGP ROUTES"
                },
                {
                    "AcceptedRouteCount": 3,
                    "LastStatusChange": "2023-04-11 12:30:49+00:00",
                    "OutsideIpAddress": "18.216.245.201",
                    "Status": "UP",
                    "StatusMessage": "3 BGP ROUTES"
                }
            ],
            "CustomerGateways": [
                {
                    "BgpAsn": "64513",
                    "CustomerGatewayId": "cgw-0171e5b81d042c2a3",
                    "IpAddress": "3.18.73.221",
                    "State": "available",
                    "Type": "ipsec.1",
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "Csr1000v-1-to-spoke"
                        }
                    ]
                }
            ]
        }
    ]
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
    "netbrainHostName": "modified-TGW-Burlington(tgw-0cf091f03edf14349)",
    "TransitGatewayId": "tgw-0cf091f03edf14349",
    "TransitGatewayArn": "arn:aws:ec2:us-east-1:747895045325:transit-gateway/tgw-0cf091f03edf14349",
    "State": "available",
    "OwnerId": "747895045325",
    "Description": "",
    "CreationTime": "2019-10-17 14:34:58+00:00",
    "Options": {
        "AmazonSideAsn": 64512,
        "TransitGatewayCidrBlocks": [
            "172.16.110.0/24",
            "172.16.144.0/24"
        ],
        "AutoAcceptSharedAttachments": "enable",
        "DefaultRouteTableAssociation": "enable",
        "AssociationDefaultRouteTableId": "tgw-rtb-0fd3feead375641ee",
        "DefaultRouteTablePropagation": "enable",
        "PropagationDefaultRouteTableId": "tgw-rtb-0fd3feead375641ee",
        "VpnEcmpSupport": "enable",
        "DnsSupport": "enable",
        "MulticastSupport": "disable"
    },
    "Tags": [
        {
            "Key": "jerryName",
            "Value": "jerry_TestSharedTGW_from325_to_925"
        },
        {
            "Key": "yduName",
            "Value": "ydu-add-auto"
        },
        {
            "Key": "Name",
            "Value": "modified-TGW-Burlington"
        }
    ],
    # TransitGatewayConnects: https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_transit_gateway_connects.html
    "TransitGatewayConnects": [],
    # TransitGatewayVpcAttachments: https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_transit_gateway_vpc_attachments.html
    "TransitGatewayVpcAttachments": [
        {
            "TransitGatewayAttachmentId": "tgw-attach-05dcc1f653e6a9068",
            "TransitGatewayId": "tgw-0cf091f03edf14349",
            "VpcId": "vpc-0cc7817f50c71a1ee",
            "VpcOwnerId": "747895045325",
            "State": "available",
            "SubnetIds": [
                "subnet-07dda622172154f86",
                "subnet-036a9acb0c0eaa2b5"
            ],
            "CreationTime": "2019-12-12 20:23:19+00:00",
            "Options": {
                "DnsSupport": "enable",
                "Ipv6Support": "disable",
                "ApplianceModeSupport": "disable"
            },
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Spoke3"
                }
            ]
        },
        {
            "TransitGatewayAttachmentId": "tgw-attach-065ac179a37aebaa9",
            "TransitGatewayId": "tgw-0cf091f03edf14349",
            "VpcId": "vpc-0797a80cf72fdc101",
            "VpcOwnerId": "747895045325",
            "State": "available",
            "SubnetIds": [
                "subnet-065a4164a027dfcb8",
                "subnet-0824ed5caa75b34f2",
                "subnet-06f599635248e1411",
                "subnet-001ec943d1372a97a",
                "subnet-0496f76fd6e4c58ae",
                "subnet-0c3f5802bb568caf3"
            ],
            "CreationTime": "2019-10-17 14:41:07+00:00",
            "Options": {
                "DnsSupport": "enable",
                "Ipv6Support": "disable",
                "ApplianceModeSupport": "disable"
            },
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Spoke2"
                }
            ]
        },
        {
            "TransitGatewayAttachmentId": "tgw-attach-06c2908749d33c077",
            "TransitGatewayId": "tgw-0cf091f03edf14349",
            "VpcId": "vpc-03320aa17c98d8f0d",
            "VpcOwnerId": "747895045325",
            "State": "available",
            "SubnetIds": [
                "subnet-08cfe323236764aa6",
                "subnet-08ebfea5e1b74292a"
            ],
            "CreationTime": "2023-04-19 02:05:28+00:00",
            "Options": {
                "DnsSupport": "enable",
                "Ipv6Support": "disable",
                "ApplianceModeSupport": "disable"
            },
            "Tags": []
        },
        {
            "TransitGatewayAttachmentId": "tgw-attach-0892219188cfb2cf6",
            "TransitGatewayId": "tgw-0cf091f03edf14349",
            "VpcId": "vpc-9d91ebe7",
            "VpcOwnerId": "070113567925",
            "State": "available",
            "SubnetIds": [
                "subnet-a1dcf2c6",
                "subnet-71ae573c",
                "subnet-357a070b",
                "subnet-f44470da",
                "subnet-30416b6c",
                "subnet-69a44767"
            ],
            "CreationTime": "2021-03-08 01:33:15+00:00",
            "Options": {
                "DnsSupport": "enable",
                "Ipv6Support": "disable",
                "ApplianceModeSupport": "disable"
            },
            "Tags": []
        },
        {
            "TransitGatewayAttachmentId": "tgw-attach-0d68673b393c2d608",
            "TransitGatewayId": "tgw-0cf091f03edf14349",
            "VpcId": "vpc-03bf7347a44aea79a",
            "VpcOwnerId": "747895045325",
            "State": "available",
            "SubnetIds": [
                "subnet-01f62fa49059b2723",
                "subnet-054492c8c9f9918a0"
            ],
            "CreationTime": "2023-04-19 03:42:13+00:00",
            "Options": {
                "DnsSupport": "enable",
                "Ipv6Support": "disable",
                "ApplianceModeSupport": "disable"
            },
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "spoke1-path-test-donotdelete-ydu"
                }
            ]
        },
        {
            "TransitGatewayAttachmentId": "tgw-attach-0f95950ca37143ea9",
            "TransitGatewayId": "tgw-0cf091f03edf14349",
            "VpcId": "vpc-071d040c8daf0ceb5",
            "VpcOwnerId": "747895045325",
            "State": "available",
            "SubnetIds": [
                "subnet-02f596e85dd47d086"
            ],
            "CreationTime": "2023-04-19 01:59:31+00:00",
            "Options": {
                "DnsSupport": "enable",
                "Ipv6Support": "disable",
                "ApplianceModeSupport": "disable"
            },
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "spoke4-path-test-donotdelete-ydu"
                }
            ]
        }
    ]
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
    "netbrainHostName": "(igw-0d9c0b7e6b80be1b9)",
    "Attachments": [
        {
            "State": "available",
            "VpcId": "vpc-00a3b35e314056695"
        }
    ],
    "InternetGatewayId": "igw-0d9c0b7e6b80be1b9",
    "OwnerId": "747895045325",
    "Tags": [
        {
            "Key": "DeletedName",
            "Value": "IGW-Spoke1"
        },
        {
            "Key": "Name",
            "Value": ""
        }
    ]
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
    "netbrainHostName": "ydu-0107-EIGW(eigw-00e7cad3148c7eecb)",
    "Attachments": [
        {
            "State": "attached",
            "VpcId": "vpc-00a3b35e314056695"
        }
    ],
    "EgressOnlyInternetGatewayId": "eigw-00e7cad3148c7eecb",
    "Tags": [
        {
            "Key": "DeletedName",
            "Value": "spoke-1-eigw"
        },
        {
            "Key": "Name",
            "Value": "ydu-0107-EIGW"
        }
    ]
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
    "netbrainHostName": "CLB-Test(us-east-1-CLB-Test)",
    "LoadBalancerName": "CLB-Test",
    "DNSName": "CLB-Test-2145122114.us-east-1.elb.amazonaws.com",
    "CanonicalHostedZoneName": "CLB-Test-2145122114.us-east-1.elb.amazonaws.com",
    "CanonicalHostedZoneNameID": "Z35SXDOTRQ7X7K",
    "ListenerDescriptions": [
        {
            "Listener": {
                "Protocol": "HTTP",
                "LoadBalancerPort": 80,
                "InstanceProtocol": "HTTP",
                "InstancePort": 80
            },
            "PolicyNames": []
        }
    ],
    "Policies": {
        "AppCookieStickinessPolicies": [],
        "LBCookieStickinessPolicies": [],
        "OtherPolicies": []
    },
    "BackendServerDescriptions": [],
    "AvailabilityZones": [
        "us-east-1a",
        "us-east-1f"
    ],
    "Subnets": [
        "subnet-06f599635248e1411",
        "subnet-0ad89a2855eed0f21"
    ],
    "VPCId": "vpc-0797a80cf72fdc101",
    "Instances": [
        {
            "InstanceId": "i-00b7c339d4342abe8"
        },
        {
            "InstanceId": "i-01c48b4b29207d3f6"
        }
    ],
    "HealthCheck": {
        "Target": "HTTP:80/",
        "Interval": 30,
        "Timeout": 5,
        "UnhealthyThreshold": 2,
        "HealthyThreshold": 10
    },
    "SourceSecurityGroup": {
        "OwnerAlias": "747895045325",
        "GroupName": "launch-wizard-16"
    },
    "SecurityGroups": [
        "sg-010c1e365627dc62c",
        "sg-07cd62c795a8290f6"
    ],
    "CreatedTime": "2020-06-12 01:15:52.980000+00:00",
    "Scheme": "internet-facing",
    # PolicyDescriptions :https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_load_balancer_policies.html
    "PolicyDescriptions": [],
    # InstanceStates: https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_instance_health.html
    "InstanceStates": [
        {
            "InstanceId": "i-00b7c339d4342abe8",
            "State": "InService",
            "ReasonCode": "N/A",
            "Description": "N/A"
        },
        {
            "InstanceId": "i-01c48b4b29207d3f6",
            "State": "InService",
            "ReasonCode": "N/A",
            "Description": "N/A"
        }
    ]
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
    "netbrainHostName": "ydu-test-nlb(8f9bb06e96b01cb9)",
    "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-east-1:747895045325:loadbalancer/net/ydu-test-nlb/8f9bb06e96b01cb9",
    "DNSName": "ydu-test-nlb-8f9bb06e96b01cb9.elb.us-east-1.amazonaws.com",
    "CanonicalHostedZoneId": "Z26RNL4JYFTOTI",
    "CreatedTime": "2020-04-16 18:30:00.094000+00:00",
    "LoadBalancerName": "ydu-test-nlb",
    "Scheme": "internet-facing",
    "VpcId": "vpc-0797a80cf72fdc101",
    "State": {
        "Code": "active"
    },
    "Type": "network",
    "AvailabilityZones": [
        {
            "ZoneName": "us-east-1f",
            "SubnetId": "subnet-0ad89a2855eed0f21",
            "LoadBalancerAddresses": []
        },
        {
            "ZoneName": "us-east-1b",
            "SubnetId": "subnet-093010f077757c06b",
            "LoadBalancerAddresses": []
        },
        {
            "ZoneName": "us-east-1a",
            "SubnetId": "subnet-07a6bbba0ecb86bed",
            "LoadBalancerAddresses": []
        }
    ],
    "IpAddressType": "ipv4"
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
    "netbrainHostName": "ydu-0107-To-ATT-NetBond(4858a220-af8f-4c35-b8b8-9f8b22579220)",
    "directConnectGatewayId": "4858a220-af8f-4c35-b8b8-9f8b22579220",
    "directConnectGatewayName": "ydu-0107-To-ATT-NetBond",
    "amazonSideAsn": 64515,
    "ownerAccount": "747895045325",
    "directConnectGatewayState": "available",
    # Direct Connect Gateway Attachments: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/client/describe_direct_connect_gateway_attachments.html
    "directConnectGatewayAttachments": [
        {
            "directConnectGatewayId": "4858a220-af8f-4c35-b8b8-9f8b22579220",
            "virtualInterfaceId": "dxvif-fgvbkc82",
            "virtualInterfaceRegion": "us-east-2",
            "virtualInterfaceOwnerAccount": "747895045325",
            "attachmentState": "attached",
            "attachmentType": "privateVirtualInterface"
        },
        {
            "directConnectGatewayId": "4858a220-af8f-4c35-b8b8-9f8b22579220",
            "virtualInterfaceId": "dxvif-fgch1dug",
            "virtualInterfaceRegion": "us-east-2",
            "virtualInterfaceOwnerAccount": "747895045325",
            "attachmentState": "attached",
            "attachmentType": "privateVirtualInterface"
        }
    ],
    # Direct Connect Gateway Associations: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/client/describe_direct_connect_gateway_associations.html
    "directConnectGatewayAssociations": [
        {
            "directConnectGatewayId": "4858a220-af8f-4c35-b8b8-9f8b22579220",
            "directConnectGatewayOwnerAccount": "747895045325",
            "associationState": "associated",
            "associatedGateway": {
                "id": "vgw-0f524f7ee86cc36a1",
                "type": "virtualPrivateGateway",
                "ownerAccount": "747895045325",
                "region": "us-west-2"
            },
            "associationId": "a090f965-0d2c-413f-8941-8b6b8229c2a0",
            "allowedPrefixesToDirectConnectGateway": [
                {
                    "cidr": "1.1.1.1/32"
                }
            ],
            "virtualGatewayId": "vgw-0f524f7ee86cc36a1",
            "virtualGatewayRegion": "us-west-2",
            "virtualGatewayOwnerAccount": "747895045325"
        },
        {
            "directConnectGatewayId": "4858a220-af8f-4c35-b8b8-9f8b22579220",
            "directConnectGatewayOwnerAccount": "747895045325",
            "associationState": "associated",
            "associatedGateway": {
                "id": "vgw-073f3dd73ac4bc890",
                "type": "virtualPrivateGateway",
                "ownerAccount": "747895045325",
                "region": "us-east-1"
            },
            "associationId": "47be625c-bf3b-4aa9-91e3-3b51ee0f6792",
            "allowedPrefixesToDirectConnectGateway": [
                {
                    "cidr": "172.16.105.0/24"
                },
                {
                    "cidr": "172.16.109.0/24"
                }
            ],
            "virtualGatewayId": "vgw-073f3dd73ac4bc890",
            "virtualGatewayRegion": "us-east-1",
            "virtualGatewayOwnerAccount": "747895045325"
        },
        {
            "directConnectGatewayId": "4858a220-af8f-4c35-b8b8-9f8b22579220",
            "directConnectGatewayOwnerAccount": "747895045325",
            "associationState": "associated",
            "associatedGateway": {
                "id": "vgw-01fc88164f72433e2",
                "type": "virtualPrivateGateway",
                "ownerAccount": "747895045325",
                "region": "us-east-2"
            },
            "associationId": "95226c76-5516-479b-afd8-4fa590abce65",
            "allowedPrefixesToDirectConnectGateway": [
                {
                    "cidr": "172.26.1.0/24"
                },
                {
                    "cidr": "172.26.0.0/24"
                }
            ],
            "virtualGatewayId": "vgw-01fc88164f72433e2",
            "virtualGatewayRegion": "us-east-2",
            "virtualGatewayOwnerAccount": "747895045325"
        },
        {
            "directConnectGatewayId": "4858a220-af8f-4c35-b8b8-9f8b22579220",
            "directConnectGatewayOwnerAccount": "747895045325",
            "associationState": "associated",
            "associatedGateway": {
                "id": "vgw-0bf6f287a9b85ca7d",
                "type": "virtualPrivateGateway",
                "ownerAccount": "070113567925",
                "region": "us-east-2"
            },
            "associationId": "1c850c56-d502-43b1-9c3f-744fa9781e3b",
            "allowedPrefixesToDirectConnectGateway": [
                {
                    "cidr": "172.46.0.0/16"
                }
            ],
            "virtualGatewayId": "vgw-0bf6f287a9b85ca7d",
            "virtualGatewayRegion": "us-east-2",
            "virtualGatewayOwnerAccount": "070113567925"
        }
    ],
    # Direct Connect Gateway Association Proposals: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/client/describe_direct_connect_gateway_association_proposals.html
    "directConnectGatewayAssociationProposals": []
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
    "netbrainHostName": "ydu-0107-NATGW(nat-01d93d718149d18b5)",
    "CreateTime": "2020-03-30 16:02:01+00:00",
    "NatGatewayAddresses": [
        {
            "AllocationId": "eipalloc-0eb05bbebc5383088",
            "NetworkInterfaceId": "eni-0023d92ac6f9c8171",
            "PrivateIp": "10.56.0.44",
            "PublicIp": "15.223.93.245"
        }
    ],
    "NatGatewayId": "nat-01d93d718149d18b5",
    "State": "available",
    "SubnetId": "subnet-0d6b8fe5e2c7aa90c",
    "VpcId": "vpc-09e3aa218b9e81d3d",
    "Tags": [
        {
            "Key": "Name",
            "Value": "ydu-0107-NATGW"
        }
    ],
    "ConnectivityType": "public",
    # Subnet: https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_subnets.html
    "Subnet": [
        {
            "AvailabilityZone": "ca-central-1b",
            "AvailabilityZoneId": "cac1-az2",
            "AvailableIpAddressCount": 247,
            "CidrBlock": "10.56.0.0/24",
            "DefaultForAz": false,
            "MapPublicIpOnLaunch": false,
            "MapCustomerOwnedIpOnLaunch": false,
            "State": "available",
            "SubnetId": "subnet-0d6b8fe5e2c7aa90c",
            "VpcId": "vpc-09e3aa218b9e81d3d",
            "OwnerId": "747895045325",
            "AssignIpv6AddressOnCreation": false,
            "Ipv6CidrBlockAssociationSet": [],
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Case1_subnet_1"
                }
            ],
            "SubnetArn": "arn:aws:ec2:ca-central-1:747895045325:subnet/subnet-0d6b8fe5e2c7aa90c",
            "EnableDns64": false,
            "Ipv6Native": false,
            "PrivateDnsNameOptionsOnLaunch": {
                "HostnameType": "ip-name",
                "EnableResourceNameDnsARecord": false,
                "EnableResourceNameDnsAAAARecord": false
            }
        }
    ]
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
    "netbrainHostName": "NB-AWS-Lab-Firewall-1(us-east-1-194a86f1-8a17-4da7-b710-01224f5deb75)",
    "UpdateToken": "d1f67f7d-6ca2-48c7-90e9-22523c7ed265",
    "Firewall": {
        "FirewallName": "NB-AWS-Lab-Firewall-1",
        "FirewallArn": "arn:aws:network-firewall:us-east-1:747895045325:firewall/NB-AWS-Lab-Firewall-1",
        "FirewallPolicyArn": "arn:aws:network-firewall:us-east-1:747895045325:firewall-policy/Lab-Firewall-2",
        "VpcId": "vpc-0e2aedae2e15f4561",
        "SubnetMappings": [
            {
                "SubnetId": "subnet-0555fa21f5c6bb617"
            },
            {
                "SubnetId": "subnet-0992ee10c5afbbb42"
            }
        ],
        "DeleteProtection": false,
        "SubnetChangeProtection": false,
        "FirewallPolicyChangeProtection": false,
        "FirewallId": "194a86f1-8a17-4da7-b710-01224f5deb75",
        "Tags": [],
        "EncryptionConfiguration": {
            "KeyId": "AWS_OWNED_KMS_KEY",
            "Type": "AWS_OWNED_KMS_KEY"
        }
    },
    "FirewallStatus": {
        "Status": "READY",
        "ConfigurationSyncStateSummary": "IN_SYNC",
        "SyncStates": {
            "us-east-1a": {
                "Attachment": {
                    "SubnetId": "subnet-0555fa21f5c6bb617",
                    "EndpointId": "vpce-0ba08cf3d86416117",
                    "Status": "READY"
                },
                "Config": {
                    "arn:aws:network-firewall:us-east-1:747895045325:stateful-rulegroup/2ND-Stateful-Rule-Group": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "8daa5ad8-3fd2-4704-9e2b-1af25c494424"
                    },
                    "arn:aws:network-firewall:us-east-1:747895045325:stateless-rulegroup/Fw-to-Stateful-Rule": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "d9d28a0b-75d4-45b4-ad25-9bc22a00abb1"
                    },
                    "arn:aws:network-firewall:us-east-1:aws-managed:stateful-rulegroup/MalwareDomainsStrictOrder": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "1d78f40c-ed91-4981-ba0a-5da3891da281"
                    },
                    "arn:aws:network-firewall:us-east-1:747895045325:firewall-policy/Lab-Firewall-2": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "092e45c5-d3f6-4473-90d5-de234b562664"
                    },
                    "arn:aws:network-firewall:us-east-1:747895045325:stateless-rulegroup/Lab-Firewall-1-Stateless-Rule": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "343f0ee5-0d57-46ee-8ffb-ea9e60a6f874"
                    }
                }
            },
            "us-east-1f": {
                "Attachment": {
                    "SubnetId": "subnet-0992ee10c5afbbb42",
                    "EndpointId": "vpce-0fc9ea6dcf3090c26",
                    "Status": "READY"
                },
                "Config": {
                    "arn:aws:network-firewall:us-east-1:747895045325:stateful-rulegroup/2ND-Stateful-Rule-Group": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "8daa5ad8-3fd2-4704-9e2b-1af25c494424"
                    },
                    "arn:aws:network-firewall:us-east-1:747895045325:stateless-rulegroup/Fw-to-Stateful-Rule": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "d9d28a0b-75d4-45b4-ad25-9bc22a00abb1"
                    },
                    "arn:aws:network-firewall:us-east-1:aws-managed:stateful-rulegroup/MalwareDomainsStrictOrder": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "1d78f40c-ed91-4981-ba0a-5da3891da281"
                    },
                    "arn:aws:network-firewall:us-east-1:747895045325:firewall-policy/Lab-Firewall-2": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "092e45c5-d3f6-4473-90d5-de234b562664"
                    },
                    "arn:aws:network-firewall:us-east-1:747895045325:stateless-rulegroup/Lab-Firewall-1-Stateless-Rule": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "343f0ee5-0d57-46ee-8ffb-ea9e60a6f874"
                    }
                }
            }
        }
    },
    "ResponseMetadata": {
        "RequestId": "0f52c3df-6c04-45bf-b5c0-7df8e6519205",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "0f52c3df-6c04-45bf-b5c0-7df8e6519205",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "2776",
            "date": "Fri, 02 Jun 2023 01:59:34 GMT"
        },
        "RetryAttempts": 0
    }
}
```
</details>
<br />
  

