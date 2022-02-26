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
    chash = int.from_bytes(sha256(c).digest(),byteorder='big') # hash in bitstring form
    #c_int = OS2IP(chash) #convert to integer using OS2IP int_m

    # 2) create signature
    # The signature will be an iteger oin the range of the RSA key length
    s = pow(chash,d,n) # (hash(msg))^d.mod(n)
    print (" s: ", s)

    return s


def authenticate(c,s,n,e):

    valid = False

    
    # 2) authenticate hash_msg and decrypt_c are the same 
    hash_msg = pow(s,e,n)
    
    if(hash_msg == c):  valid = True

    return valid

def RSAverify(msg):

    # Let's get our n,e,d using our RSAkey pair methods
    keyPair = RSAKeyPair(p,q)
    n = keyPair[0]
    e = keyPair[1]
    d = keyPair[2]

    # Let's get our signture

    s = RSAsign(c,d,n)

    # RSA verify signature
    # Decrypt the signatuere using the public key and compare the hash
    #  from the signature to the hash of the originally signed message:
    
    hash = int.from_bytes(sha256(msg).digest(), byteorder='big')
    hashFromSignature = pow(s, e, n)
    print("Signature valid:", hash == hashFromSignature)




# Let's verify with our message
RSAverify(c)
# Let's verify with a tempered message
RSAverify(b"Tempered message")






