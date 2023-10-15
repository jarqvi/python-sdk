# coding: utf-8

"""
    Liara Mail API Documentaion

    A fully featured mail delivery platform for incoming & outgoing e-mail

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

class SMTPDataCredentialsInner(BaseModel):
    """
    SMTPDataCredentialsInner
    """
    description: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = Field(default=None, alias="createdAt")
    username: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["description", "createdAt", "username"]

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
    def from_json(cls, json_str: str) -> SMTPDataCredentialsInner:
        """Create an instance of SMTPDataCredentialsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SMTPDataCredentialsInner:
        """Create an instance of SMTPDataCredentialsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SMTPDataCredentialsInner.model_validate(obj)

        _obj = SMTPDataCredentialsInner.model_validate({
            "description": obj.get("description"),
            "createdAt": obj.get("createdAt"),
            "username": obj.get("username")
        })
        return _obj


