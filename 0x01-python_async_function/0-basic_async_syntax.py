#!/usr/bin/env python3
'''
The basics of async
'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
    async coroutine that takes an int and waits a random delay
    '''
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
