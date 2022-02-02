from cmath import sqrt
from math import floor
import numlib as nl
import numpy as np

'''

'''

# set the modulus
m = 2**64
R = nl.Zmod(m)  # R is now the ring of integers modulo 2^64

# set parameters of the linear congruence generator including initial state:
a = 214319739410341
c = R(12121212121) # an element of R
state = 10**10+1

# let's use knuth to compute v2
def knuth():

    # S1) initialize values
    t = 2
    h = a
    h_prime = m
    p = 1
    p_prime = 0
    r = a
    s = 1+a**2

    # S2) Euclidean step
    q = floor(h_prime/h)
    u = h_prime - (q*h)
    v = p_prime - (q*p)

    while((u**2+v**2)<s):
        s = u**2+v**2
        h_prime = h
        h = u
        p_prime = p
        p = v
        q = floor(h_prime/h)
        u = h_prime - (q*h)
        v = p_prime - (q*p)

    # S3)a - Compute v2
    u = u-h
    v = v-p
    if ((u**2+v**2)<s):
        s=u**2+v**2

    v2 = s **0.5
    #print(v2)

    # S3)b - set up U and V matrices
    U = np.array([[-h,p],[-h_prime,p]])
    V = [[p_prime,h_prime],[-p,-h]]
    if(p_prime<0):
        V = np.multiply(V,-1)

    #print(U,V)

    

    return (s**0.5)
    
    
print(knuth())

# Not done yet, comparison part
#comparison = 2^(int(30/2))
#if (main()>= comparison ):
    #print("passed")

# We want v2 to >= than 2^30/2
