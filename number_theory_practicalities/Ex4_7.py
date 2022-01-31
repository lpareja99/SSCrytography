
from audioop import avg
import numlib as nl
import math
import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
"""
 --------------------------------------------------------------------------------------
    Original Code: Dr. Scott Simmons
    Authors: Marina Amorim, Laura Pareja
    Class: SS Math - Cryptography
    Topic: Big Prime number randomly generator
    Date Creation: 01/31/22
    Last Date Modified: 01/24/22

 --------------------------------------------------------------------------------------

    EXERCISE 4: Write a program that verifies that the expected number of tries before your prime
    generating function returns a 200-bit prime is about 200*ln(2)/2 is approx 69.

--------------------------------------------------------------------------------------

    EXERCISE 7:(Optional) Write a program that displays the sampling distribution for the number of
     tries before finding a prime using the method outlined above. The mean and standard 
     deviation should both be about 69.


    Notes: Use numpy to do the calculations of avg and std. I used pandas to plot because it's 
    how I'm used to do it from Data Analitics, but there is probably an easier way.

 """

NUM_BITS = 200
ROUNDS_PLOT = 2000

# Exercise 4 counter
def generateBigPrime(numBits):

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
    
    #print (decimalNum, "numbers tries until prime found: ", numTried)
    return decimalNum

#Exercise 4
def expectedNumTrial(numBits):
    total_tries=[]

    # expected probability base on algorithm
    p = (numBits * math.log(2))/2  # 1/p = kln(2)/s
    print("Aprox expected to look at numbers loked at: ", p)
    
    # Manually checking
    for _ in range (ROUNDS_PLOT):
        total_tries.append(generateBigPrime(numBits))
    avg_tries= np.average(total_tries)
    stdv = np.std(total_tries)

    print("The avg of tries was", avg_tries, "with a std of",stdv)

    df = pd.DataFrame({
        'data': total_tries,
        'mean': avg_tries,
        'std': stdv})
    df.plot()
    plt.show()


#xpectedNumTrial(200)