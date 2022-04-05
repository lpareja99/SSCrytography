#blumblumshub.py
import random
import numlib

n = 0x4ff8568a0d39836d32dbf022675362b03ae6c566b8027ad9811b71cbe8c5fa37bc60188e4b915cc8de90d2c24ecba81c42f5bd601cc93c4c880ccb0539ed68c5435fc1cb83e1ddf840293eaaef32c46a3366bfd4fb907a1623c9fd5478f5b0ef749c40aebd56509b67e4b08c87d54f910f6fc8b310ce2d10c0cab35784adf4b5

state = random.randint(1,n-1)
while numlib.gcd(state, n) != 1:
    state = random.randint(1,n-1)

state = state  * state  % n

def prbg_():
    global state
    state  = state  * state  % n
    return state  % 2

def prbg(length):
    bitstring = ''
    for _ in range(length):
        bitstring += str(prbg_())
    return bitstring