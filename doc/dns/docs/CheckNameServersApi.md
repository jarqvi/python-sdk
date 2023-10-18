# openapi_client.CheckNameServersApi

All URIs are relative to *https://dns-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_name_server**](CheckNameServersApi.md#check_name_server) | **PUT** /api/v1/zones/{zone}/check | check nameserver


# **check_name_server**
> Submitted check_name_server(zone)

check nameserver

check nameserver of zone

### Example

* Api Key Authentication (jwt):
```python
import dns.openapi_client
from dns.openapi_client.models.submitted import Submitted
from dns.openapi_client.rest import ApiException
from pprint import pprint

with dns.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dns.openapi_client.CheckNameServersApi(api_client)
    zone = 'example.com'
    
    try:
        api_response: Submitted = api_instance.check_name_server(zone)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of the zone to check status | 

### Return type

[**Submitted**](Submitted.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | bad request maybe validation error on zone name |  -  |
**401** | Missing authentication |  -  |
**404** | Zone does not exists or its status is not pending |  -  |
**406** | Please try later. |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

