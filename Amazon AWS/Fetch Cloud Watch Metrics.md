# Introduction

The `GetCloudWatchMetrics` function is a static method defined in the `NBAWSAPILibrary` class. It leverages the AWS cloud watch solution to fetch metrics of AWS resources via the AWS SDK.

# Supported devices

* AWS EC2 instances
* AWS NAT Gateways
* AWS Transit Gateways
* AWS DX Router
* AWS Network Firewall
* AWS Classic Load Balancer
* AWS Elastic Load Balancer
* AWS Application Load Balancer
* AWS Gateway Load Balancer


# API Definition
 - `GetCloudWatchResourceId` method would be used to get the resource ID for the AWS resource based on the device type and parameters that were passed to the function.This retrieved resource ID is then used to construct the CloudWatch metric query, which is passed as a parameter to `NBAWSAPILibrary.GetCloudWatchMetrics` method to retrieve the metric data.




 - `GetCloudWatchMetrics` is a method that retrieves CloudWatch metrics data for a specified resource. It takes in a dictionary of parameters, which includes information such as the resource ID, the CloudWatch metric data query, and the CloudWatch client configuration

```python
class NBAWSAPILibrary:
    @staticmethod
    def GetCloudWatchResourceID(param: object):        
        """Get the resource ID for a given AWS resource to use with CloudWatch metrics.
 
        Args:
            param (dict): A dictionary containing the parameters needed to identify the resource.
 
        Returns:
            (str): The ID of the resource.
 
        Raises:
            Exception: If the given resource is not supported for CloudWatch metrics.
        """
 
        # implementation
        # ...
 
    @staticmethod
    def GetCloudWatchMetrics(params: object) -> object:
        """ Fetches AWS cloud watch metrics from Azure Insights module
 
        Leverage AWS cloud watch module to fetch resource metrics via SDK
        Ref:
        1. AWS Cloud Watch Metrics service:
 
        Args:
            param (dict): e.g. {
                'apiServerId': 'b737cc5a-75a4-4663-97d6-eb2c6b576880', 
                'RegionName': 'us-east-1',
                'func_param': {'StartTime': datetime.datetime(2020, 9, 23, 12, 10, 22, 716496), 'EndTime': datetime.datetime(2020, 9, 24, 12, 10, 22, 716496), ...}
            }
 
 
        Returns:
            (object) http response json body
 
        Raises:
        """
 
        # implementation
        # ...
```

# Input Parameters:
 - `param`(str) - it is a NetBrain object that contains essential information, including `apiServerId`, `RegionName`, and so on.


# Output:
> resp_body_json: The JSON response body of the HTTP request to the Azure monitor metrics API. This is a dictionary with string keys and values.

# Raises:
> This function does not raise any exceptions.

# Example

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
import json
import datetime
 
def BuildParameters(context, device_name, params):
    self_node = GetDeviceProperties(context, device_name, {'techName': 'Amazon AWS', 'paramType': 'SDN', 'params': ['*']})
    return self_node['params']
 
def RetrieveData(param):
    _id = NBAWSAPILibrary.GetCloudWatchResourceId(param)
    dt_now = datetime.datetime.now()
    dt_yestoday = dt_now - datetime.timedelta(days=1)
    param['func_param'] = {
        'StartTime': dt_yestoday,
        'EndTime': dt_now,
        'MaxDatapoints': 20,
        'MetricDataQueries':[
            {
                'Id': 'a0',
                'MetricStat': {
                    'Period': 300,
                    'Stat': 'Sum',
                    'Metric': {
                        'Namespace':'AWS/ApplicationELB',
                        'MetricName':'RequestCount',
                        'Dimensions':[
                            {
                                "Name": "LoadBalancer",
                                "Value": _id
                            }
                        ]
                    }
                }
            }
        ]
    }
    res = NBAWSAPILibrary.GetCloudWatchMetrics(param)
    data = json.loads(res)
    return [data]
    
 ```
