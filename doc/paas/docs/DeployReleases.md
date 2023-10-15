# DeployReleases


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | The id of Deployed sources | [optional] 
**port** | **float** | The port of your app | [optional] 
**type** | **str** | The platform of your app | [optional] 

## Example

```python
from openapi_client.models.deploy_releases import DeployReleases

# TODO update the JSON string below
json = "{}"
# create an instance of DeployReleases from a JSON string
deploy_releases_instance = DeployReleases.from_json(json)
# print the JSON string representation of the object
print DeployReleases.to_json()

# convert the object into a dict
deploy_releases_dict = deploy_releases_instance.to_dict()
# create an instance of DeployReleases from a dict
deploy_releases_form_dict = deploy_releases.from_dict(deploy_releases_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


