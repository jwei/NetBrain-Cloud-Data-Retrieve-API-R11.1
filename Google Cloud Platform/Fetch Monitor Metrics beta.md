# Table of Contents
- [Introduction](#introduction)
- [API Definition](#api_def)
    - [Input Parameters](#input)
    - [Output](#output)
- [Sample](#sample)
    - [Sample 1: Get Resource Metrics of GCP VPC Network Instances Per Peering Group Usage](#sample1)
    - [Sample 2: Get Resource Metrics of GCP VPN Gateway Connections](#sample2)

# Introduction <a id="introduction"></a>
The `GetMonitorMetrics` function is a static method defined in the `NBGCPAPILibrary` class. It leverages the Google Monitor solution to fetch metrics of Google resources via the Google RESTful API.
For a complete list of available metrics for each Google resource, please reference to Google document: https://cloud.google.com/monitoring/api/metrics

# API Definition <a id="api_def"></a>
```python
class NBGCPAPILibrary:
    @staticmethod
    def GetMonitorMetrics(
            api_server_id: str,
            proj_id: str,
            url_params: dict,
            api_version: str = 'v3'
    ) -> object:
        # implementation
        # ...
```

## Input Parameters <a id="input"></a>
 - `api_server_id`(str) - The external API server used to discover this GCP resource..
 - `proj_id`(str) - The project ID of the GCP resource belonging to. 
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
 - `api_version[optional]`(str) - API Version of the Google Rest API. default 'v3'
## Output <a id="output"></a>
> resp_body_json: The JSON response body of the HTTP request to the Google monitor metrics API. This is a dictionary with string keys and values.


# Special Notes <a id="special-notes"></a>

## GCP Virtual Private Cloud <a id="vpc"></a>
- In NetBrain, we generate "VPC Router" for each GCP Virtual Network to represent its networking entity
- The VPC's resource id is saved in the "networkId" in the nb_node data from `RetrieveData` method
- For the usage please check samples below.

## Unsupported Virtual Node <a id="unsupported-virtual-node"></a>
- There are some virual nodes building in NetBrain structure, which might not have metrics data:
  - Internet Gateway
  - Global Internet Gateway

# Samples <a id="sample"></a>
**Filtering Metrics**

To filter metrics, you will need to modify the following variables:

- `FILTER_METRIC_TYPE_PREFIX`
- `FILTER_METRIC_TYPE`

These variables control the metric types that are included in your API requests. You can find a comprehensive list of available metrics for various Google Cloud Platform (GCP) resources by referring to the [Metrics list](https://cloud.google.com/monitoring/api/metrics). This list will provide you with the necessary metric types to use for your filtering requirements.

**Filtering by Resource**

To retrieve specific resource metrics, you can use label-based filtering. This involves utilizing labels to narrow down your search for metrics associated with a particular resource. For more information on the available monitored resource types and their labels, please consult the [Monitored resource types](https://cloud.google.com/monitoring/api/resources) documentation.

By effectively using these labels, you can tailor your API requests to obtain the precise metric data you require for your GCP resources.

## Sample 1: Get Resource Metrics of GCP VPC Network Instances Per Peering Group Usage <a id="sample1"></a>
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

# The field "key" of the corresponding data field of GCP resources in NetBrain data model
GCP_RESOURCE_ID_KEY = 'networkId'
GCP_RESOURCE_NAME_KEY = 'gcp_name'
GCP_RESOURCE_SELF_LINK_KEY = 'selfLink'

# Time Range for the GCP Monitor statistics
END_TIME = datetime.now(timezone.utc)
START_TIME = END_TIME - timedelta(hours=24)

# Metrics
#   to get a complete list, please ref to: https://cloud.google.com/monitoring/api/metrics_gcp
FILTER_METRIC_TYPE_PREFIX = "compute.googleapis.com/"
FILTER_METRIC_TYPE = "quota/instances_per_peering_group/usage"



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


def GetResourceInfoFromNetBrainDataModel(params: dict) -> dict:
    """
    Get Resource Info from NetBrain Data Model
    Args:
        params(dict): dictionary of netbrain data model
    Returns:
        (dict) the Resource Info that contains
            - API Server ID
            - Project ID
            - GCP Resource ID
            - GCP Resource Name
            - GCP Resource Self Link
    """
    # Common used variables: GCP related Resource id, name, self link uri
    nb_node = params['params']

    # Setup api server id
    api_server_id = params['apiServerId']

    # Get proj_id
    proj_id = NBGCPAPILibrary.GetProjectIdByResource(nb_node)

    gcp_resource_id = nb_node[GCP_RESOURCE_ID_KEY] if GCP_RESOURCE_ID_KEY in nb_node else None
    gcp_resource_name = nb_node[GCP_RESOURCE_NAME_KEY] if GCP_RESOURCE_NAME_KEY in nb_node else None
    gcp_resource_self_link = nb_node[GCP_RESOURCE_SELF_LINK_KEY] if GCP_RESOURCE_SELF_LINK_KEY in nb_node else None

    resource_info = {
        'apiServerId': api_server_id,
        'projId': proj_id,
        'id': gcp_resource_id,
        'name': gcp_resource_name,
        'selfLink': gcp_resource_self_link
    }
    return resource_info


def RetrieveData(params):
    # Get resource info that is used to send RestAPI to the GCP Monitor Service
    resource_info = GetResourceInfoFromNetBrainDataModel(params)

    # Setup url_params
    url_params = {
        'filter': {
            'metric.type': FILTER_METRIC_TYPE_PREFIX + FILTER_METRIC_TYPE,
            # Returning labels to filter specific resource
            #    See full return type list, please ref: https://cloud.google.com/monitoring/api/resources
            'resource.labels.network_id': resource_info['id']
        },
        'interval.startTime': START_TIME.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'interval.endTime': END_TIME.strftime('%Y-%m-%dT%H:%M:%SZ')
    }

    # Get Live Data
    data = NBGCPAPILibrary.GetMonitorMetrics(
        api_server_id=resource_info['apiServerId'],
        proj_id=resource_info['projId'],
        url_params=url_params
    )
    return json.dumps(data, indent=4, default=str)

```

## Sample 2: Get Resource Metrics of GCP VPN Gateway Connections <a id="sample2"></a>
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

# The field "key" of the corresponding data field of GCP resources in NetBrain data model
GCP_RESOURCE_ID_KEY = 'id'
GCP_RESOURCE_NAME_KEY = 'gcp_name'
GCP_RESOURCE_SELF_LINK_KEY = 'selfLink'

# Time Range for the GCP Monitor statistics
END_TIME = datetime.now(timezone.utc)
START_TIME = END_TIME - timedelta(seconds=330)

# Metrics
#   to get a complete list, please ref to: https://cloud.google.com/monitoring/api/metrics_gcp
FILTER_METRIC_TYPE_PREFIX = "vpn.googleapis.com/"
FILTER_METRIC_TYPE = "gateway/connections"



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


def GetResourceInfoFromNetBrainDataModel(params: dict) -> dict:
    """
    Get Resource Info from NetBrain Data Model
    Args:
        params(dict): dictionary of netbrain data model
    Returns:
        (dict) the Resource Info that contains
            - API Server ID
            - Project ID
            - GCP Resource ID
            - GCP Resource Name
            - GCP Resource Self Link
    """
    # Common used variables: GCP related Resource id, name, self link uri
    nb_node = params['params']

    # Setup api server id
    api_server_id = params['apiServerId']

    # Get proj_id
    proj_id = NBGCPAPILibrary.GetProjectIdByResource(nb_node)

    gcp_resource_id = nb_node[GCP_RESOURCE_ID_KEY] if GCP_RESOURCE_ID_KEY in nb_node else None
    gcp_resource_name = nb_node[GCP_RESOURCE_NAME_KEY] if GCP_RESOURCE_NAME_KEY in nb_node else None
    gcp_resource_self_link = nb_node[GCP_RESOURCE_SELF_LINK_KEY] if GCP_RESOURCE_SELF_LINK_KEY in nb_node else None

    resource_info = {
        'apiServerId': api_server_id,
        'projId': proj_id,
        'id': gcp_resource_id,
        'name': gcp_resource_name,
        'selfLink': gcp_resource_self_link
    }
    return resource_info


def RetrieveData(params):
    # Get resource info that is used to send RestAPI to the GCP Monitor Service
    resource_info = GetResourceInfoFromNetBrainDataModel(params)

    # Setup url_params
    url_params = {
        'filter': {
            'metric.type': FILTER_METRIC_TYPE_PREFIX + FILTER_METRIC_TYPE,
            # Returning labels to filter specific resource
            #    See full return type list, please ref: https://cloud.google.com/monitoring/api/resources
            'resource.labels.gateway_id': resource_info['id']
        },
        'interval.startTime': START_TIME.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'interval.endTime': END_TIME.strftime('%Y-%m-%dT%H:%M:%SZ')
    }

    # Get Live Data
    data = NBGCPAPILibrary.GetMonitorMetrics(
        api_server_id=resource_info['apiServerId'],
        proj_id=resource_info['projId'],
        url_params=url_params
    )
    return json.dumps(data, indent=4, default=str)

```

