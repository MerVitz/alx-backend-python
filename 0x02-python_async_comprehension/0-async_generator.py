#!/usr/bin/env python3
"""
Module that defines an asynchronous comprehension.
"""
from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using async comprehension.

    Returns:
        List[float]: List of 10 random numbers.
    """
    return [number async for number in async_generator()]
