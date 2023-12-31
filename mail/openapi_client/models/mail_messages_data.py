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


from typing import List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt
from openapi_client.models.mail_message import MailMessage

class MailMessagesData(BaseModel):
    """
    MailMessagesData
    """
    total: Optional[Union[StrictFloat, StrictInt]] = None
    messages: Optional[List[MailMessage]] = None
    __properties: ClassVar[List[str]] = ["total", "messages"]

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
    def from_json(cls, json_str: str) -> MailMessagesData:
        """Create an instance of MailMessagesData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in messages (list)
        _items = []
        if self.messages:
            for _item in self.messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['messages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MailMessagesData:
        """Create an instance of MailMessagesData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MailMessagesData.model_validate(obj)

        _obj = MailMessagesData.model_validate({
            "total": obj.get("total"),
            "messages": [MailMessage.from_dict(_item) for _item in obj.get("messages")] if obj.get("messages") is not None else None
        })
        return _obj


