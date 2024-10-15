#!/usr/bin/env python3
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence if it exists, else return None.

    Args:
        lst: A sequence of any type.
    
    Returns:
        The first element of lst, or None if lst is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

