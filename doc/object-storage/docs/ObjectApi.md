# openapi_client.ObjectApi

All URIs are relative to *https://storage-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_object**](ObjectApi.md#delete_object) | **DELETE** /api/v1/buckets/{bucket}/objects/{prefix} | Delete Object
[**download_object**](ObjectApi.md#download_object) | **GET** /api/v1/buckets/{bucket}/download/${object} | Download Object
[**get_list_objects**](ObjectApi.md#get_list_objects) | **GET** /api/v1/buckets/{bucket}/objects/{prefix} | List Objects
[**get_stat_object**](ObjectApi.md#get_stat_object) | **GET** /api/v1/buckets/{bucket}/objects/statistics/{object} | Get Stat Object
[**upload_object**](ObjectApi.md#upload_object) | **GET** /api/v1/buckets/{bucket}/upload/{object} | Upload Object


# **delete_object**
> delete_object(bucket, prefix)

Delete Object

Delete an object from storage

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.ObjectApi(api_client)
    bucket = 'bucket_example' # str | 
    prefix = 'prefix_example' # str | 

    try:
        # Delete Object
        api_instance.delete_object(bucket, prefix)
    except Exception as e:
        print("Exception when calling ObjectApi->delete_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **prefix** | **str**|  | 

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
**204** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_object**
> DownloadObject200Response download_object(bucket, object, expiry=expiry)

Download Object

Return presigned url for download object

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.download_object200_response import DownloadObject200Response
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
    api_instance = openapi_client.ObjectApi(api_client)
    bucket = 'bucket_example' # str | 
    object = 'object_example' # str | specify object path
    expiry = 'expiry_example' # str | example: 2 days 7 hours 45 minutes (optional)

    try:
        # Download Object
        api_response = api_instance.download_object(bucket, object, expiry=expiry)
        print("The response of ObjectApi->download_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->download_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **object** | **str**| specify object path | 
 **expiry** | **str**| example: 2 days 7 hours 45 minutes | [optional] 

### Return type

[**DownloadObject200Response**](DownloadObject200Response.md)

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

# **get_list_objects**
> Objects get_list_objects(bucket, prefix, number=number, page=page)

List Objects

Return list of objects ( max:50, min:1 )

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.objects import Objects
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
    api_instance = openapi_client.ObjectApi(api_client)
    bucket = 'bucket_example' # str | 
    prefix = 'prefix_example' # str | 
    number = 'number_example' # str | specify number of object ( max: 50, min: 1 ) (optional)
    page = 'page_example' # str |  (optional)

    try:
        # List Objects
        api_response = api_instance.get_list_objects(bucket, prefix, number=number, page=page)
        print("The response of ObjectApi->get_list_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->get_list_objects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **prefix** | **str**|  | 
 **number** | **str**| specify number of object ( max: 50, min: 1 ) | [optional] 
 **page** | **str**|  | [optional] 

### Return type

[**Objects**](Objects.md)

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

# **get_stat_object**
> Stat get_stat_object(bucket, object)

Get Stat Object

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.stat import Stat
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
    api_instance = openapi_client.ObjectApi(api_client)
    bucket = 'bucket_example' # str | 
    object = 'object_example' # str | 

    try:
        # Get Stat Object
        api_response = api_instance.get_stat_object(bucket, object)
        print("The response of ObjectApi->get_stat_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->get_stat_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **object** | **str**|  | 

### Return type

[**Stat**](Stat.md)

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

# **upload_object**
> DownloadObject200Response upload_object(bucket, object)

Upload Object

Return presigned url for download object

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.download_object200_response import DownloadObject200Response
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
    api_instance = openapi_client.ObjectApi(api_client)
    bucket = 'bucket_example' # str | 
    object = 'object_example' # str | specify object path

    try:
        # Upload Object
        api_response = api_instance.upload_object(bucket, object)
        print("The response of ObjectApi->upload_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectApi->upload_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **object** | **str**| specify object path | 

### Return type

[**DownloadObject200Response**](DownloadObject200Response.md)

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

