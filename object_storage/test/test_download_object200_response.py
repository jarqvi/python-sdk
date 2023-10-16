# coding: utf-8

"""
    Object Storage API Documentaion

    A scalable, reliable, and cost effective Object Storage solution to support your application from liara-cloud

    The version of the OpenAPI document: 1.0.0
    Contact: support@liara.ir
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.download_object200_response import DownloadObject200Response  # noqa: E501

class TestDownloadObject200Response(unittest.TestCase):
    """DownloadObject200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DownloadObject200Response:
        """Test DownloadObject200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DownloadObject200Response`
        """
        model = DownloadObject200Response()  # noqa: E501
        if include_optional:
            return DownloadObject200Response(
                status = '',
                data = openapi_client.models.download_object_200_response_data.downloadObject_200_response_data(
                    url = '', )
            )
        else:
            return DownloadObject200Response(
        )
        """

    def testDownloadObject200Response(self):
        """Test DownloadObject200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()