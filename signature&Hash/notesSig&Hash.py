"""
 --------------------------------------------------------------------------------------
    Authors: Marina Amorim, Laura Pareja
    Class: SS Math - Cryptography
    Topic: RSA Signature and Hash
    Date Creation: 02/23/22
    Last Date Modified: 02/24/22
 """

from hashlib import sha256
from random import random
from tkinter import N
from exercise12 import I2OSP, OS2IP
import random
import numlib as nl
import math


message = b"to be one, or to be zero, that is the question"
sha256(message).hexdigest() #hexadecimal
sha256(message).digest() #bitstring

# output always 64 hex-string of 64 

# RSA public-key
#e = 65537
p = 44877000451498057437997347977944035796556799528709
q = 26320393208481318556778606552195768263755411992807
c = b"A message to encrypt"

def OS2IP(X):
    """Return the integer primitive x for the octet-string X."""
    # the sum below is the same as: int.from_bytes(X, byteorder = 'big')
    return sum([x * 256**i for i, x in enumerate(X[::-1])])

def RSAKeyPair(p,q):

    # 1) create your own RSA public key
    n = p*q
    e = 0
    order_n = (p-1)*(q-1)

    while (nl.gcd(e,order_n) !=1):
        e = random.randint(1,n)
    
    a,d,b = nl.xgcd(e,order_n) # d is part of the private key

    #print(" Private RSA key: \nn:", n, "\nd: ", d)
    #print(" Public RSA key: \nn:", n, "\ne: ", e)
    return [n,e,d]

def RSAsign(c,d,n): # exercise
    # 1) encript the msg
    chash = int.from_bytes(sha256(c).digest(),byteorder='big')
    # The signature will be an iteger oin the range of the RSA key length
    s = pow(chash,d,n) 
    print (" s: ", s)
    return s

def authenticate(c,s,n,e): # I THINK TO DELETE
    hash_msg = pow(s,e,n)   
    valid = True if hash_msg == c else False
    return valid

def RSAverify(msg, s, public_k):
    e = public_k[1]
    n = public_k[0]

    # RSA verify signature
    # Decrypt the signatuere using the public key and compare the hash
    #  from the signature to the hash of the originally signed message
    hash = int.from_bytes(sha256(msg).digest(), byteorder='big')
    hashSig = pow(s, e, n)
    valid = True if hash == hashSig else False
    return valid


# Exercise 15: Write a function called RSAsign that takes a (bytes-string)
#              message and outputs its signature as an integer.
def ex15(c,p,q):
    print("EXERCISE 15")
    print(" Cyper msg: ", c)
    keyPairs = RSAKeyPair(p,q)
    n = keyPairs[0]
    d =  keyPairs[2]
    s = RSAsign(c,d,n)
    print(" New signature: ", s)

# Exercise 16: Write a function called RSAverify that takes as input a message
#              and a signature, verifies the authenticity and integrity of the 
#              message, and that outputs True or False, accordingly.
def ex16(c,p,q):

    keyPair = RSAKeyPair(p,q) #create key pairs
    n = keyPair[0]
    e = keyPair[1]
    d = keyPair[2]
    s = RSAsign(c,d,n) #create signature
    public_key = [n,e]

    # Let's verify with our message
    valid1 = RSAverify(c,s,public_key)
    print(" Verification from: \n c: ",c,"\n s: ", s, valid1)
    # Let's verify with a tempered message
    valid2 = RSAverify(b"Tempered message",s,public_key)
    print(" Verification from: \n c: ",b"Tempered message","\n s: ", s, valid2)

# Exercise 17: Create RSA public and private keys and send the public key to
#              Simmons so he can send you a signed message that you can decode 
#              and verify.
def ex17(p,q):
    keyPair = RSAKeyPair(p,q)
    n = keyPair[0]
    e = keyPair[1]
    d = keyPair[2]
    print(" RSA Pair of keys generated: \n  Public Key {n,e} and Private Key {n,d}")
    print(" n: ", n)
    print(" e: ", e)
    print(" d: ", d)
    

    

ex15(c,p,q)
ex16(c,p,q)
ex17(p,q)






