# Table of Contents
- [Introduction](#introduction)
- [API Definition](#api_def)
    - [Input Parameters](#input-parameters)
    - [Output](#output)
- [Sample](#sample)

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

# Samples <a id="sample"></a>


## Sample1: GCP Metrics CPU Usage
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
    # Setup url_params
    currentTime = datetime.now(timezone.utc)
    pastTime = currentTime - timedelta(seconds = 330)
    url_params = {
        'filter': {
            'metric.type' : "compute.googleapis.com/instance/cpu/usage_time"
        },
        'interval.startTime': pastTime.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'interval.endTime': currentTime.strftime('%Y-%m-%dT%H:%M:%SZ')
    }
    # Get Live Data
    data = NBGoogleAPILibrary.GetMonitorMetrics(
        api_server_id=params['apiServerId'],
        params=params,
        url_params=url_params
    )
    return data

```

## Sample2: GCP Metrics Cloud NAT New Connections Count
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
    # Setup url_params
    currentTime = datetime.now(timezone.utc)
    pastTime = currentTime - timedelta(seconds = 330)
    url_params = {
        'filter': {
            'metric.type' : "router.googleapis.com/nat/new_connections_count"
        },
        'interval.startTime': pastTime.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'interval.endTime': currentTime.strftime('%Y-%m-%dT%H:%M:%SZ')
    }
    # Get Live Data
    data = NBGoogleAPILibrary.GetMonitorMetrics(
        api_server_id=api_server_id,
        params=params,
        url_params=url_params
    )
    return data


 ```
