import numlib as nl

# Exercise 1: With p = 303+2^{100}-3^{100}+5^{100}, compute the 
#             probability that a uniformly randomly chosen element 
#             of {Z}/p^* is a generator

p = 303 + pow(2,100) - pow(3,100) + pow(5,100)
p_generators = nl.factor(p-1) # prime divisor numbers
F = nl.Zmodp(p)  # F is now the group (Z/p)*

# ARE WE SUPPOSED TO GET g RANDOMLY PRIME GENERATED?
g = F(101*5**77) # g is now an element of F
g_order = nl.mulorder(g, exponent = p-1) # mulorder_ accepts a list of potential orders


print("p divisors: ", p_generators)
print("g_order: ", g_order)
print(g_order == p-1)
