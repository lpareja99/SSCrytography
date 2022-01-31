

from cmath import sqrt
import math 
import numlib as nl


a=214319739410341
m=2**64
R = nl.Zmod(m)

def steele_vigna(t):
    #print(m**(1/t))
    #print(a)
    if (a<m**(1/t)):
        v=sqrt((a**2)+1)
        return v
    else:
        print("doesn't work in this case")


def large_knuth(t):
    vt=sqrt(a**2 +1)
    u = (math.pi**(t/2) * vt)/ math.factorial(math.floor(t/2))
    print (t, "  -->  ",u)

def main():
    for i in range(3,20):
        print(steele_vigna(i))
        large_knuth(i)

main()