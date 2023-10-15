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

from openapi_client.api.forward_api import ForwardApi  # noqa: E501


class TestForwardApi(unittest.TestCase):
    """ForwardApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ForwardApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_address_forwarding(self) -> None:
        """Test case for create_address_forwarding

        add address endpoint to forwarding mails  # noqa: E501
        """
        pass

    def test_delete_extra_endpoint(self) -> None:
        """Test case for delete_extra_endpoint

        delete extra endpoint address  # noqa: E501
        """
        pass

    def test_get_list_address_forwarding(self) -> None:
        """Test case for get_list_address_forwarding

        get all extra address to forwarding mails  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
