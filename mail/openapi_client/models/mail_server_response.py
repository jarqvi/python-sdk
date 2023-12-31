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


from typing import Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from openapi_client.models.check_dns_response_dns_setup import CheckDNSResponseDnsSetup
from openapi_client.models.mail_server_response_rate_limit_tier import MailServerResponseRateLimitTier

class MailServerResponse(BaseModel):
    """
    MailServerResponse
    """
    dns_setup: Optional[CheckDNSResponseDnsSetup] = None
    domain: Optional[StrictStr] = None
    records_status: Optional[StrictStr] = Field(default=None, alias="recordsStatus")
    status: Optional[StrictStr] = None
    rate_limit_tier: Optional[MailServerResponseRateLimitTier] = Field(default=None, alias="rateLimitTier")
    created_at: Optional[StrictStr] = Field(default=None, alias="createdAt")
    id: Optional[StrictStr] = None
    smtp_server: Optional[StrictStr] = None
    smtp_port: Optional[Union[StrictFloat, StrictInt]] = None
    root_part_of_domain: Optional[StrictStr] = Field(default=None, alias="rootPartOfDomain")
    __properties: ClassVar[List[str]] = ["dns_setup", "domain", "recordsStatus", "status", "rateLimitTier", "createdAt", "id", "smtp_server", "smtp_port", "rootPartOfDomain"]

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
    def from_json(cls, json_str: str) -> MailServerResponse:
        """Create an instance of MailServerResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of dns_setup
        if self.dns_setup:
            _dict['dns_setup'] = self.dns_setup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rate_limit_tier
        if self.rate_limit_tier:
            _dict['rateLimitTier'] = self.rate_limit_tier.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MailServerResponse:
        """Create an instance of MailServerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MailServerResponse.model_validate(obj)

        _obj = MailServerResponse.model_validate({
            "dns_setup": CheckDNSResponseDnsSetup.from_dict(obj.get("dns_setup")) if obj.get("dns_setup") is not None else None,
            "domain": obj.get("domain"),
            "recordsStatus": obj.get("recordsStatus"),
            "status": obj.get("status"),
            "rateLimitTier": MailServerResponseRateLimitTier.from_dict(obj.get("rateLimitTier")) if obj.get("rateLimitTier") is not None else None,
            "createdAt": obj.get("createdAt"),
            "id": obj.get("id"),
            "smtp_server": obj.get("smtp_server"),
            "smtp_port": obj.get("smtp_port"),
            "rootPartOfDomain": obj.get("rootPartOfDomain")
        })
        return _obj


