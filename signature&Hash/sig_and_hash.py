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
#from tkinter import N
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

# Decrypt method from Simmons
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


# It is giving me decryption errors
def ex16_pt2():
    n = 1181180297900622537506127198477981514841813682949089928220108951255708821489739695123415064097996163
    d = 549230482706811301599137164188826043765980672311380088763362378032793681227642719098003036780797315
    m_1 = 450401155434731371118421813986941421709598043925196498331270928327438580575483032645117800146428215
    m_2 = 717237654965488152560168993455511154625980237096791741000876995711454224297915427772828765964856628
    e = 835937754772491041426113458976152014686797422701759713870028802309149705366715474017367236669502675
    public_key = [n,e]
    #s = int(b'16923038885717885119743540814151698386884206802619080989741313736450001980214220787970078946186503271037707085953287589205047931103579006878338087704106733287295900176140897567431636821660465657648050251236447081404743868086044201889085958094669157569099571467747055939097033645956367314952401138717564236488661910686875537732293063546998539437777060694983260658577402367193810914622350920608469081876798550160381934644860482725991001601383417998370993378870129')
    #s = 0x1cc2278bbeb7ddbd3e70ad3d5c0e65f94f0d326ce9b92e1845f63ca057ea814e50b7116f905f374b62b206f98407ab3ae604575ad5b765511db788c498aa25d95357d7fd093471aa53f56d867331897da22eccdb83c7628b5fbd0cea9b167c93510a099ba75260e9cd493c89c26039bf62c3f3a9745eeb68e3ac9faf156bda915f1f26f890eb7bfd893606b3172f8596b6960c123e72cbef17dbf417e5608a5d5dd300a38553646ca22945cfc2bca161d1ece536c404d0a97ad50285aaac371
    print(RSAdecrypt(n,d,m_1).decode('utf8'))
    print(RSAdecrypt(n,d,m_2).decode('utf8'))
    RSAverify(m_1,s,public_key)
    

    

#ex15(c,p,q)
#ex16(c,p,q)
ex16_pt2()
#ex17(p,q)






