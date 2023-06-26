# Usage
To retrieve the configuration data for a resource, you can utilize NetBrain's built-in configuration file function, which does not require coding. This function enables you to quickly obtain the resource configuration.


# Table of Contents
* [AWS VPC Router](#aws-vpc-router)
* [AWS Gateway VPC Endpoint](#aws-vpc-endpoint)
* [AWS Interface VPC Endpoint](#aws-vpc-endpoint)
* [AWS Virtual Private Gateway](#aws-virtual-private-gateway)
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
    "netbrainHostName": "Spoke1(vpc-xxxxxxxxxxxxxxxxx)",
    "CidrBlock": "172.16.101.0/24",
    "DhcpOptionsId": "xxxx-xxxxxxxxx",
    "State": "available",
    "VpcId": "vpc-xxxxxxxxxxxxxxxxx",
    "OwnerId": "747895045325",
    "InstanceTenancy": "default",
    "CidrBlockAssociationSet": [
        {
            "AssociationId": "vpc-cidr-assoc-xxxxxxxxxxxxxxxxx",
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
            "SubnetId": "subnet-xxxxxxxxxxxxxxxxx",
            "VpcId": "vpc-xxxxxxxxxxxxxxxxx",
            "OwnerId": "xxxxxxxxxxxxxxxxx",
            "AssignIpv6AddressOnCreation": false,
            "Ipv6CidrBlockAssociationSet": [],
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "BMC-Subnet"
                }
            ],
            "SubnetArn": "arn:aws:ec2:us-east-1:xxxxxxxxxxxxxxxxx:subnet/subnet-xxxxxxxxxxxxxxxxx",
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
                "VpcId": "vpc-xxxxxxxxxxxxxxxxx",
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
            "VpcPeeringConnectionId": "pcx-xxxxxxxxxxxxxxxxx"
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
                "OwnerId": "xxxxxxxxxxxxxxxxx",
                "PeeringOptions": {
                    "AllowDnsResolutionFromRemoteVpc": false,
                    "AllowEgressFromLocalClassicLinkToRemoteVpc": false,
                    "AllowEgressFromLocalVpcToRemoteClassicLink": false
                },
                "VpcId": "vpc-xxxxxxxxxxxxxxxxx",
                "Region": "us-east-2"
            },
            "RequesterVpcInfo": {
                "CidrBlock": "172.16.101.0/24",
                "CidrBlockSet": [
                    {
                        "CidrBlock": "172.16.101.0/24"
                    }
                ],
                "OwnerId": "xxxxxxxxxxxxxxxxx",
                "PeeringOptions": {
                    "AllowDnsResolutionFromRemoteVpc": false,
                    "AllowEgressFromLocalClassicLinkToRemoteVpc": false,
                    "AllowEgressFromLocalVpcToRemoteClassicLink": false
                },
                "VpcId": "vpc-xxxxxxxxxxxxxxxxx",
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
            "VpcPeeringConnectionId": "pcx-xxxxxxxxxxxxxxxxx"
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
                "OwnerId": "xxxxxxxxxxxxxxxxx",
                "PeeringOptions": {
                    "AllowDnsResolutionFromRemoteVpc": false,
                    "AllowEgressFromLocalClassicLinkToRemoteVpc": false,
                    "AllowEgressFromLocalVpcToRemoteClassicLink": false
                },
                "VpcId": "vpc-xxxxxxxxxxxxxxxxx",
                "Region": "ca-central-1"
            },
            "RequesterVpcInfo": {
                "CidrBlock": "172.16.101.0/24",
                "CidrBlockSet": [
                    {
                        "CidrBlock": "172.16.101.0/24"
                    }
                ],
                "OwnerId": "xxxxxxxxxxxxxxxxx",
                "PeeringOptions": {
                    "AllowDnsResolutionFromRemoteVpc": false,
                    "AllowEgressFromLocalClassicLinkToRemoteVpc": false,
                    "AllowEgressFromLocalVpcToRemoteClassicLink": false
                },
                "VpcId": "vpc-xxxxxxxxxxxxxxxxx",
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
            "VpcPeeringConnectionId": "pcx-xxxxxxxxxxxxxxxxx"
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
    "netbrainHostName": "spoke2-s3-vpcgwe(vpce-xxxxxxxxxxxxxxxxx)",
    "VpcEndpointId": "vpce-xxxxxxxxxxxxxxxxx",
    "VpcEndpointType": "Gateway",
    "VpcId": "vpc-xxxxxxxxxxxxxxxxx",
    "ServiceName": "com.amazonaws.us-east-1.s3",
    "State": "available",
    "PolicyDocument": "{\"Version\":\"2008-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"*\",\"Resource\":\"*\"}]}",
    "RouteTableIds": [
        "rtb-xxxxxxxxxxxxxxxxx"
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
    "OwnerId": "xxxxxxxxxxxxxxxxx",
    # VPC Endpoint Connections: https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_vpc_endpoint_connections.html
    "VpcEndpointConnections": []
}
```

</details>
<br />


## AWS Virtual Private Gateway

### Introduction
The configuration of the AWS Virtual Private Gateway is dependent on the AWS SDK response of the AWS Virtual Private Gateway as the primary response. The full resource configuration consists of some associated resources' data, including `Vpc Endpoint Connections`, `Vpn Connections`, and `Customer Gateways`.

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
    "netbrainHostName": "spoke-vpc-3-vgw(vgw-xxxxxxxxxxxxxxxxx)",
    "State": "available",
    "Type": "ipsec.1",

    "VpcAttachments": [
        {
            "State": "attached",
            "VpcId": "vpc-xxxxxxxxxxxxxxxxx"
        }
    ],
    "VpnGatewayId": "vgw-xxxxxxxxxxxxxxxxx",
    "AmazonSideAsn": 64512,
    "Tags": [
        {
            "Key": "Name",
            "Value": "spoke-vpc-3-vgw"
        }
    ],
    # VPN Connections: https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_vpn_connections.html
    "VpnConnections": [
        {
            "CustomerGatewayConfiguration": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<vpn_connection id=\"vpn-xxxxxxxxxxxxxxxxx\">\n  <customer_gateway_id>cgw-xxxxxxxxxxxxxxxxx</customer_gateway_id>\n  <vpn_gateway_id>vgw-xxxxxxxxxxxxxxxxx</vpn_gateway_id>\n  <vpn_connection_type>ipsec.1</vpn_connection_type>\n  <ipsec_tunnel>\n    <customer_gateway>\n      <tunnel_outside_address>\n        <ip_address>3.15.245.169</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.225.10</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64513</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </customer_gateway>\n    <vpn_gateway>\n      <tunnel_outside_address>\n        <ip_address>3.18.239.122</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.225.9</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64512</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </vpn_gateway>\n    <ike>\n      <authentication_protocol>sha1</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>28800</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>main</mode>\n      <pre_shared_key>xlk6lMNzd4CNRP8YUX4PlRLVL4pV1FWS</pre_shared_key>\n    </ike>\n    <ipsec>\n      <protocol>esp</protocol>\n      <authentication_protocol>hmac-sha1-96</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>3600</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>tunnel</mode>\n      <clear_df_bit>true</clear_df_bit>\n      <fragmentation_before_encryption>true</fragmentation_before_encryption>\n      <tcp_mss_adjustment>1379</tcp_mss_adjustment>\n      <dead_peer_detection>\n        <interval>10</interval>\n        <retries>3</retries>\n      </dead_peer_detection>\n    </ipsec>\n  </ipsec_tunnel>\n  <ipsec_tunnel>\n    <customer_gateway>\n      <tunnel_outside_address>\n        <ip_address>3.15.245.169</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.68.26</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64513</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </customer_gateway>\n    <vpn_gateway>\n      <tunnel_outside_address>\n        <ip_address>52.15.217.142</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.68.25</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64512</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </vpn_gateway>\n    <ike>\n      <authentication_protocol>sha1</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>28800</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>main</mode>\n      <pre_shared_key>KMA_6TXDeJzOJAnrn6gnMEtCO0jbE655</pre_shared_key>\n    </ike>\n    <ipsec>\n      <protocol>esp</protocol>\n      <authentication_protocol>hmac-sha1-96</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>3600</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>tunnel</mode>\n      <clear_df_bit>true</clear_df_bit>\n      <fragmentation_before_encryption>true</fragmentation_before_encryption>\n      <tcp_mss_adjustment>1379</tcp_mss_adjustment>\n      <dead_peer_detection>\n        <interval>10</interval>\n        <retries>3</retries>\n      </dead_peer_detection>\n    </ipsec>\n  </ipsec_tunnel>\n</vpn_connection>",
            "CustomerGatewayId": "cgw-xxxxxxxxxxxxxxxxx",
            "Category": "VPN",
            "State": "available",
            "Type": "ipsec.1",
            "VpnConnectionId": "vpn-xxxxxxxxxxxxxxxxx",
            "VpnGatewayId": "vgw-xxxxxxxxxxxxxxxxx",
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
                    "OutsideIpAddress": "xxx.xxx.xxx.xxx",
                    "Status": "UP",
                    "StatusMessage": "0 BGP ROUTES"
                },
                {
                    "AcceptedRouteCount": 0,
                    "LastStatusChange": "2023-04-29 01:09:41+00:00",
                    "OutsideIpAddress": "xxx.xxx.xxx.xxx",
                    "Status": "UP",
                    "StatusMessage": "0 BGP ROUTES"
                }
            ],
            # Customer Gateways: https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_customer_gateways.html
            "CustomerGateways": [
                {
                    "BgpAsn": "64513",
                    "CustomerGatewayId": "cgw-xxxxxxxxxxxxxxxxx",
                    "IpAddress": "xxx.xxx.xxx.xxx",
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
            "CustomerGatewayConfiguration": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<vpn_connection id=\"vpn-xxxxxxxxxxxxxxxxx\">\n  <customer_gateway_id>cgw-xxxxxxxxxxxxxxxxx</customer_gateway_id>\n  <vpn_gateway_id>vgw-xxxxxxxxxxxxxxxxx</vpn_gateway_id>\n  <vpn_connection_type>ipsec.1</vpn_connection_type>\n  <ipsec_tunnel>\n    <customer_gateway>\n      <tunnel_outside_address>\n        <ip_address>3.18.73.221</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.14.138</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64513</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </customer_gateway>\n    <vpn_gateway>\n      <tunnel_outside_address>\n        <ip_address>3.19.204.36</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.14.137</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64512</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </vpn_gateway>\n    <ike>\n      <authentication_protocol>sha1</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>28800</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>main</mode>\n      <pre_shared_key>W.1xFZ9TAtwgIn5g5vxKikxaIVFDH56i</pre_shared_key>\n    </ike>\n    <ipsec>\n      <protocol>esp</protocol>\n      <authentication_protocol>hmac-sha1-96</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>3600</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>tunnel</mode>\n      <clear_df_bit>true</clear_df_bit>\n      <fragmentation_before_encryption>true</fragmentation_before_encryption>\n      <tcp_mss_adjustment>1379</tcp_mss_adjustment>\n      <dead_peer_detection>\n        <interval>10</interval>\n        <retries>3</retries>\n      </dead_peer_detection>\n    </ipsec>\n  </ipsec_tunnel>\n  <ipsec_tunnel>\n    <customer_gateway>\n      <tunnel_outside_address>\n        <ip_address>3.18.73.221</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.10.6</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64513</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </customer_gateway>\n    <vpn_gateway>\n      <tunnel_outside_address>\n        <ip_address>18.216.245.201</ip_address>\n      </tunnel_outside_address>\n      <tunnel_inside_address>\n        <ip_address>169.254.10.5</ip_address>\n        <network_mask>255.255.255.252</network_mask>\n        <network_cidr>30</network_cidr>\n      </tunnel_inside_address>\n      <bgp>\n        <asn>64512</asn>\n        <hold_time>30</hold_time>\n      </bgp>\n    </vpn_gateway>\n    <ike>\n      <authentication_protocol>sha1</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>28800</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>main</mode>\n      <pre_shared_key>yrPRMk7SGQyo.es7ywU38qHAucXH8E8Q</pre_shared_key>\n    </ike>\n    <ipsec>\n      <protocol>esp</protocol>\n      <authentication_protocol>hmac-sha1-96</authentication_protocol>\n      <encryption_protocol>aes-128-cbc</encryption_protocol>\n      <lifetime>3600</lifetime>\n      <perfect_forward_secrecy>group2</perfect_forward_secrecy>\n      <mode>tunnel</mode>\n      <clear_df_bit>true</clear_df_bit>\n      <fragmentation_before_encryption>true</fragmentation_before_encryption>\n      <tcp_mss_adjustment>1379</tcp_mss_adjustment>\n      <dead_peer_detection>\n        <interval>10</interval>\n        <retries>3</retries>\n      </dead_peer_detection>\n    </ipsec>\n  </ipsec_tunnel>\n</vpn_connection>",
            "CustomerGatewayId": "cgw-xxxxxxxxxxxxxxxxx",
            "Category": "VPN",
            "State": "available",
            "Type": "ipsec.1",
            "VpnConnectionId": "vpn-xxxxxxxxxxxxxxxxx",
            "VpnGatewayId": "vgw-xxxxxxxxxxxxxxxxx",
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
                    "OutsideIpAddress": "xxx.xxx.xxx.xxx",
                    "Status": "UP",
                    "StatusMessage": "3 BGP ROUTES"
                },
                {
                    "AcceptedRouteCount": 3,
                    "LastStatusChange": "2023-04-11 12:30:49+00:00",
                    "OutsideIpAddress": "xxx.xxx.xxx.xxx",
                    "Status": "UP",
                    "StatusMessage": "3 BGP ROUTES"
                }
            ],
            "CustomerGateways": [
                {
                    "BgpAsn": "64513",
                    "CustomerGatewayId": "cgw-xxxxxxxxxxxxxxxxx",
                    "IpAddress": "xxx.xxx.xxx.xxx",
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
    "netbrainHostName": "modified-TGW-Burlington(tgw-xxxxxxxxxxxxxxxxx)",
    "TransitGatewayId": "tgw-xxxxxxxxxxxxxxxxx",
    "TransitGatewayArn": "arn:aws:ec2:us-east-1:747895045325:transit-gateway/tgw-xxxxxxxxxxxxxxxxx",
    "State": "available",
    "OwnerId": "xxxxxxxxxxxxxxxxx",
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
        "AssociationDefaultRouteTableId": "tgw-rtb-xxxxxxxxxxxxxxxxx",
        "DefaultRouteTablePropagation": "enable",
        "PropagationDefaultRouteTableId": "tgw-rtb-xxxxxxxxxxxxxxxxx",
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
    # Transit Gateway Connects: https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_transit_gateway_connects.html
    "TransitGatewayConnects": [],
    # Transit Gateway Vpc Attachments: https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_transit_gateway_vpc_attachments.html
    "TransitGatewayVpcAttachments": [
        {
            "TransitGatewayAttachmentId": "tgw-attach-xxxxxxxxxxxxxxxxx",
            "TransitGatewayId": "tgw-xxxxxxxxxxxxxxxxx",
            "VpcId": "vpc-xxxxxxxxxxxxxxxxx",
            "VpcOwnerId": "xxxxxxxxxxxxxxxxx",
            "State": "available",
            "SubnetIds": [
                "subnet-xxxxxxxxxxxxxxxxx",
                "subnet-xxxxxxxxxxxxxxxxx"
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
            "TransitGatewayAttachmentId": "tgw-attach-xxxxxxxxxxxxxxxxx",
            "TransitGatewayId": "tgw-xxxxxxxxxxxxxxxxx",
            "VpcId": "vpc-xxxxxxxxxxxxxxxxx",
            "VpcOwnerId": "xxxxxxxxxxxxxxxxx",
            "State": "available",
            "SubnetIds": [
                "subnet-xxxxxxxxxxxxxxxxx",
                "subnet-xxxxxxxxxxxxxxxxx",
                "subnet-xxxxxxxxxxxxxxxxx",
                "subnet-xxxxxxxxxxxxxxxxx",
                "subnet-xxxxxxxxxxxxxxxxx",
                "subnet-xxxxxxxxxxxxxxxxx"
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
            "TransitGatewayAttachmentId": "tgw-attach-xxxxxxxxxxxxxxxxx",
            "TransitGatewayId": "tgw-xxxxxxxxxxxxxxxxx",
            "VpcId": "vpc-xxxxxxxxxxxxxxxxx",
            "VpcOwnerId": "xxxxxxxxxxxxxxxxx",
            "State": "available",
            "SubnetIds": [
                "subnet-xxxxxxxxxxxxxxxxx",
                "subnet-xxxxxxxxxxxxxxxxx"
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
            "TransitGatewayAttachmentId": "tgw-attach-xxxxxxxxxxxxxxxxx",
            "TransitGatewayId": "tgw-xxxxxxxxxxxxxxxxx",
            "VpcId": "vpc-xxxxxxxxxxxxxxxxx",
            "VpcOwnerId": "xxxxxxxxxxxxxxxxx",
            "State": "available",
            "SubnetIds": [
                "subnet-xxxxxxxxxxxxxxxxx",
                "subnet-xxxxxxxxxxxxxxxxx",
                "subnet-xxxxxxxxxxxxxxxxx",
                "subnet-xxxxxxxxxxxxxxxxx",
                "subnet-xxxxxxxxxxxxxxxxx",
                "subnet-xxxxxxxxxxxxxxxxx"
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
            "TransitGatewayAttachmentId": "tgw-attach-xxxxxxxxxxxxxxxxx",
            "TransitGatewayId": "tgw-xxxxxxxxxxxxxxxxx",
            "VpcId": "vpc-xxxxxxxxxxxxxxxxx",
            "VpcOwnerId": "xxxxxxxxxxxxxxxxx",
            "State": "available",
            "SubnetIds": [
                "subnet-xxxxxxxxxxxxxxxxx",
                "subnet-xxxxxxxxxxxxxxxxx"
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
            "TransitGatewayAttachmentId": "tgw-attach-xxxxxxxxxxxxxxxxx",
            "TransitGatewayId": "tgw-xxxxxxxxxxxxxxxxx",
            "VpcId": "vpc-xxxxxxxxxxxxxxxxx",
            "VpcOwnerId": "xxxxxxxxxxxxxxxxx",
            "State": "available",
            "SubnetIds": [
                "subnet-xxxxxxxxxxxxxxxxx"
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
The configuration of the AWS Internet Gateway relies solely on the corresponding AWS SDK of the internet gateway. The AWS SDK provides detailed information regarding the configuration of the internet gateway, including its connectivity, security, etc.

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
    "netbrainHostName": "(igw-xxxxxxxxxxxxxxxxx)",
    "Attachments": [
        {
            "State": "available",
            "VpcId": "vpc-xxxxxxxxxxxxxxxxx"
        }
    ],
    "InternetGatewayId": "igw-xxxxxxxxxxxxxxxxx",
    "OwnerId": "xxxxxxxxxxxxxxxxx",
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
The configuration of the AWS Egress Internet Gateway relies solely on the corresponding AWS SDK of the egress internet gateway. The AWS SDK provides detailed information regarding the configuration of the egress internet gateway, including its connectivity, security, etc.

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
    "netbrainHostName": "ydu-0107-EIGW(eigw-xxxxxxxxxxxxxxxxx)",
    "Attachments": [
        {
            "State": "attached",
            "VpcId": "vpc-xxxxxxxxxxxxxxxxx"
        }
    ],
    "EgressOnlyInternetGatewayId": "eigw-xxxxxxxxxxxxxxxxx",
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
    "DNSName": "CLB-Test-xxxxxxxxxxxxxxxxx.us-east-1.elb.amazonaws.com",
    "CanonicalHostedZoneName": "CLB-Test-xxxxxxxxxxxxxxxxx.us-east-1.elb.amazonaws.com",
    "CanonicalHostedZoneNameID": "xxxxxxxxxxxxx",
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
        "subnet-xxxxxxxxxxxxxxxxx",
        "subnet-xxxxxxxxxxxxxxxxx"
    ],
    "VPCId": "vpc-xxxxxxxxxxxxxxxxx",
    "Instances": [
        {
            "InstanceId": "i-xxxxxxxxxxxxxxxxx"
        },
        {
            "InstanceId": "i-xxxxxxxxxxxxxxxxx"
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
        "OwnerAlias": "xxxxxxxxxxxxxxxxx",
        "GroupName": "launch-wizard-16"
    },
    "SecurityGroups": [
        "sg-xxxxxxxxxxxxxxxxx",
        "sg-xxxxxxxxxxxxxxxxx"
    ],
    "CreatedTime": "2020-06-12 01:15:52.980000+00:00",
    "Scheme": "internet-facing",
    # Policy Descriptions: https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_load_balancer_policies.html
    "PolicyDescriptions": [],
    # Instance States: https://boto3.amazonaws.com/v1/documentation/api/1.26.86/reference/services/ec2/client/describe_instance_health.html
    "InstanceStates": [
        {
            "InstanceId": "i-xxxxxxxxxxxxxxxxx",
            "State": "InService",
            "ReasonCode": "N/A",
            "Description": "N/A"
        },
        {
            "InstanceId": "i-xxxxxxxxxxxxxxxxx",
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
    "netbrainHostName": "ydu-test-nlb(xxxxxxxxxxxxxxxxx)",
    "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-east-1:xxxxxxxxxxxxxxxxx:loadbalancer/net/ydu-test-nlb/xxxxxxxxxxxxxxxxx",
    "DNSName": "ydu-test-nlb-xxxxxxxxxxxxxxxxx.elb.us-east-1.amazonaws.com",
    "CanonicalHostedZoneId": "Z26RNL4JYFTOTI",
    "CreatedTime": "2020-04-16 18:30:00.094000+00:00",
    "LoadBalancerName": "ydu-test-nlb",
    "Scheme": "internet-facing",
    "VpcId": "vpc-xxxxxxxxxxxxxxxxx",
    "State": {
        "Code": "active"
    },
    "Type": "network",
    "AvailabilityZones": [
        {
            "ZoneName": "us-east-1f",
            "SubnetId": "subnet-xxxxxxxxxxxxxxxxx",
            "LoadBalancerAddresses": []
        },
        {
            "ZoneName": "us-east-1b",
            "SubnetId": "subnet-xxxxxxxxxxxxxxxxx",
            "LoadBalancerAddresses": []
        },
        {
            "ZoneName": "us-east-1a",
            "SubnetId": "subnet-xxxxxxxxxxxxxxxxx",
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
    "netbrainHostName": "EqDC2-xxxxxxxxxxxxxxxxx(dxcon-xxxxxxxxxxxx)",
    "ownerAccount": "string",
    "virtualInterfaceId": "string",
    "location": "string",
    "connectionId": "string",
    "virtualInterfaceType": "string",
    "virtualInterfaceName": "string",
    "vlan": 123,
    "asn": 123,
    "amazonSideAsn": 123,
    "authKey": "string",
    "amazonAddress": "string",
    "customerAddress": "string",
    "addressFamily": "ipv4",
    "virtualInterfaceState": "available",
    "customerRouterConfig": "string",
    "mtu": 123,
    "jumboFrameCapable": true,
    "virtualGatewayId": "string",
    "directConnectGatewayId": "string",
    "routeFilterPrefixes": [
        {
            "cidr": "string"
        }
    ],
    "bgpPeers": [
        {
            "bgpPeerId": "string",
            "asn": 123,
            "authKey": "string",
            "addressFamily": "ipv4",
            "amazonAddress": "string",
            "customerAddress": "string",
            "bgpPeerState": "available",
            "bgpStatus": "up",
            "awsDeviceV2": "string",
            "awsLogicalDeviceId": "string"
        }
    ],
    "region": "string",
    "awsDeviceV2": "string",
    "awsLogicalDeviceId": "string",
    "tags": [
        {
            "key": "string",
            "value": "string"
        }
    ],
    "siteLinkEnabled": true,
    # connections: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/client/describe_connections.html
    "connections": [
        {
            "ownerAccount": "string",
            "connectionId": "string",
            "connectionName": "string",
            "connectionState": "available",
            "region": "string",
            "location": "string",
            "bandwidth": "string",
            "vlan": 123,
            "partnerName": "string",
            "loaIssueTime": "2015-01-01T00:00:00",
            "lagId": "string",
            "awsDevice": "string",
            "jumboFrameCapable": true,
            "awsDeviceV2": "string",
            "awsLogicalDeviceId": "string",
            "hasLogicalRedundancy": "yes",
            "tags": [
                {
                    "key": "string",
                    "value": "string"
                }
            ],
            "providerName": "string",
            "macSecCapable": true,
            "portEncryptionStatus": "string",
            "encryptionMode": "string",
            "macSecKeys": [
                {
                    "secretARN": "string",
                    "ckn": "string",
                    "state": "string",
                    "startOn": "string"
                }
            ]
        }
    ]
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
    "netbrainHostName": "ydu-0107-To-ATT-NetBond(xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)",
    "directConnectGatewayId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "directConnectGatewayName": "ydu-0107-To-ATT-NetBond",
    "amazonSideAsn": 64515,
    "ownerAccount": "xxxxxxxxxxxx",
    "directConnectGatewayState": "available",
    # Direct Connect Gateway Attachments: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/client/describe_direct_connect_gateway_attachments.html
    "directConnectGatewayAttachments": [
        {
            "directConnectGatewayId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "virtualInterfaceId": "dxvif-xxxxxxxxxxxx",
            "virtualInterfaceRegion": "us-east-2",
            "virtualInterfaceOwnerAccount": "xxxxxxxxxxxx",
            "attachmentState": "attached",
            "attachmentType": "privateVirtualInterface"
        },
        {
            "directConnectGatewayId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "virtualInterfaceId": "dxvif-xxxxxxxx",
            "virtualInterfaceRegion": "us-east-2",
            "virtualInterfaceOwnerAccount": "xxxxxxxxxxxx",
            "attachmentState": "attached",
            "attachmentType": "privateVirtualInterface"
        }
    ],
    # Direct Connect Gateway Associations: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/directconnect/client/describe_direct_connect_gateway_associations.html
    "directConnectGatewayAssociations": [
        {
            "directConnectGatewayId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "directConnectGatewayOwnerAccount": "xxxxxxxxxxxx",
            "associationState": "associated",
            "associatedGateway": {
                "id": "vgw-xxxxxxxxxxxx",
                "type": "virtualPrivateGateway",
                "ownerAccount": "xxxxxxxxxxxx",
                "region": "us-west-2"
            },
            "associationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "allowedPrefixesToDirectConnectGateway": [
                {
                    "cidr": "1.1.1.1/32"
                }
            ],
            "virtualGatewayId": "vgw-xxxxxxxxxxxx",
            "virtualGatewayRegion": "us-west-2",
            "virtualGatewayOwnerAccount": "xxxxxxxxxxxx"
        },
        {
            "directConnectGatewayId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "directConnectGatewayOwnerAccount": "xxxxxxxxxxxx",
            "associationState": "associated",
            "associatedGateway": {
                "id": "vgw-xxxxxxxxxxxx",
                "type": "virtualPrivateGateway",
                "ownerAccount": "xxxxxxxxxxxx",
                "region": "us-east-1"
            },
            "associationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "allowedPrefixesToDirectConnectGateway": [
                {
                    "cidr": "172.16.105.0/24"
                },
                {
                    "cidr": "172.16.109.0/24"
                }
            ],
            "virtualGatewayId": "vgw-xxxxxxxxxxxx",
            "virtualGatewayRegion": "us-east-1",
            "virtualGatewayOwnerAccount": "xxxxxxxxxxxx"
        },
        {
            "directConnectGatewayId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "directConnectGatewayOwnerAccount": "xxxxxxxxxxxx",
            "associationState": "associated",
            "associatedGateway": {
                "id": "vgw-xxxxxxxxxxxx",
                "type": "virtualPrivateGateway",
                "ownerAccount": "xxxxxxxxxxxx",
                "region": "us-east-2"
            },
            "associationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "allowedPrefixesToDirectConnectGateway": [
                {
                    "cidr": "172.26.1.0/24"
                },
                {
                    "cidr": "172.26.0.0/24"
                }
            ],
            "virtualGatewayId": "vgw-xxxxxxxxxxxx",
            "virtualGatewayRegion": "us-east-2",
            "virtualGatewayOwnerAccount": "xxxxxxxxxxxx"
        },
        {
            "directConnectGatewayId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "directConnectGatewayOwnerAccount": "xxxxxxxxxxxx",
            "associationState": "associated",
            "associatedGateway": {
                "id": "vgw-xxxxxxxxxxxx",
                "type": "virtualPrivateGateway",
                "ownerAccount": "xxxxxxxxxxxx",
                "region": "us-east-2"
            },
            "associationId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "allowedPrefixesToDirectConnectGateway": [
                {
                    "cidr": "172.46.0.0/16"
                }
            ],
            "virtualGatewayId": "vgw-xxxxxxxxxxxx",
            "virtualGatewayRegion": "us-east-2",
            "virtualGatewayOwnerAccount": "xxxxxxxxxxxx"
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
    "netbrainHostName": "ydu-0107-NATGW(nat-xxxxxxxxxxxx)",
    "CreateTime": "2020-03-30 16:02:01+00:00",
    "NatGatewayAddresses": [
        {
            "AllocationId": "eipalloc-xxxxxxxxxxxx",
            "NetworkInterfaceId": "eni-xxxxxxxxxxxx",
            "PrivateIp": "xxx.xxx.xxx.xxx",
            "PublicIp": "xxx.xxx.xxx.xxx"
        }
    ],
    "NatGatewayId": "nat-xxxxxxxxxxxx",
    "State": "available",
    "SubnetId": "subnet-xxxxxxxxxxxx",
    "VpcId": "vpc-xxxxxxxxxxxx",
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
            "SubnetId": "subnet-xxxxxxxxxxxx",
            "VpcId": "vpc-xxxxxxxxxxxx",
            "OwnerId": "xxxxxxxxxxxx",
            "AssignIpv6AddressOnCreation": false,
            "Ipv6CidrBlockAssociationSet": [],
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Case1_subnet_1"
                }
            ],
            "SubnetArn": "arn:aws:ec2:ca-central-1:xxxxxxxxxxxx:subnet/subnet-xxxxxxxxxxxx",
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
The configuration of the AWS Firewall relies solely on the corresponding AWS SDK of the AWS network firewall. The AWS SDK provides detailed information regarding the configuration of the network firewall, including its connectivity, security, etc.

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
    "netbrainHostName": "NB-AWS-Lab-Firewall-1(us-east-1-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)",
    "UpdateToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "Firewall": {
        "FirewallName": "NB-AWS-Lab-Firewall-1",
        "FirewallArn": "arn:aws:network-firewall:us-east-1:xxxxxxxxxxxx:firewall/NB-AWS-Lab-Firewall-1",
        "FirewallPolicyArn": "arn:aws:network-firewall:us-east-1:xxxxxxxxxxxx:firewall-policy/Lab-Firewall-2",
        "VpcId": "vpc-xxxxxxxxxxxx",
        "SubnetMappings": [
            {
                "SubnetId": "subnet-xxxxxxxxxxxx"
            },
            {
                "SubnetId": "subnet-xxxxxxxxxxxx"
            }
        ],
        "DeleteProtection": false,
        "SubnetChangeProtection": false,
        "FirewallPolicyChangeProtection": false,
        "FirewallId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
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
                    "SubnetId": "subnet-xxxxxxxxxxxx",
                    "EndpointId": "vpce-xxxxxxxxxxxx",
                    "Status": "READY"
                },
                "Config": {
                    "arn:aws:network-firewall:us-east-1:xxxxxxxxxxxx:stateful-rulegroup/2ND-Stateful-Rule-Group": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                    },
                    "arn:aws:network-firewall:us-east-1:xxxxxxxxxxxx:stateless-rulegroup/Fw-to-Stateful-Rule": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                    },
                    "arn:aws:network-firewall:us-east-1:aws-managed:stateful-rulegroup/MalwareDomainsStrictOrder": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                    },
                    "arn:aws:network-firewall:us-east-1:xxxxxxxxxxxx:firewall-policy/Lab-Firewall-2": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                    },
                    "arn:aws:network-firewall:us-east-1:xxxxxxxxxxxx:stateless-rulegroup/Lab-Firewall-1-Stateless-Rule": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                    }
                }
            },
            "us-east-1f": {
                "Attachment": {
                    "SubnetId": "subnet-xxxxxxxxxxxx",
                    "EndpointId": "vpce-xxxxxxxxxxxx",
                    "Status": "READY"
                },
                "Config": {
                    "arn:aws:network-firewall:us-east-1:xxxxxxxxxxxx:stateful-rulegroup/2ND-Stateful-Rule-Group": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                    },
                    "arn:aws:network-firewall:us-east-1:xxxxxxxxxxxx:stateless-rulegroup/Fw-to-Stateful-Rule": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                    },
                    "arn:aws:network-firewall:us-east-1:aws-managed:stateful-rulegroup/MalwareDomainsStrictOrder": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                    },
                    "arn:aws:network-firewall:us-east-1:xxxxxxxxxxxx:firewall-policy/Lab-Firewall-2": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                    },
                    "arn:aws:network-firewall:us-east-1:xxxxxxxxxxxx:stateless-rulegroup/Lab-Firewall-1-Stateless-Rule": {
                        "SyncStatus": "IN_SYNC",
                        "UpdateToken": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
                    }
                }
            }
        }
    },
    "ResponseMetadata": {
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
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
  

