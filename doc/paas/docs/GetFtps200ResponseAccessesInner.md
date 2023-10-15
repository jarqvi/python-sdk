# GetFtps200ResponseAccessesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**disk** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**v** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.get_ftps200_response_accesses_inner import GetFtps200ResponseAccessesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetFtps200ResponseAccessesInner from a JSON string
get_ftps200_response_accesses_inner_instance = GetFtps200ResponseAccessesInner.from_json(json)
# print the JSON string representation of the object
print GetFtps200ResponseAccessesInner.to_json()

# convert the object into a dict
get_ftps200_response_accesses_inner_dict = get_ftps200_response_accesses_inner_instance.to_dict()
# create an instance of GetFtps200ResponseAccessesInner from a dict
get_ftps200_response_accesses_inner_form_dict = get_ftps200_response_accesses_inner.from_dict(get_ftps200_response_accesses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


