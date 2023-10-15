# TmpAccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**TmpAccessData**](TmpAccessData.md) |  | [optional] 

## Example

```python
from openapi_client.models.tmp_access import TmpAccess

# TODO update the JSON string below
json = "{}"
# create an instance of TmpAccess from a JSON string
tmp_access_instance = TmpAccess.from_json(json)
# print the JSON string representation of the object
print TmpAccess.to_json()

# convert the object into a dict
tmp_access_dict = tmp_access_instance.to_dict()
# create an instance of TmpAccess from a dict
tmp_access_form_dict = tmp_access.from_dict(tmp_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


