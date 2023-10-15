# openapi_client.KeyApi

All URIs are relative to *https://storage-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_key**](KeyApi.md#create_key) | **POST** /api/v1/keys | Create Keys
[**delete_key**](KeyApi.md#delete_key) | **DELETE** /api/v1/keys/{key} | Delete Key
[**get_key**](KeyApi.md#get_key) | **GET** /api/v1/keys/{key} | Get Key
[**get_list_keys**](KeyApi.md#get_list_keys) | **GET** /api/v1/keys | Get List of Keys
[**revoke_secret_key**](KeyApi.md#revoke_secret_key) | **PATCH** /api/v1/keys/{key}/revoke | Revoke secret key
[**update_key**](KeyApi.md#update_key) | **PATCH** /api/v1/keys/{key} | Update key


# **create_key**
> CreateKey201Response create_key(body)

Create Keys

Create access and secret key

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.create_key import CreateKey
from openapi_client.models.create_key201_response import CreateKey201Response
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
    api_instance = openapi_client.KeyApi(api_client)
    body = openapi_client.CreateKey() # CreateKey | Declare Buckets for access key

    try:
        # Create Keys
        api_response = api_instance.create_key(body)
        print("The response of KeyApi->create_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyApi->create_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateKey**](CreateKey.md)| Declare Buckets for access key | 

### Return type

[**CreateKey201Response**](CreateKey201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key**
> delete_key(key)

Delete Key

Delete access key

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
    api_instance = openapi_client.KeyApi(api_client)
    key = 'key_example' # str | 

    try:
        # Delete Key
        api_instance.delete_key(key)
    except Exception as e:
        print("Exception when calling KeyApi->delete_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

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

# **get_key**
> get_key(key)

Get Key

Get a key

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
    api_instance = openapi_client.KeyApi(api_client)
    key = 'key_example' # str | 

    try:
        # Get Key
        api_instance.get_key(key)
    except Exception as e:
        print("Exception when calling KeyApi->get_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

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
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_keys**
> Keys get_list_keys()

Get List of Keys

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.keys import Keys
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
    api_instance = openapi_client.KeyApi(api_client)

    try:
        # Get List of Keys
        api_response = api_instance.get_list_keys()
        print("The response of KeyApi->get_list_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyApi->get_list_keys: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Keys**](Keys.md)

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
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_secret_key**
> RevokeSecretKey200Response revoke_secret_key(key)

Revoke secret key

Revoke secret key

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.revoke_secret_key200_response import RevokeSecretKey200Response
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
    api_instance = openapi_client.KeyApi(api_client)
    key = 'key_example' # str | 

    try:
        # Revoke secret key
        api_response = api_instance.revoke_secret_key(key)
        print("The response of KeyApi->revoke_secret_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyApi->revoke_secret_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

[**RevokeSecretKey200Response**](RevokeSecretKey200Response.md)

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

# **update_key**
> CreateBucket201Response update_key(key, body)

Update key

Update buckets of key ( redefine )

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.create_bucket201_response import CreateBucket201Response
from openapi_client.models.create_key import CreateKey
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
    api_instance = openapi_client.KeyApi(api_client)
    key = 'key_example' # str | 
    body = openapi_client.CreateKey() # CreateKey | Declare Buckets for access key

    try:
        # Update key
        api_response = api_instance.update_key(key, body)
        print("The response of KeyApi->update_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyApi->update_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **body** | [**CreateKey**](CreateKey.md)| Declare Buckets for access key | 

### Return type

[**CreateBucket201Response**](CreateBucket201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
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

