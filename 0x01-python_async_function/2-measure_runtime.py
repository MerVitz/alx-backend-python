#!/usr/bin/env python3
"""
This module measures the runtime of wait_n.
"""
import time
import asyncio
from 1-concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n and returns the average time.
    Args:
        n (int): Number of coroutines to execute.
        max_delay (int): Maximum delay in seconds.
    Returns:
        float: Average runtime per coroutine.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n

