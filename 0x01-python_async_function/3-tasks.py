#!/usr/bin/env python3
"""
This module creates an asyncio task for wait_random.
"""
import asyncio
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio task for wait_random.
    Args:
        max_delay (int): Maximum delay in seconds.
    Returns:
        asyncio.Task: An asyncio task.
    """
    return asyncio.create_task(wait_random(max_delay))

