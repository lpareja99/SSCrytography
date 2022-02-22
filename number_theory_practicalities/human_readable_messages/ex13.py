import math
from blumblumshub import prbg
from exercise12 import I2OSP, OS2IP

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




""""
 --------------------------------------------------------------------------------------

    EXERCISE 13: Send Simmons a human-readable message that you have encoded using
    UTF-8 and encrypted using padding. Simmons' RSA public key is (n, e) where 
    e=65537 and n is below.
--------------------------------------------------------------------------------------
"""
n= 0xc66b4f6ab55b33afdffcdec21ec79ca9339cbf49e82feb91b469e99b2fae67f5c04ab5bafa4b75aba04464ab585b6e681e9cf0b765608bb383f582482a49df0a4c689a85073e06d5638163f45ce42d4dd5180c324fe45783cc3313117b53e549984c41d962bc110fd8ddd95f602ef357b6e57732562e47cd8286d05454c51d13ca0bfa7ba2d506a2262410ff78d0bc160a4ca2f7d7ae4ff71c46086cac03c1fe38c679f8edb537055e7e48d60538d85ba9c342fb19c708fdf75bbf76d544569b
e= 65537
message ="Uma verdade matemática não é simples nem complicada por si mesma. É uma verdade. (Emile Lemoine)"
RSAencrypt(n, e, message)
