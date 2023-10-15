# GetDiskBackup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backups** | [**List[GetDiskBackupBackupsInner]**](GetDiskBackupBackupsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_disk_backup import GetDiskBackup

# TODO update the JSON string below
json = "{}"
# create an instance of GetDiskBackup from a JSON string
get_disk_backup_instance = GetDiskBackup.from_json(json)
# print the JSON string representation of the object
print GetDiskBackup.to_json()

# convert the object into a dict
get_disk_backup_dict = get_disk_backup_instance.to_dict()
# create an instance of GetDiskBackup from a dict
get_disk_backup_form_dict = get_disk_backup.from_dict(get_disk_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


