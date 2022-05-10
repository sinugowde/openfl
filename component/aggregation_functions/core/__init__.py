# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""Aggregation functions core package."""

from .adaptive_aggregation import AdaptiveAggregation
from .interface import AggregationFunction

from logging import getLogger
logger = getLogger(__name__)
logger.debug(f'** in function: __init__')


__all__ = ['AggregationFunction',
           'AdaptiveAggregation']
