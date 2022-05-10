# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""Aggregation functions package."""

from .adagrad_adaptive_aggregation import AdagradAdaptiveAggregation
from .adam_adaptive_aggregation import AdamAdaptiveAggregation
from .core import AggregationFunction
from .experimental import PrivilegedAggregationFunction
from .fedcurv_weighted_average import FedCurvWeightedAverage
from .geometric_median import GeometricMedian
from .median import Median
from .weighted_average import WeightedAverage
from .yogi_adaptive_aggregation import YogiAdaptiveAggregation

from logging import getLogger
logger = getLogger(__name__)
logger.debug(f'** in function: __init__')

__all__ = ['Median',
           'WeightedAverage',
           'GeometricMedian',
           'AdagradAdaptiveAggregation',
           'AdamAdaptiveAggregation',
           'YogiAdaptiveAggregation',
           'AggregationFunction',
           'PrivilegedAggregationFunction',
           'FedCurvWeightedAverage']
