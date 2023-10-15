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
import time
import os
import openapi_client
from openapi_client.models.download_attachments200_response import DownloadAttachments200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mail-service.iran.liara.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mail-service.iran.liara.ir"
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
    api_instance = openapi_client.AttachmentsApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    message_id = 'message_id_example' # str | 
    attachment_id = 'attachment_id_example' # str | 

    try:
        # download attachment
        api_response = api_instance.download_attachments(mail_server_id, message_id, attachment_id)
        print("The response of AttachmentsApi->download_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->download_attachments: %s\n" % e)
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
import time
import os
import openapi_client
from openapi_client.models.mail_attachments import MailAttachments
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://mail-service.iran.liara.ir
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mail-service.iran.liara.ir"
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
    api_instance = openapi_client.AttachmentsApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        # get all attachments for message
        api_response = api_instance.get_all_attachments(mail_server_id, message_id)
        print("The response of AttachmentsApi->get_all_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->get_all_attachments: %s\n" % e)
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

