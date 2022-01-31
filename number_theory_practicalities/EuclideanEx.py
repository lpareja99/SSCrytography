#ex 8
from Ex4_7 import generateBigPrime
import math
import numlib as nl

def main(numBits,a):

    # generate prime number p
    p = generateBigPrime(numBits)

    # verify preposition
    if (a**(p-1) == 1*nl.Zmod(a)):
        print("here")
        return
    else:
        print("not here")
    print(p)

main(200,123456789)



