# openapi_client.MessagesApi

All URIs are relative to *https://mail-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_temporary**](MessagesApi.md#generate_temporary) | **POST** /api/v1/mails/{mailServerID}/messages/{messageID}/temporary-access | generate temporary access to email html
[**get_all_mails**](MessagesApi.md#get_all_mails) | **GET** /api/v1/mails/{mailServerID}/messages | get all mails
[**get_single_mail**](MessagesApi.md#get_single_mail) | **GET** /api/v1/mails/{mailServerID}/messages/{messageID} | get single mail
[**get_single_mail_html**](MessagesApi.md#get_single_mail_html) | **GET** /api/v1/mails/{mailServerID}/messages/{messageID}/render | get single mail html
[**send_mail**](MessagesApi.md#send_mail) | **POST** /api/v1/mails/{mailServerID}/messages | send a mail


# **generate_temporary**
> TmpAccess generate_temporary(mail_server_id, message_id, expiration=expiration)

generate temporary access to email html

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.tmp_access import TmpAccess
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.MessagesApi(api_client)
    mail_server_id = 'mail_server_id_example'
    message_id = 'message_id_example'
    expiration = 1

    try:
        api_response: TmpAccess = api_instance.generate_temporary(mail_server_id, message_id, expiration=expiration)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **message_id** | **str**|  | 
 **expiration** | **float**| Specifying hourly expiration schedule options | [optional] [default to 1]

### Return type

[**TmpAccess**](TmpAccess.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Generate token limitation |  -  |
**404** | Mail Server or Mail Message not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_mails**
> MailMessages get_all_mails(mail_server_id, direction, page=page, count=count, state=state, subject=subject, var_from=var_from, to=to)

get all mails

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.mail_messages import MailMessages
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.MessagesApi(api_client)
    mail_server_id = 'mail_server_id_example'
    direction = 'direction_example'
    page = 1
    count = 15
    state = 'state_example'
    subject = 'subject_example'
    var_from = 'var_from_example'
    to = 'to_example'

    try:
        api_response: MailMessages = api_instance.get_all_mails(mail_server_id, direction, page=page, count=count, state=state, subject=subject, var_from=var_from, to=to)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **direction** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **count** | **float**|  | [optional] [default to 15]
 **state** | **str**|  | [optional] 
 **subject** | **str**|  | [optional] 
 **var_from** | **str**|  | [optional] 
 **to** | **str**|  | [optional] 

### Return type

[**MailMessages**](MailMessages.md)

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

# **get_single_mail**
> GetSingleMail200Response get_single_mail(mail_server_id, message_id)

get single mail

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.get_single_mail200_response import GetSingleMail200Response
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.MessagesApi(api_client)
    mail_server_id = 'mail_server_id_example' 
    message_id = 'message_id_example'

    try:
        api_response: GetSingleMail200Response = api_instance.get_single_mail(mail_server_id, message_id)
        
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

[**GetSingleMail200Response**](GetSingleMail200Response.md)

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

# **get_single_mail_html**
> get_single_mail_html(mail_server_id, message_id, token)

get single mail html

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.MessagesApi(api_client)
    mail_server_id = 'mail_server_id_example'
    message_id = 'message_id_example'
    token = 'token_example'

    try:
        api_instance.get_single_mail_html(mail_server_id, message_id, token)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **message_id** | **str**|  | 
 **token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success and returns some html text |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Mail Server or Mail Message not found |  -  |
**409** | Account already taken. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_mail**
> PostMails201Response send_mail(mail_server_id, body=body)

send a mail

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.post_mails201_response import PostMails201Response
from mail.openapi_client.models.model3 import Model3
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.MessagesApi(api_client)
    mail_server_id = 'mail_server_id_example'
    body: Model3 = mail.openapi_client.Model3(
        html = 'html_example',
        text = 'text_example',
        subject = 'subject_example',
        to = 'to_example',
        var_from = 'var_from_example',
        reply_to = 'reply_to_example',
        attachments = {
            "name" : "name_example",
            "content_type": "content_type_example",
            "data": "data_example"
        }
    )

    try:
        api_response: PostMails201Response = api_instance.send_mail(mail_server_id, body=body)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **body** | [**Model3**](Model3.md)|  | [optional] 

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
**403** | No valid dns records exists for this mail server |  -  |
**404** | Mail Server not found |  -  |
**406** | The source and destination addresses must not be the same |  -  |
**429** | Too mnay requests |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

