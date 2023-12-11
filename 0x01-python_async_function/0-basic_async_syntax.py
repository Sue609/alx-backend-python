#!/usr/bin/env python3
'''
The basics of async
'''
import random
import asyncio


async def wait_random(max_delay=10):
    '''
    async coroutine that takes an int and waits a random delay
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
