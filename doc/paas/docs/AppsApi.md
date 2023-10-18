# openapi_client.AppsApi

All URIs are relative to *https://api.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_plan**](AppsApi.md#change_plan) | **POST** /v1/projects/{name}/resize | Change plan
[**create_app**](AppsApi.md#create_app) | **POST** /v1/projects | Create a app
[**delete_app_by_name**](AppsApi.md#delete_app_by_name) | **DELETE** /v1/projects/{name} | Delete a app
[**get_app_applets**](AppsApi.md#get_app_applets) | **GET** /v1/projects/{name}/applets | Get applets of app
[**get_app_by_name**](AppsApi.md#get_app_by_name) | **GET** /v1/projects/{name} | Get details of a project
[**get_app_logs**](AppsApi.md#get_app_logs) | **GET** /v1/projects/{name}/logs | Get logs of app
[**get_app_releases**](AppsApi.md#get_app_releases) | **GET** /v1/projects/{name}/releases | Get releases of app
[**get_apps**](AppsApi.md#get_apps) | **GET** /v1/projects | Get details of all projects
[**restart_app**](AppsApi.md#restart_app) | **POST** /v1/projects/{name}/actions/restart | To restart a app
[**turn_app**](AppsApi.md#turn_app) | **POST** /v1/projects/{name}/actions/scale | Turn on or off a app


# **change_plan**
> change_plan(name, plan)

Change plan

create app that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.change_plan_request import ChangePlanRequest
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.AppsApi(api_client)
    name = 'name_example'
    plan: ChangePlanRequest = paas.openapi_client.ChangePlanRequest(plan_id = 'plan_id_example')

    try:
        api_instance.change_plan(name, plan)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 
 **plan** | [**ChangePlanRequest**](ChangePlanRequest.md)| The plan of your app | 

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
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app**
> create_app(create_app)

Create a app

create app that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.create_app import CreateApp
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.AppsApi(api_client)
    create_app: CreateApp = paas.openapi_client.CreateApp(name = 'name_example', plan_id= 'plan_id_example', platform = 'platform_example')

    try:
        api_instance.create_app(create_app)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_app** | [**CreateApp**](CreateApp.md)|  | 

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
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_by_name**
> delete_app_by_name(name)

Delete a app

delete app that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.AppsApi(api_client)
    name = 'name_example' 
    
    try:
        api_instance.delete_app_by_name(name)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the app to delete | 

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
**200** | Your request has been submitted. |  -  |
**204** | App deleted. |  -  |
**401** | Missing authentication |  -  |
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_applets**
> Applets get_app_applets(name)

Get applets of app

get applets of app that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.applets import Applets
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.AppsApi(api_client)
    name = 'name_example'
    
    try:
        api_response: Applets = api_instance.get_app_applets(name)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 

### Return type

[**Applets**](Applets.md)

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

# **get_app_by_name**
> ProjectAllDetails get_app_by_name(name)

Get details of a project

get all details of all project that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.project_all_details import ProjectAllDetails
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.AppsApi(api_client)
    name = 'name_example'
    
    try:
        api_response: ProjectAllDetails = api_instance.get_app_by_name(name)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 

### Return type

[**ProjectAllDetails**](ProjectAllDetails.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Missing authentication |  -  |
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_logs**
> List[LogsInner] get_app_logs(name, since)

Get logs of app

get logs of app that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.logs_inner import LogsInner
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.AppsApi(api_client)
    name = 'name_example'
    since = 'since_example'
    
    try:
        api_response: LogsInner = api_instance.get_app_logs(name, since)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 
 **since** | **str**| Show logs since timestamp | 

### Return type

[**List[LogsInner]**](LogsInner.md)

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

# **get_app_releases**
> Releases get_app_releases(name, page, count)

Get releases of app

get releases of app that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.releases import Releases
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.AppsApi(api_client)
    name = 'name_example'
    page = 1.0
    count = 10.0 
    
    try:
        api_response: Releases = api_instance.get_app_releases(name, page, count)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app | 
 **page** | **float**| The page of your releases | [default to 1.0]
 **count** | **float**| The count of your releases | [default to 10.0]

### Return type

[**Releases**](Releases.md)

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

# **get_apps**
> Projects get_apps()

Get details of all projects

get all details of all projects that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.projects import Projects
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.AppsApi(api_client)
    try:
        api_response: Projects = api_instance.get_apps()
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Projects**](Projects.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Missing authentication |  -  |
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_app**
> restart_app(name)

To restart a app

to restart app that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.AppsApi(api_client)
    name = 'name_example'
    
    try:
        api_instance.restart_app(name)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the app to restart | 

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
**200** | Your request has been submitted. |  -  |
**401** | Missing authentication |  -  |
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **turn_app**
> turn_app(name, scale)

Turn on or off a app

turn on or off a app that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.turn_app_request import TurnAppRequest
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.AppsApi(api_client)
    name = 'name_example'
    scale: TurnAppRequest = paas.openapi_client.TurnAppRequest()
    
    try:
        api_instance.turn_app(name, scale)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the app to turn on or off | 
 **scale** | [**TurnAppRequest**](TurnAppRequest.md)| Return 1 to turn on or 0 to turn off | 

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
**200** | Your request has been submitted. |  -  |
**401** | Missing authentication |  -  |
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

