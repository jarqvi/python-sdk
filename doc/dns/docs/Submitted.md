# Submitted


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | succes | [optional] 
**data** | **str** | Your request has been submitted. | [optional] 

## Example

```python
from openapi_client.models.submitted import Submitted

# TODO update the JSON string below
json = "{}"
# create an instance of Submitted from a JSON string
submitted_instance = Submitted.from_json(json)
# print the JSON string representation of the object
print Submitted.to_json()

# convert the object into a dict
submitted_dict = submitted_instance.to_dict()
# create an instance of Submitted from a dict
submitted_form_dict = submitted.from_dict(submitted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


