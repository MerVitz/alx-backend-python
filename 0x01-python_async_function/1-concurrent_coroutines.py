#!/usr/bin/env python3
"""
This module spawns wait_random n times and returns the list of delays.
"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.
    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)

