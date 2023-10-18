# openapi_client.AccountsApi

All URIs are relative to *https://mail-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_mail_available**](AccountsApi.md#check_mail_available) | **GET** /api/v1/mails/{mailServerID}/accounts/{accountName}/check-availability | check if mail account is available
[**create_mail_a_ccount**](AccountsApi.md#create_mail_a_ccount) | **POST** /api/v1/mails/{mailServerID}/accounts | add mail account
[**delete_mail_account**](AccountsApi.md#delete_mail_account) | **DELETE** /api/v1/mails/{mailServerID}/accounts/{accountID} | delete mail account
[**get_all_mail_accounts**](AccountsApi.md#get_all_mail_accounts) | **GET** /api/v1/mails/{mailServerID}/accounts | get all mail accounts


# **check_mail_available**
> PostMails201Response check_mail_available(mail_server_id, account_name)

check if mail account is available

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.post_mails201_response import PostMails201Response
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.AccountsApi(api_client)
    mail_server_id = 'mail_server_id_example' 
    account_name = 'account_name_example' 

    try:
        api_response: PostMails201Response = api_instance.check_mail_available(mail_server_id, account_name)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **account_name** | **str**|  | 

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
**404** | Mail Server not found |  -  |
**409** | Account already taken. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mail_a_ccount**
> PostMails201Response create_mail_a_ccount(mail_server_id, body=body)

add mail account

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.model5 import Model5
from mail.openapi_client.models.post_mails201_response import PostMails201Response
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.AccountsApi(api_client)
    mail_server_id = 'mail_server_id_example'
    body: Model5 = mail.openapi_client.Model5(name = 'name_example')

    try:
        api_response: PostMails201Response = api_instance.create_mail_a_ccount(mail_server_id, body=body)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **body** | [**Model5**](Model5.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**404** | Mail Server not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mail_account**
> delete_mail_account(mail_server_id, account_id)

delete mail account

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.AccountsApi(api_client)
    mail_server_id = 'mail_server_id_example'
    account_id = 'account_id_example'

    try:
        api_instance.delete_mail_account(mail_server_id, account_id)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **account_id** | **str**|  | 

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
**404** | Mail Server or Mail Account not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_mail_accounts**
> MailAccounts get_all_mail_accounts(mail_server_id)

get all mail accounts

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.mail_accounts import MailAccounts
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.AccountsApi(api_client)
    mail_server_id = 'mail_server_id_example'

    try:
        api_response: MailAccounts = api_instance.get_all_mail_accounts(mail_server_id)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 

### Return type

[**MailAccounts**](MailAccounts.md)

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

