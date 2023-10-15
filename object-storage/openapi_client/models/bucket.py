# coding: utf-8

"""
    Object Storage API Documentaion

    A scalable, reliable, and cost effective Object Storage solution to support your application from liara-cloud

    The version of the OpenAPI document: 1.0.0
    Contact: support@liara.ir
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field

class Bucket(BaseModel):
    """
    Bucket
    """
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    plan: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    permission: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = Field(default=None, alias="createdAt")
    updated_at: Optional[StrictStr] = Field(default=None, alias="updatedAt")
    __properties: ClassVar[List[str]] = ["id", "name", "plan", "status", "permission", "createdAt", "updatedAt"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Bucket:
        """Create an instance of Bucket from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Bucket:
        """Create an instance of Bucket from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Bucket.model_validate(obj)

        _obj = Bucket.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "plan": obj.get("plan"),
            "status": obj.get("status"),
            "permission": obj.get("permission"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


