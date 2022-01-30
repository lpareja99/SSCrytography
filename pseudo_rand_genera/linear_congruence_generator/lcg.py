#lcg.py
# Pseudorandom number generation - Linear Congruence Generator
# Generate a random output applying a linear function
# and taking the result modulo m. Where m is a large fixed number
import numlib as nl

# set the modulus
m = 2**64
R = nl.Zmod(m)  # R is now the ring of integers modulo 2^64

# set parameters of the linear congruence generator including initial state:
a = 123456789
c = R(12121212121) # an element of R
state = 10**10+1

def prng():
    """Return the next sequential integer between 0 and m-1, inclusive."""
    global state
    state = int(a*state+c) # a*state+c is an element of R = Z/m
    return state