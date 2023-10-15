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
import time
import os
import openapi_client
from openapi_client.models.model11 import Model11
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
    api_instance = openapi_client.InboundrulesApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    model11 = openapi_client.Model11() # Model11 |  (optional)

    try:
        # add inbound rule.
        api_response = api_instance.add_inbound_rule(mail_server_id, model11=model11)
        print("The response of InboundrulesApi->add_inbound_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundrulesApi->add_inbound_rule: %s\n" % e)
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
    api_instance = openapi_client.InboundrulesApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 
    inboundrule_id = 'inboundrule_id_example' # str | 

    try:
        # delete inbound rule.
        api_instance.delete_inbound_rule(mail_server_id, inboundrule_id)
    except Exception as e:
        print("Exception when calling InboundrulesApi->delete_inbound_rule: %s\n" % e)
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
import time
import os
import openapi_client
from openapi_client.models.mail_inbound_rules import MailInboundRules
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
    api_instance = openapi_client.InboundrulesApi(api_client)
    mail_server_id = 'mail_server_id_example' # str | 

    try:
        # get all inbound rules.
        api_response = api_instance.get_all_inbound_rules(mail_server_id)
        print("The response of InboundrulesApi->get_all_inbound_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InboundrulesApi->get_all_inbound_rules: %s\n" % e)
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

