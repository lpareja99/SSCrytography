
import numlib as nl
from sympy.ntheory.factor_ import totient

# Exercise 12

p = 1162281642500018516457695142918123385886797686236787603454999
q = 1576485350800305182150586120662765326256410287326195239351103
n=p*q


order_n = totient(n) # the euler phi function returns the order of n

def check():
    if (nl.gcd(n)==1):
        print('numbers are relatively prime')
    else:
        print('numbers are not relatively prime')


check()
