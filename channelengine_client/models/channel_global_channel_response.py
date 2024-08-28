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

class ChannelGlobalChannelResponse(object):
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
        'country_code': 'str',
        'global_channel_id': 'int',
        'channels': 'list[ChannelChannelResponse]',
        'language_code': 'str',
        'global_channel_name': 'str'
    }

    attribute_map = {
        'country_code': 'CountryCode',
        'global_channel_id': 'GlobalChannelId',
        'channels': 'Channels',
        'language_code': 'LanguageCode',
        'global_channel_name': 'GlobalChannelName'
    }

    def __init__(self, country_code=None, global_channel_id=None, channels=None, language_code=None, global_channel_name=None):  # noqa: E501
        """ChannelGlobalChannelResponse - a model defined in Swagger"""  # noqa: E501
        self._country_code = None
        self._global_channel_id = None
        self._channels = None
        self._language_code = None
        self._global_channel_name = None
        self.discriminator = None
        if country_code is not None:
            self.country_code = country_code
        if global_channel_id is not None:
            self.global_channel_id = global_channel_id
        if channels is not None:
            self.channels = channels
        if language_code is not None:
            self.language_code = language_code
        if global_channel_name is not None:
            self.global_channel_name = global_channel_name

    @property
    def country_code(self):
        """Gets the country_code of this ChannelGlobalChannelResponse.  # noqa: E501

        The country code of the Global Channel.  # noqa: E501

        :return: The country_code of this ChannelGlobalChannelResponse.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this ChannelGlobalChannelResponse.

        The country code of the Global Channel.  # noqa: E501

        :param country_code: The country_code of this ChannelGlobalChannelResponse.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def global_channel_id(self):
        """Gets the global_channel_id of this ChannelGlobalChannelResponse.  # noqa: E501

        The ID of the Global Channel.  # noqa: E501

        :return: The global_channel_id of this ChannelGlobalChannelResponse.  # noqa: E501
        :rtype: int
        """
        return self._global_channel_id

    @global_channel_id.setter
    def global_channel_id(self, global_channel_id):
        """Sets the global_channel_id of this ChannelGlobalChannelResponse.

        The ID of the Global Channel.  # noqa: E501

        :param global_channel_id: The global_channel_id of this ChannelGlobalChannelResponse.  # noqa: E501
        :type: int
        """

        self._global_channel_id = global_channel_id

    @property
    def channels(self):
        """Gets the channels of this ChannelGlobalChannelResponse.  # noqa: E501

        The status of the instances.  # noqa: E501

        :return: The channels of this ChannelGlobalChannelResponse.  # noqa: E501
        :rtype: list[ChannelChannelResponse]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this ChannelGlobalChannelResponse.

        The status of the instances.  # noqa: E501

        :param channels: The channels of this ChannelGlobalChannelResponse.  # noqa: E501
        :type: list[ChannelChannelResponse]
        """

        self._channels = channels

    @property
    def language_code(self):
        """Gets the language_code of this ChannelGlobalChannelResponse.  # noqa: E501

        The language code of the Global Channel.  # noqa: E501

        :return: The language_code of this ChannelGlobalChannelResponse.  # noqa: E501
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this ChannelGlobalChannelResponse.

        The language code of the Global Channel.  # noqa: E501

        :param language_code: The language_code of this ChannelGlobalChannelResponse.  # noqa: E501
        :type: str
        """

        self._language_code = language_code

    @property
    def global_channel_name(self):
        """Gets the global_channel_name of this ChannelGlobalChannelResponse.  # noqa: E501

        The name of the Global Channel.  # noqa: E501

        :return: The global_channel_name of this ChannelGlobalChannelResponse.  # noqa: E501
        :rtype: str
        """
        return self._global_channel_name

    @global_channel_name.setter
    def global_channel_name(self, global_channel_name):
        """Sets the global_channel_name of this ChannelGlobalChannelResponse.

        The name of the Global Channel.  # noqa: E501

        :param global_channel_name: The global_channel_name of this ChannelGlobalChannelResponse.  # noqa: E501
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
        if issubclass(ChannelGlobalChannelResponse, dict):
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
        if not isinstance(other, ChannelGlobalChannelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other