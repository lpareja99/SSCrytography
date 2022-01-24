from lcg import prng

numbers = []
last_number = 0
done = False

def main():
    for _ in range(5):
        print(prng())

main()
       

def test():
    last_number = 0
    while (not done):
        last_number = prng()
        print(last_number)

        if (last_number not in numbers):
            numbers.append(last_number)
        else:
            done = True
            print("all possible numbers reached")

#1234567902244668910
#8826425326919980895
#10890877254142952100
#15231402302547497037
#10264820975732655146


# 64 iterations and then it turns constant?
# 1.8446744e+19 possibility in best case ??
# a needs to be relatively prime to m to not achieve worst case scenario
