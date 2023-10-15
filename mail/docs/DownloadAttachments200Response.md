# DownloadAttachments200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**DownloadAttachments200ResponseData**](DownloadAttachments200ResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.download_attachments200_response import DownloadAttachments200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadAttachments200Response from a JSON string
download_attachments200_response_instance = DownloadAttachments200Response.from_json(json)
# print the JSON string representation of the object
print DownloadAttachments200Response.to_json()

# convert the object into a dict
download_attachments200_response_dict = download_attachments200_response_instance.to_dict()
# create an instance of DownloadAttachments200Response from a dict
download_attachments200_response_form_dict = download_attachments200_response.from_dict(download_attachments200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


