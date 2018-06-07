# coding: utf-8

"""
    Swagger

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DeviceInnerDeviceInfoPrimaryEndpoint(object):
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
        'certificate': 'str',
        'fqdn': 'str',
        'ipv4_address': 'object',
        'ipv6_address': 'object',
        'port': 'int',
        'protocol': 'str'
    }

    attribute_map = {
        'certificate': 'certificate',
        'fqdn': 'fqdn',
        'ipv4_address': 'ipv4Address',
        'ipv6_address': 'ipv6Address',
        'port': 'port',
        'protocol': 'protocol'
    }

    def __init__(self, certificate=None, fqdn=None, ipv4_address=None, ipv6_address=None, port=None, protocol=None):  # noqa: E501
        """DeviceInnerDeviceInfoPrimaryEndpoint - a model defined in Swagger"""  # noqa: E501

        self._certificate = None
        self._fqdn = None
        self._ipv4_address = None
        self._ipv6_address = None
        self._port = None
        self._protocol = None
        self.discriminator = None

        if certificate is not None:
            self.certificate = certificate
        if fqdn is not None:
            self.fqdn = fqdn
        if ipv4_address is not None:
            self.ipv4_address = ipv4_address
        if ipv6_address is not None:
            self.ipv6_address = ipv6_address
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol

    @property
    def certificate(self):
        """Gets the certificate of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501


        :return: The certificate of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this DeviceInnerDeviceInfoPrimaryEndpoint.


        :param certificate: The certificate of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501
        :type: str
        """

        self._certificate = certificate

    @property
    def fqdn(self):
        """Gets the fqdn of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501


        :return: The fqdn of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this DeviceInnerDeviceInfoPrimaryEndpoint.


        :param fqdn: The fqdn of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501
        :type: str
        """

        self._fqdn = fqdn

    @property
    def ipv4_address(self):
        """Gets the ipv4_address of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501


        :return: The ipv4_address of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501
        :rtype: object
        """
        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, ipv4_address):
        """Sets the ipv4_address of this DeviceInnerDeviceInfoPrimaryEndpoint.


        :param ipv4_address: The ipv4_address of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501
        :type: object
        """

        self._ipv4_address = ipv4_address

    @property
    def ipv6_address(self):
        """Gets the ipv6_address of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501


        :return: The ipv6_address of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501
        :rtype: object
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """Sets the ipv6_address of this DeviceInnerDeviceInfoPrimaryEndpoint.


        :param ipv6_address: The ipv6_address of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501
        :type: object
        """

        self._ipv6_address = ipv6_address

    @property
    def port(self):
        """Gets the port of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501


        :return: The port of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DeviceInnerDeviceInfoPrimaryEndpoint.


        :param port: The port of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501


        :return: The protocol of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this DeviceInnerDeviceInfoPrimaryEndpoint.


        :param protocol: The protocol of this DeviceInnerDeviceInfoPrimaryEndpoint.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeviceInnerDeviceInfoPrimaryEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other