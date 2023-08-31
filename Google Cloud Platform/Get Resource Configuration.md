# Usage
To retrieve the configuration data for a resource, you can utilize NetBrain's built-in configuration file function, which does not require coding. This function enables you to quickly obtain the resource configuration.

# Table of Contents
  - [Google VPC Router](#google-vpc-router)
  - [Google VPN Gateway](#google-vpn-gateway)
  - [Google Cloud Router](#google-cloud-router)
  - [Google Load Balancer](#google-load-balancer)
  - [Google Firewall](#google-firewall)
  - [Google Cloud NAT Gateway](#google-cloud-nat-gateway)
  - [Google Virtual Machine](#google-virtual-machine)
  - [Google Cloud Internet Gateway](#google-cloud-internet-gateway)
  - [Partner Google Interconnect](#partner-google-interconnect)
  - [Dedicated Google Interconnect](#dedicated-google-interconnect)
  - [Google Cloud Private Service Connect Endpoint](#google-cloud-private-service-connect-endpoint)

## Google VPC Router

### Introduction
The configuration of the Google Virtual Network distributed router relies solely on the corresponding Google API of the virtual network. The Google API provides detailed information regarding the configuration of the virtual network, including its subnetworks, peerings, etc.

### Content
Below are the Google APIs used to generate this configuration.
|Resource/Action|Relationship|Google API Version|Google API document|
|------|------|------|------|
| VPC Router - Get | self | v1 | https://cloud.google.com/compute/docs/reference/rest/v1/networks/get | 

### Sample
<details><summary>Configuration File</summary>
    
```json5
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "central-vpc-hub-router(<vpc_id>-router)",
    "kind": "compute#network",
    "id": "xxxxxxxxxxxxxxxxxxx",
    "creationTimestamp": "2021-04-21T14:17:20.628-07:00",
    "name": "central-vpc-hub",
    "description": "Second Host Project",
    "selfLink": "https://www.googleapis.com/compute/v1/projects/<project-id>/global/networks/central-vpc-hub",
    "selfLinkWithId": "https://www.googleapis.com/compute/v1/projects/<project-id>/global/networks/xxxxxxxxxxxxxxxxxxx",
    "autoCreateSubnetworks": false,
    "subnetworks": [
        "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-central1/subnetworks/subnet-1",
        "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-central1/subnetworks/subnet-2"
    ],
    "peerings": [
        {
            "name": "host-proj2-vpc-to-host-proj1-vpc",
            "network": "https://www.googleapis.com/compute/v1/projects/<project-id>/global/networks/central-vpc-hub",
            "state": "INACTIVE",
            "stateDetails": "[2022-04-22T17:42:28.882-07:00]: Peer network tried to connect and failed.",
            "autoCreateRoutes": true,
            "exportCustomRoutes": true,
            "importCustomRoutes": true,
            "exchangeSubnetRoutes": true,
            "exportSubnetRoutesWithPublicIp": true,
            "importSubnetRoutesWithPublicIp": true,
            "stackType": "IPV4_ONLY"
        }
    ],
    "routingConfig": {
        "routingMode": "GLOBAL"
    },
    "mtu": 1460,
    "networkFirewallPolicyEnforcementOrder": "AFTER_CLASSIC_FIREWALL"
}
```

</details>
<br />

## Google VPN Gateway

### Introduction
The configuration of the Google VPN gateway is dependent on the Google API response of the Google VPN gateway as the primary response. The full resource configuration consists of some associated resources' API data, including tunnels.

### Content

Below are the Google APIs used to generate this configuration.

|Resource/Action|Relationship|Google API Version|Google API document|
|------|------|------|------|
| VPN Gateway - Get | self | v1 | https://cloud.google.com/compute/docs/reference/rest/v1/vpnGateways/get | 
| Tunnels - Get | tunnels | v1 | https://cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels/get https://cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels/list | 

### Sample
<details><summary>Configuration File</summary>

```json5
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "tyler-vpn-000(<vpn_gateway_id>)",
    "kind": "compute#vpnGateway",
    "id": "<vpn_gateway_id>",
    "creationTimestamp": "2021-08-19T12:02:24.423-07:00",
    "name": "tyler-vpn-000",
    "description": "",
    "region": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-east1",
    "network": "https://www.googleapis.com/compute/v1/projects/<project-id>/global/networks/default",
    "selfLink": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-east1/vpnGateways/tyler-vpn-000",
    "labelFingerprint": "xxxxxxxxxxxx",
    "vpnInterfaces": [
        {
            "id": 0,
            "ipAddress": "xx.xx.xx.xx"
        }
    ],
    // vpn tunnels: 
    //   https://cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels/get
    //   https://cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels/list
    "tunnels": [
        {
            "kind": "compute#vpnTunnel",
            "id": "5256021233025810772",
            "creationTimestamp": "2021-06-14T13:44:43.411-07:00",
            "name": "to-hostproj1-tunnel-1",
            "description": "to-hostproj1-tunnel-1",
            "region": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-west4",
            "vpnGateway": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-west4/vpnGateways/serv-proj2-us-west4-cloudvpn",
            "vpnGatewayInterface": 0,
            "peerGcpGateway": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-west4/vpnGateways/host-proj1-vpc-spk3-cloudvpn",
            "router": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-west4/routers/serv-proj2-us-west4-cloudvpn",
            "peerIp": "xx.xx.xx.xx",
            "sharedSecret": "*",
            "sharedSecretHash": "AH91_FUBngpP0Oy65ZGeI2UBf96K",
            "status": "ESTABLISHED",
            "selfLink": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-west4/vpnTunnels/to-hostproj1-tunnel-1",
            "ikeVersion": 2,
            "detailedStatus": "Tunnel is up and running.",
            "localTrafficSelector": [
                "0.0.0.0/0"
            ],
            "remoteTrafficSelector": [
                "0.0.0.0/0"
            ],
            "labelFingerprint": "xxxxxxxxxxx"
        }
    ]
}


```

</details>
<br />

## Google Cloud Router

### Introduction
The configuration of the Google Cloud Router is dependent on the Google API response of the Google Routers as the primary response. The Google API provides detailed information regarding the configuration of the routers, including its name, region, network and etc.

### Content
Below are the Google APIs used to generate this configuration.
|Resource/Action|Relationship|Google API Version|Google API document|
|------|------|------|------|
| Cloud Routers - Get | self | v1 | https://cloud.google.com/compute/docs/reference/rest/v1/routers/get

### Sample
<details><summary>Configuration File</summary>

```json5
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "central-cloud-router-2(<router_id>)",
    "kind": "compute#router",
    "id": "<router_id>",
    "creationTimestamp": "2021-02-09T09:02:01.340-08:00",
    "name": "central-cloud-router-2",
    "description": "",
    "region": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-central1",
    "network": "https://www.googleapis.com/compute/v1/projects/<project-id>/global/networks/central-vpc-hub",
    "bgp": {
        "asn": 65511,
        "advertiseMode": "DEFAULT"
    },
    "selfLink": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-central1/routers/central-cloud-router-2",
    "encryptedInterconnectRouter": false
}
```

</details>
<br />

## Google Load Balancer
### Introduction
The configuration of the Google load balancer is dependent on the Google API response of the Google load balancer as the primary response. The full resource configuration consists of some associated resources' API data, including backendService, group.

### Content
Below are the Google APIs used to generate this configuration.
|Resource/Action|Relationship|Google API Version|Google API document|
|------|------|------|------|
| Load Balancers / Forwarding Rules - Get | self | v1 | https://cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/get
| Backend Services - Get | backendService | v1 | https://cloud.google.com/compute/docs/reference/rest/v1/backendServices/get
| Instance Groups - Get | backendService.backends.group | v1 | https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/get

### Sample
<details><summary>Configuration File</summary>

```json5
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "host-proj2-tcp-internal-lb1(<ldb_id>-internal-tcp-loadbalancer)",
    "kind": "compute#forwardingRule",
    "id": "<ldb_id>",
    "creationTimestamp": "2021-07-15T18:35:38.345-07:00",
    "name": "host-proj2-tcp-internal-lb1-frontend",
    "description": "",
    "region": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-central1",
    "IPAddress": "172.18.3.12",
    "IPProtocol": "TCP",
    "selfLink": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-central1/forwardingRules/host-proj2-tcp-internal-lb1-frontend",
    "loadBalancingScheme": "INTERNAL",
    "subnetwork": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-central1/subnetworks/subnet-1",
    "network": "https://www.googleapis.com/compute/v1/projects/<project-id>/global/networks/central-vpc-hub",
    "backendService": {
        "kind": "compute#backendService",
        "id": "3089886968714976396",
        "creationTimestamp": "2021-07-15T18:35:31.122-07:00",
        "name": "host-proj2-tcp-internal-lb1",
        "description": "",
        "selfLink": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-central1/backendServices/host-proj2-tcp-internal-lb1",
        "backends": [
            {
                "group": {
                    "kind": "compute#instanceGroup",
                    "id": "<group_id>",
                    "creationTimestamp": "2021-07-15T18:31:27.956-07:00",
                    "name": "host-proj2-ig",
                    "description": "This instance group is controlled by Instance Group Manager 'host-proj2-ig'. To modify instances in this group, use the Instance Group Manager API: https://cloud.google.com/compute/docs/reference/latest/instanceGroupManagers",
                    "network": "https://www.googleapis.com/compute/v1/projects/<project-id>/global/networks/central-vpc-hub",
                    "fingerprint": "xxxxxxxxxxx",
                    "zone": "https://www.googleapis.com/compute/v1/projects/<project-id>/zones/us-central1-a",
                    "selfLink": "https://www.googleapis.com/compute/v1/projects/<project-id>/zones/us-central1-a/instanceGroups/host-proj2-ig",
                    "size": 1,
                    "subnetwork": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-central1/subnetworks/subnet-1"
                },
                "balancingMode": "CONNECTION",
                "failover": true
            }
        ],
        "healthChecks": [
            "https://www.googleapis.com/compute/v1/projects/<project-id>/global/healthChecks/tcp-health-check"
        ],
        "timeoutSec": 30,
        "protocol": "TCP",
        "fingerprint": "OgJSiZYsVAU=",
        "sessionAffinity": "CLIENT_IP_PORT_PROTO",
        "region": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-central1",
        "failoverPolicy": {
            "disableConnectionDrainOnFailover": false,
            "dropTrafficIfUnhealthy": false,
            "failoverRatio": 0
        },
        "loadBalancingScheme": "INTERNAL",
        "connectionDraining": {
            "drainingTimeoutSec": 300
        },
        "network": "https://www.googleapis.com/compute/v1/projects/<project-id>/global/networks/central-vpc-hub"
    },
    "serviceLabel": "lb",
    "serviceName": "lb.host-proj2-tcp-internal-lb1-frontend.il4.us-central1.lb.<project-id>.internal",
    "networkTier": "PREMIUM",
    "labelFingerprint": "xxxxxxxxxxx",
    "fingerprint": "xxxxxxxxxxx",
    "allPorts": true
}
```

</details>
<br />


## Google Firewall

### Introduction
There is no supported API data for GCP Firewall. The resource configuration consists of basic data, including id, name and networkName.

### Sample
<details><summary>Configuration File</summary>

```json5
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "europewest-vpc-firewall(<firewall-id>-firewall)",
    "id": "<firewall-id>-firewall",
    "name": "europewest-vpc-firewall(<firewall-id>-firewall)",
    "networkName": "europewest-vpc"
}
```

</details>
<br />


## Google Cloud NAT Gateway

### Introduction
The configuration of the Google Cloud NAT Gateway distributed router relies solely on the corresponding Google API of the routers. The Google API provides detailed information regarding the configuration of the NAT Gateway, including its subnetworks, peerings, etc.

### Content
Below are the Google APIs used to generate this configuration.
|Resource/Action|Relationship|Google API Version|Google API document|
|------|------|------|------|
| NAT Gateway - Get | self | v1 | https://cloud.google.com/compute/docs/reference/rest/v1/routers/get

### Sample
<details><summary>Configuration File</summary>

```json5
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "tyler-nat-gw(<NAT-gateway-id>-tyler-nat-gw)"
}
```

</details>
<br />

## Google Virtual Machine

### Introduction
Configuration feature is not supported for Google Virtual Machine yet. Please send API to get the resource data instead. Reference: https://cloud.google.com/compute/docs/reference/rest/v1/instances/get


## Google Cloud Internet Gateway
### Introduction
Configuration feature is currently not available for the Google Cloud Internet Gateway. The structure of the resource data is as follows:

### Sample
<details><summary>Configuration File</summary>

```json5
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "Global-igw(<igw-id>)(<igw-id>)",
    "id": "<igw-id>",
    "name": "Global-igw(<igw-id>)(<igw-id>)"
}
```

</details>
<br/>

## Partner Google Interconnect <a id="partner-google-interconnect"></a>
### Introduction
The configuration of the Google Interconnect relies solely on the corresponding Google API of the interconnectAttachments. The Google API provides detailed information regarding the configuration of the instance, including its bandwidth, partnerMetadata, etc.

### Content
Below are the Google APIs used to generate this configuration.
|Resource/Action|Relationship|Google API Version|Google API document|
|------|------|------|------|
| Partner Google Interconnect  - Get | self | v1 | https://cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments/get

### Sample
<details><summary>Configuration File</summary>

```json5
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "chicago-zone2-cgcil02(<interconnect-id>-partnerinterconnect)",
    "kind": "compute#interconnectAttachment",
    "selfLink": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-east4/interconnectAttachments/gcptonetbondb",
    "id": "<interconnect-id>",
    "creationTimestamp": "2021-04-08T12:44:16.166-07:00",
    "name": "gcptonetbondb",
    "router": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-east4/routers/gcp-router-b",
    "region": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-east4",
    "mtu": 1500,
    "cloudRouterIpAddress": "xx.xx.xx.xx/29",
    "customerRouterIpAddress": "xx.xx.xx.xx/29",
    "type": "PARTNER",
    "pairingKey": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx/us-east4/2",
    "adminEnabled": true,
    "vlanTag8021q": 1141,
    "edgeAvailabilityDomain": "AVAILABILITY_DOMAIN_2",
    "bandwidth": "BPS_50M",
    "partnerMetadata": {
        "partnerName": "AT&T",
        "interconnectName": "chicago-zone2-cgcil02",
        "portalUrl": "https://synaptic.att.com/"
    },
    "labelFingerprint": "42WmSpB8rSM=",
    "state": "ACTIVE",
    "partnerAsn": "8030",
    "encryption": "NONE",
    "dataplaneVersion": 1,
    "stackType": "IPV4_ONLY"
}
```

</details>
<br />


## Dedicated Google Interconnect <a id="dedicated-google-interconnect"></a>
### Introduction
The configuration of the Dedicated Google Interconnect relies solely on the corresponding Google API of the interconnectAttachments. The Google API provides detailed information regarding the configuration of the instance, including its bandwidth, encryption, etc.

### Content
Below are the Google APIs used to generate this configuration.
|Resource/Action|Relationship|Google API Version|Google API document|
|------|------|------|------|
| Dedicated Google Interconnect  - Get | self | v1 | https://cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments/get
| Interconnect Attachments - Get | interconnectAttachments | v1 | https://cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments/get

### Sample
<details><summary>Configuration File</summary>

```json5
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "chicago-zone2-cgcil02(<interconnect-id>-partnerinterconnect)",
    "kind": "compute#interconnectAttachment",
    "selfLink": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-east4/interconnectAttachments/gcptonetbondb",
    "id": "<interconnect-id>",
    "creationTimestamp": "2021-04-08T12:44:16.166-07:00",
    "name": "gcptonetbondb",
    "router": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-east4/routers/gcp-router-b",
    "region": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-east4",
    "mtu": 1500,
    "cloudRouterIpAddress": "xx.xx.xx.xx/29",
    "customerRouterIpAddress": "xx.xx.xx.xx/29",
    "type": "DEDICATED",
    "pairingKey": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx/us-east4/2",
    "adminEnabled": true,
    "vlanTag8021q": 1141,
    "edgeAvailabilityDomain": "AVAILABILITY_DOMAIN_2",
    "bandwidth": "BPS_50M",
    // "partnerMetadata": {
    //     "partnerName": "AT&T",
    //     "interconnectName": "chicago-zone2-cgcil02",
    //     "portalUrl": "https://synaptic.att.com/"
    // },
    "labelFingerprint": "42WmSpB8rSM=",
    "state": "ACTIVE",
    "partnerAsn": "8030",
    "encryption": "NONE",
    "dataplaneVersion": 1,
    "stackType": "IPV4_ONLY",
    "interconnectAttachments": [
        {
            "kind": "compute#interconnectAttachment",
            "selfLink": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-east4/interconnectAttachments/gcptonetbondb",
            "id": "<interconnect-id>",
            "creationTimestamp": "2021-04-08T12:44:16.166-07:00",
            "name": "gcptonetbondb",
            "router": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-east4/routers/gcp-router-b",
            "region": "https://www.googleapis.com/compute/v1/projects/<project-id>/regions/us-east4",
            "mtu": 1500,
            "cloudRouterIpAddress": "xx.xx.xx.xx/29",
            "customerRouterIpAddress": "xx.xx.xx.xx/29",
            "type": "DEDICATED",
            "pairingKey": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx/us-east4/2",
            "adminEnabled": true,
            "vlanTag8021q": 1141,
            "edgeAvailabilityDomain": "AVAILABILITY_DOMAIN_2",
            "bandwidth": "BPS_50M",
            "labelFingerprint": "42WmSpB8rSM=",
            "state": "ACTIVE",
            "partnerAsn": "8030",
            "encryption": "NONE",
            "dataplaneVersion": 1,
            "stackType": "IPV4_ONLY",
            // "partnerMetadata": {
            //     "partnerName": "AT&T",
            //     "interconnectName": "chicago-zone2-cgcil02",
            //     "portalUrl": "https://synaptic.att.com/"
            // },
        }
    ]
}
```

</details>
<br />

## Google Cloud Private Service Connect Endpoint

### Introduction
The configuration of the Google Cloud Private Service Connect Endpoint relies solely on the corresponding Google API of the Virtual Machine. The Google API provides detailed information regarding the configuration of the instance, including its IpAddress, serviceDirectoryRegistrations, etc.

### Content
Below are the Google APIs used to generate this configuration.
|Resource/Action|Relationship|Google API Version|Google API document|
|------|------|------|------|
| NAT Gateway - Get | self | v1 | https://cloud.google.com/compute/docs/reference/rest/v1/globalForwardingRules/get

### Sample
<details><summary>Configuration File</summary>

```json5
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "psctest1(<psc-id>)",
    "kind": "compute#forwardingRule",
    "id": "<psc-id>",
    "creationTimestamp": "2022-09-08T07:37:00.890-07:00",
    "name": "psctest1",
    "IPAddress": "xx.xx.xx.xx",
    "IPProtocol": "TCP",
    "target": "all-apis",
    "selfLink": "https://www.googleapis.com/compute/v1/projects/<project-id>/global/forwardingRules/psctest1",
    "network": "https://www.googleapis.com/compute/v1/projects/<project-id>/global/networks/central-vpc-hub",
    "serviceDirectoryRegistrations": [
        {
            "namespace": "goog-psc-central-vpc-hub-5165306842222363136",
            "serviceDirectoryRegion": "us-central1"
        }
    ],
    "labelFingerprint": "xxxxxxxxxx",
    "pscConnectionId": "xxxxxxxxxxxxxx"
}
```

</details>
<br />