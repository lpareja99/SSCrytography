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
        j = 1 #denotes current row index, initialize j



        while j != k: # go until j and k match (S6)
            for i in range(t-1):
                #Vi = V[:,i]
                Vi = V[i]
                Vj = V[j]
                #Ui = U[:,i]
                Ui = U[i]
                Uj = U[j]
                if i != j and abs(2*np.dot(Vi,Vj)) > np.dot(Vj, Vj):
                    q = math.floor(np.dot(Vi,Vj) / np.dot(Vj,Vj)+ 0.5)
                    V[i] = Vi - q*Vj # Vi = Vi - q*Vj
                    U[j] = Uj + q*Ui # Uj = Uj + q*Ui
                    s = min(s, np.dot(Uj,Uj)) # s = min(s,Uj*Uj)
                    k = j

            # S6) Advance j
            if(j == t - 1):
                j = 0
            else:
                j = j + 1
            print(j, k)

        print("U = \n", U); print("V = \n", V)
        quit()



        while( j!= k ): # go until j and k match (S6)
            # S5) Transform mtx's
            for i in range(1,t):
                Vi = V[:,i]
                Vj = V[j]
                Ui = U[:,i]
                Uj = U[j]
                if((i != j) and (2 * abs(np.dot(Vi,Vj> np.dot(Vj,Vj))))):
                    q = round(np.dot(Vi,Vj) / np.dot(Vj,Vj))
                    Vi = Vi - q*Vj # Vi = Vi - q*Vj
                    Uj = Uj + q*Ui # Uj = Uj + q*Ui
                    s = min(s,np.dot(Uj,Uj)) # s = min(s,Uj*Uj)
                    k = j
                    
            # S6) Advance j
            if(j == t):
                j = 1
            else:
                j = j+1
        
        # S7) Prepare for search 
        X = np.zeros(t,dtype=int)
        Y = np.zeros(t,dtype=int)
        k = t
        Z = []
        for j in range(0,t-1):
            Z.append(math.floor(math.sqrt(np.dot(V[j],V[j]*(s/(m**2))))))
    
        print("Z:", Z)

        # S8) advance Xk
        if (X[k] == Z[k]):
            #Go to step 10
            print("go to step 10")
        else: 
            X[k] = X[k] + 1
            Y[k] = Y[k] + U[k] #no sure about this Y = Y + Uk

        # S9) Advance k
        while ( k <= t): # < or <=
            k = k+1
            X[k] = -Z[k]
            # Y = Y - 2*Z[k]*U[k] how do represent Y, is it Y[k]
        
        if ( k > t ):
            s = min(s, np.dot(Y,Y))

        # S10) Decrease k
        k = k-1
        if( k >= 1):
            #go to step 8
            print("return to step 8")
        else:
            vt = math.sqrt(s)
            print(vt)

        
print(knuth(3))