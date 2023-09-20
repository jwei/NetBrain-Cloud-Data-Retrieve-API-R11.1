# Introduction <a id="introduction"></a>
The `GetResourceDataByAPI` function is a static method of the `NBGCPAPILibrary` class that retrieves Google resource data via the Google REST API.


# API Definition <a id="api_def"></a>
```python
class NBGCPAPILibrary:
    @staticmethod
    def GetResourceDataByAPI(
            api_server_id: str,
            resource_uri: str,
            http_method: str = 'GET',
            url_params: dict = None,
            json_body: object = None,
    ) -> object:
        # implementation
        # ...
```

## Input Parameters <a id="input"></a>
The function takes in several arguments, including:
 - `api_server_id` (str) The external API Server ID of this technology instance. User should be able to get it in API Script context. Check Sample Google API Parser in NetBrain Parser Library for usage reference.
 - `resource_uri` (str) The resource identifier
 - `http_method[optional]` (str) GET or POST. The default method is "GET". 
 - `url_params[optional]` (dict) API request params for GET request
 - `json_body[optional]` (object) API request body

## Output <a id="output"></a>
> The JSON response body of the HTTP request to the Google RESTful API, which can be found in Azure API Document (e.g. https://cloud.google.com/compute/docs/reference/rest/v1)
> This is a dictionary with string keys and values.

# Samples <a id="sample"></a>
## Sample 1: Get Resource API Data of GCP General Resource <a id="sample1"></a>


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


def BuildParameters(context, device_name, params):
    nb_node = GetDeviceProperties(
        context, device_name,
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
    proj_id = nb_node["projectId"] if "projectId" in nb_node else None

    gcp_resource_id = nb_node[GCP_RESOURCE_ID_KEY] if GCP_RESOURCE_ID_KEY in nb_node else None
    gcp_resource_name = nb_node[GCP_RESOURCE_NAME_KEY] if GCP_RESOURCE_NAME_KEY in nb_node else None
    gcp_resource_self_link = nb_node[GCP_RESOURCE_SELF_LINK_KEY] if GCP_RESOURCE_SELF_LINK_KEY in nb_node else None

    # Unsupported Devices
    if gcp_resource_self_link == None:
        raise Exception("Error: Not support device '{}'".format(gcp_resource_name))


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

    # Get Live Data
    data = NBGCPAPILibrary.GetResourceDataByAPI(
        api_server_id=resource_info['apiServerId'],
        resource_uri=resource_info['selfLink']
    )
    return json.dumps(data, indent=4, default=str)

```

