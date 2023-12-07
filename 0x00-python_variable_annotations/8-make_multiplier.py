#!/usr/bin/env python3
'''
complex types - function
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    function that creates a multiplier
    '''
    return lambda x: x * multiplier
