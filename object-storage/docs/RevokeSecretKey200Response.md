# RevokeSecretKey200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**access_key** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.revoke_secret_key200_response import RevokeSecretKey200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeSecretKey200Response from a JSON string
revoke_secret_key200_response_instance = RevokeSecretKey200Response.from_json(json)
# print the JSON string representation of the object
print RevokeSecretKey200Response.to_json()

# convert the object into a dict
revoke_secret_key200_response_dict = revoke_secret_key200_response_instance.to_dict()
# create an instance of RevokeSecretKey200Response from a dict
revoke_secret_key200_response_form_dict = revoke_secret_key200_response.from_dict(revoke_secret_key200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


