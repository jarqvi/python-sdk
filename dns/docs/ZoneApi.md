# openapi_client.ZoneApi

All URIs are relative to *https://dns-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_zone**](ZoneApi.md#create_zone) | **POST** /api/v1/zones | Create Zone
[**delete_zone**](ZoneApi.md#delete_zone) | **DELETE** /api/v1/zones/{zone} | Delete Zone
[**get_list_zones**](ZoneApi.md#get_list_zones) | **GET** /api/v1/zones | List all zones
[**get_zone**](ZoneApi.md#get_zone) | **GET** /api/v1/zones/{zone} | Get Zone


# **create_zone**
> CreateZone create_zone(zone_struct)

Create Zone

creates a new zone on dns server

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.create_zone import CreateZone
from openapi_client.models.create_zone_request import CreateZoneRequest
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
    api_instance = openapi_client.ZoneApi(api_client)
    zone_struct = openapi_client.CreateZoneRequest() # CreateZoneRequest | The zone to create

    try:
        # Create Zone
        api_response = api_instance.create_zone(zone_struct)
        print("The response of ZoneApi->create_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneApi->create_zone: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_struct** | [**CreateZoneRequest**](CreateZoneRequest.md)| The zone to create | 

### Return type

[**CreateZone**](CreateZone.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**409** | Conflict |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zone**
> Submitted delete_zone(zone)

Delete Zone

Deletes this zone, all dns records

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
    api_instance = openapi_client.ZoneApi(api_client)
    zone = 'zone_example' # str | The name of the zone to delete

    try:
        # Delete Zone
        api_response = api_instance.delete_zone(zone)
        print("The response of ZoneApi->delete_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneApi->delete_zone: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of the zone to delete | 

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
**200** | Your request has been submitted. |  -  |
**204** | Zone deleted. |  -  |
**401** | Missing authentication |  -  |
**404** | Zone does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_zones**
> Zones get_list_zones()

List all zones

list all zones that user owns

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.zones import Zones
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
    api_instance = openapi_client.ZoneApi(api_client)

    try:
        # List all zones
        api_response = api_instance.get_list_zones()
        print("The response of ZoneApi->get_list_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneApi->get_list_zones: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Zones**](Zones.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone**
> CreateZone get_zone(zone)

Get Zone

Get this zone, all dns records

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.create_zone import CreateZone
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
    api_instance = openapi_client.ZoneApi(api_client)
    zone = 'zone_example' # str | The name of the zone

    try:
        # Get Zone
        api_response = api_instance.get_zone(zone)
        print("The response of ZoneApi->get_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZoneApi->get_zone: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The name of the zone | 

### Return type

[**CreateZone**](CreateZone.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | zone details |  -  |
**401** | Missing authentication |  -  |
**404** | Zone does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

