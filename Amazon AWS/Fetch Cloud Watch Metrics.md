# Table of Contents
- [Introduction](#introduction)
- [Supported Devices](#devices)
- [API Definition](#definition)
    - [Input Parameters](#input)
    - [Output](#output)
    - [Exception Raises](#raises)
- [Sample](#sample)


# Introduction <a name="introduction"></a>

The `GetCloudWatchMetrics` function is a static method defined in the `NBAWSAPILibrary` class. It leverages the AWS CloudWatch solution to fetch metrics of AWS resources via the AWS SDK.

Reference: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_metric_data.html

# Supported devices  <a name="devices"></a>

* AWS EC2 Instance
* AWS NAT Gateway
* AWS Transit Gateway
* AWS DX Router
* AWS Network Firewall
* AWS Classic Load Balancer
* AWS Network Load Balancer
* AWS Application Load Balancer
* AWS Gateway Load Balancer


# API Definition <a name="definition"></a>
 - `GetCloudWatchResourceId` method would be used to get the resource ID for the AWS resource based on the device type and parameters that were passed to the function.This retrieved resource ID is then used to construct the CloudWatch metric query, which is passed as a parameter to `NBAWSAPILibrary.GetCloudWatchMetrics` method to retrieve the metric data.


 - `GetCloudWatchMetrics` is a method that retrieves CloudWatch metrics data for a specified resource. It takes in a dictionary of parameters, which includes information such as the resource ID, the CloudWatch metric data query, and the CloudWatch client configuration

```python
class NBAWSAPILibrary:
    @staticmethod
    def GetCloudWatchResourceID(param: object):        
        """ Get the resource ID for a given AWS resource to use with CloudWatch metrics.
 
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
        """ Fetches AWS CloudWatch metrics from AWS CloudWatch module
 
        Leverage AWS CloudWatch module to fetch resource metrics via SDK
        Ref:
        1. AWS CloudWatch Metrics service:
 
        Args:
            param (dict): e.g. {
                'apiServerId': 'b737cc5a-75a4-4663-97d6-eb2c6b576880', 
                'RegionName': 'us-east-1',
                'func_param': {'StartTime': datetime.datetime(2020, 9, 23, 12, 10, 22, 716496), 'EndTime': datetime.datetime(2020, 9, 24, 12, 10, 22, 716496), ...}
            }
 
 
        Returns:
            (object) response json body
 
        Raises:
           Exception: It raises a generic Exception if the provided parameters are invalid.
        """
 
        # implementation
        # ...
```

## Input Parameters <a name="input"></a>
 - `param`(str) - it is a NetBrain object that contains `apiServerId`, `RegionName` and essential information in `func_param`.
    - `func_param` (dict) including `StartTime`, `EndTime`, `MetricDataQueries` and so on. 
       - `MetricDataQueries` (list) [REQUIRED] The metric queries to be returned. A single GetMetricData call can include as many as 500 MetricDataQuery structures. Each of these structures can specify either a metric to retrieve, a Metrics Insights query, or a math expression to perform on retrieved data. Please use this [link](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) as reference to construct the metric query.
       - `StartTime` (datetime) [REQUIRED] The time stamp indicating the earliest data to be returned.
       - `EndTime` (datetime) [REQUIRED] The time stamp indicating the latest data to be returned.
       - `MaxDatapoints` (integer) The maximum number of data points the request should return before paginating. If you omit this, the default of 100,800 is used.


## Output <a name="output"></a>
> resp_body_json: The JSON response body of request to the AWS CloudWatch metrics SDK. This is a dictionary with string keys and values.

## Exception Raises <a name="raises"></a>
> The `GetCloudWatchMetrics` function raises a generic Exception if the provided parameters are invalid. 

# Sample <a name="sample"></a>

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
                                'Name': 'LoadBalancer',
                                'Value': _id
                            }
                        ]
                    }
                }
            }
        ]
    }
    res = NBAWSAPILibrary.GetCloudWatchMetrics(param)
    return json.dumps(res, indent=4, default=str)
    
 ```
