# Zone


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | The name of the zone, “liara.ir”, max length: 253, pattern: ^([a-zA-Z0-9][\\-a-zA-Z0-9]*\\.)+[\\-a-zA-Z0-9]{2,20}$ | [optional] 
**status** | **str** | The status of the zone, valid values: [CREATING, PENDING, ACTIVE, DELETING] | [optional] 
**current_name_servers** | **List[str]** |  | [optional] 
**name_servers** | **List[str]** |  | [optional] 
**last_check_at** | **str** | Last time when zones nameservers was checked | [optional] 
**created_at** | **str** | Time when zone was created | [optional] 

## Example

```python
from openapi_client.models.zone import Zone

# TODO update the JSON string below
json = "{}"
# create an instance of Zone from a JSON string
zone_instance = Zone.from_json(json)
# print the JSON string representation of the object
print Zone.to_json()

# convert the object into a dict
zone_dict = zone_instance.to_dict()
# create an instance of Zone from a dict
zone_form_dict = zone.from_dict(zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


