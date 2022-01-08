# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 12:33:41 2022

@author: apan

this is logging sample pro.

"""

from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

logger.debug('hello')
