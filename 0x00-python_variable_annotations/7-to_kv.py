#!/usr/bin/env python3
"""
coplex types - string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    annoted function that returns a tuple and takes a union and a string.
    '''
    return (k, float(v**2))
