# coding: utf-8

"""
    Liara Mail API Documentaion

    A fully featured mail delivery platform for incoming & outgoing e-mail

    The version of the OpenAPI document: 1.0.0
    Contact: support@liara.ir
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.model11 import Model11  # noqa: E501

class TestModel11(unittest.TestCase):
    """Model11 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Model11:
        """Test Model11
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Model11`
        """
        model = Model11()  # noqa: E501
        if include_optional:
            return Model11(
                rule = ''
            )
        else:
            return Model11(
                rule = '',
        )
        """

    def testModel11(self):
        """Test Model11"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
