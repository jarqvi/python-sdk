# DownloadObject200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**DownloadObject200ResponseData**](DownloadObject200ResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.download_object200_response import DownloadObject200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadObject200Response from a JSON string
download_object200_response_instance = DownloadObject200Response.from_json(json)
# print the JSON string representation of the object
print DownloadObject200Response.to_json()

# convert the object into a dict
download_object200_response_dict = download_object200_response_instance.to_dict()
# create an instance of DownloadObject200Response from a dict
download_object200_response_form_dict = download_object200_response.from_dict(download_object200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


