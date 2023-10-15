# CreateZone


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**Zone**](Zone.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_zone import CreateZone

# TODO update the JSON string below
json = "{}"
# create an instance of CreateZone from a JSON string
create_zone_instance = CreateZone.from_json(json)
# print the JSON string representation of the object
print CreateZone.to_json()

# convert the object into a dict
create_zone_dict = create_zone_instance.to_dict()
# create an instance of CreateZone from a dict
create_zone_form_dict = create_zone.from_dict(create_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


