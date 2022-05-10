# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""NoCompressionPipeline module."""

from .pipeline import Float32NumpyArrayToBytes
from .pipeline import TransformationPipeline


from logging import getLogger
logger = getLogger(__name__)


class NoCompressionPipeline(TransformationPipeline):
    """The data pipeline without any compression."""

    def __init__(self, **kwargs):
        """Initialize."""
        logger.debug(f'** in function: NoCompressionPipeline:__init__')
        super(NoCompressionPipeline, self).__init__(
            transformers=[Float32NumpyArrayToBytes()], **kwargs)
