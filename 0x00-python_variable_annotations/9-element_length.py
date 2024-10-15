#!/usr/bin/env python3
"""
This module provides a function that returns a list of tuples with elements and their lengths.
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    each containing a sequence and its length.

    :param lst: An iterable of sequences
    :return: A list of tuples with sequences and their lengths
    """
    return [(i, len(i)) for i in lst]

