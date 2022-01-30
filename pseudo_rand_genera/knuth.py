from cmath import sqrt
from math import floor
import numlib as nl

# set the modulus
m = 2**64
R = nl.Zmod(m)  # R is now the ring of integers modulo 2^64

# set parameters of the linear congruence generator including initial state:
a = 123456789
c = R(12121212121) # an element of R
state = 10**10+1

# let's use knuth to compute v2
def main():
    h=a
    h_prime=m
    p=1
    p_prime=0
    r=a
    s=1+a^2
    done=False
    while(not done):
        q=floor(h_prime/h)
        u=h_prime-(q*h)
        v=p_prime
        if(u^2+v^2<s):
            s=u^2+v^2
            h_prime=h
            h=u
            p_prime=p
            p=v
        else:
            done=True
    u=u-h
    v=v-p
    if (u^2+v^2<s):
        s=u^2+v^2
        return sqrt(s)
    
    
print(main())

# Not done yet, comparison part
#comparison = 2^(int(30/2))
#if (main()>= comparison ):
    #print("passed")

# We want v2 to >= than 2^30/2
