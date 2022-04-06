import math
import numlib as nl
import polylib as pl
from random import randint
from commonFunctions import I2OSP,OS2IP,sqrt

p = 2**255-19
F = nl.Zmodp(p)
a = F(0x2aaaaaaa_aaaaaaaa_aaaaaaaa_aaaaaaaa_aaaaaaaa_aaaaaaaa_aaaaaa98_4914a144)
b = F(0x7b425ed0_97b425ed_097b425e_d097b425_ed097b42_5ed097b4_260b5e9c_7710c864)
E = nl.EllCurve(a, b, debug=True)
q = 0x10000000_00000000_00000000_00000000_14def9de_a2f79cd6_5812631a_5cf5d3ed

m = (E(0x375357c574ba626305162a7ee1aea098d08115e3b1141ebcfdd7eb93a9f72a07, 0x64f481427dc5e13fa747a4f22c1f2a0498d5e67c834bff39578dd1fa758f730a), 
     E(0x1ee406b7a7646a78472ab6e24fec10379c01c58fb53bb8fc27d0eb40fdea7c3e, 0x1722c75b3d91af25dee9001726aec64591274490b078672b05d745995cf3d032))

def bytes2curve(bytestring):
    """return a tuple of encoded point(s) of Wei25519"""
    points = []
    for start in range(0, len(bytestring), 30):
        for i in range(256):
            x = OS2IP(bytestring[start: start+30] + i.to_bytes(1, byteorder='big'))
            fx = int(E.f(x))
            if pow(fx, (p-1)//2, p) == 1:
                P = E(x, sqrt(fx, p))
                if nl.addorder(P, q*8) > 8:
                    break
        points.append(P)
    return tuple(points)

def curve2bytes(points):
    """map a tuple of point(s) on Wei25519 to a byte-string"""
    bytestring = b""
    for point in points:
        x = int(point.co[0]*point.co[2]**-1)  # the x-coordinate as an integer
        bytestring += I2OSP(x, xLen = 31)[31 - math.ceil(math.log(x, 256)):-1]
    return bytestring

def point(order):
    """return a point of the given order"""
    found_order = -1
    while found_order != order:
        x = randint(0, p-1)
        fx = int(E.f(x))
        if pow(fx, (p-1)//2, p) == 1:
            y = sqrt(fx, p)
            pt = E(x, y)
            found_order = nl.addorder(pt, q*8)
    return pt

# find generator of degree 8
P = point(q*8)  # P is now a generator of E
print(P)

curve2bytes(m)


