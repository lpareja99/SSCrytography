

import math



def sqroot(n):
    """return sqrt(n) if integer n is a perfect square; otherwise, return 0"""
    assert type(n) is int and n > 0
    lower, upper = 1, n
    while lower + 1 < upper:
        middle = (lower + upper)//2
        if middle * middle < n:
            lower = middle
        else:
            upper = middle
    return lower if lower ** 2 == n else upper if upper ** 2 == n else 0



def ceil_sqroot(n):
    """return integer ceiling(sqrt(n)) where n is a positive integer"""
    assert type(n) is int and n > 0
    lower, upper = 1, n
    while lower + 1 < upper:
        middle = (lower + upper)//2
        if middle * middle < n:
            lower = middle
        else:
            upper = middle
    return upper



def fermatfactor(n):
    a = ceil_sqroot(n)
    b = sqroot(a*a - n)
    while not b:
        a += 1
        b = sqroot(a*a - n)
    return [int(a - b),int(a+b)]





