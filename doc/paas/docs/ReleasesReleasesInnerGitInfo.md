# ReleasesReleasesInnerGitInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**commit** | **str** |  | [optional] 
**committed_at** | **datetime** |  | [optional] 
**remote** | **str** |  | [optional] 
**author** | [**ReleasesReleasesInnerGitInfoAuthor**](ReleasesReleasesInnerGitInfoAuthor.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.releases_releases_inner_git_info import ReleasesReleasesInnerGitInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReleasesReleasesInnerGitInfo from a JSON string
releases_releases_inner_git_info_instance = ReleasesReleasesInnerGitInfo.from_json(json)
# print the JSON string representation of the object
print ReleasesReleasesInnerGitInfo.to_json()

# convert the object into a dict
releases_releases_inner_git_info_dict = releases_releases_inner_git_info_instance.to_dict()
# create an instance of ReleasesReleasesInnerGitInfo from a dict
releases_releases_inner_git_info_form_dict = releases_releases_inner_git_info.from_dict(releases_releases_inner_git_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


