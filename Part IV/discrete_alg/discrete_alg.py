import numlib as nl
import sympy
from sympy import totient 

# Exercise 1: With p = 303+2^{100}-3^{100}+5^{100}, compute the 
#             probability that a uniformly randomly chosen element 
#             of {Z}/p^* is a generator

p = 303 + pow(2,100) - pow(3,100) + pow(5,100) #number 2 use
a = 101*5**77 #possible generator

def discrAlg(p,a):
    p_generators = nl.factor(p-1) # list of generators
    F = nl.Zmodp(p)  # (Z/p)*
    g = F(a) # g element of F
    g_order = nl.mulorder(g, exponent = p-1) #return g_order

    # if g is a generator:
    #   - g is prime
    #   - g-order == p-1
    print("p: ", p,", P divisors: ", p_generators)
    print("g: ",g,", g_order: ", g_order)
    print("Is g a generator? :", g_order == p-1)

def probOfgenerator(p):
    # Z/p is a cyclic group because p is prime
    # The number of coprime elements to p is p-1.
    # Now let's use the euler phi function on p-1 to find the num
    # of generators
    generators = sympy.totient(p-1)
    prob = generators/p
    print("probability of g being generator given p: ", prob)

#discrAlg(p,a)
probOfgenerator(p)
