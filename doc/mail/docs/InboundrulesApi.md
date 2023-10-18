# openapi_client.InboundrulesApi

All URIs are relative to *https://mail-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_inbound_rule**](InboundrulesApi.md#add_inbound_rule) | **POST** /api/v1/mails/{mailServerID}/inboundrules | add inbound rule.
[**delete_inbound_rule**](InboundrulesApi.md#delete_inbound_rule) | **DELETE** /api/v1/mail/{mailServerID}/inboundrules/{inboundruleID} | delete inbound rule.
[**get_all_inbound_rules**](InboundrulesApi.md#get_all_inbound_rules) | **GET** /api/v1/mails/{mailServerID}/inboundrules | get all inbound rules.


# **add_inbound_rule**
> PostMails201Response add_inbound_rule(mail_server_id, model11=model11)

add inbound rule.

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.model11 import Model11
from mail.openapi_client.models.post_mails201_response import PostMails201Response
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.InboundrulesApi(api_client)
    mail_server_id = 'mail_server_id_example' 
    model11: Model11 = mail.openapi_client.Model11(rule = 'rule_example')
    
    try:
        api_response: PostMails201Response = api_instance.add_inbound_rule(mail_server_id, model11=model11)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **model11** | [**Model11**](Model11.md)|  | [optional] 

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

# **delete_inbound_rule**
> delete_inbound_rule(mail_server_id, inboundrule_id)

delete inbound rule.

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.InboundrulesApi(api_client)
    mail_server_id = 'mail_server_id_example'
    inboundrule_id = 'inboundrule_id_example'
    
    try:
        api_instance.delete_inbound_rule(mail_server_id, inboundrule_id)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **inboundrule_id** | **str**|  | 

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
**404** | Mail Server or Inbound rule not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_inbound_rules**
> MailInboundRules get_all_inbound_rules(mail_server_id)

get all inbound rules.

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.mail_inbound_rules import MailInboundRules
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.InboundrulesApi(api_client)
    mail_server_id = 'mail_server_id_example'
    
    try:
        api_response: MailInboundRules = api_instance.get_all_inbound_rules(mail_server_id)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 

### Return type

[**MailInboundRules**](MailInboundRules.md)

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
**409** | Rule already exists. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

