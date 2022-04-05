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



def ex2():

    p = 303+2**100-3**100+5**100
    F = nl.Zmodp(p)
    g = F(101*5**77)
    d = 0x4907b21cad05d4c8fa06b35f0fca7500755116d46124a5ccf9392c9e01
    h = g**d
   
    c1, c2 = (0xfefc30f69ef7776dbdf47668de5807036ee6bd33c4f357adc49c35dc8a, 0x7c86628dd471891145fe7393c83373bf8628cb25ad0a702bfd9f230982)
    c1=F(c1)
    c2=F(c2)
    new_message = c2*((c1)**-d)
    k = math.floor(math.log((p-1), 256))
    message = I2OSP(new_message,k)
    print("First message",message.decode("utf-8"))


def ex2_part2():

    p = 303+2**100-3**100+5**100
    F = nl.Zmodp(p)
    g = F(101*5**77)
    d = 0x4907b21cad05d4c8fa06b35f0fca7500755116d46124a5ccf9392c9e01
    h = g**d
    ciphertexts = [
    (0x1a08226a7d5d5d569caed0183b97d045eab3fca31d6c3670d2efbe15d7, 0x73e4612f97caecfdc008028ce29511ac8fee60768e3464d4c3bb94fb96),
    (0xbfd5eec2601c152a3d565efcad12ef2239a3cc2bdbdaebae10743f48b4, 0x6c59e0277921da40bd2ae2669838ee0adfeb1d23046991a20d06313bf0),
    (0x414ff938f1efd2caf5a007ddebb682e12b6f6b1ca41d2a8ef1950ed8d2, 0xb4b9432c9951583b7307f406059833c5dc5c6a7105a08dc1785460bbcf),
    (0xa000191cfaad8a381c8fe663bd77bffdfa87b7c43fcbab09031d51edf1, 0x203f992eb7d93e73f790bd7e95572cda0bf5767b70f86819e30e0fd022),
    (0x6a929a7d396fc202ecbd98f4a3f94773fc1794bcb6ff0a1975eb2b5e39, 0xa8344b9877e4e7f3a69f9f72fc861dfe6f57724d40c28272eeb77413aa),
    (0xa2c2df4112fd7b1593ef1adee27b843270fef39854976108404c79495e, 0xeffb38521b000e7b9955907492b62f8da9dc9d73c010d81f8f0acd49e1),
    (0x99697df71db1d265dbb7895cca94ad5aeec0295125f5c5b776db0a3fff, 0x30e58722c80d0e917e6205486f0c862ca10c1a6569e60d06340360d692)]
    i=0
    full_message =""
    while (i<=len(ciphertexts)):
        c1,c2=ciphertexts[i]
        i+=2
        c1=F(c1)
        c2=F(c2)
        new_message = c2*((c1)**-d)
        k = math.floor(math.log((p-1), 256))
        message = (I2OSP(new_message,k)).decode("utf-8")
        full_message+= " " + message




    print("Second message",full_message)





    


ex2()
ex2_part2()


