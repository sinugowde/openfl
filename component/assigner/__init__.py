# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""Assigner package."""

from .assigner import Assigner
from .random_grouped_assigner import RandomGroupedAssigner
from .static_grouped_assigner import StaticGroupedAssigner

from logging import getLogger
logger = getLogger(__name__)
logger.debug(f'** in function: __init__')

__all__ = [
    'Assigner',
    'RandomGroupedAssigner',
    'StaticGroupedAssigner',
]
