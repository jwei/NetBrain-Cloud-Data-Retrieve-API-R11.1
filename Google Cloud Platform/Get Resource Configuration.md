# Usage
To retrieve the configuration data for a resource, you can utilize NetBrain's built-in configuration file function, which does not require coding. This function enables you to quickly obtain the resource configuration.

# Table of Contents
* [Google VPC Router](#google-vpc-router)

## Google VPC Router

### Introduction
The configuration of the Google Virtual Network distributed router relies solely on the corresponding Google API of the virtual network. The Google API provides detailed information regarding the configuration of the virtual network, including its subnetworks, peerings, etc.

### Content
Below are the Google APIs used to generate this configuration.
|Resource/Action|Relationship|Google API Version|Google API document|
|------|------|------|------|
| Virtual Networks - Get | self | v1 | https://cloud.google.com/compute/docs/reference/rest/v1/networks/get | 

### Sample
<details><summary>Configuration File</summary>
    
```json5
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "central-vpc-hub-router(3951884830549813391-router)",
    "kind": "compute#network",
    "id": "3951884830549813391",
    "creationTimestamp": "2021-04-21T14:17:20.628-07:00",
    "name": "central-vpc-hub",
    "description": "Second Host Project",
    "selfLink": "https://www.googleapis.com/compute/v1/projects/{project_id}/global/networks/central-vpc-hub",
    "selfLinkWithId": "https://www.googleapis.com/compute/v1/projects/netbrain-gcp-lab-005/global/networks/3951884830549813391",
    "autoCreateSubnetworks": false,
    "subnetworks": [
        "https://www.googleapis.com/compute/v1/projects/netbrain-gcp-lab-005/regions/us-central1/subnetworks/subnet-1",
        "https://www.googleapis.com/compute/v1/projects/netbrain-gcp-lab-005/regions/us-central1/subnetworks/subnet-2"
    ],
    "peerings": [
        {
            "name": "host-proj2-vpc-to-host-proj1-vpc",
            "network": "https://www.googleapis.com/compute/v1/projects/norse-fragment-296509/global/networks/central-vpc-hub",
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

# Google VPN Gateway

### Introduction
The configuration of the Google VPN gateway is dependent on the Google API response of the Google VPN gateway as the primary response. The full resource configuration consists of some associated resources' API data, including vpnInterfaces, tunnels.

### Content

Below are the Google APIs used to generate this configuration.

### Sample
<details><summary>Configuration File</summary>

```json5
{
    "netbrainNotes": "This config file is generated via API",
    "netbrainHostName": "tyler-vpn-000(5234964296885277743)",
    "kind": "compute#vpnGateway",
    "id": "5234964296885277743",
    "creationTimestamp": "2021-08-19T12:02:24.423-07:00",
    "name": "tyler-vpn-000",
    "description": "",
    "region": "https://www.googleapis.com/compute/v1/projects/qa-testresource/regions/us-east1",
    "network": "https://www.googleapis.com/compute/v1/projects/qa-testresource/global/networks/default",
    "selfLink": "https://www.googleapis.com/compute/v1/projects/qa-testresource/regions/us-east1/vpnGateways/tyler-vpn-000",
    "labelFingerprint": "42WmSpB8rSM=",
    "vpnInterfaces": [
        {
            "id": 0,
            "ipAddress": "35.242.15.185"
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
            "region": "https://www.googleapis.com/compute/v1/projects/netbrain-gcp-lab-002/regions/us-west4",
            "vpnGateway": "https://www.googleapis.com/compute/v1/projects/netbrain-gcp-lab-002/regions/us-west4/vpnGateways/serv-proj2-us-west4-cloudvpn",
            "vpnGatewayInterface": 0,
            "peerGcpGateway": "https://www.googleapis.com/compute/v1/projects/norse-fragment-296509/regions/us-west4/vpnGateways/host-proj1-vpc-spk3-cloudvpn",
            "router": "https://www.googleapis.com/compute/v1/projects/netbrain-gcp-lab-002/regions/us-west4/routers/serv-proj2-us-west4-cloudvpn",
            "peerIp": "34.124.11.22",
            "sharedSecret": "*",
            "sharedSecretHash": "AH91_FUBngpP0Oy65ZGeI2UBf96K",
            "status": "ESTABLISHED",
            "selfLink": "https://www.googleapis.com/compute/v1/projects/netbrain-gcp-lab-002/regions/us-west4/vpnTunnels/to-hostproj1-tunnel-1",
            "ikeVersion": 2,
            "detailedStatus": "Tunnel is up and running.",
            "localTrafficSelector": [
                "0.0.0.0/0"
            ],
            "remoteTrafficSelector": [
                "0.0.0.0/0"
            ],
            "labelFingerprint": "42WmSpB8rSM="
        }
    ]
}


```

</details>
<br />

# Google Cloud Router

### Introduction
The configuration of the Google Cloud Router is dependent on the Google API response of the Google Routers as the primary response. The Google API provides detailed information regarding the configuration of the routers, including its name, region, network and etc.

### Content
Below are the Google APIs used to generate this configuration.

### Sample
Configuration File

# Google Load Balancer
### Introduction
The configuration of the Google load balancer is dependent on the Google API response of the Google load balancer as the primary response. The full resource configuration consists of some associated resources' API data, including backendService, group.

### Content
Below are the Google APIs used to generate this configuration.

### Sample

# Google Firewall

### Introduction
There is no supported API data for GCP Firewall. The resource configuration consists of basic data, including id, name and networkName.

### Sample
Configuration File

# Google Cloud NAT Gateway

### Introduction
The configuration of the Google Cloud NAT Gateway distributed router relies solely on the corresponding Google API of the routers. The Google API provides detailed information regarding the configuration of the NAT Gateway, including its subnetworks, peerings, etc.

### Content
Below are the Google APIs used to generate this configuration.

### Sample
<details><summary>Configuration File</summary>

```json5

```

</details>
<br />

# Google Virtual Machine

### Introduction
The configuration of the Google Virtual Machine relies solely on the corresponding Google API of the Virtual Machine. The Google API provides detailed information regarding the configuration of the instance, including its subnetworks, peerings, etc.

### Content
Below are the Google APIs used to generate this configuration.

### Sample
<details><summary>Configuration File</summary>

```json5

```

</details>
<br />

# Google Network Endpoint Group

# Google Interconnect (Partner/ Dedicated)

# Google Peering Edge Router
