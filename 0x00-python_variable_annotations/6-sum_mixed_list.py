#!/usr/bin/env python3
"""
This module provides a function that sums a list of integers and floats.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floats and returns the result as a float.

    :param mxd_lst: A list of integers and floats
    :return: The sum of the list as a float
    """
    return sum(mxd_lst)

