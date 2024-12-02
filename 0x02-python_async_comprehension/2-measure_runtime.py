#!/usr/bin/env python3
"""
Module to measure the runtime of four parallel async comprehensions.
"""
import asyncio
from typing import Callable
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and measures the runtime.

    Returns:
        float: Total runtime for the parallel execution.
    """
    start = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = asyncio.get_event_loop().time()
    return end - start
