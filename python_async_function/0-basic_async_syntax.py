#!/usr/bin/env python3
"""The basics of async functions"""

import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return the delay time.

    Args:
        max_delay (int): The maximum delay time in seconds. Defaults to 10.

    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
