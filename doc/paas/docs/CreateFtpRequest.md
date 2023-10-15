# CreateFtpRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**read_only** | **bool** |  | 

## Example

```python
from openapi_client.models.create_ftp_request import CreateFtpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFtpRequest from a JSON string
create_ftp_request_instance = CreateFtpRequest.from_json(json)
# print the JSON string representation of the object
print CreateFtpRequest.to_json()

# convert the object into a dict
create_ftp_request_dict = create_ftp_request_instance.to_dict()
# create an instance of CreateFtpRequest from a dict
create_ftp_request_form_dict = create_ftp_request.from_dict(create_ftp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


