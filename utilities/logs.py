# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

"""Logs utilities."""

import logging

from rich.console import Console
from rich.logging import RichHandler
from tensorboardX import SummaryWriter

from logging import getLogger
logger = getLogger(__name__)


writer = None


def get_writer():
    """Create global writer object."""
    logger.debug(f'** in function: get_writer')
    global writer
    if not writer:
        writer = SummaryWriter('./logs/tensorboard', flush_secs=5)


def write_metric(node_name, task_name, metric_name, metric, round_number):
    """Write metric callback."""
    logger.debug(f'** in function: write_metric')
    get_writer()
    writer.add_scalar(f'{node_name}/{task_name}/{metric_name}', metric, round_number)


def setup_loggers(log_level=logging.INFO):
    """Configure loggers."""
    logger.debug(f'** in function: setup_loggers')
    root = logging.getLogger()
    root.setLevel(log_level)
    console = Console(width=160)
    handler = RichHandler(console=console)
    formatter = logging.Formatter(
        '[%(asctime)s][%(name)s][%(levelname)s] - %(message)s'
    )
    handler.setFormatter(formatter)
    root.addHandler(handler)
