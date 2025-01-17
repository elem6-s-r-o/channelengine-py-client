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

class MerchantShipmentLabelCarrierResponse(object):
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
        'name': 'str',
        'code': 'str',
        'restrictions': 'str',
        'price': 'float',
        'recommendation': 'ChannelCarrierRecommendationApi',
        'collection_method': 'ChannelCarrierCollectionMethodApi',
        'handover_date_time': 'datetime'
    }

    attribute_map = {
        'name': 'Name',
        'code': 'Code',
        'restrictions': 'Restrictions',
        'price': 'Price',
        'recommendation': 'Recommendation',
        'collection_method': 'CollectionMethod',
        'handover_date_time': 'HandoverDateTime'
    }

    def __init__(self, name=None, code=None, restrictions=None, price=None, recommendation=None, collection_method=None, handover_date_time=None):  # noqa: E501
        """MerchantShipmentLabelCarrierResponse - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._code = None
        self._restrictions = None
        self._price = None
        self._recommendation = None
        self._collection_method = None
        self._handover_date_time = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if restrictions is not None:
            self.restrictions = restrictions
        if price is not None:
            self.price = price
        if recommendation is not None:
            self.recommendation = recommendation
        if collection_method is not None:
            self.collection_method = collection_method
        if handover_date_time is not None:
            self.handover_date_time = handover_date_time

    @property
    def name(self):
        """Gets the name of this MerchantShipmentLabelCarrierResponse.  # noqa: E501

        The channel's name for the shipping label carrier  # noqa: E501

        :return: The name of this MerchantShipmentLabelCarrierResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MerchantShipmentLabelCarrierResponse.

        The channel's name for the shipping label carrier  # noqa: E501

        :param name: The name of this MerchantShipmentLabelCarrierResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this MerchantShipmentLabelCarrierResponse.  # noqa: E501

        The channel's code for the shipping label carrier  # noqa: E501

        :return: The code of this MerchantShipmentLabelCarrierResponse.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this MerchantShipmentLabelCarrierResponse.

        The channel's code for the shipping label carrier  # noqa: E501

        :param code: The code of this MerchantShipmentLabelCarrierResponse.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def restrictions(self):
        """Gets the restrictions of this MerchantShipmentLabelCarrierResponse.  # noqa: E501

        Optional. Any restrictions on this carriers, e.g. weight and/or dimensions  # noqa: E501

        :return: The restrictions of this MerchantShipmentLabelCarrierResponse.  # noqa: E501
        :rtype: str
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this MerchantShipmentLabelCarrierResponse.

        Optional. Any restrictions on this carriers, e.g. weight and/or dimensions  # noqa: E501

        :param restrictions: The restrictions of this MerchantShipmentLabelCarrierResponse.  # noqa: E501
        :type: str
        """

        self._restrictions = restrictions

    @property
    def price(self):
        """Gets the price of this MerchantShipmentLabelCarrierResponse.  # noqa: E501

        Optional. Price for this shipping label  # noqa: E501

        :return: The price of this MerchantShipmentLabelCarrierResponse.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this MerchantShipmentLabelCarrierResponse.

        Optional. Price for this shipping label  # noqa: E501

        :param price: The price of this MerchantShipmentLabelCarrierResponse.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def recommendation(self):
        """Gets the recommendation of this MerchantShipmentLabelCarrierResponse.  # noqa: E501


        :return: The recommendation of this MerchantShipmentLabelCarrierResponse.  # noqa: E501
        :rtype: ChannelCarrierRecommendationApi
        """
        return self._recommendation

    @recommendation.setter
    def recommendation(self, recommendation):
        """Sets the recommendation of this MerchantShipmentLabelCarrierResponse.


        :param recommendation: The recommendation of this MerchantShipmentLabelCarrierResponse.  # noqa: E501
        :type: ChannelCarrierRecommendationApi
        """

        self._recommendation = recommendation

    @property
    def collection_method(self):
        """Gets the collection_method of this MerchantShipmentLabelCarrierResponse.  # noqa: E501


        :return: The collection_method of this MerchantShipmentLabelCarrierResponse.  # noqa: E501
        :rtype: ChannelCarrierCollectionMethodApi
        """
        return self._collection_method

    @collection_method.setter
    def collection_method(self, collection_method):
        """Sets the collection_method of this MerchantShipmentLabelCarrierResponse.


        :param collection_method: The collection_method of this MerchantShipmentLabelCarrierResponse.  # noqa: E501
        :type: ChannelCarrierCollectionMethodApi
        """

        self._collection_method = collection_method

    @property
    def handover_date_time(self):
        """Gets the handover_date_time of this MerchantShipmentLabelCarrierResponse.  # noqa: E501

        Optional. When to handover the package to the carrier  It is in the ISO format including the timezone offset.  E.g. 2020-10-03T18:00:00+02:00  which is 3rd Oct 2020, at 18:00 PM in Amsterdam (Summer Time aka CEST: UTC +2:00 )  # noqa: E501

        :return: The handover_date_time of this MerchantShipmentLabelCarrierResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._handover_date_time

    @handover_date_time.setter
    def handover_date_time(self, handover_date_time):
        """Sets the handover_date_time of this MerchantShipmentLabelCarrierResponse.

        Optional. When to handover the package to the carrier  It is in the ISO format including the timezone offset.  E.g. 2020-10-03T18:00:00+02:00  which is 3rd Oct 2020, at 18:00 PM in Amsterdam (Summer Time aka CEST: UTC +2:00 )  # noqa: E501

        :param handover_date_time: The handover_date_time of this MerchantShipmentLabelCarrierResponse.  # noqa: E501
        :type: datetime
        """

        self._handover_date_time = handover_date_time

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
        if issubclass(MerchantShipmentLabelCarrierResponse, dict):
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
        if not isinstance(other, MerchantShipmentLabelCarrierResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
