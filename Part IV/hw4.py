
# wghat multiplies 
from re import L

import numlib as nl
z = 8
myMod = 29
l= 17
a,r,s = nl.xgcd(z,myMod)
R_1 = nl.Zmod(a)
R_2 = nl.Zmod(myMod)

#if (R_1(z)==0):

b=l/a
solution = r*int(b)

print(solution)

test = 8*187
print(R_2(test))

def SolveMult(z,myMod,l):
    a,r,s = nl.xgcd(z,myMod)
    R_1 = nl.Zmod(a)
    R_2 = nl.Zmod(myMod)
    b=l/a
    solution = r*int(b) 
    print(solution)
    return(solution)


