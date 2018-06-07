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


class NetworkDeviceDetailResponseResponse(object):
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
        'management_ip_addr': 'str',
        'serial_number': 'str',
        'nw_device_name': 'str',
        'op_state': 'str',
        'platform_id': 'str',
        'nw_device_id': 'str',
        'sys_uptime': 'str',
        'mode': 'str',
        'reset_reason': 'str',
        'nw_device_role': 'str',
        'up_time': 'str',
        'nw_device_family': 'str',
        'mac_address': 'str',
        'connected_time': 'str',
        'software_version': 'str',
        'sub_mode': 'str',
        'nw_device_type': 'str',
        'overall_health': 'str',
        'memory_score': 'str',
        'cpu_score': 'str'
    }

    attribute_map = {
        'management_ip_addr': 'managementIpAddr',
        'serial_number': 'serialNumber',
        'nw_device_name': 'nwDeviceName',
        'op_state': 'opState',
        'platform_id': 'platformId',
        'nw_device_id': 'nwDeviceId',
        'sys_uptime': 'sysUptime',
        'mode': 'mode',
        'reset_reason': 'resetReason',
        'nw_device_role': 'nwDeviceRole',
        'up_time': 'upTime',
        'nw_device_family': 'nwDeviceFamily',
        'mac_address': 'macAddress',
        'connected_time': 'connectedTime',
        'software_version': 'softwareVersion',
        'sub_mode': 'subMode',
        'nw_device_type': 'nwDeviceType',
        'overall_health': 'overallHealth',
        'memory_score': 'memoryScore',
        'cpu_score': 'cpuScore'
    }

    def __init__(self, management_ip_addr=None, serial_number=None, nw_device_name=None, op_state=None, platform_id=None, nw_device_id=None, sys_uptime=None, mode=None, reset_reason=None, nw_device_role=None, up_time=None, nw_device_family=None, mac_address=None, connected_time=None, software_version=None, sub_mode=None, nw_device_type=None, overall_health=None, memory_score=None, cpu_score=None):  # noqa: E501
        """NetworkDeviceDetailResponseResponse - a model defined in Swagger"""  # noqa: E501

        self._management_ip_addr = None
        self._serial_number = None
        self._nw_device_name = None
        self._op_state = None
        self._platform_id = None
        self._nw_device_id = None
        self._sys_uptime = None
        self._mode = None
        self._reset_reason = None
        self._nw_device_role = None
        self._up_time = None
        self._nw_device_family = None
        self._mac_address = None
        self._connected_time = None
        self._software_version = None
        self._sub_mode = None
        self._nw_device_type = None
        self._overall_health = None
        self._memory_score = None
        self._cpu_score = None
        self.discriminator = None

        if management_ip_addr is not None:
            self.management_ip_addr = management_ip_addr
        if serial_number is not None:
            self.serial_number = serial_number
        if nw_device_name is not None:
            self.nw_device_name = nw_device_name
        if op_state is not None:
            self.op_state = op_state
        if platform_id is not None:
            self.platform_id = platform_id
        if nw_device_id is not None:
            self.nw_device_id = nw_device_id
        if sys_uptime is not None:
            self.sys_uptime = sys_uptime
        if mode is not None:
            self.mode = mode
        if reset_reason is not None:
            self.reset_reason = reset_reason
        if nw_device_role is not None:
            self.nw_device_role = nw_device_role
        if up_time is not None:
            self.up_time = up_time
        if nw_device_family is not None:
            self.nw_device_family = nw_device_family
        if mac_address is not None:
            self.mac_address = mac_address
        if connected_time is not None:
            self.connected_time = connected_time
        if software_version is not None:
            self.software_version = software_version
        if sub_mode is not None:
            self.sub_mode = sub_mode
        if nw_device_type is not None:
            self.nw_device_type = nw_device_type
        if overall_health is not None:
            self.overall_health = overall_health
        if memory_score is not None:
            self.memory_score = memory_score
        if cpu_score is not None:
            self.cpu_score = cpu_score

    @property
    def management_ip_addr(self):
        """Gets the management_ip_addr of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The management_ip_addr of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._management_ip_addr

    @management_ip_addr.setter
    def management_ip_addr(self, management_ip_addr):
        """Sets the management_ip_addr of this NetworkDeviceDetailResponseResponse.


        :param management_ip_addr: The management_ip_addr of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._management_ip_addr = management_ip_addr

    @property
    def serial_number(self):
        """Gets the serial_number of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The serial_number of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this NetworkDeviceDetailResponseResponse.


        :param serial_number: The serial_number of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def nw_device_name(self):
        """Gets the nw_device_name of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The nw_device_name of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._nw_device_name

    @nw_device_name.setter
    def nw_device_name(self, nw_device_name):
        """Sets the nw_device_name of this NetworkDeviceDetailResponseResponse.


        :param nw_device_name: The nw_device_name of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._nw_device_name = nw_device_name

    @property
    def op_state(self):
        """Gets the op_state of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The op_state of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._op_state

    @op_state.setter
    def op_state(self, op_state):
        """Sets the op_state of this NetworkDeviceDetailResponseResponse.


        :param op_state: The op_state of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._op_state = op_state

    @property
    def platform_id(self):
        """Gets the platform_id of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The platform_id of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        """Sets the platform_id of this NetworkDeviceDetailResponseResponse.


        :param platform_id: The platform_id of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._platform_id = platform_id

    @property
    def nw_device_id(self):
        """Gets the nw_device_id of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The nw_device_id of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._nw_device_id

    @nw_device_id.setter
    def nw_device_id(self, nw_device_id):
        """Sets the nw_device_id of this NetworkDeviceDetailResponseResponse.


        :param nw_device_id: The nw_device_id of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._nw_device_id = nw_device_id

    @property
    def sys_uptime(self):
        """Gets the sys_uptime of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The sys_uptime of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._sys_uptime

    @sys_uptime.setter
    def sys_uptime(self, sys_uptime):
        """Sets the sys_uptime of this NetworkDeviceDetailResponseResponse.


        :param sys_uptime: The sys_uptime of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._sys_uptime = sys_uptime

    @property
    def mode(self):
        """Gets the mode of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The mode of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this NetworkDeviceDetailResponseResponse.


        :param mode: The mode of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def reset_reason(self):
        """Gets the reset_reason of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The reset_reason of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._reset_reason

    @reset_reason.setter
    def reset_reason(self, reset_reason):
        """Sets the reset_reason of this NetworkDeviceDetailResponseResponse.


        :param reset_reason: The reset_reason of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._reset_reason = reset_reason

    @property
    def nw_device_role(self):
        """Gets the nw_device_role of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The nw_device_role of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._nw_device_role

    @nw_device_role.setter
    def nw_device_role(self, nw_device_role):
        """Sets the nw_device_role of this NetworkDeviceDetailResponseResponse.


        :param nw_device_role: The nw_device_role of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._nw_device_role = nw_device_role

    @property
    def up_time(self):
        """Gets the up_time of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The up_time of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._up_time

    @up_time.setter
    def up_time(self, up_time):
        """Sets the up_time of this NetworkDeviceDetailResponseResponse.


        :param up_time: The up_time of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._up_time = up_time

    @property
    def nw_device_family(self):
        """Gets the nw_device_family of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The nw_device_family of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._nw_device_family

    @nw_device_family.setter
    def nw_device_family(self, nw_device_family):
        """Sets the nw_device_family of this NetworkDeviceDetailResponseResponse.


        :param nw_device_family: The nw_device_family of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._nw_device_family = nw_device_family

    @property
    def mac_address(self):
        """Gets the mac_address of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The mac_address of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this NetworkDeviceDetailResponseResponse.


        :param mac_address: The mac_address of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def connected_time(self):
        """Gets the connected_time of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The connected_time of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """Sets the connected_time of this NetworkDeviceDetailResponseResponse.


        :param connected_time: The connected_time of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._connected_time = connected_time

    @property
    def software_version(self):
        """Gets the software_version of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The software_version of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """Sets the software_version of this NetworkDeviceDetailResponseResponse.


        :param software_version: The software_version of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._software_version = software_version

    @property
    def sub_mode(self):
        """Gets the sub_mode of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The sub_mode of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._sub_mode

    @sub_mode.setter
    def sub_mode(self, sub_mode):
        """Sets the sub_mode of this NetworkDeviceDetailResponseResponse.


        :param sub_mode: The sub_mode of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._sub_mode = sub_mode

    @property
    def nw_device_type(self):
        """Gets the nw_device_type of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The nw_device_type of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._nw_device_type

    @nw_device_type.setter
    def nw_device_type(self, nw_device_type):
        """Sets the nw_device_type of this NetworkDeviceDetailResponseResponse.


        :param nw_device_type: The nw_device_type of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._nw_device_type = nw_device_type

    @property
    def overall_health(self):
        """Gets the overall_health of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The overall_health of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._overall_health

    @overall_health.setter
    def overall_health(self, overall_health):
        """Sets the overall_health of this NetworkDeviceDetailResponseResponse.


        :param overall_health: The overall_health of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._overall_health = overall_health

    @property
    def memory_score(self):
        """Gets the memory_score of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The memory_score of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._memory_score

    @memory_score.setter
    def memory_score(self, memory_score):
        """Sets the memory_score of this NetworkDeviceDetailResponseResponse.


        :param memory_score: The memory_score of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._memory_score = memory_score

    @property
    def cpu_score(self):
        """Gets the cpu_score of this NetworkDeviceDetailResponseResponse.  # noqa: E501


        :return: The cpu_score of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._cpu_score

    @cpu_score.setter
    def cpu_score(self, cpu_score):
        """Sets the cpu_score of this NetworkDeviceDetailResponseResponse.


        :param cpu_score: The cpu_score of this NetworkDeviceDetailResponseResponse.  # noqa: E501
        :type: str
        """

        self._cpu_score = cpu_score

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
        if not isinstance(other, NetworkDeviceDetailResponseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other