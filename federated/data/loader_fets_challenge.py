# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""PyTorchDataLoader module."""

from math import ceil, fabs

import numpy as np

from .loader import DataLoader

from logging import getLogger
logger = getLogger(__name__)


class FeTSChallengeDataLoaderWrapper(DataLoader):
    """Federation Data Loader for FeTS Challenge Model."""

    def __init__(self, data_path, feature_shape):
        logger.debug(f'** in function: FeTSChallengeDataLoaderWrapper:__init__')
        self.train_dataloader = None
        self.val_dataloader = None
        self.feature_shape = feature_shape

    def set_dataloaders(self, train_dataloader, val_dataloader):
        logger.debug(f'** in function: FeTSChallengeDataLoaderWrapper:set_dataloaders')
        self.train_dataloader = train_dataloader
        self.val_dataloader = val_dataloader

    def get_feature_shape(self):
        """Get the shape of an example feature array.

        Returns:
            tuple: shape of an example feature array
        """
        logger.debug(f'** in function: FeTSChallengeDataLoaderWrapper:get_feature_shape')
        return self.feature_shape

    def get_train_loader(self, batch_size=None, num_batches=None):
        """
        Get training data loader.

        Returns
        -------
        loader object
        """
        logger.debug(f'** in function: FeTSChallengeDataLoaderWrapper:get_train_loader')
        return self.train_dataloader

    def get_valid_loader(self, batch_size=None):
        """
        Get validation data loader.

        Returns:
            loader object
        """
        logger.debug(f'** in function: FeTSChallengeDataLoaderWrapper:get_valid_loader')
        return self.val_dataloader

    def get_train_data_size(self):
        """
        Get total number of training samples.

        Returns:
            int: number of training samples
        """
        logger.debug(f'** in function: FeTSChallengeDataLoaderWrapper:get_train_data_size')
        return len(self.train_dataloader.dataset)

    def get_valid_data_size(self):
        """
        Get total number of validation samples.

        Returns:
            int: number of validation samples
        """
        logger.debug(f'** in function: FeTSChallengeDataLoaderWrapper:get_valid_data_size')
        return len(self.val_dataloader.dataset)
