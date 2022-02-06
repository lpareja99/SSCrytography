"""
 --------------------------------------------------------------------------------------
    Authors: Marina Amorim, Laura Pareja
    Class: SS Math - Cryptography
    Topic: RSA
    Date Creation: 02/01/22
    Last Date Modified: 02/01/22

 --------------------------------------------------------------------------------------

    EXERCISE 12: Verify that your key e=65537 is indeed relatively prime to phi(n) for your n.
--------------------------------------------------------------------------------------

    
 """
import numlib as nl
from sympy.ntheory.factor_ import totient

# Exercise 12

p = 1162281642500018516457695142918123385886797686236787603454999
q = 1576485350800305182150586120662765326256410287326195239351103
e=65537
n=p*q
order_n = (p-1)*(q-1) # as defined the order of n is (p-1)*(q-1)

def check():
    if (nl.gcd(e,n)==1):
        print('Numbers are relatively prime')
    else:
        print('Numbers are not relatively prime')


check()



def decipherToNum_1(e,num):
    q,inverse,s = nl.xgcd(e,order_n)
    d= inverse
    solution=pow(num,d,n)
    print("Solution for exercise 13 is:",solution)

def decipherToNum_2(e,n,num):
    order_n2 = totient(n) # the euler phi function returns the order of n
    q,inverse,s = nl.xgcd(e,order_n2)
    solution=pow(num,inverse,n)
    print("Solution for exercise 14 is:",solution)



# Decipher ex 13
decipherToNum_1(65537,1228656544646342294930925759475188964963998457780851975302427012554675014888739125369008335923675038120110871984093074455)

# Decipher exercise 14
decipherToNum_2(65537, 932311734169679424087726241879,504779851614048359547310249856)


# Decipher ex 15
decipherToNum_2(65537,932311734169679424087726241879,538940096304536933932071588652)
