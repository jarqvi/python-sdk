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
import object_storage.openapi_client
from object_storage.openapi_client.models.get_hisotrical_metrics200_response import GetHisotricalMetrics200Response
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.MetricsApi(api_client)
    bucket = 'bucket_example'
    since = 'since_example'
    
    try:
        api_response: GetHisotricalMetrics200Response = api_instance.get_hisotrical_metrics(bucket, since)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

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
import object_storage.openapi_client
from object_storage.openapi_client.models.get_metrics_summary200_response import GetMetricsSummary200Response
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.MetricsApi(api_client)
    bucket = 'bucket_example'
    
    try:
        api_response: GetMetricsSummary200Response = api_instance.get_metrics_summary(bucket)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

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

