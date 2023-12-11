#!/usr/bin/env python3
'''
executing multiple coroutines at the same time with async
'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
     alter it into a new function task_wait_
    '''
    delays = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(delays)
