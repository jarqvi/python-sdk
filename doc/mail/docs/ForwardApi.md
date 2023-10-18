# openapi_client.ForwardApi

All URIs are relative to *https://mail-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address_forwarding**](ForwardApi.md#create_address_forwarding) | **POST** /api/v1/mails/{mailServerID}/accounts/{accountID}/forwards | add address endpoint to forwarding mails
[**delete_extra_endpoint**](ForwardApi.md#delete_extra_endpoint) | **DELETE** /api/v1/mails/{mailServerID}/accounts/{accountID}/forwards/{addressID} | delete extra endpoint address
[**get_list_address_forwarding**](ForwardApi.md#get_list_address_forwarding) | **GET** /api/v1/mails/{mailServerID}/accounts/{accountID}/forwards | get all extra address to forwarding mails


# **create_address_forwarding**
> PostMails201Response create_address_forwarding(mail_server_id, account_id, body=body)

add address endpoint to forwarding mails

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.model6 import Model6
from mail.openapi_client.models.post_mails201_response import PostMails201Response
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.ForwardApi(api_client)
    mail_server_id = 'mail_server_id_example'
    account_id = 'account_id_example' 
    body: Model6 = mail.openapi_client.Model6(address = 'example_address')

    try:
        api_response: PostMails201Response = api_instance.create_address_forwarding(mail_server_id, account_id, body=body)       
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **account_id** | **str**|  | 
 **body** | [**Model6**](Model6.md)|  | [optional] 

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
**403** | Max number of forwarders |  -  |
**404** | Mail Server or Mail Account not found |  -  |
**409** | Address endpoint already exists |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_extra_endpoint**
> delete_extra_endpoint(mail_server_id, account_id, address_id)

delete extra endpoint address

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.ForwardApi(api_client)
    mail_server_id = 'mail_server_id_example'
    account_id = 'account_id_example'
    address_id = 'address_id_example'

    try:
        api_instance.delete_extra_endpoint(mail_server_id, account_id, address_id)  
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **account_id** | **str**|  | 
 **address_id** | **str**|  | 

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
**404** | Mail Server or Mail Account or Mail Forward not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_address_forwarding**
> MailForwards get_list_address_forwarding(mail_server_id, account_id)

get all extra address to forwarding mails

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.mail_forwards import MailForwards
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.ForwardApi(api_client)
    mail_server_id = 'mail_server_id_example' 
    account_id = 'account_id_example'
    
    try:
        api_response: MailForwards = api_instance.get_list_address_forwarding(mail_server_id, account_id)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **account_id** | **str**|  | 

### Return type

[**MailForwards**](MailForwards.md)

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
**404** | Mail Server or Mail Account not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

