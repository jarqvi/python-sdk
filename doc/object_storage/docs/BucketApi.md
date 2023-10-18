# openapi_client.BucketApi

All URIs are relative to *https://storage-service.iran.liara.ir*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_bucket_access**](BucketApi.md#change_bucket_access) | **PATCH** /api/v1/buckets/{bucket}/type/{permission} | change Bucket Access Policy
[**check_bucket**](BucketApi.md#check_bucket) | **GET** /api/v1/buckets/{bucket}/check-availability | Check Bucket availability
[**create_bucket**](BucketApi.md#create_bucket) | **POST** /api/v1/buckets | Create Bucket
[**destroy_bucket**](BucketApi.md#destroy_bucket) | **DELETE** /api/v1/buckets/{bucket} | Destroy Bucket
[**get_buckets**](BucketApi.md#get_buckets) | **GET** /api/v1/buckets | List all Buckets
[**get_list_previous_buckets**](BucketApi.md#get_list_previous_buckets) | **GET** /api/v1/buckets/migration/from | List storage service buckets
[**get_migrations**](BucketApi.md#get_migrations) | **GET** /api/v1/buckets/migrations | list migration operation
[**get_single_buckets**](BucketApi.md#get_single_buckets) | **GET** /api/v1/buckets/{bucket} | Get Single Buckets
[**migrating_buckets**](BucketApi.md#migrating_buckets) | **POST** /api/v1/buckets/migrates | Migrating buckets
[**upgrade_bucket**](BucketApi.md#upgrade_bucket) | **PATCH** /api/v1/buckets/{bucket}/upgrade/{plan} | Upgrade Bucket


# **change_bucket_access**
> ChangeBucketAccess200Response change_bucket_access(bucket, permission)

change Bucket Access Policy

Change Bucket Access policy on an object storage ( public / private )

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.change_bucket_access200_response import ChangeBucketAccess200Response
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.BucketApi(api_client)    
    bucket = 'bucket_example'
    permission = 'permission_example'
    
    try:
        api_response: ChangeBucketAccess200Response = api_instance.change_bucket_access(bucket, permission)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **permission** | **str**|  | 

### Return type

[**ChangeBucketAccess200Response**](ChangeBucketAccess200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_bucket**
> CreateBucket201Response check_bucket(bucket)

Check Bucket availability

Check if you can create Bucket with specified Name.

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.create_bucket201_response import CreateBucket201Response
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.BucketApi(api_client)    
    bucket = 'bucket_example'
    
    try:
        api_response: CreateBucket201Response = api_instance.check_bucket(bucket)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 

### Return type

[**CreateBucket201Response**](CreateBucket201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bucket**
> CreateBucket201Response create_bucket(body)

Create Bucket

creates a new bucket on an object storage

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.create_bucket import CreateBucket
from object_storage.openapi_client.models.create_bucket201_response import CreateBucket201Response
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.BucketApi(api_client) 
    body: CreateBucket = object_storage.openapi_client.CreateBucket(
        name = 'name_example',
        plan = 'plan_example',
        permission = 'permission_example',
    )
    
    try:
        api_response: CreateBucket201Response = api_instance.create_bucket(body)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBucket**](CreateBucket.md)| create bucket. Acceptable values for permission: ( private / public ) and for plan: ( 20g, 40g, 80g, 160g ) | 

### Return type

[**CreateBucket201Response**](CreateBucket201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**409** | Conflict |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_bucket**
> destroy_bucket(bucket)

Destroy Bucket

Delete Bucket on an object storage

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.BucketApi(api_client)
    bucket = 'bucket_example'
    
    try:
        api_instance.destroy_bucket(bucket)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 

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
**204** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buckets**
> ListBucket get_buckets()

List all Buckets

List all Bucket

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.list_bucket import ListBucket
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.BucketApi(api_client)
    
    try:
        api_response: ListBucket = api_instance.get_buckets()
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ListBucket**](ListBucket.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | Missing authentication |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_previous_buckets**
> get_list_previous_buckets()

List storage service buckets

List previous buckets of storage service in liara.

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.BucketApi(api_client)
    
    try:
        api_instance.get_list_previous_buckets()
    except ApiException as e:
        print(e)

```



### Parameters
This endpoint does not need any parameter.

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
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migrations**
> GetMigrations200Response get_migrations()

list migration operation

list migration operation

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.get_migrations200_response import GetMigrations200Response
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.BucketApi(api_client)
    
    try:
        api_response: GetMigrations200Response = api_instance.get_migrations()
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMigrations200Response**](GetMigrations200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_buckets**
> GetSingleBuckets200Response get_single_buckets(bucket)

Get Single Buckets

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.get_single_buckets200_response import GetSingleBuckets200Response
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.BucketApi(api_client)
    bucket = 'bucket_example'
    
    try:
        api_response: GetSingleBuckets200Response = api_instance.get_single_buckets(bucket)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 

### Return type

[**GetSingleBuckets200Response**](GetSingleBuckets200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**401** | Missing authentication |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrating_buckets**
> migrating_buckets(body)

Migrating buckets

Move data from one bucket to another

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.migrate_bucket import MigrateBucket
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.BucketApi(api_client)
    body: MigrateBucket = object_storage.openapi_client.MigrateBucket(
        var_from = 'var_from_example',
        to = 'to_example',
        path = 'path_example'
    )
    
    try:
        api_instance.migrating_buckets(body)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrateBucket**](MigrateBucket.md)| Migrate buckets | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**404** | Not Found |  -  |
**500** | server does not response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upgrade_bucket**
> UpgradeBucket200Response upgrade_bucket(bucket, plan)

Upgrade Bucket

Upgrade Bucket plan ( just make space bigger )

### Example

* Api Key Authentication (jwt):
```python
import object_storage.openapi_client
from object_storage.openapi_client.models.upgrade_bucket200_response import UpgradeBucket200Response
from object_storage.openapi_client.rest import ApiException
from pprint import pprint

with object_storage.create_sdk("YOUR-API-TOKEN") as api_client:
    api_instance = object_storage.openapi_client.BucketApi(api_client)
    bucket = 'bucket_example'
    plan = 'plan_example'
    
    try:
        api_response: UpgradeBucket200Response = api_instance.upgrade_bucket(bucket, plan)
        
        pprint(api_response)
    except ApiException as e:
        print(e)

```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**|  | 
 **plan** | **str**|  | 

### Return type

[**UpgradeBucket200Response**](UpgradeBucket200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Missing authentication |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | server does not response |  -  |
**502** | bad gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

