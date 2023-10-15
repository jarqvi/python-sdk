# ProjectsProjectsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of project | [optional] 
**project_id** | **str** | The name of project | [optional] 
**type** | **str** | The platform of project | [optional] 
**status** | **str** | The status of project | [optional] 
**scale** | **float** | The being on of project | [optional] 
**plan_id** | **str** | The plan of project | [optional] 
**created_at** | **str** | The time to create the project | [optional] 
**is_deployed** | **bool** | The project deployment status | [optional] 

## Example

```python
from openapi_client.models.projects_projects_inner import ProjectsProjectsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsProjectsInner from a JSON string
projects_projects_inner_instance = ProjectsProjectsInner.from_json(json)
# print the JSON string representation of the object
print ProjectsProjectsInner.to_json()

# convert the object into a dict
projects_projects_inner_dict = projects_projects_inner_instance.to_dict()
# create an instance of ProjectsProjectsInner from a dict
projects_projects_inner_form_dict = projects_projects_inner.from_dict(projects_projects_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


