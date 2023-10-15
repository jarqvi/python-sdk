# openapi_client.ReportsApi

All URIs are relative to *https://api.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_database_cpu_reports**](ReportsApi.md#get_database_cpu_reports) | **GET** /v1/databases/{id}/metrics/cpu | Get cpu reports of database
[**get_database_memory_reports**](ReportsApi.md#get_database_memory_reports) | **GET** /v1/databases/{id}/metrics/memory | Get memory reports of database
[**get_database_network_receive_reports**](ReportsApi.md#get_database_network_receive_reports) | **GET** /v1/databases/{id}/metrics/network-receive | Get network-receive reports of database
[**get_database_network_transmit_reports**](ReportsApi.md#get_database_network_transmit_reports) | **GET** /v1/databases/{id}/metrics/network-transmit | Get network-transmit reports of database
[**get_database_summary_reports**](ReportsApi.md#get_database_summary_reports) | **GET** /v1/databases/{id}/metrics/summary | Get summary reports of database


# **get_database_cpu_reports**
> Reports get_database_cpu_reports(id, since)

Get cpu reports of database

get cpu reports of database that user owns

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
    id = 'id_example' # str | The name of your database
    since = 3.4 # float | The since of your cpu reports

    try:
        # Get cpu reports of database
        api_response = api_instance.get_database_cpu_reports(id, since)
        print("The response of ReportsApi->get_database_cpu_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_database_cpu_reports: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of your database | 
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
**404** | Database does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_memory_reports**
> Reports get_database_memory_reports(id, since)

Get memory reports of database

get memory reports of database that user owns

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
    id = 'id_example' # str | The name of your database
    since = 3.4 # float | The since of your memory reports

    try:
        # Get memory reports of database
        api_response = api_instance.get_database_memory_reports(id, since)
        print("The response of ReportsApi->get_database_memory_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_database_memory_reports: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of your database | 
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
**404** | Database does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_network_receive_reports**
> Reports get_database_network_receive_reports(id, since)

Get network-receive reports of database

get network-receive reports of database that user owns

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
    id = 'id_example' # str | The name of your database
    since = 3.4 # float | The since of your network-receive reports

    try:
        # Get network-receive reports of database
        api_response = api_instance.get_database_network_receive_reports(id, since)
        print("The response of ReportsApi->get_database_network_receive_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_database_network_receive_reports: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of your database | 
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
**404** | Database does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_network_transmit_reports**
> Reports get_database_network_transmit_reports(id, since)

Get network-transmit reports of database

get network-transmit reports of database that user owns

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
    id = 'id_example' # str | The name of your database
    since = 3.4 # float | The since of your network-transmit reports

    try:
        # Get network-transmit reports of database
        api_response = api_instance.get_database_network_transmit_reports(id, since)
        print("The response of ReportsApi->get_database_network_transmit_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_database_network_transmit_reports: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of your database | 
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
**404** | Database does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_summary_reports**
> GetDatabaseSummaryReports200Response get_database_summary_reports(id)

Get summary reports of database

get summary reports of database that user owns

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.get_database_summary_reports200_response import GetDatabaseSummaryReports200Response
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
    id = 'id_example' # str | The name of your database

    try:
        # Get summary reports of database
        api_response = api_instance.get_database_summary_reports(id)
        print("The response of ReportsApi->get_database_summary_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_database_summary_reports: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of your database | 

### Return type

[**GetDatabaseSummaryReports200Response**](GetDatabaseSummaryReports200Response.md)

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
**404** | Database does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

