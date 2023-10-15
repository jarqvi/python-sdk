# GetDisksMountsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**mounted_to** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_disks_mounts_inner import GetDisksMountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDisksMountsInner from a JSON string
get_disks_mounts_inner_instance = GetDisksMountsInner.from_json(json)
# print the JSON string representation of the object
print GetDisksMountsInner.to_json()

# convert the object into a dict
get_disks_mounts_inner_dict = get_disks_mounts_inner_instance.to_dict()
# create an instance of GetDisksMountsInner from a dict
get_disks_mounts_inner_form_dict = get_disks_mounts_inner.from_dict(get_disks_mounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


