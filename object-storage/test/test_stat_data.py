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

from openapi_client.models.stat_data import StatData  # noqa: E501

class TestStatData(unittest.TestCase):
    """StatData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StatData:
        """Test StatData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StatData`
        """
        model = StatData()  # noqa: E501
        if include_optional:
            return StatData(
                object = openapi_client.models.stat_data_object.Stat_data_object(
                    size = 1.337, 
                    meta_data = openapi_client.models.stat_data_object_meta_data.Stat_data_object_metaData(
                        content_type = '', ), 
                    last_modified = '', 
                    version_id = '', 
                    etag = '', )
            )
        else:
            return StatData(
        )
        """

    def testStatData(self):
        """Test StatData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
