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
import time
import os
import openapi_client
from openapi_client.models.deploy_releases import DeployReleases
from openapi_client.models.releases_deploy200_response import ReleasesDeploy200Response
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
    api_instance = openapi_client.DeployApi(api_client)
    name = 'name_example' # str | The name of your app for deploy
    deploy_releases = openapi_client.DeployReleases() # DeployReleases | 

    try:
        # Deploy releases
        api_response = api_instance.releases_deploy(name, deploy_releases)
        print("The response of DeployApi->releases_deploy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeployApi->releases_deploy: %s\n" % e)
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
import time
import os
import openapi_client
from openapi_client.models.sources_deploy200_response import SourcesDeploy200Response
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
    api_instance = openapi_client.DeployApi(api_client)
    name = 'name_example' # str | The name of your app for deploy
    file = None # bytearray | The .gz file to deploy

    try:
        # Deploy sources code
        api_response = api_instance.sources_deploy(name, file)
        print("The response of DeployApi->sources_deploy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeployApi->sources_deploy: %s\n" % e)
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

