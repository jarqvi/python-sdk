# openapi_client.MailsApi

All URIs are relative to *https://mail-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_mail_server_plan**](MailsApi.md#change_mail_server_plan) | **PUT** /api/v1/mails/{mailServerID}/plans | change mail server plan
[**check_domain_available**](MailsApi.md#check_domain_available) | **GET** /api/v1/mails/{domain}/check-availability | check if domain name is available
[**check_mail_server_dns_status**](MailsApi.md#check_mail_server_dns_status) | **GET** /api/v1/mails/{mailServerID}/dns-check | mail server check dns status
[**delete_mail_server**](MailsApi.md#delete_mail_server) | **DELETE** /api/v1/mails/{mailServerID} | delete mail server
[**edit_mail_server**](MailsApi.md#edit_mail_server) | **PATCH** /api/v1/mails/{mailServerID} | edit mail server
[**get_count_free_mails**](MailsApi.md#get_count_free_mails) | **GET** /api/v1/mails/{mailServerID}/remaining-free-emails | count number of free mails every month
[**get_count_mails**](MailsApi.md#get_count_mails) | **GET** /api/v1/mails/{mailServerID}/counts | count number of sent mails every day
[**get_mails**](MailsApi.md#get_mails) | **GET** /api/v1/mails | get all mail servers
[**get_single_mail_server**](MailsApi.md#get_single_mail_server) | **GET** /api/v1/mails/{mailServerID} | get single mail server
[**post_mails**](MailsApi.md#post_mails) | **POST** /api/v1/mails | create mail server


# **change_mail_server_plan**
> PostMails201Response change_mail_server_plan(mail_server_id, body=body)

change mail server plan

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.model10 import Model10
from mail.openapi_client.models.post_mails201_response import PostMails201Response
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.MailsApi(api_client)
    mail_server_id = 'mail_server_id_example'
    body: Model10 = mail.openapi_client.Model10(plan = 'plan_example')
    
    try:
        api_response = api_instance.change_mail_server_plan(mail_server_id, body=body)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **body** | [**Model10**](Model10.md)|  | [optional] 

### Return type

[**PostMails201Response**](PostMails201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Mail Server or Mail Account not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_domain_available**
> PostMails201Response check_domain_available(domain)

check if domain name is available

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.post_mails201_response import PostMails201Response
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.MailsApi(api_client)
    domain = 'domain_example'
    
    try:
        api_response: PostMails201Response = api_instance.check_domain_available(domain)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | 

### Return type

[**PostMails201Response**](PostMails201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_mail_server_dns_status**
> CheckDNS check_mail_server_dns_status(mail_server_id)

mail server check dns status

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.check_dns import CheckDNS
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.MailsApi(api_client)
    mail_server_id = 'mail_server_id_example'
    
    try:
        api_response: CheckDNS = api_instance.check_mail_server_dns_status(mail_server_id)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 

### Return type

[**CheckDNS**](CheckDNS.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Mail Server not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mail_server**
> delete_mail_server(mail_server_id)

delete mail server

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.MailsApi(api_client)
    mail_server_id = 'mail_server_id_example'
    
    try:
        api_instance.delete_mail_server(mail_server_id)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 

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
**204** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Mail Server not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_mail_server**
> PostMails201Response edit_mail_server(mail_server_id, body=body)

edit mail server

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.mode`ls.model8 import Model8
from mail.openapi_client.models.post_mails201_response import PostMails201Response
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.MailsApi(api_client)
    mail_server_id = 'mail_server_id_example'
    body: Model8 = mail.openapi_client.Model8(mode = 'dev', inboundSpamThreshold = 0)
    
    try:
        api_response: PostMails201Response = api_instance.edit_mail_server(mail_server_id, body=body)
        
        pprint(api_response)
    except ApiException as e:
        print(e)`

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **body** | [**Model8**](Model8.md)|  | [optional] 

### Return type

[**PostMails201Response**](PostMails201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Mail Server not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_free_mails**
> RemainingFreeMails get_count_free_mails(mail_server_id)

count number of free mails every month

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.remaining_free_mails import RemainingFreeMails
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.MailsApi(api_client)
    mail_server_id = 'mail_server_id_example'
    
    try:
        api_response: RemainingFreeMails = api_instance.get_count_free_mails(mail_server_id)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 

### Return type

[**RemainingFreeMails**](RemainingFreeMails.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Mail Server not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_count_mails**
> CountMailPerDay get_count_mails(mail_server_id, last_n_days=last_n_days)

count number of sent mails every day

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.count_mail_per_day import CountMailPerDay
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.MailsApi(api_client)
    mail_server_id = 'mail_server_id_example' 
    last_n_days = 30 
    
    try:
        api_response: CountMailPerDay = api_instance.get_count_mails(mail_server_id, last_n_days=last_n_days)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **last_n_days** | **float**|  | [optional] [default to 30]

### Return type

[**CountMailPerDay**](CountMailPerDay.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Mail Server not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mails**
> MailServers get_mails()

get all mail servers

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.mail_servers import MailServers
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.MailsApi(api_client)

    try:
        api_response: MailServers = api_instance.get_mails()
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters
This endpoint does not need any parameter.

### Return type

[**MailServers**](MailServers.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_mail_server**
> MailServer get_single_mail_server(mail_server_id)

get single mail server

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.mail_server import MailServer
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.MailsApi(api_client)
    mail_server_id = 'mail_server_id_example'
    
    try:
        api_response: MailServer = api_instance.get_single_mail_server(mail_server_id)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 

### Return type

[**MailServer**](MailServer.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Mail Server not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_mails**
> PostMails201Response post_mails(body=body)

create mail server

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.model1 import Model1
from mail.openapi_client.models.post_mails201_response import PostMails201Response
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.MailsApi(api_client)
    body: Model1 = mail.openapi_client.Model1(plan = 'plan_example', domain = 'domain_example', mode = 'DEV')
    
    try:
        api_response: PostMails201Response = api_instance.post_mails(body=body)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model1**](Model1.md)|  | [optional] 

### Return type

[**PostMails201Response**](PostMails201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Invalid request for plan |  -  |
**402** | Not enough balance |  -  |
**403** | Allowed to create only one Mail Server on the free plan |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

