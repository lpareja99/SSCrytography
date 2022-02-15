"""
 --------------------------------------------------------------------------------------
    Authors: Marina Amorim, Laura Pareja
    Class: SS Math - Cryptography
    Topic: RSA
    Date Creation: 02/01/22
    Last Date Modified: 02/01/22

 --------------------------------------------------------------------------------------

    EXERCISE 12: Verify that your key e=65537 is indeed relatively prime to phi(n) for your n.
--------------------------------------------------------------------------------------

    
 """
import numlib as nl
from sympy.ntheory.factor_ import totient
from fermstsAlgo import fermatfactor

#from rsa.decipher import decipherToNum

# Exercise 12

p = 1162281642500018516457695142918123385886797686236787603454999
q = 1576485350800305182150586120662765326256410287326195239351103
e=65537
n=p*q
order_n = (p-1)*(q-1) # as defined the order of n is (p-1)*(q-1)

def check():
    if (nl.gcd(e,n)==1):
        print('Numbers are relatively prime')
    else:
        print('Numbers are not relatively prime')


#check()



def decipherToNum_1(e,num):
    q,inverse,s = nl.xgcd(e,order_n)
    d= inverse
    solution=pow(num,d,n)
    print("Solution for exercise 13 is:",solution)

def decipherToNum_2(e,n,num):
    order_n2 = totient(n) # the euler phi function returns the order of n
    q,inverse,s = nl.xgcd(e,order_n2)
    solution=pow(num,inverse,n)
    print("Solution for exercise 14 is:",solution)


def decipherToNum_3(e,n,num):

    order = fermatfactor(n)
    p = order[0]
    q= order[1]
    if (p*q==n):
        print("true")
   
    order_n2 = (p-1)*(q-1)
    q,inverse,s = nl.xgcd(e,order_n2)
    solution=pow(num,inverse,n)
    print("Solution for exercise 15 is:",solution)
    



# Decipher ex 13
#decipherToNum_1(65537,1228656544646342294930925759475188964963998457780851975302427012554675014888739125369008335923675038120110871984093074455)

# Decipher exercise 14
#decipherToNum_2(65537, 932311734169679424087726241879,504779851614048359547310249856)


# Decipher ex 15
#decipherToNum_2(65537,932311734169679424087726241879,538940096304536933932071588652)


decipherToNum_3(3,0x50886174e2215b2a1af3aa90b4856cc816f2d93732342613699c424c8b4a9e022974cf8aadd449dd8c80149f76854c61f139b4f7180acbdf49971d867809d4cb06603a3c5645295f0083b276f0f751f5bc71630d0c1c84ef65306ae9efd9820fc8bc162d07ea1ff9bf5dc4720f72dc4a6d33ffdcfc4a1f7847df61eeaa56c5bd,0x162f500e12eb59444046adb4d34d4d8184c534136dee2d798b25d6e0fea86135bda2504b2217f0f37613360079e5a77adb9af13b415744c54473047e7f01789cc7774fe4b2c35e47bfed7e34c61e4c9295f5f11943e0043a7f978886210c4bab34b3159cfcedb5e7ba143234205cf27c04a5b6c9a42df5245cf1bc13bc601425)
#decipherToNum_3(65537,0x50886174e2215b2a1af3aa90b4856cc816f2d93732342613699c424c8b4a9e022974cf8aadd449dd8c80149f76854c61f139b4f7180acbdf49971d867809d4cb06603a3c5645295f0083b276f0f751f5bc71630d0c1c84ef65306ae9efd9820fc8bc162d07ea1ff9bf5dc4720f72dc4a6d33ffdcfc4a1f7847df61eeaa56c5bd,0x50886174e2215b2a1af3aa90b4856cc816f2d93732342613699c424c8b4a9e022974cf8aadd449dd8c80149f76854c61f139b4f7180acbdf49971d867809d4cb06603a3c5645295f0083b276f0f751f5bc71630d0c1c84ef65306ae9efd9820fc8bc162d07ea1ff9bf5dc4720f72dc4a6d33ffdcfc4a1f7847df61eeaa56c5bd)