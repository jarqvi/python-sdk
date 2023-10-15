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

from openapi_client.models.reports import Reports  # noqa: E501

class TestReports(unittest.TestCase):
    """Reports unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Reports:
        """Test Reports
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Reports`
        """
        model = Reports()  # noqa: E501
        if include_optional:
            return Reports(
                end = 1.337,
                result = [
                    openapi_client.models.reports_result_inner.Reports_result_inner(
                        values = [
                            [
                                null
                                ]
                            ], 
                        applet = '', )
                    ]
            )
        else:
            return Reports(
        )
        """

    def testReports(self):
        """Test Reports"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
