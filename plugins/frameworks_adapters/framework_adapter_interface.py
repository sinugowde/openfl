# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
"""Framework Adapter plugin interface."""

from logging import getLogger
logger = getLogger(__name__)


class FrameworkAdapterPluginInterface:
    """Framework adapter plugin class."""

    def __init__(self) -> None:
        """Initialize framework adapter."""
        logger.debug(f'** in function: FrameworkAdapterPluginInterface:__init__')
        pass

    @staticmethod
    def serialization_setup():
        """Prepare model for serialization (optional)."""
        logger.debug(f'** in function: FrameworkAdapterPluginInterface:serialization_setup')
        pass

    @staticmethod
    def get_tensor_dict(model, optimizer=None) -> dict:
        """
        Extract tensor dict from a model and an optimizer.

        Returns:
        dict {weight name: numpy ndarray}
        """
        logger.debug(f'** in function: FrameworkAdapterPluginInterface:get_tensor_dict')
        raise NotImplementedError

    @staticmethod
    def set_tensor_dict(model, tensor_dict, optimizer=None, device='cpu'):
        """
        Set tensor dict from a model and an optimizer.

        Given a dict {weight name: numpy ndarray} sets weights to
        the model and optimizer objects inplace.
        """
        logger.debug(f'** in function: FrameworkAdapterPluginInterface:set_tensor_dict')
        raise NotImplementedError
