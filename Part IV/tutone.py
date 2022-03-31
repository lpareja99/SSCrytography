from numlib import *

p =8675311
assert p % 4 ==3
F = Zmodp(p, negatives = True)
E = EllCurve(F(2),F(3), debug = True)
assert E.disc !=0
print(E)
def sqrt(a, p):
    return a ** ((p+1)//4)
    

for x in F:
    fx = E.f(x)
    if fx** ((p-1)//2)==1:
        pt = E(x, sqrt(fx,p))
        print(pt,'has order', addorder(pt,8676172))
        

