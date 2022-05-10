# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
"""Serializer plugin interface."""

from logging import getLogger
logger = getLogger(__name__)

class Serializer:
    """Serializer API plugin."""

    def __init__(self) -> None:
        """Initialize serializer."""
        logger.debug(f'** in function: Serializer:__init__')
        pass

    @staticmethod
    def serialize(object_, filename):
        """Serialize an object and save to disk."""
        logger.debug(f'** in function: Serializer:serialize')
        raise NotImplementedError

    @staticmethod
    def restore_object(filename):
        """Load and deserialize an object."""
        logger.debug(f'** in function: Serializer:restore_object')
        raise NotImplementedError
