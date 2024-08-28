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

class ChannelListedProductResponse(object):
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
        'channel_product_no': 'str',
        'channel_status': 'ListedProductChannelStatus',
        'ean': 'str',
        'export_status': 'ListedProductExportStatus',
        'merchant_product_no': 'str',
        'last_exported_price': 'float',
        'last_exported_stock': 'int'
    }

    attribute_map = {
        'channel_product_no': 'ChannelProductNo',
        'channel_status': 'ChannelStatus',
        'ean': 'Ean',
        'export_status': 'ExportStatus',
        'merchant_product_no': 'MerchantProductNo',
        'last_exported_price': 'LastExportedPrice',
        'last_exported_stock': 'LastExportedStock'
    }

    def __init__(self, channel_product_no=None, channel_status=None, ean=None, export_status=None, merchant_product_no=None, last_exported_price=None, last_exported_stock=None):  # noqa: E501
        """ChannelListedProductResponse - a model defined in Swagger"""  # noqa: E501
        self._channel_product_no = None
        self._channel_status = None
        self._ean = None
        self._export_status = None
        self._merchant_product_no = None
        self._last_exported_price = None
        self._last_exported_stock = None
        self.discriminator = None
        if channel_product_no is not None:
            self.channel_product_no = channel_product_no
        if channel_status is not None:
            self.channel_status = channel_status
        if ean is not None:
            self.ean = ean
        if export_status is not None:
            self.export_status = export_status
        if merchant_product_no is not None:
            self.merchant_product_no = merchant_product_no
        if last_exported_price is not None:
            self.last_exported_price = last_exported_price
        if last_exported_stock is not None:
            self.last_exported_stock = last_exported_stock

    @property
    def channel_product_no(self):
        """Gets the channel_product_no of this ChannelListedProductResponse.  # noqa: E501

        The unique product reference used by the Channel  # noqa: E501

        :return: The channel_product_no of this ChannelListedProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._channel_product_no

    @channel_product_no.setter
    def channel_product_no(self, channel_product_no):
        """Sets the channel_product_no of this ChannelListedProductResponse.

        The unique product reference used by the Channel  # noqa: E501

        :param channel_product_no: The channel_product_no of this ChannelListedProductResponse.  # noqa: E501
        :type: str
        """

        self._channel_product_no = channel_product_no

    @property
    def channel_status(self):
        """Gets the channel_status of this ChannelListedProductResponse.  # noqa: E501


        :return: The channel_status of this ChannelListedProductResponse.  # noqa: E501
        :rtype: ListedProductChannelStatus
        """
        return self._channel_status

    @channel_status.setter
    def channel_status(self, channel_status):
        """Sets the channel_status of this ChannelListedProductResponse.


        :param channel_status: The channel_status of this ChannelListedProductResponse.  # noqa: E501
        :type: ListedProductChannelStatus
        """

        self._channel_status = channel_status

    @property
    def ean(self):
        """Gets the ean of this ChannelListedProductResponse.  # noqa: E501

        EAN  # noqa: E501

        :return: The ean of this ChannelListedProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._ean

    @ean.setter
    def ean(self, ean):
        """Sets the ean of this ChannelListedProductResponse.

        EAN  # noqa: E501

        :param ean: The ean of this ChannelListedProductResponse.  # noqa: E501
        :type: str
        """

        self._ean = ean

    @property
    def export_status(self):
        """Gets the export_status of this ChannelListedProductResponse.  # noqa: E501


        :return: The export_status of this ChannelListedProductResponse.  # noqa: E501
        :rtype: ListedProductExportStatus
        """
        return self._export_status

    @export_status.setter
    def export_status(self, export_status):
        """Sets the export_status of this ChannelListedProductResponse.


        :param export_status: The export_status of this ChannelListedProductResponse.  # noqa: E501
        :type: ListedProductExportStatus
        """

        self._export_status = export_status

    @property
    def merchant_product_no(self):
        """Gets the merchant_product_no of this ChannelListedProductResponse.  # noqa: E501

        Your product number (SKU)  # noqa: E501

        :return: The merchant_product_no of this ChannelListedProductResponse.  # noqa: E501
        :rtype: str
        """
        return self._merchant_product_no

    @merchant_product_no.setter
    def merchant_product_no(self, merchant_product_no):
        """Sets the merchant_product_no of this ChannelListedProductResponse.

        Your product number (SKU)  # noqa: E501

        :param merchant_product_no: The merchant_product_no of this ChannelListedProductResponse.  # noqa: E501
        :type: str
        """

        self._merchant_product_no = merchant_product_no

    @property
    def last_exported_price(self):
        """Gets the last_exported_price of this ChannelListedProductResponse.  # noqa: E501

        Your product last exported price  # noqa: E501

        :return: The last_exported_price of this ChannelListedProductResponse.  # noqa: E501
        :rtype: float
        """
        return self._last_exported_price

    @last_exported_price.setter
    def last_exported_price(self, last_exported_price):
        """Sets the last_exported_price of this ChannelListedProductResponse.

        Your product last exported price  # noqa: E501

        :param last_exported_price: The last_exported_price of this ChannelListedProductResponse.  # noqa: E501
        :type: float
        """

        self._last_exported_price = last_exported_price

    @property
    def last_exported_stock(self):
        """Gets the last_exported_stock of this ChannelListedProductResponse.  # noqa: E501

        Your product last exported stock  # noqa: E501

        :return: The last_exported_stock of this ChannelListedProductResponse.  # noqa: E501
        :rtype: int
        """
        return self._last_exported_stock

    @last_exported_stock.setter
    def last_exported_stock(self, last_exported_stock):
        """Sets the last_exported_stock of this ChannelListedProductResponse.

        Your product last exported stock  # noqa: E501

        :param last_exported_stock: The last_exported_stock of this ChannelListedProductResponse.  # noqa: E501
        :type: int
        """

        self._last_exported_stock = last_exported_stock

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
        if issubclass(ChannelListedProductResponse, dict):
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
        if not isinstance(other, ChannelListedProductResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other