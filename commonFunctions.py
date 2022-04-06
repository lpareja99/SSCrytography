import math
import numlib as nl
import polylib as pl
from random import randint

'''
FUNTIONS IN ALPHABETICAL ORDER:
    - I2OSP(x, xLen)
    - OS2IP(x)
    - sqrt(a, p)
'''

def I2OSP(x, xLen):
    """Map an integer x to an octet-string X of length xLen."""
    assert x < 256**xLen, "integer too large"
    # below is the same as: return x.to_bytes(xLen, byteorder = 'big')
    if x == 0:
        return b'\x00'
    bs = b''
    while x:
        bs += (x % 256).to_bytes(1, byteorder = 'big')
        x //= 256
    return b'\x00' * (xLen - len(bs)) + bs[::-1]


def OS2IP(X):
    """Return the integer primitive x for the octet-string X."""
    # the sum below is the same as: int.from_bytes(X, byteorder = 'big')
    return sum([x * 256**i for i, x in enumerate(X[::-1])])


def sqrt(a, p):
    """Return a square root of a in Z/p.

    Args:
        a (int): a quadratic residue (i.e., square) modulo p.
        p (int): an odd prime.

    Returns:
        (int). An integer whose square equals a, modulo p.
    """
    assert p % 2 == 1 and nl.isprime(p), "p must be an odd prime"
    assert pow(a, (p-1)//2, p) == 1, "no square root exists"

    if p % 4 == 3:
        return a**((p+1)//4) % p
    else:
        # Cipolla's algorithm:
        t = randint(0, p-1)
        while pow(t**2-4*a, (p-1)//2, p) != p-1:
            t = randint(0, p-1)
        Fp = nl.Zmodp(p)  # Fp = Z/p
        poly = pl.FPolynomial([Fp(a), Fp(t), Fp(1)]) # a+tx+x^2 in Fp[x]
        Fp2 = nl.FPmod(poly) # the extension field Fp[x]/<a+tx+x^2>
        x = Fp2([0, 1])      # the element x in Fp[x]/<a+tx+x^2>
        sqroot = x**((p+1)//2) # this is constant in Fp[x]/<a+tx+x^2>
        sqroot = sqroot[0]  # now sqroot is in Fp
        return int(sqroot)  # return an int
