#!/usr/bin/env python3
"""
This module provides a function that returns another function to multiply a float by a given multiplier.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    :param multiplier: The float value to multiply by
    :return: A function that takes a float and multiplies it by the multiplier
    """
    return lambda x: x * multiplier

