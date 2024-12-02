#!/usr/bin/env python3
"""
Module that defines an asynchronous generator.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    Loops 10 times, waiting 1 second before yielding each random number.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Ensures 1-second delay in each iteration
        yield random.uniform(0, 10)
