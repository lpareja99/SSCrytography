"""
 --------------------------------------------------------------------------------------
    Original Code: Dr. Scott Simmons
    Authors: Marina Amorim, Laura Pareja
    Class: SS Math - Cryptography
    Topic: Big Prime number randomly generator
    Date Creation: 01/31/22
    Last Date Modified: 02/01/22

 --------------------------------------------------------------------------------------

    EXERCISE 8: Use your program above to generate a 200-bit
    prime p and then verify that a^{p-1} = 1 mod p where a is,
    say, 1234567, or any positive integer less than p. Note: you may wish to use
    Python's built-in pow() function.

--------------------------------------------------------------------------------------

    
 """

#ex 8
from Ex4_7 import generateBigPrime
import numlib as nl
import random

NUM_BITS=200
SMAL_NUM_BITS=random.randint(1, 10)
A=int(123456789)
    
def fermatsTheorem(numBits,a):
    # generate prime number p
    p = int(generateBigPrime(numBits))
    
    # We have to apply the mod to the left part, because the (mod p) is
    #  for the both a^p-1 and 1 ( but we know 1 mod anything is 1) 

    if(pow(a,p-1,p)==1):
        print("The theorem works for a")
    else:
        print("no")

# It will not work with 1
# For this function we will just check up to a prime with a random number of bits up to 10 (so we have time to run it)

def fermatsUpToP(numBits):
    p = int(generateBigPrime(numBits))
    
    for i in range(1,p):
        if(pow(i,p-1,p)!=1):
            print('no')
            return 
    else:
        print ("The theorem works for any number under our prime:",p)


fermatsTheorem(NUM_BITS,A)
fermatsUpToP(SMAL_NUM_BITS)




