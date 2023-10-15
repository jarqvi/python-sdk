# CreateSMTP


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**data** | [**CreateSMTPData**](CreateSMTPData.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_smtp import CreateSMTP

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSMTP from a JSON string
create_smtp_instance = CreateSMTP.from_json(json)
# print the JSON string representation of the object
print CreateSMTP.to_json()

# convert the object into a dict
create_smtp_dict = create_smtp_instance.to_dict()
# create an instance of CreateSMTP from a dict
create_smtp_form_dict = create_smtp.from_dict(create_smtp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


