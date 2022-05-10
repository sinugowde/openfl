# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
"""Cloudpickle serializer plugin."""

import cloudpickle

from .serializer_interface import Serializer

from logging import getLogger
logger = getLogger(__name__)

class CloudpickleSerializer(Serializer):
    """Serializer API plugin."""

    def __init__(self) -> None:
        """Initialize serializer."""
        super().__init__()
        logger.debug(f'** in function: CloudpickleSerializer:__init__')

    @staticmethod
    def serialize(object_, filename):
        """Serialize an object and save to disk."""
        logger.debug(f'** in function: CloudpickleSerializer:serialize')
        with open(filename, 'wb') as f:
            cloudpickle.dump(object_, f)

    @staticmethod
    def restore_object(filename):
        """Load and deserialize an object."""
        
        logger.debug(f'** in function: CloudpickleSerializer:restore_object')
        with open(filename, 'rb') as f:
            return cloudpickle.load(f)
