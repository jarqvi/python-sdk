# Stat


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**StatData**](StatData.md) |  | [optional] 

## Example

```python
from openapi_client.models.stat import Stat

# TODO update the JSON string below
json = "{}"
# create an instance of Stat from a JSON string
stat_instance = Stat.from_json(json)
# print the JSON string representation of the object
print Stat.to_json()

# convert the object into a dict
stat_dict = stat_instance.to_dict()
# create an instance of Stat from a dict
stat_form_dict = stat.from_dict(stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


