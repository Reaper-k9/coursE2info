from math import factorial

def fact(a):
    return factorial(a)
print(fact(4))

def facto(b):
    if b == 0 : return 1
    return b*facto(b-1)
print(facto(5))