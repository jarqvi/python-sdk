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

from openapi_client.api.accounts_api import AccountsApi  # noqa: E501


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccountsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_check_mail_available(self) -> None:
        """Test case for check_mail_available

        check if mail account is available  # noqa: E501
        """
        pass

    def test_create_mail_a_ccount(self) -> None:
        """Test case for create_mail_a_ccount

        add mail account  # noqa: E501
        """
        pass

    def test_delete_mail_account(self) -> None:
        """Test case for delete_mail_account

        delete mail account  # noqa: E501
        """
        pass

    def test_get_all_mail_accounts(self) -> None:
        """Test case for get_all_mail_accounts

        get all mail accounts  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
