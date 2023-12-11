#!/usr/bin/env python
'''
executing multiple coroutines at the same time with async
'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    '''
    function that takes in tow ints
    '''
    lists = [wait_random(max_delay) for _ in range(n)]

    delays = await asyncio.gather(*lists)

    return sorted(delays)
