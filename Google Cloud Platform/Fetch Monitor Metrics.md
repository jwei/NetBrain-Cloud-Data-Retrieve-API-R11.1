# Table of Contents
- [Introduction](#introduction)
- [API Definition](#api_def)
    - [Input Parameters](#input)
    - [Output](#output)

# Introduction <a name="introduction"></a>
The `GetMonitorMetrics` function is a static method defined in the `NBGoogleAPILibrary` class. It leverages the Google Monitor solution to fetch metrics of Google resources via the Google RESTful API.
For a complete list of available metrics for each Google resource, please reference to Google document: https://cloud.google.com/monitoring/api/metrics

# API Definition <a name="api_def"></a>
```python
class NBGoogleAPILibrary:
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

## Input Parameters <a name="input"></a>
 - `api_server_id`(str) - The Google Tenant API Server Instance ID saved in Device.
 - `proj_id`(str) - The project ID for the Google resource belonging to.
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
 - `api_version[optional]`(str) - The API version to use for the Google monitor metrics API, default is v3

## Output <a name="output"></a>
> resp_body_json: The JSON response body of the HTTP request to the Google monitor metrics API. This is a dictionary with string keys and values.

# Samples <a name="sample"></a>
## Sample 1 -- Get General Resource Metrics  <a name="sample_1"></a>
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

def BuildParameters(context, device_name, params):
    node_props = GetDeviceProperties(context, device_name,
        {
            'techName': 'Google Cloud',
            'paramType': 'SDN',
            'params':['nbProperties','id']
        })
    
    nb_props = json.loads(node_props['params']['nbProperties'])

    params = [{
        'devName': device_name,
        'projId': nb_props['projectId'],
        'deviceId':node_props['params']['id']
    }]
    return params


def RetrieveData(params):
    instanceName = params['devName']
    #Get Current Time and Start Time for Metrics
    currentTime = datetime.now(timezone.utc)
    pastTime = currentTime - timedelta(seconds = 180)

    api_server_id = params['apiServerId']
    proj_id = params['projId']
    url_params = {
        'filter': {
           'metric.type' : "compute.googleapis.com/instance/cpu/usage_time",
           'metric.labels.instance_name': instanceName
        },
        'interval.startTime': pastTime.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'interval.endTime': currentTime.strftime('%Y-%m-%dT%H:%M:%SZ')
    }
    # Get Live Data
    data = NBGoogleAPILibrary.GetMonitorMetrics(
        api_server_id=params['apiServerId'],
        azure_resource_uri=params['params']['id'],
        params={'metricnames': metric_name}
    )
    return data
 ```
