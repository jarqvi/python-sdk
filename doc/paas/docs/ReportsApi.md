# openapi_client.ReportsApi

All URIs are relative to *https://api.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_cpu_reports**](ReportsApi.md#get_app_cpu_reports) | **GET** /v1/projects/{name}/metrics/cpu | Get cpu reports of app
[**get_app_memory_reports**](ReportsApi.md#get_app_memory_reports) | **GET** /v1/projects/{name}/metrics/memory | Get memory reports of app
[**get_app_network_receive_reports**](ReportsApi.md#get_app_network_receive_reports) | **GET** /v1/projects/{name}/metrics/network-receive | Get network-receive reports of app
[**get_app_summary_reports**](ReportsApi.md#get_app_summary_reports) | **GET** /v1/projects/{name}/metrics/summary | Get summary reports of app
[**get_network_transmit_reports**](ReportsApi.md#get_network_transmit_reports) | **GET** /v1/projects/{name}/metrics/network-transmit | Get network-transmit reports of app


# **get_app_cpu_reports**
> Reports get_app_cpu_reports(name, since)

Get cpu reports of app

get cpu reports of app that user owns

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.reports import Reports
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
    api_instance = openapi_client.ReportsApi(api_client)
    name = 'name_example' # str | The name of your app
    since = 3.4 # float | The since of your cpu reports

    try:
        # Get cpu reports of app
        api_response = api_instance.get_app_cpu_reports(name, since)
        print("The response of ReportsApi->get_app_cpu_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_app_cpu_reports: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 
 **since** | **float**| The since of your cpu reports | 

### Return type

[**Reports**](Reports.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_memory_reports**
> Reports get_app_memory_reports(name, since)

Get memory reports of app

get memory reports of app that user owns

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.reports import Reports
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
    api_instance = openapi_client.ReportsApi(api_client)
    name = 'name_example' # str | The name of your app
    since = 3.4 # float | The since of your memory reports

    try:
        # Get memory reports of app
        api_response = api_instance.get_app_memory_reports(name, since)
        print("The response of ReportsApi->get_app_memory_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_app_memory_reports: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 
 **since** | **float**| The since of your memory reports | 

### Return type

[**Reports**](Reports.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_network_receive_reports**
> Reports get_app_network_receive_reports(name, since)

Get network-receive reports of app

get network-receive reports of app that user owns

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.reports import Reports
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
    api_instance = openapi_client.ReportsApi(api_client)
    name = 'name_example' # str | The name of your app
    since = 3.4 # float | The since of your network-receive reports

    try:
        # Get network-receive reports of app
        api_response = api_instance.get_app_network_receive_reports(name, since)
        print("The response of ReportsApi->get_app_network_receive_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_app_network_receive_reports: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 
 **since** | **float**| The since of your network-receive reports | 

### Return type

[**Reports**](Reports.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_summary_reports**
> GetAppSummaryReports200Response get_app_summary_reports(name)

Get summary reports of app

get summary reports of app that user owns

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.get_app_summary_reports200_response import GetAppSummaryReports200Response
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
    api_instance = openapi_client.ReportsApi(api_client)
    name = 'name_example' # str | The name of your app

    try:
        # Get summary reports of app
        api_response = api_instance.get_app_summary_reports(name)
        print("The response of ReportsApi->get_app_summary_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_app_summary_reports: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 

### Return type

[**GetAppSummaryReports200Response**](GetAppSummaryReports200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_transmit_reports**
> Reports get_network_transmit_reports(name, since)

Get network-transmit reports of app

get network-transmit reports of app that user owns

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.reports import Reports
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
    api_instance = openapi_client.ReportsApi(api_client)
    name = 'name_example' # str | The name of your app
    since = 3.4 # float | The since of your network-transmit reports

    try:
        # Get network-transmit reports of app
        api_response = api_instance.get_network_transmit_reports(name, since)
        print("The response of ReportsApi->get_network_transmit_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_network_transmit_reports: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 
 **since** | **float**| The since of your network-transmit reports | 

### Return type

[**Reports**](Reports.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

