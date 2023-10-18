# openapi_client.EventApi

All URIs are relative to *https://mail-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_events**](EventApi.md#get_all_events) | **GET** /api/v1/mails/{mailServerID}/messages/{messageID}/events | get all events for message


# **get_all_events**
> MailEvents get_all_events(mail_server_id, message_id, page=page, count=count)

get all events for message

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.mail_events import MailEvents
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.EventApi(api_client)
    mail_server_id = 'mail_server_id_example' 
    message_id = 'message_id_example' 
    page = 1 
    count = 15 

    try:
        api_response: MailEvents = api_instance.get_all_events(mail_server_id, message_id, page=page, count=count)        
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **message_id** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **count** | **float**|  | [optional] [default to 15]

### Return type

[**MailEvents**](MailEvents.md)

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
**404** | Mail Server or Mail Message not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

