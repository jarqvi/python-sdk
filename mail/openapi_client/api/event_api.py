# coding: utf-8

"""
    Liara Mail API Documentaion

    A fully featured mail delivery platform for incoming & outgoing e-mail

    The version of the OpenAPI document: 1.0.0
    Contact: support@liara.ir
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_call, ValidationError

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictFloat, StrictInt, field_validator

from typing import Optional, Union

from openapi_client.models.mail_events import MailEvents

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EventApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def get_all_events(self, mail_server_id : Annotated[str, Field(strict=True)], message_id : Annotated[str, Field(strict=True)], page : Optional[Union[StrictFloat, StrictInt]] = None, count : Optional[Union[Annotated[float, Field(le=100, strict=True)], Annotated[int, Field(le=100, strict=True)]]] = None, **kwargs) -> MailEvents:  # noqa: E501
        """get all events for message  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_all_events(mail_server_id, message_id, page, count, async_req=True)
        >>> result = thread.get()

        :param mail_server_id: (required)
        :type mail_server_id: str
        :param message_id: (required)
        :type message_id: str
        :param page:
        :type page: float
        :param count:
        :type count: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MailEvents
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_all_events_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_all_events_with_http_info(mail_server_id, message_id, page, count, **kwargs)  # noqa: E501

    @validate_call
    def get_all_events_with_http_info(self, mail_server_id : Annotated[str, Field(strict=True)], message_id : Annotated[str, Field(strict=True)], page : Optional[Union[StrictFloat, StrictInt]] = None, count : Optional[Union[Annotated[float, Field(le=100, strict=True)], Annotated[int, Field(le=100, strict=True)]]] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get all events for message  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_all_events_with_http_info(mail_server_id, message_id, page, count, async_req=True)
        >>> result = thread.get()

        :param mail_server_id: (required)
        :type mail_server_id: str
        :param message_id: (required)
        :type message_id: str
        :param page:
        :type page: float
        :param count:
        :type count: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(MailEvents, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'mail_server_id',
            'message_id',
            'page',
            'count'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_events" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['mail_server_id'] is not None:
            _path_params['mailServerID'] = _params['mail_server_id']

        if _params['message_id'] is not None:
            _path_params['messageID'] = _params['message_id']


        # process the query parameters
        _query_params = []
        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        if _params.get('count') is not None:  # noqa: E501
            _query_params.append(('count', _params['count']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['jwt']  # noqa: E501

        _response_types_map = {
            '200': "MailEvents",
            '400': None,
            '404': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/mails/{mailServerID}/messages/{messageID}/events', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
