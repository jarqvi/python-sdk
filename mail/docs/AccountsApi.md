# openapi_client.AccountsApi

All URIs are relative to *https://mail-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_mail_available**](AccountsApi.md#check_mail_available) | **GET** /api/v1/mails/{mailServerID}/accounts/{accountName}/check-availability | check if mail account is available
[**create_mail_a_ccount**](AccountsApi.md#create_mail_a_ccount) | **POST** /api/v1/mails/{mailServerID}/accounts | add mail account
[**delete_mail_account**](AccountsApi.md#delete_mail_account) | **DELETE** /api/v1/mails/{mailServerID}/accounts/{accountID} | delete mail account
[**get_all_mail_accounts**](AccountsApi.md#get_all_mail_accounts) | **GET** /api/v1/mails/{mailServerID}/accounts | get all mail accounts


# **check_mail_available**
> PostMails201Response check_mail_available(mail_server_id, account_name)

check if mail account is available

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.AccountsApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    account_name = 'account_name_example' # str | 

    try:
        # check if mail account is available
        api_response = api_instance.check_mail_available(mail_server_id, account_name)
        print("The response of AccountsApi->check_mail_available:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->check_mail_available: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **account_name** | **str**|  | 

### Return type

[**PostMails201Response**](PostMails201Response.md)

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
**409** | Account already taken. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mail_a_ccount**
> PostMails201Response create_mail_a_ccount(mail_server_id, body=body)

add mail account

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.model5 import Model5
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
    api_instance = openapi_client.AccountsApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    body = openapi_client.Model5() # Model5 |  (optional)

    try:
        # add mail account
        api_response = api_instance.create_mail_a_ccount(mail_server_id, body=body)
        print("The response of AccountsApi->create_mail_a_ccount:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->create_mail_a_ccount: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **body** | [**Model5**](Model5.md)|  | [optional] 

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

# **delete_mail_account**
> delete_mail_account(mail_server_id, account_id)

delete mail account

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
    api_instance = openapi_client.AccountsApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    account_id = 'account_id_example' # str | 

    try:
        # delete mail account
        api_instance.delete_mail_account(mail_server_id, account_id)
    except Exception as e:
        print("Exception when calling AccountsApi->delete_mail_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 
 **account_id** | **str**|  | 

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
**404** | Mail Server or Mail Account not found |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_mail_accounts**
> MailAccounts get_all_mail_accounts(mail_server_id)

get all mail accounts

### Example

* Api Key Authentication (jwt):
```python
import time
import os
import openapi_client
from openapi_client.models.mail_accounts import MailAccounts
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
    api_instance = openapi_client.AccountsApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 

    try:
        # get all mail accounts
        api_response = api_instance.get_all_mail_accounts(mail_server_id)
        print("The response of AccountsApi->get_all_mail_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_all_mail_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mail_server_id** | **str**|  | 

### Return type

[**MailAccounts**](MailAccounts.md)

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

