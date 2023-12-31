# coding: utf-8

"""
    DBaaS

    Manage your databases using our API

    The version of the OpenAPI document: 1.0.0
    Contact: info@liara.ir
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.download_backup200_response import DownloadBackup200Response  # noqa: E501

class TestDownloadBackup200Response(unittest.TestCase):
    """DownloadBackup200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DownloadBackup200Response:
        """Test DownloadBackup200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DownloadBackup200Response`
        """
        model = DownloadBackup200Response()  # noqa: E501
        if include_optional:
            return DownloadBackup200Response(
                link = ''
            )
        else:
            return DownloadBackup200Response(
        )
        """

    def testDownloadBackup200Response(self):
        """Test DownloadBackup200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
