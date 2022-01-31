import numlib as nl
import sys
import random

NUM_BITS = 200

"""
 --------------------------------------------------------------------------------------
    Original Code: Dr. Scott Simmons
    Authors: Marina Amorim, Laura Pareja
    Class: SS Math - Cryptography
    Topic: Big Prime number randomly generator
    Date Creation: 01/31/22
    Last Date Modified: 01/24/22

 --------------------------------------------------------------------------------------

    EXERCISE #3: Replace the 200 above with say numBites and write a function, using the scheme
    outlined above, that returns a numBites-bit prime.

 -----------------------------------------------------------------------------------------

    EXERCISE 4: Write a program that verifies that the expected number of tries before your prime
    generating function returns a 200-bit prime is about 200*ln(2)/2 is approx 69.

    Notes: 

 """

# Exercise 3
def generateBigPrime(numBits):

    expectedNumTrial(numBits)

    numTried = 0 # exercise 4 counter
    # primes beyond 2 must be odd always
    # set first and last bite to 1 to guarantee big number and odd

    decimalNum = random.getrandbits(numBits)
    decimalNum |= (1 << numBits - 1) | 1 #set first and last bite to 1
    numTried = numTried + 1 # ex4 

    while (not nl.isprime(decimalNum)):
        decimalNum = random.getrandbits(numBits)
        decimalNum |= (1 << numBits - 1) | 1 
        numTried = numTried + 1 #ex4
    
    print (decimalNum, "numbers tries until prime found: ", numTried)


#Exercise 4
def expectedNumTrial(numBits):

    return


def main():
    for i in range (200,250):
        generateBigPrime(200)


main()
