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
    api_instance = openapi_client.SmtpApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    username = 'username_example' # str | 

    try:
        # delete smtp credential
        api_instance.delete_smtp_credential(mail_server_id, username)
    except Exception as e:
        print("Exception when calling SmtpApi->delete_smtp_credential: %s\n" % e)
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
import time
import os
import openapi_client
from openapi_client.models.create_smtp import CreateSMTP
from openapi_client.models.model4 import Model4
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
    api_instance = openapi_client.SmtpApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    body = openapi_client.Model4() # Model4 |  (optional)

    try:
        # generate credentials to connet mail server with SMTP
        api_response = api_instance.generate_credentials(mail_server_id, body=body)
        print("The response of SmtpApi->generate_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmtpApi->generate_credentials: %s\n" % e)
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
import time
import os
import openapi_client
from openapi_client.models.smtp import SMTP
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
    api_instance = openapi_client.SmtpApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 

    try:
        # get credential to connect to mail server with SMTP
        api_response = api_instance.get_credential(mail_server_id)
        print("The response of SmtpApi->get_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmtpApi->get_credential: %s\n" % e)
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
import time
import os
import openapi_client
from openapi_client.models.create_smtp import CreateSMTP
from openapi_client.models.model9 import Model9
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
    api_instance = openapi_client.SmtpApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    body = openapi_client.Model9() # Model9 |  (optional)

    try:
        # revoke credentials to connect mail server with SMTP
        api_response = api_instance.revoke_credentials(mail_server_id, body=body)
        print("The response of SmtpApi->revoke_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmtpApi->revoke_credentials: %s\n" % e)
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

