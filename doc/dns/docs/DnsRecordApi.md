# openapi_client.DnsRecordApi

All URIs are relative to *https://dns-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dns_record**](DnsRecordApi.md#create_dns_record) | **POST** /api/v1/zones/{zone}/dns-records | Create dns record
[**delete_dns_record**](DnsRecordApi.md#delete_dns_record) | **DELETE** /api/v1/zones/{zone}/dns-records/{id} | delete dns record
[**edit_dns_record**](DnsRecordApi.md#edit_dns_record) | **PUT** /api/v1/zones/{zone}/dns-records/{id} | edit dns record
[**get_dns_record**](DnsRecordApi.md#get_dns_record) | **GET** /api/v1/zones/{zone}/dns-records/{id} | Get dns record
[**get_list_dns_records**](DnsRecordApi.md#get_list_dns_records) | **GET** /api/v1/zones/{zone}/dns-records | Get all dns record


# **create_dns_record**
> DnsRecordResponse create_dns_record(zone, dns_record)

Create dns record

Creates a new dns record, returns the dns record on creation

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.dns_record import DnsRecord
from openapi_client.models.dns_record_response import DnsRecordResponse
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
    api_instance = openapi_client.DnsRecordApi(api_client)
    zone = 'zone_example' # str | The name of the zone to delete
    dns_record = openapi_client.DnsRecord() # DnsRecord | 

    try:
        # Create dns record
        api_response = api_instance.create_dns_record(zone, dns_record)
        print("The response of DnsRecordApi->create_dns_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DnsRecordApi->create_dns_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of the zone to delete | 
 **dns_record** | [**DnsRecord**](DnsRecord.md)|  | 

### Return type

[**DnsRecordResponse**](DnsRecordResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | Zone does not exists. |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dns_record**
> delete_dns_record(zone, id)

delete dns record

Delete dns record from this zone

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.DnsRecordApi(api_client)
    zone = 'zone_example' # str | The name of the zone to delete dns record
    id = 'id_example' # str | The id of dns record to delete its data

    try:
        # delete dns record
        api_instance.delete_dns_record(zone, id)
    except Exception as e:
        print("Exception when calling DnsRecordApi->delete_dns_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of the zone to delete dns record | 
 **id** | **str**| The id of dns record to delete its data | 

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
**204** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | Zone does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_dns_record**
> DnsRecordResponse edit_dns_record(zone, id, dns_record)

edit dns record

you can not edit type of dns record

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.dns_record import DnsRecord
from openapi_client.models.dns_record_response import DnsRecordResponse
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
    api_instance = openapi_client.DnsRecordApi(api_client)
    zone = 'zone_example' # str | The name of the zone to edit dns record
    id = 'id_example' # str | The id of dns record to edit its data
    dns_record = openapi_client.DnsRecord() # DnsRecord | 

    try:
        # edit dns record
        api_response = api_instance.edit_dns_record(zone, id, dns_record)
        print("The response of DnsRecordApi->edit_dns_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DnsRecordApi->edit_dns_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of the zone to edit dns record | 
 **id** | **str**| The id of dns record to edit its data | 
 **dns_record** | [**DnsRecord**](DnsRecord.md)|  | 

### Return type

[**DnsRecordResponse**](DnsRecordResponse.md)

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
**404** | Zone does not exists. |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dns_record**
> DnsRecordResponse get_dns_record(zone, id)

Get dns record

Get Dns Record data on this zone

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.dns_record_response import DnsRecordResponse
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
    api_instance = openapi_client.DnsRecordApi(api_client)
    zone = 'zone_example' # str | The name of the zone to see dns record
    id = 'id_example' # str | The id of dns record to see its data

    try:
        # Get dns record
        api_response = api_instance.get_dns_record(zone, id)
        print("The response of DnsRecordApi->get_dns_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DnsRecordApi->get_dns_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of the zone to see dns record | 
 **id** | **str**| The id of dns record to see its data | 

### Return type

[**DnsRecordResponse**](DnsRecordResponse.md)

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
**404** | Zone or dns record Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_dns_records**
> AllDnsRecordResponse get_list_dns_records(zone)

Get all dns record

Get all Dns Records on this zone

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.all_dns_record_response import AllDnsRecordResponse
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
    api_instance = openapi_client.DnsRecordApi(api_client)
    zone = 'zone_example' # str | The name of the zone to see all dns records

    try:
        # Get all dns record
        api_response = api_instance.get_list_dns_records(zone)
        print("The response of DnsRecordApi->get_list_dns_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DnsRecordApi->get_list_dns_records: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of the zone to see all dns records | 

### Return type

[**AllDnsRecordResponse**](AllDnsRecordResponse.md)

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
**404** | Zone Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

