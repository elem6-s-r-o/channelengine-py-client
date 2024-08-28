# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    OpenAPI spec version: 2.17.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import channelengine_client
from channelengine_client.api.custom_fields_api import CustomFieldsApi  # noqa: E501
from channelengine_client.rest import ApiException


class TestCustomFieldsApi(unittest.TestCase):
    """CustomFieldsApi unit test stubs"""

    def setUp(self):
        self.api = CustomFieldsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_custom_fields_get_custom_fields(self):
        """Test case for custom_fields_get_custom_fields

        Gets custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()