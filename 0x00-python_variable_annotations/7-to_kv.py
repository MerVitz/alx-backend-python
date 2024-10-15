#!/usr/bin/env python3
"""
This module provides a function that creates a tuple from a string and an int/float.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is a string `k` and the second
    element is the square of the int/float `v` (as a float).

    :param k: The string
    :param v: The int or float
    :return: A tuple containing the string and the squared value of `v`
    """
    return (k, float(v ** 2))

