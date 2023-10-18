# openapi_client.DomainsApi

All URIs are relative to *https://api.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_domain**](DomainsApi.md#check_domain) | **GET** /v1/domains/{id}/check | Check a domain
[**create_app_domain**](DomainsApi.md#create_app_domain) | **POST** /v1/domains | Create a domain
[**delete_domain**](DomainsApi.md#delete_domain) | **DELETE** /v1/domains/{id} | Delete a domain
[**disable_ssl**](DomainsApi.md#disable_ssl) | **POST** /v1/domains/{id}/ssl/disable | Disable ssl
[**enable_ssl**](DomainsApi.md#enable_ssl) | **POST** /v1/domains/provision-ssl-certs | Enable ssl
[**get_app_domains**](DomainsApi.md#get_app_domains) | **GET** /v1/domains | Get all domains
[**redirect_domain**](DomainsApi.md#redirect_domain) | **POST** /v1/domains/{id}/set-redirect | Redirect a domain
[**set_app_domain**](DomainsApi.md#set_app_domain) | **POST** /v1/domains/set-project | Set a domain for project


# **check_domain**
> CheckDomain check_domain(id)

Check a domain

check a domain that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.check_domain import CheckDomain
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DomainsApi(api_client)
    id = 'id_example'
    
    try:
        api_response:CheckDomain = api_instance.check_domain(id)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of your domain | 

### Return type

[**CheckDomain**](CheckDomain.md)

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
**404** | Domain does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app_domain**
> CreateAppDomain201Response create_app_domain(domain)

Create a domain

create a domain that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.create_app_domain201_response import CreateAppDomain201Response
from paas.openapi_client.models.create_app_domain_request import CreateAppDomainRequest
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DomainsApi(api_client)
    domain: CreateAppDomainRequest = paas.openapi_client.CreateAppDomainRequest()
    domain.name = 'name_example'
    domain.project = 'project_example'
    domain.type = 'type_example'
    
    try:
        api_response:CreateAppDomain201Response = api_instance.create_app_domain(domain)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**CreateAppDomainRequest**](CreateAppDomainRequest.md)| The domain of your app | 

### Return type

[**CreateAppDomain201Response**](CreateAppDomain201Response.md)

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
**404** | App does not exists. |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain**
> delete_domain(id)

Delete a domain

delete a domain that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DomainsApi(api_client)
    id = 'id_example'
    
    try:
        api_instance.delete_domain(id)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of your domain | 

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
**404** | Domain does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_ssl**
> disable_ssl(id)

Disable ssl

disable ssl that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DomainsApi(api_client)
    id = 'id_example'
    
    try:
        api_instance.disable_ssl(id)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of your domain | 

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
**404** | Domain does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_ssl**
> EnableSsl200Response enable_ssl(domain)

Enable ssl

enable ssl that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.enable_ssl200_response import EnableSsl200Response
from paas.openapi_client.models.enable_ssl_request import EnableSslRequest
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DomainsApi(api_client)
    domain: EnableSslRequest = paas.openapi_client.EnableSslRequest()
    domain.domain = "example.com"
    
    try:
        api_response: EnableSsl200Response = api_instance.enable_ssl(domain)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**EnableSslRequest**](EnableSslRequest.md)| The domain of your app | 

### Return type

[**EnableSsl200Response**](EnableSsl200Response.md)

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
**404** | Domain does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_domains**
> Domains get_app_domains(project)

Get all domains

get all domains that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.domains import Domains
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DomainsApi(api_client)
    project = 'project_example'
    
    try:
        api_response: Domains = api_instance.get_app_domains(project)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The name of your app | 

### Return type

[**Domains**](Domains.md)

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

# **redirect_domain**
> redirect_domain(id, domain)

Redirect a domain

redirect a domain that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.redirect_domain_request import RedirectDomainRequest
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DomainsApi(api_client)
    id = 'id_example'
    domain: RedirectDomainRequest = paas.openapi_client.RedirectDomainRequest()
    domain.redirect_status = 302 # 301 or 302
    domain.redirect_to = 'example.com'
    
    try:
        api_instance.redirect_domain(id, domain)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of your domain | 
 **domain** | [**RedirectDomainRequest**](RedirectDomainRequest.md)| The domain of your app | 

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
**404** | Domain does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_app_domain**
> set_app_domain(domain)

Set a domain for project

set a domain for project that user owns

### Example

* Api Key Authentication (jwt):
```python
import paas.openapi_client
from paas.openapi_client.models.set_app_domain_request import SetAppDomainRequest
from paas.openapi_client.rest import ApiException
from pprint import pprint

with paas.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = paas.openapi_client.DomainsApi(api_client)
    domain: SetAppDomainRequest = paas.openapi_client.SetAppDomainRequest()
    domain.domain_id = 'example_domain_id'
    domain.project_id = 'example_project_id'
    
    try:
        api_instance.set_app_domain(domain)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**SetAppDomainRequest**](SetAppDomainRequest.md)| The domain of your app | 

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
**404** | App or domain does not exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

