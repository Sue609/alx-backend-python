#!/usr/bin/env python3
'''
Run time for four parallel comprehensions
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    '''
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
