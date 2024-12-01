#!/usr/bin/env python3
"""
Module that defines an asynchronous generator.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    Loops 10 times, waiting 1 second before yielding each random number.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

