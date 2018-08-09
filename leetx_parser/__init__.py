"""leetx_parser - Find magnet links for TV show episodes"""

__version__ = '0.2.0'
__author__ = 'Evgeny Lobanov <evgeny1602@gmail.com>'
__all__ = []

from .leetx_parser import Leetx_parser

import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
