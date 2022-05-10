# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
"""Click types module."""

import click

from openfl.utilities import utils

from logging import getLogger
logger = getLogger(__name__)


class FqdnParamType(click.ParamType):
    """Domain Type for click arguments."""

    name = 'fqdn'

    def convert(self, value, param, ctx):
        """Validate value, if value is valid, return it."""
        logger.debug(f'** in function: FqdnParamType:convert')
        if not utils.is_fqdn(value):
            self.fail(f'{value} is not a valid domain name', param, ctx)
        return value


class IpAddressParamType(click.ParamType):
    """IpAddress Type for click arguments."""

    name = 'IpAddress type'

    def convert(self, value, param, ctx):
        """Validate value, if value is valid, return it."""
        logger.debug(f'** in function: IpAddressParamType:convert')
        if not utils.is_api_adress(value):
            self.fail(f'{value} is not a valid ip adress name', param, ctx)
        return value


FQDN = FqdnParamType()
IP_ADDRESS = IpAddressParamType()
