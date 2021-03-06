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
from blumblumshub import prbg


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


def RSAsign_2(n, d, message):
    return RSAencrypt(n, d, sha256(message).digest())

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

# Encrypt method from Simmons

def RSAencrypt(n, e, message):
    """Return ciphertext given an RSA key {n, e} and a message.

    Args:
        n (int): the modulus.
        e (int): the encrypting exponent.
        message (bytes): the message (as a bytestring) to encrypt.

    Returns:
        int. A non-negative integer less than n.
    """
    # the length of n in whole octets
    k = math.floor(math.log(n, 256))

    # check that message is short enough leaving room for padding
    mLen = len(message)
    if mLen > k - 11:
        raise ValueError("message too long")

    # generate a random bytes-string consisting of non-zero bytes
    # (this will have length at least 8)
    ps = b''
    while len(ps) < k - mLen - 3:
        decimal = int(prbg(8), 2)
        if decimal != 0:
            ps += decimal.to_bytes(1, byteorder = 'big')

    # pad message and convert to integer, encrypt, and return
    m = OS2IP(b'\x00' + b'\x02' + ps + b'\x00' + message)
    return pow(m, e, n)

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

# Decrypt method from Simmons
#   Note: In the moment you create a signature, to decript it, you pas the public key {n,e} instead of thh
#         private key {n,d} and the signature intead of the ciphertext.
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
    n = public_k[0]
    e = public_k[1]
  

    sig_decripted = RSAdecrypt(n, e, s) #decrypt signature
    hash = sha256(msg).digest() #hash msg
    valid = True if hash == sig_decripted else False #compare
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
    #our keys
    n = 1181180297900622537506127198477981514841813682949089928220108951255708821489739695123415064097996163
    d = 549230482706811301599137164188826043765980672311380088763362378032793681227642719098003036780797315
    e = 835937754772491041426113458976152014686797422701759713870028802309149705366715474017367236669502675
    public_key = [n,e]

    # simmons keys
    n_simmons = 0xc66b4f6ab55b33afdffcdec21ec79ca9339cbf49e82feb91b469e99b2fae67f5c04ab5bafa4b75aba04464ab585b6e681e9cf0b765608bb383f582482a49df0a4c689a85073e06d5638163f45ce42d4dd5180c324fe45783cc3313117b53e549984c41d962bc110fd8ddd95f602ef357b6e57732562e47cd8286d05454c51d13ca0bfa7ba2d506a2262410ff78d0bc160a4ca2f7d7ae4ff71c46086cac03c1fe38c679f8edb537055e7e48d60538d85ba9c342fb19c708fdf75bbf76d544569b
    e_simmons = 65537
    public_key_simmons = [n_simmons, e_simmons]

    # encoded msg
    m_1 = 450401155434731371118421813986941421709598043925196498331270928327438580575483032645117800146428215
    m_2 = 717237654965488152560168993455511154625980237096791741000876995711454224297915427772828765964856628

    #simmons signature
    s_simmons = 16923038885717885119743540814151698386884206802619080989741313736450001980214220787970078946186503271037707085953287589205047931103579006878338087704106733287295900176140897567431636821660465657648050251236447081404743868086044201889085958094669157569099571467747055939097033645956367314952401138717564236488661910686875537732293063546998539437777060694983260658577402367193810914622350920608469081876798550160381934644860482725991001601383417998370993378870129
    msg1 = bytes((RSAdecrypt(n,d,m_1).decode('utf8')), 'utf8')
    msg2 = bytes((RSAdecrypt(n,d,m_2).decode('utf8')), 'utf8')
    msg = msg1 + msg2 # pass decoded msg

    # check if signature is valid
    valid = RSAverify(msg ,s_simmons,public_key_simmons)
    print(valid)

def ex18():
    message = b"Yes"
    n_simmons = 0xc66b4f6ab55b33afdffcdec21ec79ca9339cbf49e82feb91b469e99b2fae67f5c04ab5bafa4b75aba04464ab585b6e681e9cf0b765608bb383f582482a49df0a4c689a85073e06d5638163f45ce42d4dd5180c324fe45783cc3313117b53e549984c41d962bc110fd8ddd95f602ef357b6e57732562e47cd8286d05454c51d13ca0bfa7ba2d506a2262410ff78d0bc160a4ca2f7d7ae4ff71c46086cac03c1fe38c679f8edb537055e7e48d60538d85ba9c342fb19c708fdf75bbf76d544569b
    e_simmons = 65537
    d_marina_laura = 549230482706811301599137164188826043765980672311380088763362378032793681227642719098003036780797315
    my_n = 1181180297900622537506127198477981514841813682949089928220108951255708821489739695123415064097996163
    s = RSAsign_2(my_n,d_marina_laura,message)
    print("Signature:",s)
    c = RSAencrypt(n_simmons, e_simmons, message)
    print("Message",c)
    e = 835937754772491041426113458976152014686797422701759713870028802309149705366715474017367236669502675
    public_k = [my_n,e]
    
    #fix this
    print(RSAverify(c, s, public_k))
   

    

    

#ex15(c,p,q)
#ex16(c,p,q)
#ex16_pt2()
#ex17(p,q)
ex18()






