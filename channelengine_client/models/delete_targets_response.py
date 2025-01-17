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

class DeleteTargetsResponse(object):
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
        'deleted_targets': 'list[DeleteTargetResponseVm]',
        'not_existing_targets': 'list[DeleteTargetResponseVm]'
    }

    attribute_map = {
        'deleted_targets': 'DeletedTargets',
        'not_existing_targets': 'NotExistingTargets'
    }

    def __init__(self, deleted_targets=None, not_existing_targets=None):  # noqa: E501
        """DeleteTargetsResponse - a model defined in Swagger"""  # noqa: E501
        self._deleted_targets = None
        self._not_existing_targets = None
        self.discriminator = None
        if deleted_targets is not None:
            self.deleted_targets = deleted_targets
        if not_existing_targets is not None:
            self.not_existing_targets = not_existing_targets

    @property
    def deleted_targets(self):
        """Gets the deleted_targets of this DeleteTargetsResponse.  # noqa: E501


        :return: The deleted_targets of this DeleteTargetsResponse.  # noqa: E501
        :rtype: list[DeleteTargetResponseVm]
        """
        return self._deleted_targets

    @deleted_targets.setter
    def deleted_targets(self, deleted_targets):
        """Sets the deleted_targets of this DeleteTargetsResponse.


        :param deleted_targets: The deleted_targets of this DeleteTargetsResponse.  # noqa: E501
        :type: list[DeleteTargetResponseVm]
        """

        self._deleted_targets = deleted_targets

    @property
    def not_existing_targets(self):
        """Gets the not_existing_targets of this DeleteTargetsResponse.  # noqa: E501


        :return: The not_existing_targets of this DeleteTargetsResponse.  # noqa: E501
        :rtype: list[DeleteTargetResponseVm]
        """
        return self._not_existing_targets

    @not_existing_targets.setter
    def not_existing_targets(self, not_existing_targets):
        """Sets the not_existing_targets of this DeleteTargetsResponse.


        :param not_existing_targets: The not_existing_targets of this DeleteTargetsResponse.  # noqa: E501
        :type: list[DeleteTargetResponseVm]
        """

        self._not_existing_targets = not_existing_targets

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
        if issubclass(DeleteTargetsResponse, dict):
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
        if not isinstance(other, DeleteTargetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
