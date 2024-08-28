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

class DeleteTargetView(object):
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
        'month': 'int',
        'year': 'int'
    }

    attribute_map = {
        'month': 'Month',
        'year': 'Year'
    }

    def __init__(self, month=None, year=None):  # noqa: E501
        """DeleteTargetView - a model defined in Swagger"""  # noqa: E501
        self._month = None
        self._year = None
        self.discriminator = None
        if month is not None:
            self.month = month
        if year is not None:
            self.year = year

    @property
    def month(self):
        """Gets the month of this DeleteTargetView.  # noqa: E501


        :return: The month of this DeleteTargetView.  # noqa: E501
        :rtype: int
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this DeleteTargetView.


        :param month: The month of this DeleteTargetView.  # noqa: E501
        :type: int
        """

        self._month = month

    @property
    def year(self):
        """Gets the year of this DeleteTargetView.  # noqa: E501


        :return: The year of this DeleteTargetView.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this DeleteTargetView.


        :param year: The year of this DeleteTargetView.  # noqa: E501
        :type: int
        """

        self._year = year

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
        if issubclass(DeleteTargetView, dict):
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
        if not isinstance(other, DeleteTargetView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other