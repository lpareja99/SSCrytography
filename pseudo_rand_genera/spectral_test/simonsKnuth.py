import math
import numlib as nl
import numpy as np

# set the modulus
m = 2**64
a = 214319739410341
c = 12121212121

m = 10**10
a = 3141592621
c = 1

# let's use Knuth to compute v2
def knuth(T):

    # S1) initialize values
    t = 2
    h = a
    h_prime = m
    p = 1
    p_prime = 0
    r = a
    s = 1 + a**2

    # S2) Euclidean step
    q = math.floor(h_prime/h)
    u = h_prime - q*h
    v = p_prime - q*p

    while u**2 + v**2 < s:
        s = u**2 + v**2
        h_prime = h
        h = u
        p_prime = p
        p = v
        q = math.floor(h_prime/h)
        u = h_prime - q*h
        v = p_prime - q*p

    # S3)a - Compute v2
    u = u - h
    v = v - p
    if u**2 + v**2 < s:
        s = u**2 + v**2

    v2 = s ** 0.5
    print("v2 =", v2)

    # S3)b - set up U and V matrices
    U = np.array([[-h, p], [-h_prime, p_prime]])
    V = np.array([[p_prime, h_prime], [-p, -h]])
    if (p_prime > 0):
        V = np.multiply(V, -1)

    #print("U = \n", U); print("V = \n", V)

    while t < T:
        # S4) advance step
        t = t+1
        r = (a*r) % m

        # enlarge U and V to be txt mtx´s
        Ut = [-r] #append first element of the row for U(-r)
        for i in range(t-2):
            Ut.append(0) #middle rows elements are 0's
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
            q = math.floor(V[i][0]*r/m + 0.5) # round
            V[i][t-1] = V[i][0]*r - q*m
            U[t-1] = U[t-1] + (q * U[i])

        s = min(s, np.dot(U[t-1], U[t-1])) #min(s, Ut*Ut)
        k = t - 1 #last index transformation
        #j = 1 #denotes current row index, initialize j
        j = 0 #denotes current row index, initialize j

        # S5) Transform
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

        # S7) Prepare for search
        X = np.zeros(t,dtype=int)
        Y = np.zeros(t,dtype=int)
        k = t
        Z = []
        for j in range(t):
            Z.append(math.floor(math.sqrt(np.dot(V[j],V[j]*(s/(m**2))))))

        print("t:", t)
        print("Z:", Z)
        print("X:", X)
        print("Y:", Y)
        print("U:", U)

        # S8) advance Xk
        print("k is", k)
        while X[k] != Z[k] and k >= 1:
            X[k] = X[k] + 1
            Y = Y + U[k] #no sure about this Y = Y + Uk

            # S9) Advance k
            while (k <= t-1): # < or <=
                k = k+1
                print("S9: k is",k,"  t is",t)
                X[k] = -Z[k]
                Y = Y - 2*Z[k]*U[k] #how do represent Y, is it Y[k]

            s = min(s, np.dot(Y,Y))

            # S10) Decrease k
            k = k-1
            print("k step 10",k)
            print("X[k] Z[k]",X[k], Z[k])

        vt = math.sqrt(s)
        print(vt)


print(knuth(3))
