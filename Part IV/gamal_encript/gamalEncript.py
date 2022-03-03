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
