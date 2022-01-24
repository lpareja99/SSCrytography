"""                                HULL-DOBELL THEOREM

 --------------------------------------------------------------------------------------
    Original Code: Dr. Scott Simmons
    Authors: Marina Amorim, Laura Pareja
    Class: SS Math - Cryptography
    Topic: Pseudo Random Number Generator, Hull-Doebell Theorem
    Date Creation: 01/24/22
    Last Date Modified: 01/24/22

 --------------------------------------------------------------------------------------

 EXERCISE #1: Does the LCG defined by the program above satisfy all three bulleted 
 conditions so that its period is 2^{64}, the largest possible?

    To prove Hull-Dobell Theorem we must test the following bullet points:
    1) m and c are relatively prime,
    2) a-1 is divisible by all prime factors of m, and
    3) a-1 is divisible by 4 if m is divisible by 4.

 -----------------------------------------------------------------------------------------

 EXERCISE #2: If possible, compute the potency of the LCG above to see if it even
 has a chance of being sufficiently "random".

 -----------------------------------------------------------------------------------------

 EXERCISE #3: Show the following (we used this above): if gcd(a, m) = d then, mod(m),
 for any integer x, we have that ax is always a multiple of d.

   Take 5 random integers (5 different x) and prove that this is true

 --------------------------------------------------------------------------------------------

 EXERCISE 4: In the previous discussion we used the fact that if a and m are relatively prime,
 then a has a multiplicative inverse modulo m; that is, there exists a^-1 in Z/m such that a^-1*a = 1mod(m)
  Above we only needed its existence but what is a^-1 if a=123456789 and m=2^{64}?
"""
# TODO: Randomize parameters a,c, state and m

from cmath import inf
from math import gcd
from re import S
import numlib as nl
from random import randint, random
import sys

#constants
NUM2CHECK = 5
POTENCY_RANGE = 50

# set the modulus
m = 2**64 # fixed m
R = nl.Zmod(m)  # R is now the ring of integers modulo 2^64

# set parameters of the linear congruence generator including initial state:
a = 123456789
#a: int
c = R(12121212121) # an element of R
state = 10**10+1

#Return the next sequential integer between 0 and m-1, inclusive.
def prng():
    global state
    state = int(a*state+c) # a*state+c is an element of R = Z/m
    return state

#recursive method to check bullet point 2
def isDivisible(x,y):
    x = int(x) 
    y = int(y)
    if (y == 1): return 1
    z = gcd(x, y)
    if (z == 1): return False    
    return isDivisible(x, y / z)

# exercise 2
def potencyRandomLevel(a): 
    for potency in range(1,POTENCY_RANGE):
        op = R((a-1)**potency) 
        if(op == 0):
            if(potency < 5): print("Exercise 2: pontency NOT high enought for randomness, ", potency)
            else: print("Exercise 2: potency high enough for randomness, ", potency)
            return

    print("Foor loop done")

#exercise 3
def exercise3():
    # get gcd(a, m) = d
    d = gcd(a,m)
    for i in range (0,NUM2CHECK):
        #max = sys.float_info.max
        #min = -sys.float_info.max - 1
        x = randint(-99999999999999999999, 99999999999999999999)
        xMod = R(x) #apply mod
        if(((a*x)%d) == 0):   print ("Exercise 3 promt satisfied for number: ", x , ",mod num: ", int(xMod))
        else:  print(" Exercise 3 promt NOT satified for number: ", x , ",mod num: ", int(xMod))

    return

#exercise 4
def exercise4 ():
    # We will find a^-1 using the euclides form and the extended gcd 
    q,r,s = nl.xgcd(a,m)

    # r will be our a^-1, but we can check it make sure 
    if( (R(a*r)) and (q==1)):
        print ("Exercise 4:", r, " is the inverse of",a)
    else:
        print ("Exercise 4:",r, "is NOT the inverse of",a)

    return

# exercise 1
def bulletPointTest():
    print("Exercise 1: checking a with the Hull-Dobell Theorem")
    # first bullet point: m and c are relatively prime
    if (gcd(m,c)==1):
        print("     First Bullet point passes")
        # second bullet point: a-1 is divisible by all prime factors of m
        if isDivisible((a-1),m):
            print("     Second bullet point passes")
            potencyRandomLevel(a)
            # third bullet point: a-1 is divisible by 4 if m is divisible by 4
            if ((m%4)==0 and (a-1)%4 == 0):
                print("     Third bullet point passes")
                return True
            else:
                print("Third bullet point fails")
                return False 
        else:
            print("Second bullet point fails")
            return False
    else:
        print("First bullet point fails")
        return False

bulletPointTest()
exercise3()
exercise4()

       
