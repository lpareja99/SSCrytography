from math import floor, sqrt
import operator

def dot(list1, list2):
    """return usual inner product of two lists"""
    return sum(map(operator.mul, list1, list2))

def add(list1, list2):
    """element-wise sum two lists"""
    return list(map(operator.add, list1, list2))

def scalarmult(scalar, list1):
    """scalar multiply a list"""
    return [scalar * elt for elt in list1]

def sub(list1, list2):
    """return element-wise difference of two lists"""
    return add(list1, scalarmult(-1, list2))

def knuth(T,a,m):
    """Return nu_T

    This implenents Knuth's alogrithm beginning on page 102 of his
    book:
         The Art of Computer Programming, 3rd Ed., Vol. 2:
         Seminumerical Algorithms, 1998
    """

    # S1) initialize values
    t = 2
    h = a
    h_prime = m
    p = 1
    p_prime = 0
    r = a
    s = 1 + a**2

    # S2) Euclidean step
    q = floor(h_prime/h)
    u = h_prime - q*h
    v = p_prime - q*p

    while u**2 + v**2 < s:
        s = u**2 + v**2
        h_prime = h
        h = u
        p_prime = p
        p = v
        q = floor(h_prime/h)
        u = h_prime - q*h
        v = p_prime - q*p

    # S3)a - compute v2
    u = u - h
    v = v - p
    if u**2 + v**2 < s:
        s = u**2 + v**2

    v2 = sqrt(s)

    if  T == 2:
        return v2

    # S3)b - set up U and V matrices
    U = [[-h, p], [-h_prime, p_prime]]
    V = [[p_prime,h_prime], [-p,-h]] if p_prime <= 0 else [[-p_prime,-h_prime], [p,h]]

    while t < T:
        # S4) advance step
        t = t+1
        r = (a*r) % m

        # add column and row
        for row in U:
            row.append(0)
        U.append([-r] + (t-2)*[0] + [1])

        for row in V:
            row.append(0)
        V.append((t-1)*[0] + [m])

        for i in range(0,t-1):
            q = round(V[i][0]*r/m)
            V[i][t-1] = V[i][0]*r - q*m
            U[t-1] = add(U[t-1], scalarmult(q, U[i]))

        s = min(s, dot(U[t-1], U[t-1]))
        k = t-1
        j = 0

        # S5) Transform
        while j != k: # go until j and k match (S6)
            for i in range(t):
                if i != j and abs(2*dot(V[i], V[j])) > dot(V[j], V[j]):
                    q = round(dot(V[i], V[j]) / dot(V[j], V[j]))
                    V[i] = sub(V[i], scalarmult(q, V[j]))
                    U[j] = add(U[j], scalarmult(q, U[i]))
                    s = min(s, dot(U[j], U[j]))
                    k = j

            # S6) Advance j
            j = 0 if j == t - 1 else j + 1

        # S7) Prepare for search
        X = [0]*t
        Y = [0]*t
        k = t-1
        Z = []
        for j in range(t):
            Z.append(floor(sqrt(dot(V[j], scalarmult((s/(m**2)), V[j])))))

        # S8) advance Xk
        while X[k] != Z[k] and k >= 0:
            X[k] += 1
            Y += U[k]

            # S9) Advance k
            k = k+1
            while (k <= t-1): # < or <=
                X[k] = -Z[k]
                Y -= scalarmult(2*Z[k], U[k])
                k = k+1

            s = min(s, dot(Y,Y))

            # S10) Decrease k
            k = k-1

    return sqrt(s)


def main():
    a = [ 23, 129, 262145, 3141592653, 137, 3141592621]
    m = [ 100000001, 2**35, 2**35, 2**35, 256, 10**10]
    for i in range (len(a)):
        print("       (v_t)^2:",end=" ")
        print(*map(lambda t: round(knuth(t,a[i],m[i])**2), range(2,9)))
        print("           v_t:",end=" ")
        print(*map(lambda t: round(knuth(t,a[i],m[i]), 3), range(2,9)))
        print("v_t > 2^(30/t):",end=" ")
        print(*map(lambda t: knuth(t,a[i],m[i]) > 2**(30/t), range(2,9)))

main()