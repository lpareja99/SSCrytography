
# wghat multiplies 
from distutils.log import debug
from re import L
import numlib as nl

def SolveAddG(z,myMod,l):
    a,r,s = nl.xgcd(z,myMod)
    R_1 = nl.Zmod(a)
    if (R_1(a)==0):
        b=l/a
        solution = r*int(b) 
        return solution
    else:
        return False

def testAdd(z,myMod,l):
    mult = SolveAddG(z,myMod,l)
    mult *= z
    R_test =  nl.Zmod(myMod)
    if (R_test(mult)==l):
        return True
    else:
        return False


def solveMulgG(n,a,p):
    F = nl.Zmodp(p)
    for x in range (p):    
        if(F(n)**x == F(a)):
            return x


""" p = 19
F = nl.Zmodp(p, negatives = True)
q = F(7)
r = F(10)
P = (2,2)
Q = (3,4) """
def solveEllip(P,Q,E):

    points = []
    for pt in set(list(nl.affine(E))):   #print all pts on the Elliptic Curve
        points.append(pt)

    ellipPointSet = set(list(nl.affine(E)))
    ellipOrder = len(ellipPointSet)
    #print(F"{E} has order {ellipOrder}") # +1 because we are adding the identity element

    for x in range (ellipOrder):  
                         
        if x*P == Q:
            return(x)

    #check if points are in the elliptic curve

""" def SolveEll_2(a,b,myMod,p1_x,p1_y,p2_x,p2_y,l):
    F =nl.Zmodp(myMod, negatives =True)
    E = nl.EllCurve(F(a),F(b), debug=True)
    for pt in nl.affine(E):
        print(pt)
    P = E(p1_x,p1_y)
    Q = E(p2_x,p2_y)
    
    order = nl.affine(E)+1
    for x in range(order-1):
        if x*P==Q:
            print(x)
    coefcls = E.disc.__class__
    b = E.f(0)
    a = E.f.derivative()()


    if hasattr(coefcls,'char') and coefcls.char and hasattr(coefcls, '__iter__'):
        y2s = {}
        fs = {}


        # build y2s and fs
    for x in coefcls:
        x2 = x ** 2
        y2s.setdefault(x2,[]).append(x)
        fs.setdefault(x2 * x +a +b,[]).append(x)

    for y2 in y2s.keys():
        for f in fs.keys():
            if y2 == f:
                for y in y2s[y2]:
                    yield E(x,y)

    else:
        return NotImplemented   """     

    
    
#Exercises
def main():
    
    print("Exercise 1",SolveAddG(8,29,17), testAdd(8,29,17))
    print("Exercise 2",SolveAddG(1234,2131233,98765), testAdd(1234,2131233,98765))
    print("exercise 3: ", solveMulgG(5,78,257))
    print("exercise 4: ", solveMulgG(15551,1357,8675309))
    F = nl.Zmodp(19, negatives=True) # Field of Z/19
    E = nl.EllCurve(F(-7),F(10), debug = True) # create elliptic curve y^2 = x^3 − 7x + 10
    #print("Elliptic Curve: ", E)
    P = E(2,2)
    Q = E(3,4)
    print("Exercise 5: ", solveEllip(P,Q,E))
    
    F = nl.Zmodp(2027, negatives=True)
    E = nl.EllCurve(F(1), F(1))
    #print(" Elleiptic Curve: ", E)
    P = E(1977,2002)
    Q = E(58,1022)
    print("Exercise 6: ", solveEllip(P,Q,E))


main()



        



