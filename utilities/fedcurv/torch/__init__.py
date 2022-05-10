# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
"""openfl.utilities.fedcurv.torch package."""
from .fedcurv import FedCurv  # NOQA

from logging import getLogger
logger = getLogger(__name__)
logger.debug(f'** in function: __init__')