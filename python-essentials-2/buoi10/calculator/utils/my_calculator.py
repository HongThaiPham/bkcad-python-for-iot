import math


def add(so):
    tong = 0
    for s in so:
        tong += s
    return tong


def sub(a, b):
    return a - b


def mul(so):
    tich = 1
    for s in so:
        tich *= s
    return tich


def div(a, b):
    return a/b


def sin(a):
    return math.sin(math.radians(a))


def cos(a):
    return math.cos(math.radians(a))
