# ProjectAllDetailsProject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of project | [optional] 
**project_id** | **str** | The name of project | [optional] 
**type** | **str** | The platform of project | [optional] 
**status** | **str** | The status of project | [optional] 
**default_subdomain** | **bool** | The defaultSubdomain status of project | [optional] 
**zero_downtime** | **bool** | The zeroDowntime status of project | [optional] 
**scale** | **float** | The being on of project | [optional] 
**envs** | [**List[ProjectAllDetailsProjectEnvsInner]**](ProjectAllDetailsProjectEnvsInner.md) | The envs of project | [optional] 
**plan_id** | **str** | The plan of project | [optional] 
**fixed_ip_status** | **str** | The fixedIPStatus of project | [optional] 
**created_at** | **str** | The time to create of project | [optional] 
**node** | [**ProjectAllDetailsProjectNode**](ProjectAllDetailsProjectNode.md) |  | [optional] 
**hourly_price** | **float** | The hourlyPrice of project | [optional] 
**is_deployed** | **bool** | The deployment status of project | [optional] 
**reserved_disk_space** | **float** | The count reservedDiskSpace of project | [optional] 

## Example

```python
from openapi_client.models.project_all_details_project import ProjectAllDetailsProject

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectAllDetailsProject from a JSON string
project_all_details_project_instance = ProjectAllDetailsProject.from_json(json)
# print the JSON string representation of the object
print ProjectAllDetailsProject.to_json()

# convert the object into a dict
project_all_details_project_dict = project_all_details_project_instance.to_dict()
# create an instance of ProjectAllDetailsProject from a dict
project_all_details_project_form_dict = project_all_details_project.from_dict(project_all_details_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


