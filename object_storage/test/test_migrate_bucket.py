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

from openapi_client.models.migrate_bucket import MigrateBucket  # noqa: E501

class TestMigrateBucket(unittest.TestCase):
    """MigrateBucket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MigrateBucket:
        """Test MigrateBucket
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MigrateBucket`
        """
        model = MigrateBucket()  # noqa: E501
        if include_optional:
            return MigrateBucket(
                var_from = '',
                to = '',
                path = ''
            )
        else:
            return MigrateBucket(
        )
        """

    def testMigrateBucket(self):
        """Test MigrateBucket"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()