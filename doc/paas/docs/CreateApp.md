# CreateApp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of app that you want to create | [optional] 
**plan_id** | **str** | The plan of app that you want to create | [optional] 
**platform** | **str** | The platform of app that you want to create | [optional] 

## Example

```python
from openapi_client.models.create_app import CreateApp

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApp from a JSON string
create_app_instance = CreateApp.from_json(json)
# print the JSON string representation of the object
print CreateApp.to_json()

# convert the object into a dict
create_app_dict = create_app_instance.to_dict()
# create an instance of CreateApp from a dict
create_app_form_dict = create_app.from_dict(create_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


