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
import time
import os
import openapi_client
from openapi_client.models.mail_events import MailEvents
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
    api_instance = openapi_client.EventApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    message_id = 'message_id_example' # str | 
    page = 1 # float |  (optional) (default to 1)
    count = 15 # float |  (optional) (default to 15)

    try:
        # get all events for message
        api_response = api_instance.get_all_events(mail_server_id, message_id, page=page, count=count)
        print("The response of EventApi->get_all_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->get_all_events: %s\n" % e)
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

