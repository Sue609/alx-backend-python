#!/usr/bin/env python3
'''
executing multiple coroutines at the same time with async
'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    '''
    function that takes in tow ints
    '''
    delays = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(delays)
