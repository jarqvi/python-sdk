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

from openapi_client.models.get_metrics_summary200_response_data_metrics import GetMetricsSummary200ResponseDataMetrics  # noqa: E501

class TestGetMetricsSummary200ResponseDataMetrics(unittest.TestCase):
    """GetMetricsSummary200ResponseDataMetrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetMetricsSummary200ResponseDataMetrics:
        """Test GetMetricsSummary200ResponseDataMetrics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetMetricsSummary200ResponseDataMetrics`
        """
        model = GetMetricsSummary200ResponseDataMetrics()  # noqa: E501
        if include_optional:
            return GetMetricsSummary200ResponseDataMetrics(
                totol_objects = [
                    null
                    ],
                total_bytes = [
                    null
                    ]
            )
        else:
            return GetMetricsSummary200ResponseDataMetrics(
        )
        """

    def testGetMetricsSummary200ResponseDataMetrics(self):
        """Test GetMetricsSummary200ResponseDataMetrics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
