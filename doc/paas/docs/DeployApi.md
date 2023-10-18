# openapi_client.DeployApi

All URIs are relative to *https://api.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**releases_deploy**](DeployApi.md#releases_deploy) | **POST** /v2/projects/{name}/releases | Deploy releases
[**sources_deploy**](DeployApi.md#sources_deploy) | **POST** /v2/projects/{name}/sources | Deploy sources code


# **releases_deploy**
> ReleasesDeploy200Response releases_deploy(name, deploy_releases)

Deploy releases

deploy releases that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.deploy_releases import DeployReleases
from paas.openapi_client.models.releases_deploy200_response import ReleasesDeploy200Response
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DeployApi(api_client)
    name = 'example_name'
    deploy_releases: DeployReleases = paas.openapi_client.DeployReleases()
    deploy_releases.source_id = 'example_source_id'
    deploy_releases.type = 'example_type'
    deploy_releases.port = 3000

    try:
        api_response: ReleasesDeploy200Response = api_instance.releases_deploy(name, deploy_releases)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app for deploy | 
 **deploy_releases** | [**DeployReleases**](DeployReleases.md)|  | 

### Return type

[**ReleasesDeploy200Response**](ReleasesDeploy200Response.md)

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

# **sources_deploy**
> SourcesDeploy200Response sources_deploy(name, file)

Deploy sources code

deploy sources code that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.sources_deploy200_response import SourcesDeploy200Response
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DeployApi(api_client)
    name = 'example'
    file = './example.tar.gz'

    try:
        api_response: SourcesDeploy200Response = api_instance.sources_deploy(name, file)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of your app for deploy | 
 **file** | **bytearray**| The .gz file to deploy | 

### Return type

[**SourcesDeploy200Response**](SourcesDeploy200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad request |  -  |
**401** | Missing authentication |  -  |
**404** | App does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

