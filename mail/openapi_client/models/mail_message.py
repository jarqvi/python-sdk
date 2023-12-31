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


from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from openapi_client.models.mail_message_status import MailMessageStatus

class MailMessage(BaseModel):
    """
    MailMessage
    """
    created_at: Optional[StrictStr] = Field(default=None, alias="createdAt")
    direction: Optional[StrictStr] = None
    var_from: Optional[StrictStr] = Field(default=None, alias="from")
    has_html: Optional[StrictBool] = Field(default=None, alias="hasHtml")
    is_dev: Optional[StrictBool] = Field(default=None, alias="isDev")
    is_free: Optional[StrictBool] = Field(default=None, alias="isFree")
    spam_score: Optional[StrictBool] = Field(default=None, alias="spamScore")
    subject: Optional[StrictStr] = None
    to: Optional[StrictStr] = None
    text: Optional[StrictStr] = None
    status: Optional[MailMessageStatus] = None
    id: Optional[StrictStr] = None
    spam_reson: Optional[Union[str, Any]] = Field(default=None, alias="spamReson")
    __properties: ClassVar[List[str]] = ["createdAt", "direction", "from", "hasHtml", "isDev", "isFree", "spamScore", "subject", "to", "text", "status", "id", "spamReson"]

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
    def from_json(cls, json_str: str) -> MailMessage:
        """Create an instance of MailMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MailMessage:
        """Create an instance of MailMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MailMessage.model_validate(obj)

        _obj = MailMessage.model_validate({
            "createdAt": obj.get("createdAt"),
            "direction": obj.get("direction"),
            "from": obj.get("from"),
            "hasHtml": obj.get("hasHtml"),
            "isDev": obj.get("isDev"),
            "isFree": obj.get("isFree"),
            "spamScore": obj.get("spamScore"),
            "subject": obj.get("subject"),
            "to": obj.get("to"),
            "text": obj.get("text"),
            "status": MailMessageStatus.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "id": obj.get("id"),
            "spamReson": obj.get("spamReson")
        })
        return _obj


