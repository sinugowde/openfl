# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
"""Device monitor plugin module."""

from logging import getLogger
logger = getLogger(__name__)

class DeviceMonitor:
    """Device monitor plugin interface."""

    def get_driver_version(self) -> str:
        """Get device's driver version."""
        logger.debug(f'** in function: DeviceMonitor:get_driver_version')
        raise NotImplementedError

    def get_device_utilization(self, index: int) -> str:
        """
        Get device utilization method.

        It is just a general method that returns a string that may be shown to the frontend user.
        """
        logger.debug(f'** in function: DeviceMonitor:get_device_utilization')
        raise NotImplementedError
