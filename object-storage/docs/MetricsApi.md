# openapi_client.MetricsApi

All URIs are relative to *https://storage-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hisotrical_metrics**](MetricsApi.md#get_hisotrical_metrics) | **GET** /api/v1/buckets/{bucket}/metrics/historical | hisotrical metrics
[**get_metrics_summary**](MetricsApi.md#get_metrics_summary) | **GET** /api/v1/buckets/{bucket}/metrics/summary | metrics summary


# **get_hisotrical_metrics**
> GetHisotricalMetrics200Response get_hisotrical_metrics(bucket, since)

hisotrical metrics

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.get_hisotrical_metrics200_response import GetHisotricalMetrics200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://storage-service.iran.liara.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://storage-service.iran.liara.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MetricsApi(api_client)
    bucket = 'bucket_example' # str | 
    since = 'since_example' # str | unix time

    try:
        # hisotrical metrics
        api_response = api_instance.get_hisotrical_metrics(bucket, since)
        print("The response of MetricsApi->get_hisotrical_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_hisotrical_metrics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **since** | **str**| unix time | 

### Return type

[**GetHisotricalMetrics200Response**](GetHisotricalMetrics200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics_summary**
> GetMetricsSummary200Response get_metrics_summary(bucket)

metrics summary

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.get_metrics_summary200_response import GetMetricsSummary200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://storage-service.iran.liara.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://storage-service.iran.liara.ir"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MetricsApi(api_client)
    bucket = 'bucket_example' # str | 

    try:
        # metrics summary
        api_response = api_instance.get_metrics_summary(bucket)
        print("The response of MetricsApi->get_metrics_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_metrics_summary: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 

### Return type

[**GetMetricsSummary200Response**](GetMetricsSummary200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

