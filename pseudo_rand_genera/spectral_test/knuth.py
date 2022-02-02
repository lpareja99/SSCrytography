from cmath import sqrt
from math import floor
import math
import numlib as nl
import numpy as np

'''

'''

# set the modulus
m = 2**64
R = nl.Zmod(m)  # R is now the ring of integers modulo 2^64

# set parameters of the linear congruence generator including initial state:
a = 214319739410341
c = R(12121212121) # an element of R
state = 10**10+1

# let's use knuth to compute v2
def knuth(T):

    # S1) initialize values
    t = 2
    h = a
    h_prime = m
    p = 1
    p_prime = 0
    r = a
    s = 1+a**2

    # S2) Euclidean step
    q = floor(h_prime/h)
    u = h_prime - (q*h)
    v = p_prime - (q*p)

    while((u**2+v**2)<s):
        s = u**2+v**2
        h_prime = h
        h = u
        p_prime = p
        p = v
        q = floor(h_prime/h)
        u = h_prime - (q*h)
        v = p_prime - (q*p)

    # S3)a - Compute v2
    u = u-h
    v = v-p
    if ((u**2+v**2)<s):
        s=u**2+v**2

    v2 = s **0.5
    #print(v2)

    # S3)b - set up U and V matrices
    U = np.array([[-h,p],[-h_prime,p]])
    V = [[p_prime,h_prime],[-p,-h]]
    if(p_prime<0):
        V = np.multiply(V,-1)

    #print(U,V)

    # S4) advance step
    while (t<T):
        t = t+1
        r = int(R(a*r))

        # enlarge U and V to be txt mtx´s
        Ut = [-r] #append first element of the row for U(-r)
        for i in range(1,t-1): Ut.append(0) #middle rows elements are 0's
        Ut.append(1) #last element row is a 1

        # add column and row
        U = np.pad(U, ((0,0),(0,1)), mode='constant', constant_values=0)
        U = np.vstack([U,Ut])

        Vt = [] #new row for V
        V = np.pad(V, ((0,0),(0,1)), mode='constant', constant_values=0)
        for i in range(0,t-1): Vt.append(0) #all element except last one are 0's
        Vt.append(m) #last element for new row is m
        V = np.vstack([V,Vt])
        
        for i in range(0,t-1): #is this working right?
            q = math.floor(V[i][0]/m)
            V[i][t-1] = (V[i][0]*r) - q*m
            U[t-1] = U[t-1] + (q * U[:,i])

        s = min(s, np.dot(U[t-1],U[t-1])) #min(s, Ut*Ut) 
        k = t #last index transformation
        j = 1 #denotes current row index


            
        print("U: ", U)
        print("V: ", V)
        print("Current s: ", s)

    # S5) 
    

    
    
    
print(knuth(3))

# Not done yet, comparison part
#comparison = 2^(int(30/2))
#if (main()>= comparison ):
    #print("passed")

# We want v2 to >= than 2^30/2
