# GetDiskBackupBackupsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 
**etag** | **str** |  | [optional] 
**size** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.get_disk_backup_backups_inner import GetDiskBackupBackupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDiskBackupBackupsInner from a JSON string
get_disk_backup_backups_inner_instance = GetDiskBackupBackupsInner.from_json(json)
# print the JSON string representation of the object
print GetDiskBackupBackupsInner.to_json()

# convert the object into a dict
get_disk_backup_backups_inner_dict = get_disk_backup_backups_inner_instance.to_dict()
# create an instance of GetDiskBackupBackupsInner from a dict
get_disk_backup_backups_inner_form_dict = get_disk_backup_backups_inner.from_dict(get_disk_backup_backups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


