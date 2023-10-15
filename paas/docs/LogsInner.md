# LogsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**datetime** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.logs_inner import LogsInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogsInner from a JSON string
logs_inner_instance = LogsInner.from_json(json)
# print the JSON string representation of the object
print LogsInner.to_json()

# convert the object into a dict
logs_inner_dict = logs_inner_instance.to_dict()
# create an instance of LogsInner from a dict
logs_inner_form_dict = logs_inner.from_dict(logs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


