
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

def solveMulgG(n,a,p):
    F = nl.Zmodp(p)
    for x in range (p):    
        if(F(n)**x == F(a)):
            return x

#exercise 3
print("exercise 3: ")
#solveMulgG(5,78,257)
#exercise 4
print("exercise 4: ")
print(solveMulgG(15551,1357,8675309))
#Multiplicative Marina&Laura 
#solveMulgG(13,4,89)
#olveMulgG(197, 23, 3001)
 
# y^2 = x^3 +ax +b mod Mymod
def SolveEll(a,b,myMod,p1_x,p1_y,p2_x,p2_y,l):
    F =nl.Zmodp(myMod)
    E = nl.EllCurve(F(a),F(b), debug=True)
    for pt in nl.affine(E):
        print(pt)
    E(p1_x,p1_y)
    E(p2_x,p2_y)


p = 19
F = nl.Zmodp(p)
q = F(7)
r = F(10)
P = (2,2)
Q = (3,4)
def solveEllip(p,q,r,F,P,Q):
    E = nl.EllCurve(q,r, debug = True) # create elliptic curve
    len(list(nl.affine(E)))
    E(4,19)*0 #magic number

    for pt in nl.affine(E):   #print all pts on the Elliptic Curve
        print(pt) 
        print(pt)**(-1)

 

    #check if points are in the elliptic curve
    

        



