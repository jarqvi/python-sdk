# AppletsAppletsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of applet | [optional] 
**name** | **str** | The name of applet | [optional] 
**timestamp** | **str** | The timestamp of applet | [optional] 
**state** | **str** | The state of applet | [optional] 
**reason** | **str** | The reason of applet | [optional] 
**release** | [**AppletsAppletsInnerRelease**](AppletsAppletsInnerRelease.md) |  | [optional] 

## Example

```python
from openapi_client.models.applets_applets_inner import AppletsAppletsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AppletsAppletsInner from a JSON string
applets_applets_inner_instance = AppletsAppletsInner.from_json(json)
# print the JSON string representation of the object
print AppletsAppletsInner.to_json()

# convert the object into a dict
applets_applets_inner_dict = applets_applets_inner_instance.to_dict()
# create an instance of AppletsAppletsInner from a dict
applets_applets_inner_form_dict = applets_applets_inner.from_dict(applets_applets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


