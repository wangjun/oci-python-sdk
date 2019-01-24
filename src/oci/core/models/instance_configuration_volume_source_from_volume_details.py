# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .instance_configuration_volume_source_details import InstanceConfigurationVolumeSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationVolumeSourceFromVolumeDetails(InstanceConfigurationVolumeSourceDetails):
    """
    Specifies the source volume.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationVolumeSourceFromVolumeDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.InstanceConfigurationVolumeSourceFromVolumeDetails.type` attribute
        of this class is ``volume`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this InstanceConfigurationVolumeSourceFromVolumeDetails.
        :type type: str

        :param id:
            The value to assign to the id property of this InstanceConfigurationVolumeSourceFromVolumeDetails.
        :type id: str

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id'
        }

        self._type = None
        self._id = None
        self._type = 'volume'

    @property
    def id(self):
        """
        Gets the id of this InstanceConfigurationVolumeSourceFromVolumeDetails.
        The OCID of the volume.


        :return: The id of this InstanceConfigurationVolumeSourceFromVolumeDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstanceConfigurationVolumeSourceFromVolumeDetails.
        The OCID of the volume.


        :param id: The id of this InstanceConfigurationVolumeSourceFromVolumeDetails.
        :type: str
        """
        self._id = id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other