# UpdateEnvs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **str** | The name of your app for update envs | [optional] 
**variables** | [**List[UpdateEnvsVariablesInner]**](UpdateEnvsVariablesInner.md) | The envs for update | [optional] 

## Example

```python
from openapi_client.models.update_envs import UpdateEnvs

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEnvs from a JSON string
update_envs_instance = UpdateEnvs.from_json(json)
# print the JSON string representation of the object
print UpdateEnvs.to_json()

# convert the object into a dict
update_envs_dict = update_envs_instance.to_dict()
# create an instance of UpdateEnvs from a dict
update_envs_form_dict = update_envs.from_dict(update_envs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


