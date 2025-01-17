# coding: utf-8

"""
    ChannelEngine Merchant API

    ChannelEngine API for merchants  # noqa: E501

    OpenAPI spec version: 2.17.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MerchantProductAttributeGroupChannelInfoResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'channel_id': 'int',
        'channel_name': 'str',
        'is_enabled': 'bool',
        'global_channel_id': 'int',
        'global_channel_name': 'str'
    }

    attribute_map = {
        'channel_id': 'ChannelId',
        'channel_name': 'ChannelName',
        'is_enabled': 'IsEnabled',
        'global_channel_id': 'GlobalChannelId',
        'global_channel_name': 'GlobalChannelName'
    }

    def __init__(self, channel_id=None, channel_name=None, is_enabled=None, global_channel_id=None, global_channel_name=None):  # noqa: E501
        """MerchantProductAttributeGroupChannelInfoResponse - a model defined in Swagger"""  # noqa: E501
        self._channel_id = None
        self._channel_name = None
        self._is_enabled = None
        self._global_channel_id = None
        self._global_channel_name = None
        self.discriminator = None
        if channel_id is not None:
            self.channel_id = channel_id
        if channel_name is not None:
            self.channel_name = channel_name
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if global_channel_id is not None:
            self.global_channel_id = global_channel_id
        if global_channel_name is not None:
            self.global_channel_name = global_channel_name

    @property
    def channel_id(self):
        """Gets the channel_id of this MerchantProductAttributeGroupChannelInfoResponse.  # noqa: E501


        :return: The channel_id of this MerchantProductAttributeGroupChannelInfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        """Sets the channel_id of this MerchantProductAttributeGroupChannelInfoResponse.


        :param channel_id: The channel_id of this MerchantProductAttributeGroupChannelInfoResponse.  # noqa: E501
        :type: int
        """

        self._channel_id = channel_id

    @property
    def channel_name(self):
        """Gets the channel_name of this MerchantProductAttributeGroupChannelInfoResponse.  # noqa: E501


        :return: The channel_name of this MerchantProductAttributeGroupChannelInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """Sets the channel_name of this MerchantProductAttributeGroupChannelInfoResponse.


        :param channel_name: The channel_name of this MerchantProductAttributeGroupChannelInfoResponse.  # noqa: E501
        :type: str
        """

        self._channel_name = channel_name

    @property
    def is_enabled(self):
        """Gets the is_enabled of this MerchantProductAttributeGroupChannelInfoResponse.  # noqa: E501


        :return: The is_enabled of this MerchantProductAttributeGroupChannelInfoResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this MerchantProductAttributeGroupChannelInfoResponse.


        :param is_enabled: The is_enabled of this MerchantProductAttributeGroupChannelInfoResponse.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def global_channel_id(self):
        """Gets the global_channel_id of this MerchantProductAttributeGroupChannelInfoResponse.  # noqa: E501


        :return: The global_channel_id of this MerchantProductAttributeGroupChannelInfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._global_channel_id

    @global_channel_id.setter
    def global_channel_id(self, global_channel_id):
        """Sets the global_channel_id of this MerchantProductAttributeGroupChannelInfoResponse.


        :param global_channel_id: The global_channel_id of this MerchantProductAttributeGroupChannelInfoResponse.  # noqa: E501
        :type: int
        """

        self._global_channel_id = global_channel_id

    @property
    def global_channel_name(self):
        """Gets the global_channel_name of this MerchantProductAttributeGroupChannelInfoResponse.  # noqa: E501


        :return: The global_channel_name of this MerchantProductAttributeGroupChannelInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._global_channel_name

    @global_channel_name.setter
    def global_channel_name(self, global_channel_name):
        """Sets the global_channel_name of this MerchantProductAttributeGroupChannelInfoResponse.


        :param global_channel_name: The global_channel_name of this MerchantProductAttributeGroupChannelInfoResponse.  # noqa: E501
        :type: str
        """

        self._global_channel_name = global_channel_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MerchantProductAttributeGroupChannelInfoResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MerchantProductAttributeGroupChannelInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
