#!/usr/bin/env python3
from typing import List, Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zoom in on an array by repeating its elements according to the zoom factor.

    Args:
        lst: A tuple of integers to zoom into.
        factor: The number of times to repeat each element.
    
    Returns:
        A list of integers where each element in lst is repeated `factor` times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

