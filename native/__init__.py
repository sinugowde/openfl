# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
"""openfl.native package."""

from .native import *  # NOQA

from logging import getLogger
logger = getLogger(__name__)
logger.debug(f'** in function: __init__')