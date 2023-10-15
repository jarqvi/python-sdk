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
import time
import os
import openapi_client
from openapi_client.models.submitted import Submitted
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dns-service.iran.liara.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dns-service.iran.liara.ir"
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
    api_instance = openapi_client.CheckNameServersApi(api_client)
    zone = 'zone_example' # str | The name of the zone to check status

    try:
        # check nameserver
        api_response = api_instance.check_name_server(zone)
        print("The response of CheckNameServersApi->check_name_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckNameServersApi->check_name_server: %s\n" % e)
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

