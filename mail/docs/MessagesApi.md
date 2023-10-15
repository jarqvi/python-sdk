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
import time
import os
import openapi_client
from openapi_client.models.tmp_access import TmpAccess
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
    api_instance = openapi_client.MessagesApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    message_id = 'message_id_example' # str | 
    expiration = 1 # float | Specifying hourly expiration schedule options (optional) (default to 1)

    try:
        # generate temporary access to email html
        api_response = api_instance.generate_temporary(mail_server_id, message_id, expiration=expiration)
        print("The response of MessagesApi->generate_temporary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->generate_temporary: %s\n" % e)
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
import time
import os
import openapi_client
from openapi_client.models.mail_messages import MailMessages
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
    api_instance = openapi_client.MessagesApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    direction = 'direction_example' # str | 
    page = 1 # float |  (optional) (default to 1)
    count = 15 # float |  (optional) (default to 15)
    state = 'state_example' # str |  (optional)
    subject = 'subject_example' # str |  (optional)
    var_from = 'var_from_example' # str |  (optional)
    to = 'to_example' # str |  (optional)

    try:
        # get all mails
        api_response = api_instance.get_all_mails(mail_server_id, direction, page=page, count=count, state=state, subject=subject, var_from=var_from, to=to)
        print("The response of MessagesApi->get_all_mails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_all_mails: %s\n" % e)
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
import time
import os
import openapi_client
from openapi_client.models.get_single_mail200_response import GetSingleMail200Response
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
    api_instance = openapi_client.MessagesApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        # get single mail
        api_response = api_instance.get_single_mail(mail_server_id, message_id)
        print("The response of MessagesApi->get_single_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_single_mail: %s\n" % e)
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
import time
import os
import openapi_client
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
    api_instance = openapi_client.MessagesApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    message_id = 'message_id_example' # str | 
    token = 'token_example' # str | 

    try:
        # get single mail html
        api_instance.get_single_mail_html(mail_server_id, message_id, token)
    except Exception as e:
        print("Exception when calling MessagesApi->get_single_mail_html: %s\n" % e)
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
import time
import os
import openapi_client
from openapi_client.models.model3 import Model3
from openapi_client.models.post_mails201_response import PostMails201Response
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
    api_instance = openapi_client.MessagesApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    body = openapi_client.Model3() # Model3 |  (optional)

    try:
        # send a mail
        api_response = api_instance.send_mail(mail_server_id, body=body)
        print("The response of MessagesApi->send_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->send_mail: %s\n" % e)
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

