#!/usr/bin/env python3

import ipdb

def plus_two(num):
    ipdb.set_trace()
    num + 2
    return num

result = plus_two(5)
print(result)