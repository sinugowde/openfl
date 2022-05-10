# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
"""Dill serializer plugin."""

import dill

from .serializer_interface import Serializer

from logging import getLogger
logger = getLogger(__name__)

class DillSerializer(Serializer):
    """Serializer API plugin."""

    def __init__(self) -> None:
        """Initialize serializer."""
        super().__init__()
        logger.debug(f'** in function: DillSerializer:__init__')

    @staticmethod
    def serialize(object_, filename):
        """Serialize an object and save to disk."""
        logger.debug(f'** in function: DillSerializer:serialize')
        with open(filename, 'wb') as f:
            dill.dump(object_, f, recurse=True)

    @staticmethod
    def restore_object(filename):
        """Load and deserialize an object."""
        logger.debug(f'** in function: DillSerializer:restore_object')
        with open(filename, 'rb') as f:
            return dill.load(f)
