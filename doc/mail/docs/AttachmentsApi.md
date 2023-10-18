# openapi_client.AttachmentsApi

All URIs are relative to *https://mail-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_attachments**](AttachmentsApi.md#download_attachments) | **GET** /api/v1/mails/{mailServerID}/messages/{messageID}/attachments/{attachmentID} | download attachment
[**get_all_attachments**](AttachmentsApi.md#get_all_attachments) | **GET** /api/v1/mails/{mailServerID}/messages/{messageID}/attachments | get all attachments for message


# **download_attachments**
> DownloadAttachments200Response download_attachments(mail_server_id, message_id, attachment_id)

download attachment

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.download_attachments200_response import DownloadAttachments200Response
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.AttachmentsApi(api_client)
    mail_server_id = 'mail_server_id_example'
    message_id = 'message_id_example'
    attachment_id = 'attachment_id_example'

    try:
        api_response: DownloadAttachments200Response = api_instance.download_attachments(mail_server_id, message_id, attachment_id)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **message_id** | **str**|  | 
 **attachment_id** | **str**|  | 

### Return type

[**DownloadAttachments200Response**](DownloadAttachments200Response.md)

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

# **get_all_attachments**
> MailAttachments get_all_attachments(mail_server_id, message_id)

get all attachments for message

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.mail_attachments import MailAttachments
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.AttachmentsApi(api_client)
    mail_server_id = 'mail_server_id_example' 
    message_id = 'message_id_example'

    try:
        api_response: MailAttachments = api_instance.get_all_attachments(mail_server_id, message_id)        
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

[**MailAttachments**](MailAttachments.md)

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
**409** | Account already taken. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

