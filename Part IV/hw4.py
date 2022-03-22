
# wghat multiplies 
from re import L

import numlib as nl

R_2 = nl.Zmod(2131233)



test = 8*187


#print(R_2(test))
test2= 1234 * -47590804135
print(R_2(test2))

def SolveMult(z,myMod,l):
    a,r,s = nl.xgcd(z,myMod)
    R_1 = nl.Zmod(a)
    if (R_1(a)==0):
        b=l/a
        solution = r*int(b) 
        return solution
    else:
        return False

print("Ex 1",SolveMult(8,29,17))
print("Ex 2",SolveMult(1234,2131233,98765))


def testMult(z,myMod,l):
    mult = SolveMult(z,myMod,l)
    mult *= z
    R_test =  nl.Zmod(myMod)
    if (R_test(mult)==l):
        return True
    else:
        return False

print(testMult(8,29,17))
print(testMult(1234,2131233,98765))
        

