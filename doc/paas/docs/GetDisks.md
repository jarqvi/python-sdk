# GetDisks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disks** | [**List[GetDisksDisksInner]**](GetDisksDisksInner.md) |  | [optional] 
**mounts** | [**List[GetDisksMountsInner]**](GetDisksMountsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_disks import GetDisks

# TODO update the JSON string below
json = "{}"
# create an instance of GetDisks from a JSON string
get_disks_instance = GetDisks.from_json(json)
# print the JSON string representation of the object
print GetDisks.to_json()

# convert the object into a dict
get_disks_dict = get_disks_instance.to_dict()
# create an instance of GetDisks from a dict
get_disks_form_dict = get_disks.from_dict(get_disks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


