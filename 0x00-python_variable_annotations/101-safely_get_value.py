#!/usr/bin/env python3
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary, returning a default if the key is missing.

    Args:
        dct: A dictionary with any key-value types.
        key: The key to retrieve from the dictionary.
        default: The default value to return if key is not in the dictionary.
    
    Returns:
        The value associated with the key, or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

