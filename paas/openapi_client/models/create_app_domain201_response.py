# coding: utf-8

"""
    PaaS

    Manage your apps using our API  [wss://api.iran.liara.ir?token=<api-token>&cmd=/bin/bash&project_id=<project-id>]( wss://api.iran.liara.ir?token=<api-token>&cmd=/bin/bash&project_id=<project-id>)  Parameters: - `token`: Your api token in liara - `cmd`: By default /bin/bash - `project_id`: The id of your project in liara  This `WebSocket` endpoint allows `real-time` communication with the projects service hosted at `Liara` You can use `WebSocket protocols` to send and receive data, enabling efficient and low-latency interactions with the projects

    The version of the OpenAPI document: 1.0.0
    Contact: info@liara.ir
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel
from openapi_client.models.create_app_domain201_response_domain import CreateAppDomain201ResponseDomain

class CreateAppDomain201Response(BaseModel):
    """
    CreateAppDomain201Response
    """
    domain: Optional[CreateAppDomain201ResponseDomain] = None
    __properties: ClassVar[List[str]] = ["domain"]

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
    def from_json(cls, json_str: str) -> CreateAppDomain201Response:
        """Create an instance of CreateAppDomain201Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of domain
        if self.domain:
            _dict['domain'] = self.domain.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateAppDomain201Response:
        """Create an instance of CreateAppDomain201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateAppDomain201Response.model_validate(obj)

        _obj = CreateAppDomain201Response.model_validate({
            "domain": CreateAppDomain201ResponseDomain.from_dict(obj.get("domain")) if obj.get("domain") is not None else None
        })
        return _obj


