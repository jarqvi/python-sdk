# ReleasesReleasesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of release | [optional] 
**type** | **str** | The type of release | [optional] 
**image_name** | **str** | The imageName of release | [optional] 
**project_type** | **str** | The projectType of release | [optional] 
**state** | **str** | The state of release | [optional] 
**port** | **float** | The port of release | [optional] 
**git_info** | [**ReleasesReleasesInnerGitInfo**](ReleasesReleasesInnerGitInfo.md) |  | [optional] 
**client** | **str** | The client of release | [optional] 
**finished_at** | **str** | The finishedAt of release | [optional] 
**created_at** | **str** | The createdAt of release | [optional] 
**tag** | **str** | The tag of release | [optional] 
**source_available** | **bool** | The sourceAvailable of release | [optional] 

## Example

```python
from openapi_client.models.releases_releases_inner import ReleasesReleasesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReleasesReleasesInner from a JSON string
releases_releases_inner_instance = ReleasesReleasesInner.from_json(json)
# print the JSON string representation of the object
print ReleasesReleasesInner.to_json()

# convert the object into a dict
releases_releases_inner_dict = releases_releases_inner_instance.to_dict()
# create an instance of ReleasesReleasesInner from a dict
releases_releases_inner_form_dict = releases_releases_inner.from_dict(releases_releases_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


