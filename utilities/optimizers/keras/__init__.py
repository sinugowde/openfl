# Copyright (C) 2021-2022 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""Keras optimizers package."""
import pkgutil

from logging import getLogger
logger = getLogger(__name__)
logger.debug(f'** in function: __init__')

if pkgutil.find_loader('tensorflow'):
    from .fedprox import FedProxOptimizer # NOQA
