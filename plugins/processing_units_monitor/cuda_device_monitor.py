# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
"""CUDA Device monitor plugin module."""

from .device_monitor import DeviceMonitor

from logging import getLogger
logger = getLogger(__name__)

class CUDADeviceMonitor(DeviceMonitor):
    """CUDA Device monitor plugin."""

    def get_driver_version(self) -> str:
        """Get CUDA driver version."""
        logger.debug(f'** in function: CUDADeviceMonitor:get_driver_version')
        raise NotImplementedError

    def get_device_memory_total(self, index: int) -> int:
        """Get total memory available on the device."""
        logger.debug(f'** in function: CUDADeviceMonitor:get_device_memory_total')
        raise NotImplementedError

    def get_device_memory_utilized(self, index: int) -> int:
        """Get utilized memory on the device."""
        logger.debug(f'** in function: CUDADeviceMonitor:get_device_memory_utilized')
        raise NotImplementedError

    def get_device_utilization(self, index: int) -> str:
        """
        Get device utilization.

        It is just a general method that returns a string that may be shown to the frontend user.
        """
        logger.debug(f'** in function: CUDADeviceMonitor:get_device_utilization')
        raise NotImplementedError

    def get_device_name(self, index: int) -> str:
        """Get device name."""
        logger.debug(f'** in function: CUDADeviceMonitor:get_device_name')
        raise NotImplementedError

    def get_cuda_version(self) -> str:
        """Get CUDA driver version."""
        logger.debug(f'** in function: CUDADeviceMonitor:get_cuda_version')
        raise NotImplementedError
