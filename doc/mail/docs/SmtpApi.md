# openapi_client.SmtpApi

All URIs are relative to *https://mail-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_smtp_credential**](SmtpApi.md#delete_smtp_credential) | **DELETE** /api/v1/mails/{mailServerID}/smtp-credentials/{username} | delete smtp credential
[**generate_credentials**](SmtpApi.md#generate_credentials) | **POST** /api/v1/mails/{mailServerID}/smtp-credentials | generate credentials to connet mail server with SMTP
[**get_credential**](SmtpApi.md#get_credential) | **GET** /api/v1/mails/{mailServerID}/smtp-credentials | get credential to connect to mail server with SMTP
[**revoke_credentials**](SmtpApi.md#revoke_credentials) | **PATCH** /api/v1/mails/{mailServerID}/smtp-credentials | revoke credentials to connect mail server with SMTP


# **delete_smtp_credential**
> delete_smtp_credential(mail_server_id, username)

delete smtp credential

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.SmtpApi(api_client)
    mail_server_id = 'mail_server_id_example'
    username = 'username_example'

    try:
        api_instance.delete_smtp_credential(mail_server_id, username)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **username** | **str**|  | 

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
**404** | Mail Server or SMTP Credential not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_credentials**
> CreateSMTP generate_credentials(mail_server_id, body=body)

generate credentials to connet mail server with SMTP

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.create_smtp import CreateSMTP
from mail.openapi_client.models.model4 import Model4
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.SmtpApi(api_client)
    mail_server_id = 'mail_server_id_example'
    body: Model4 = mail.openapi_client.Model4(description = "description_example")

    try:
        api_response: CreateSMTP = api_instance.generate_credentials(mail_server_id, body=body)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **body** | [**Model4**](Model4.md)|  | [optional] 

### Return type

[**CreateSMTP**](CreateSMTP.md)

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
**403** | Allowed to create only 10 smtp credentials |  -  |
**404** | Mail Server not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credential**
> SMTP get_credential(mail_server_id)

get credential to connect to mail server with SMTP

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.smtp import SMTP
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.SmtpApi(api_client)
    mail_server_id = 'mail_server_id_example'

    try:
        api_response: SMTP = api_instance.get_credential(mail_server_id)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 

### Return type

[**SMTP**](SMTP.md)

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

# **revoke_credentials**
> CreateSMTP revoke_credentials(mail_server_id, body=body)

revoke credentials to connect mail server with SMTP

### Example

* Api Key Authentication (jwt):
```python
import mail.openapi_client
from mail.openapi_client.models.create_smtp import CreateSMTP
from mail.openapi_client.models.model9 import Model9
from mail.openapi_client.rest import ApiException
from pprint import pprint

with mail.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = mail.openapi_client.SmtpApi(api_client)
    mail_server_id = 'mail_server_id_example' 
    body: Model9 = mail.openapi_client.Model9(username = 'username_example')

    try:
        api_response: CreateSMTP = api_instance.revoke_credentials(mail_server_id, body=body)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **body** | [**Model9**](Model9.md)|  | [optional] 

### Return type

[**CreateSMTP**](CreateSMTP.md)

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
**404** | Mail Server or Username not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

