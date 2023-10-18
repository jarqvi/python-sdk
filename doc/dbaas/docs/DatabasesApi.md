# openapi_client.DatabasesApi

All URIs are relative to *https://api.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_control_panel**](DatabasesApi.md#change_control_panel) | **POST** /v1/databases/{id}/control-panel/{status} | Change control-panel status
[**change_public_network**](DatabasesApi.md#change_public_network) | **PATCH** /v1/databases/{id}/public-network/{status} | Change public network status
[**create_database**](DatabasesApi.md#create_database) | **POST** /v1/databases | Create a database
[**delete_database**](DatabasesApi.md#delete_database) | **DELETE** /v1/databases/{id} | Delete a database
[**get_database**](DatabasesApi.md#get_database) | **GET** /v1/databases/{id} | Get a database
[**get_list_databases**](DatabasesApi.md#get_list_databases) | **GET** /v1/databases | Get all databases
[**resize_database**](DatabasesApi.md#resize_database) | **POST** /v1/databases/{id}/resize | Resize a database
[**turn_database**](DatabasesApi.md#turn_database) | **POST** /v1/databases/{id}/actions/scale | Power on or power off a database


# **change_control_panel**
> ChangeControlPanel200Response change_control_panel(id, status)

Change control-panel status

change control-panel status that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.models.change_control_panel200_response import ChangeControlPanel200Response
from dbaas.openapi_client.rest import ApiException
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.DatabasesApi(api_client)
    id = 'id_example'
    status = 'status_example'
    
    try:
        api_response: ChangeControlPanel200Response = api_instance.change_control_panel(id, status)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **status** | **str**|  | 

### Return type

[**ChangeControlPanel200Response**](ChangeControlPanel200Response.md)

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
**404** | Database not found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_public_network**
> change_public_network(id, status)

Change public network status

change public network status that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.rest import ApiException
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.DatabasesApi(api_client)
    id = 'id_example'
    status = 'status_example'
    
    try:
        api_instance.change_public_network(id, status)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **status** | **str**|  | 

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
**404** | Database not found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_database**
> CreateDatabase200Response create_database(create_a_databases)

Create a database

create a database that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.models.create_database200_response import CreateDatabase200Response
from dbaas.openapi_client.models.create_databases import CreateDatabases
from dbaas.openapi_client.rest import ApiException
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.DatabasesApi(api_client)
    create_a_databases: CreateDatabases = dbaas.openapi_client.CreateDatabases(
        hostname = 'hostname_example',
        options = {
            "standaloneReplicaSet": True,
        },
        publicNetwork = True,
        type = 'type_example',
        planID = 'planID_example',
        version = 'version_example'
    )
    
    try:
        api_response: CreateDatabase200Response = api_instance.create_database(create_a_databases)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_a_databases** | [**CreateDatabases**](CreateDatabases.md)|  | 

### Return type

[**CreateDatabase200Response**](CreateDatabase200Response.md)

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
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_database**
> delete_database(id)

Delete a database

delete a database that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.rest import ApiException
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.DatabasesApi(api_client)
    id = 'id_example'
    
    try:
        api_instance.delete_database(id)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**404** | Database not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database**
> DBDetails get_database(id)

Get a database

get a database that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.models.db_details import DBDetails
from dbaas.openapi_client.rest import ApiException
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.DatabasesApi(api_client)
    id = 'id_example'
    
    try:
        api_response: DBDetails = api_instance.get_database(id)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DBDetails**](DBDetails.md)

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
**404** | Database not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_databases**
> DBsDetails get_list_databases()

Get all databases

get all databases that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.rest import ApiException
from dbaas.openapi_client.models.dbs_details import DBsDetails
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.DatabasesApi(api_client)
    
    try:
        api_response: DBsDetails = api_instance.get_list_databases()
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters
This endpoint does not need any parameter.

### Return type

[**DBsDetails**](DBsDetails.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resize_database**
> resize_database(id, resize)

Resize a database

resize a database that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.models.resize_database_request import ResizeDatabaseRequest
from dbaas.openapi_client.rest import ApiException
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.DatabasesApi(api_client)
    id = 'id_example' 
    resize: ResizeDatabaseRequest = dbaas.openapi_client.ResizeDatabaseRequest(
        disk = True,
        planID = "planID_example",
    )
    
    try:
        api_instance.resize_database(id, resize)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **resize** | [**ResizeDatabaseRequest**](ResizeDatabaseRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | Database not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **turn_database**
> turn_database(id, scale)

Power on or power off a database

power on or power off a database that user owns

### Example

* Api Key Authentication (jwt):
```python
import dbaas.openapi_client
from dbaas.openapi_client.models.turn_database_request import TurnDatabaseRequest
from dbaas.openapi_client.rest import ApiException
from pprint import pprint

with dbaas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = dbaas.openapi_client.DatabasesApi(api_client)
    id = 'id_example'
    scale: TurnDatabaseRequest = dbaas.openapi_client.TurnDatabaseRequest(
        scale = 1
    )
    
    try:
        api_instance.turn_database(id, scale)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **scale** | [**TurnDatabaseRequest**](TurnDatabaseRequest.md)| 1 for power on or 0 for power off | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | Database not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

