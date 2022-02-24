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
e = 65537
p = 44877000451498057437997347977944035796556799528709
q = 44877000451498057437997347977944035796556799528709
c = b"this is the msg to encryp"

def OS2IP(X):
    """Return the integer primitive x for the octet-string X."""
    # the sum below is the same as: int.from_bytes(X, byteorder = 'big')
    return sum([x * 256**i for i, x in enumerate(X[::-1])])

def RSAdecrypt(n, d, ciphertext):
    
    """Return message decrypted from ciphertext using key {n, d}.

    Args:
        n (int): the modulus.
        d (int): the decrypting exponent.
        ciphertext (int): the message to decrypt.

    Returns:
        bytes. A bytes-string representing the decrypted message.
    """
    # get the padded message
    m = pow(ciphertext, d, n)
    k = math.floor(math.log(n, 256))
    message = I2OSP(m, k)

    # strip away the padding
    error = False
    if message[0] != 0:
        error = True
    message = message[1:]
    if message[0] != 2:
        error = True
    message = message[1:]
    while message[0] != 0:
        message = message[1:]
    if message[0] != 0:
        error = True
    message = message[1:]

    assert not error, "decryption error"

    return message

def RSAKeyPair(p,q):

    # 1) create your own RSA public key
    n = p*q
    e = 0
    order_n = (p-1)*(q-1)
    while (nl.gcd(e,n)!=1):
        e = random.randint(1,n)
    a,d,b = nl.xgcd(e,order_n) # d is part of the private key

    #print(" Private RSA key: \nn:", n, "\nd: ", d)
    #print(" Public RSA key: \nn:", n, "\ne: ", e)

    return [n,e,d]

def RSAsign(c,d,n): # exercise

    # 1) encript the msg
    chash = sha256(c).digest() # hash in bitstring form
    c_int = OS2IP(chash) #convert to integer using OS2IP int_m

    # 2) create signature
    s = pow((c_int),d,n) # (hash(msg))^d.mod(n)
    print (" s: ", s)

    return s



def authenticate(c,s,n,e):

    valid = False

    
    # 2) authenticate hash_msg and decrypt_c are the same 
    hash_msg = pow(s,e,n)
    
    if(hash_msg == c):  valid = True

    return valid

def main():
    e = 65537
    p = 44877000451498057437997347977944035796556799528709
    q = 44877000451498057437997347977944035796556799528709
    c = b"this is the msg to encryp"

    keyPair = RSAKeyPair(p,q)
    n = keyPair[0]
    e = keyPair[1]
    d = keyPair[2]

    s = RSAsign(c,d,n)

    #m = RSAdecrypt(n,s,c) # does not work

    valid = authenticate(c,s,n,e)
    print(valid)

    #print(s)

main()
