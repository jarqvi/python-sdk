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
from pydantic import field_validator

from typing import Optional

from openapi_client.models.mail_forwards import MailForwards
from openapi_client.models.model6 import Model6
from openapi_client.models.post_mails201_response import PostMails201Response

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ForwardApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def create_address_forwarding(self, mail_server_id : Annotated[str, Field(strict=True)], account_id : Annotated[str, Field(strict=True)], body : Optional[Model6] = None, **kwargs) -> PostMails201Response:  # noqa: E501
        """add address endpoint to forwarding mails  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_address_forwarding(mail_server_id, account_id, body, async_req=True)
        >>> result = thread.get()

        :param mail_server_id: (required)
        :type mail_server_id: str
        :param account_id: (required)
        :type account_id: str
        :param body:
        :type body: Model6
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PostMails201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_address_forwarding_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.create_address_forwarding_with_http_info(mail_server_id, account_id, body, **kwargs)  # noqa: E501

    @validate_call
    def create_address_forwarding_with_http_info(self, mail_server_id : Annotated[str, Field(strict=True)], account_id : Annotated[str, Field(strict=True)], body : Optional[Model6] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """add address endpoint to forwarding mails  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_address_forwarding_with_http_info(mail_server_id, account_id, body, async_req=True)
        >>> result = thread.get()

        :param mail_server_id: (required)
        :type mail_server_id: str
        :param account_id: (required)
        :type account_id: str
        :param body:
        :type body: Model6
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
        :rtype: tuple(PostMails201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'mail_server_id',
            'account_id',
            'body'
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
                    " to method create_address_forwarding" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['mail_server_id'] is not None:
            _path_params['mailServerID'] = _params['mail_server_id']

        if _params['account_id'] is not None:
            _path_params['accountID'] = _params['account_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['body'] is not None:
            _body_params = _params['body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['jwt']  # noqa: E501

        _response_types_map = {
            '201': "PostMails201Response",
            '400': None,
            '403': None,
            '404': None,
            '409': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/mails/{mailServerID}/accounts/{accountID}/forwards', 'POST',
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

    @validate_call
    def delete_extra_endpoint(self, mail_server_id : Annotated[str, Field(strict=True)], account_id : Annotated[str, Field(strict=True)], address_id : Annotated[str, Field(strict=True)], **kwargs) -> None:  # noqa: E501
        """delete extra endpoint address  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_extra_endpoint(mail_server_id, account_id, address_id, async_req=True)
        >>> result = thread.get()

        :param mail_server_id: (required)
        :type mail_server_id: str
        :param account_id: (required)
        :type account_id: str
        :param address_id: (required)
        :type address_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the delete_extra_endpoint_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.delete_extra_endpoint_with_http_info(mail_server_id, account_id, address_id, **kwargs)  # noqa: E501

    @validate_call
    def delete_extra_endpoint_with_http_info(self, mail_server_id : Annotated[str, Field(strict=True)], account_id : Annotated[str, Field(strict=True)], address_id : Annotated[str, Field(strict=True)], **kwargs) -> ApiResponse:  # noqa: E501
        """delete extra endpoint address  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_extra_endpoint_with_http_info(mail_server_id, account_id, address_id, async_req=True)
        >>> result = thread.get()

        :param mail_server_id: (required)
        :type mail_server_id: str
        :param account_id: (required)
        :type account_id: str
        :param address_id: (required)
        :type address_id: str
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
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'mail_server_id',
            'account_id',
            'address_id'
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
                    " to method delete_extra_endpoint" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['mail_server_id'] is not None:
            _path_params['mailServerID'] = _params['mail_server_id']

        if _params['account_id'] is not None:
            _path_params['accountID'] = _params['account_id']

        if _params['address_id'] is not None:
            _path_params['addressID'] = _params['address_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['jwt']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/mails/{mailServerID}/accounts/{accountID}/forwards/{addressID}', 'DELETE',
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

    @validate_call
    def get_list_address_forwarding(self, mail_server_id : Annotated[str, Field(strict=True)], account_id : Annotated[str, Field(strict=True)], **kwargs) -> MailForwards:  # noqa: E501
        """get all extra address to forwarding mails  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_list_address_forwarding(mail_server_id, account_id, async_req=True)
        >>> result = thread.get()

        :param mail_server_id: (required)
        :type mail_server_id: str
        :param account_id: (required)
        :type account_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: MailForwards
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_list_address_forwarding_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_list_address_forwarding_with_http_info(mail_server_id, account_id, **kwargs)  # noqa: E501

    @validate_call
    def get_list_address_forwarding_with_http_info(self, mail_server_id : Annotated[str, Field(strict=True)], account_id : Annotated[str, Field(strict=True)], **kwargs) -> ApiResponse:  # noqa: E501
        """get all extra address to forwarding mails  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_list_address_forwarding_with_http_info(mail_server_id, account_id, async_req=True)
        >>> result = thread.get()

        :param mail_server_id: (required)
        :type mail_server_id: str
        :param account_id: (required)
        :type account_id: str
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
        :rtype: tuple(MailForwards, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'mail_server_id',
            'account_id'
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
                    " to method get_list_address_forwarding" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['mail_server_id'] is not None:
            _path_params['mailServerID'] = _params['mail_server_id']

        if _params['account_id'] is not None:
            _path_params['accountID'] = _params['account_id']


        # process the query parameters
        _query_params = []
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
            '200': "MailForwards",
            '400': None,
            '404': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/mails/{mailServerID}/accounts/{accountID}/forwards', 'GET',
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
