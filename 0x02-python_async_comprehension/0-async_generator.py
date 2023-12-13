#!/usr/bin/env python3
'''
coroutine called async generator that takes no arguements.
'''


import asyncio
import random


async def async_generator():
    '''
    an async generator that takes no arguement.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
