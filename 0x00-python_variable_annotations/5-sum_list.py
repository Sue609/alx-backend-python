#!/usr/bin/env python3
'''
complex types - list of floats
'''


def sum_list(input_list: list[float]) -> float:
    '''
    function which takes a list of floats and returns floats
    '''
    total_sum = 0.0
    for i in input_list:
        total_sum += i
    return total_sum
