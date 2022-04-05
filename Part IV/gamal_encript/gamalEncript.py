#                                   ----- ElGamal Encryptation -----

# AMBIENT KEY = {G,g} of order n
#   everyonr in the planet has g

# YOU: 
#   1) create random d in Z/n --> private key
#   2) computer (h) h = g^d --> public key

# ATHENA:
#   1) wants to encrypt m in G
#   2) choose r randomly in Z/n
#   3) computes c1 = g^r --> part of a msg? element of G
#   4) computes c2 = (h^r)*m element of G
#   5) sends {c1,c2} --> encripted msg (chipertext) divide in two
#   6) r can be discarded after this is done

#   use {c1,c2} to obtain m (m is the msg) non encripted

# YOU (after receiving {c1,c2})
#   1) compute c2*c1^(-d) --> m
#   2) this is the same as --> (h^(r) * m) * ( g^(r))^(-d)
#                               g^(d*r) * m * g^(r* -d)
#                               m
#   (g^(-d)) = g^(-1) * d


# take G = (Z/p)*
# then get G to be an eleptic curve 

# I HAVE NO IDEA
import numlib as nl
import math

def I2OSP(x, xLen):
    """Map an integer x to an octet-string X of length xLen."""
    assert x < 256**xLen, "integer too large"
    # below is the same as: return x.to_bytes(xLen, byteorder = 'big')
    if x == 0:
        return b'\x00'
    bs = b''
    while x:
        bs += (x % 256).to_bytes(1, byteorder = 'big')
        x //= 256
    return b'\x00' * (xLen - len(bs)) + bs[::-1]

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


p = 303+2**100-3**100+5**100
F = nl.Zmodp(p)
g = F(101*5**77)
d = 0x4907b21cad05d4c8fa06b35f0fca7500755116d46124a5ccf9392c9e01
g_order = nl.mulorder(g, exponent = p-1)
h = g**d


message = (0xfefc30f69ef7776dbdf47668de5807036ee6bd33c4f357adc49c35dc8a, 0x7c86628dd471891145fe7393c83373bf8628cb25ad0a702bfd9f230982)

print(RSAdecrypt(h,d,message))