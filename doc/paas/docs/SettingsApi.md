# openapi_client.SettingsApi

All URIs are relative to *https://api.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**default_subdomain**](SettingsApi.md#default_subdomain) | **POST** /v1/projects/{id}/default-subdomain/{status} | Default subdomain
[**ip_static**](SettingsApi.md#ip_static) | **POST** /v1/projects/{id}/fixed-ip/{status} | IP static
[**update_envs**](SettingsApi.md#update_envs) | **POST** /v1/projects/update-envs | Update envs
[**zero_downtime**](SettingsApi.md#zero_downtime) | **POST** /v1/projects/{id}/zero-downtime/{status} | Zero downtime


# **default_subdomain**
> default_subdomain(id, status)

Default subdomain

default subdomain that user owns

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.iran.liara.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.iran.liara.ir"
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
    api_instance = openapi_client.SettingsApi(api_client)
    id = 'id_example' # str | 
    status = 'status_example' # str | disable or enable

    try:
        # Default subdomain
        api_instance.default_subdomain(id, status)
    except Exception as e:
        print("Exception when calling SettingsApi->default_subdomain: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **status** | **str**| disable or enable | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | App does not exists. |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_static**
> IpStatic200Response ip_static(id, status)

IP static

ip static that user owns

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.ip_static200_response import IpStatic200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.iran.liara.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.iran.liara.ir"
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
    api_instance = openapi_client.SettingsApi(api_client)
    id = 'id_example' # str | 
    status = 'status_example' # str | disable or enable

    try:
        # IP static
        api_response = api_instance.ip_static(id, status)
        print("The response of SettingsApi->ip_static:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->ip_static: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **status** | **str**| disable or enable | 

### Return type

[**IpStatic200Response**](IpStatic200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | App does not exists. |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_envs**
> UpdateEnvs200Response update_envs(update_envs)

Update envs

update envs that user owns

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.update_envs import UpdateEnvs
from openapi_client.models.update_envs200_response import UpdateEnvs200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.iran.liara.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.iran.liara.ir"
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
    api_instance = openapi_client.SettingsApi(api_client)
    update_envs = openapi_client.UpdateEnvs() # UpdateEnvs | 

    try:
        # Update envs
        api_response = api_instance.update_envs(update_envs)
        print("The response of SettingsApi->update_envs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->update_envs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_envs** | [**UpdateEnvs**](UpdateEnvs.md)|  | 

### Return type

[**UpdateEnvs200Response**](UpdateEnvs200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zero_downtime**
> zero_downtime(id, status)

Zero downtime

zero downtime that user owns

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.iran.liara.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.iran.liara.ir"
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
    api_instance = openapi_client.SettingsApi(api_client)
    id = 'id_example' # str | 
    status = 'status_example' # str | disable or enable

    try:
        # Zero downtime
        api_instance.zero_downtime(id, status)
    except Exception as e:
        print("Exception when calling SettingsApi->zero_downtime: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **status** | **str**| disable or enable | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | App does not exists. |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

