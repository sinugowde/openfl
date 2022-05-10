# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""Databases package."""

from .tensor_db import TensorDB

from logging import getLogger
logger = getLogger(__name__)
logger.debug(f'** in function: __init__')

__all__ = [
    'TensorDB',
]
