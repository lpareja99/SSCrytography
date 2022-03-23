
# wghat multiplies 
from re import L

import numlib as nl

R_2 = nl.Zmod(2131233)



test = 8*187


#print(R_2(test))
test2= 1234 * -47590804135
print(R_2(test2))

def SolveAddG(z,myMod,l):
    a,r,s = nl.xgcd(z,myMod)
    R_1 = nl.Zmod(a)
    if (R_1(a)==0):
        b=l/a
        solution = r*int(b) 
        return solution
    else:
        return False

print("Ex 1",SolveAddG(8,29,17))
print("Ex 2",SolveAddG(1234,2131233,98765))


def testAdd(z,myMod,l):
    mult = SolveAddG(z,myMod,l)
    mult *= z
    R_test =  nl.Zmod(myMod)
    if (R_test(mult)==l):
        return True
    else:
        return False

print(testAdd(8,29,17))
print(testAdd(1234,2131233,98765))

# Take equationz^x = l mod myMod
# z=5 l=78 mymod=257
def SolveMultG(z,myMod,l):
    F = nl.Zmodp(myMod)
    multOrder = nl.mulorder(F(z))
    for x in range(myMod):
        if (multOrder ** x ==l):
            return x
    #return False





print(SolveMultG(5,257,78))
print(SolveMultG(15551,8675309,1357))
 
# y^2 = x^3 +ax +b mod Mymod
def SolveEll(a,b,myMod,p1_x,p1_y,p2_x,p2_y,l):
    F =nl.Zmodp(myMod)
    E = nl.EllCurve(F(a),F(b), debug=True)
    for pt in nl.affine(E):
        print(pt)
    E(p1_x,p1_y)
    E(p2_x,p2_y)

        



