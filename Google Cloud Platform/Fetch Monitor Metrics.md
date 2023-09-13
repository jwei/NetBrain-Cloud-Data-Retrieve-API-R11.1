# Table of Contents
- [Introduction](#introduction)
- [API Definition](#api_def)
    - [Input Parameters](#input)
    - [Output](#output)
- [Special Notes](#special-notes)
    - [Virtual Private Cloud](#vpc)
    - [Unsupported Virtual Node](#unsupported-virtual-node)
    - [Dedicated Interconnect](#dedicated-interconnect)
- [Sample](#sample)
    - [Sample 1: Get Resource Metrics of VPC Instances Per VPC Network-limit](#sample1)
    - [Sample 2: Get Resource Metrics of VPN Gateway Connections](#sample2)
    - [Sample 3: Get Resource Metrics of Cloud Router Sent Routes Count](#sample3)    
    - [Sample 4: Get Resource Metrics of Load Balance Max Rate](#sample4)
    - [Sample 5: Get Resource Metrics of Cloud NAT New Connections Count](#sample5)
    - [Sample 6: Get Resource Metrics of Partner Interconnect Network Attachment Capacity](#sample6)
    - [Sample 7: Get Resource Metrics of Private Service Connect](#sample7)


# Introduction <a id="introduction"></a>
The `GetMonitorMetrics` function is a static method defined in the `NBGoogleAPILibrary` class. It leverages the Google Monitor solution to fetch metrics of Google resources via the Google RESTful API.
For a complete list of available metrics for each Google resource, please reference to Google document: https://cloud.google.com/monitoring/api/metrics

# API Definition <a id="api_def"></a>
```python
class NBGoogleAPILibrary:
    @staticmethod
    def GetMonitorMetrics(
            api_server_id: str,
            params: dict,
            url_params: dict,
            api_version: str = 'v3'
    ) -> object:
        # implementation
        # ...
```

## Input Parameters <a id="input"></a>
 - `api_server_id`(str) - The Google Tenant API Server Instance ID saved in Device.
 - `params`(dict) - A dictionary containing additional parameters to use when calling the Google monitor metrics API. 
 - `url_params`(dic) - A dictionary, containing additional URL parameters like filter and interval, used when calling the Google monitor metrics API. For a complete list of available metrics for each Google resource, please reference to the document: https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list
     - <details><summary>e.g.:</summary>

        ```json5
        {
            'filter':  {
                'metric.type' : 'router.googleapis.com/bgp/received_routes_count',
                'metric.labels.bgp_peer_name' : 'auto-ia-bgp-gcptonetbonda-xxxx'
            },
            'interval.startTime': '2023-08-16T05:40:54Z',
            'interval.endTime': '2023-08-16T07:40:54Z'
        }
        ```
        </details>
 - `api_version[optional]`(str) - The API version to use for the Google monitor metrics API.
## Output <a id="output"></a>
> resp_body_json: The JSON response body of the HTTP request to the Google monitor metrics API. This is a dictionary with string keys and values.


# Special Notes <a id="special-notes"></a>

## Virtual Private Cloud <a id="vpc"></a>
- In NetBrain, we generate "VPC Router" for each GCP Virtual Network to represent its networking entity
- The VPC's resource id is saved in the "networkId" in the nb_node data from `RetrieveData` method
- For the usage please check samples below.

## Unsupported Virtual Node <a id="unsupported-virtual-node"></a>
- There are some virual nodes building in NetBrain structure, which might not have metrics data:
  - Firewall
  - Internet Gateway
  - Global Internet Gateway

## Dedicated Interconnect  <a id="dedicated-interconnect"></a>
- There is no user-case / actual node in Test Env

# Samples <a id="sample"></a>
- Related Docs:
  - [Metrics list](https://cloud.google.com/monitoring/api/metrics)
  - [Monitored resource types](https://cloud.google.com/monitoring/api/resources)

## Sample 1: Get Resource Metrics of VPC Instances Per VPC Network-limit <a id="sample1"></a>
```python

'''
Begin Declare Input Parameters
[
]
End Declare

For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''

from datetime import datetime, timezone, timedelta
import json

def BuildParameters(context, device_name, params):
    nb_node = GetDeviceProperties(
        context,
        device_name,
        {
            'techName': 'Google Cloud',
            'paramType': 'SDN',
            'params': ['*']
        }
    )
    return nb_node


def RetrieveData(params):
    # Common used variable: nb_node, resource id, resource name, resource self link
    nb_node = params['params']
    gcp_resource_id = nb_node['networkId'] if "networkId" in nb_node else None
    gcp_resource_name = nb_node['name'] if "name" in nb_node else None
    gcp_resource_self_link = nb_node['selfLink'] if "selfLink" in nb_node else None

    # Setup api server id
    api_server_id = params['apiServerId']

    # Setup projectId
    if 'projectId' not in params['params']['nbProperties']:
        msg = 'Error: Global Resource is not supported, because no projectId in nbProperties'
        raise Exception(msg)
    proj_id = params['params']['nbProperties']['projectId']

    # Setup url_params
    currentTime = datetime.now(timezone.utc)
    pastTime = currentTime - timedelta(hours=24)
    url_params = {
        'filter': {
            'metric.type' : "compute.googleapis.com/quota/instances_per_vpc_network/limit",
            'resource.labels.network_id': gcp_resource_id
        },
        'interval.startTime': pastTime.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'interval.endTime': currentTime.strftime('%Y-%m-%dT%H:%M:%SZ')
    }

    # Get Live Data
    data = NBGoogleAPILibrary.GetMonitorMetrics(
        api_server_id=api_server_id,
        proj_id=proj_id,
        url_params=url_params
    )
    return data


```

## Sample 2: Get Resource Metrics of VPN Gateway Connections <a id="sample2"></a>
```python


'''
Begin Declare Input Parameters
[
]
End Declare

For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''

from datetime import datetime, timezone, timedelta
import json

def BuildParameters(context, device_name, params):
    nb_node = GetDeviceProperties(
        context,
        device_name,
        {
            'techName': 'Google Cloud',
            'paramType': 'SDN',
            'params': ['*']
        }
    )
    return nb_node


def RetrieveData(params):
    # Common used variable: nb_node, resource id, resource name, resource self link
    nb_node = params['params']
    gcp_resource_id = nb_node['id'] if "id" in nb_node else None
    gcp_resource_name = nb_node['name'] if "name" in nb_node else None
    gcp_resource_self_link = nb_node['selfLink'] if "selfLink" in nb_node else None

    # Setup api server id
    api_server_id = params['apiServerId']

    # Setup projectId
    if 'projectId' not in params['params']['nbProperties']:
        msg = 'Error: Global Resource is not supported, because no projectId in nbProperties'
        raise Exception(msg)
    proj_id = params['params']['nbProperties']['projectId']

    # Setup url_params
    currentTime = datetime.now(timezone.utc)
    pastTime = currentTime - timedelta(seconds=330)
    url_params = {
        'filter': {
            'metric.type' : "vpn.googleapis.com/gateway/connections",
            'resource.labels.gateway_id': gcp_resource_id
        },
        'interval.startTime': pastTime.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'interval.endTime': currentTime.strftime('%Y-%m-%dT%H:%M:%SZ')
    }

    # Get Live Data
    data = NBGoogleAPILibrary.GetMonitorMetrics(
        api_server_id=api_server_id,
        proj_id=proj_id,
        url_params=url_params
    )
    return data
```
## Sample 3: Get Resource Metrics of Cloud Router Sent Routes Count<a id="sample3"></a>
```python

'''
Begin Declare Input Parameters
[
]
End Declare

For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''

from datetime import datetime, timezone, timedelta
import json


def BuildParameters(context, device_name, params):
    nb_node = GetDeviceProperties(
        context,
        device_name,
        {
            'techName': 'Google Cloud',
            'paramType': 'SDN',
            'params': ['*']
        }
    )
    return nb_node


def RetrieveData(params):
    # Common used variables: GCP related Resource id, name, self link uri
    nb_node = params['params']
    gcp_resource_id = nb_node['id'] if "id" in nb_node else None
    gcp_resource_name = nb_node['name'] if "name" in nb_node else None
    gcp_resource_self_link = nb_node['selfLink'] if "selfLink" in nb_node else None

    # Setup api server id
    api_server_id = params['apiServerId']

    # Setup projectId
    if 'projectId' not in params['params']['nbProperties']:
        msg = 'Error: Global Resource is not supported, because no projectId in nbProperties'
        raise Exception(msg)
    proj_id = params['params']['nbProperties']['projectId']

    # Setup url_params
    currentTime = datetime.now(timezone.utc)
    pastTime = currentTime - timedelta(seconds=330)
    url_params = {
        'filter': {
            'metric.type': "router.googleapis.com/sent_routes_count",
            'resource.labels.router_id': gcp_resource_id
        },
        'interval.startTime': pastTime.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'interval.endTime': currentTime.strftime('%Y-%m-%dT%H:%M:%SZ')
    }

    # Get Live Data
    data = NBGoogleAPILibrary.GetMonitorMetrics(
        api_server_id=api_server_id,
        proj_id=proj_id,
        url_params=url_params
    )
    return data


```

## Sample 4: Get Resource Metrics of HTTP Load Balance  Total Latencies<a id="sample4"></a>
```python

'''
Begin Declare Input Parameters
[
]
End Declare

For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''

from datetime import datetime, timezone, timedelta
import json


def BuildParameters(context, device_name, params):
    nb_node = GetDeviceProperties(
        context,
        device_name,
        {
            'techName': 'Google Cloud',
            'paramType': 'SDN',
            'params': ['*']
        }
    )
    return nb_node


def RetrieveData(params):
    # Common used variables: GCP related Resource id, name, self link uri
    nb_node = params['params']
    gcp_resource_id = nb_node['id'] if "id" in nb_node else None
    gcp_resource_name = nb_node['gcp_name'] if "gcp_name" in nb_node else None
    gcp_resource_self_link = nb_node['selfLink'] if "selfLink" in nb_node else None

    # Setup api server id
    api_server_id = params['apiServerId']

    # Setup projectId
    if 'projectId' not in params['params']['nbProperties']:
        msg = 'Error: Global Resource is not supported, because no projectId in nbProperties'
        raise Exception(msg)
    proj_id = params['params']['nbProperties']['projectId']

    # Get forwarding rule name
    forwarding_rule = nb_node['nbProperties']["forwardingRules"][0].split("/")[-1]

    # Setup url_params
    currentTime = datetime.now(timezone.utc)
    pastTime = currentTime - timedelta(hours=4)
    url_params = {
        'filter': {
            'metric.type': "loadbalancing.googleapis.com/https/total_latencies",
            'resource.labels.forwarding_rule_name': forwarding_rule
        },
        'interval.startTime': pastTime.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'interval.endTime': currentTime.strftime('%Y-%m-%dT%H:%M:%SZ')
    }

    # Get Live Data
    data = NBGoogleAPILibrary.GetMonitorMetrics(
        api_server_id=api_server_id,
        proj_id=proj_id,
        url_params=url_params
    )
    return data
```


## Sample 5: Get Resource Metrics of Cloud NAT New Connections Count<a id="sample5"></a>
```python
'''
Begin Declare Input Parameters
[
]
End Declare

For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''

from datetime import datetime, timezone, timedelta
import json


def BuildParameters(context, device_name, params):
    nb_node = GetDeviceProperties(
        context,
        device_name,
        {
            'techName': 'Google Cloud',
            'paramType': 'SDN',
            'params': ['*']
        }
    )
    return nb_node


def RetrieveData(params):
    # Common used variables: GCP related Resource id, name, self link uri
    nb_node = params['params']
    gcp_resource_id = nb_node['id'] if "id" in nb_node else None
    gcp_resource_name = nb_node['gcp_name'] if "gcp_name" in nb_node else None
    gcp_resource_self_link = nb_node['selfLink'] if "selfLink" in nb_node else None
    
    # Setup api server id
    api_server_id = params['apiServerId']

    # Setup projectId
    if 'projectId' not in params['params']['nbProperties']:
        msg = 'Error: Global Resource is not supported, because no projectId in nbProperties'
        raise Exception(msg)
    proj_id = params['params']['nbProperties']['projectId']

    # Setup url_params
    currentTime = datetime.now(timezone.utc)
    pastTime = currentTime - timedelta(seconds=330)
    url_params = {
        'filter': {
            'metric.type': "compute.googleapis.com/nat/new_connections_count",
            'metric.labels.nat_gateway_name': gcp_resource_name
        },
        'interval.startTime': pastTime.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'interval.endTime': currentTime.strftime('%Y-%m-%dT%H:%M:%SZ')
    }

    # Get Live Data
    data = NBGoogleAPILibrary.GetMonitorMetrics(
        api_server_id=api_server_id,
        proj_id=proj_id,
        url_params=url_params
    )
    return data

```


## Sample 6: Get Resource Metrics of Partner Interconnect Network Attachment Capacity<a id="sample6"></a>
```python
'''
Begin Declare Input Parameters
[
]
End Declare

For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''

from datetime import datetime, timezone, timedelta
import json


def BuildParameters(context, device_name, params):
    nb_node = GetDeviceProperties(
        context,
        device_name,
        {
            'techName': 'Google Cloud',
            'paramType': 'SDN',
            'params': ['*']
        }
    )
    return nb_node


def RetrieveData(params):
    # Setup api server id
    api_server_id = params['apiServerId']
    # GCP resource id, name, self_link
    nb_node = params['params']
    gcp_resource_id = nb_node['id'] if "id" in nb_node else None
    gcp_resource_name = nb_node['gcp_name'] if "name" in nb_node else None
    gcp_resource_self_link = nb_node['selfLink'] if "selfLink" in nb_node else None


    # Setup projectId
    if 'projectId' not in params['params']['nbProperties']:
        msg = 'Error: Global Resource is not supported, because no projectId in nbProperties'
        raise Exception(msg)
    proj_id = params['params']['nbProperties']['projectId']

    # raise Exception(str(params['params']))
    # Setup url_params
    currentTime = datetime.now(timezone.utc)
    pastTime = currentTime - timedelta(seconds=330)
    url_params = {
        'filter': {
            'metric.type': "interconnect.googleapis.com/network/attachment/capacity",
            'resource.labels.interconnect': gcp_resource_name
        },
        'interval.startTime': pastTime.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'interval.endTime': currentTime.strftime('%Y-%m-%dT%H:%M:%SZ')
    }

    # Get Live Data
    data = NBGoogleAPILibrary.GetMonitorMetrics(
        api_server_id=api_server_id,
        proj_id=proj_id,
        url_params=url_params
    )
    return data

```



## Sample 7: Get Resource Metrics of Private Service Connect<a id="sample7"></a>
```python
# Research morethermore on this one
# Note: forwarding rule -> all-ip -> private service endpoint

'''
Begin Declare Input Parameters
[
]
End Declare

For sample
[
    {"name": "$param1"},
    {"name": "$param2"}
]
'''

from datetime import datetime, timezone, timedelta
import json


def BuildParameters(context, device_name, params):
    nb_node = GetDeviceProperties(
        context,
        device_name,
        {
            'techName': 'Google Cloud',
            'paramType': 'SDN',
            'params': ['*']
        }
    )
    return nb_node


def RetrieveData(params):
    # Setup api server id
    api_server_id = params['apiServerId']

    # Setup projectId
    if 'projectId' not in params['params']['nbProperties']:
        msg = 'Error: Global Resource is not supported, because no projectId in nbProperties'
        raise Exception(msg)
    proj_id = params['params']['nbProperties']['projectId']

    # raise Exception(str(params['params']))
    # Setup url_params
    currentTime = datetime.now(timezone.utc)
    pastTime = currentTime - timedelta(seconds=330)
    url_params = {
        'filter': {
            'metric.type': "compute.googleapis.com/private_service_connect/consumer/closed_connections_count",
            'resource.labels.psc_connection_id': params['params']['pscConnectionId']
        },
        'interval.startTime': pastTime.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'interval.endTime': currentTime.strftime('%Y-%m-%dT%H:%M:%SZ')
    }

    # Get Live Data
    data = NBGoogleAPILibrary.GetMonitorMetrics(
        api_server_id=api_server_id,
        proj_id=proj_id,
        url_params=url_params
    )
    return data

```