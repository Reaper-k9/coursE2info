import collections
import random

def polynome(a,b,c):
    lst = collections.deque()
    lst.append(random.randint(1, 10))
    lst.append(str(a))
    lst.append(str(b))
    lst.append(str(c))
    k = len(lst) - 1
    for i in range(len(lst)-1):
        lst[i] = f"{lst[i]}x^{k}"
        k -= 1
    return " + ".join(lst)

print(polynome(5, 4, 2))

a = int(input("Entrez une valeur pour a: "))
b = int(input("Entrez une valeur pour b: "))
c = int(input("Entrez une valeur pour c: "))
d = int(input("Entrez une valeur pour d: "))


def polynome_(a, b, c, d):
    lst = collections.deque()
    lst.append(str(a))
    lst.append(str(b))
    lst.append(str(c))
    lst.append(str(d))
    k = len(lst) - 1
    for i in range(len(lst)-1):
        lst[i] = f"{lst[i]}x^{k}"
        k -= 1
    return " + ".join(lst)
print(polynome_(a, b, c, d))

a1 = int(input("Entrez une valeur pour a1: "))
b1 = int(input("Entrez une valeur pour b1: "))
c1 = int(input("Entrez une valeur pour c1: "))
d1 = int(input("Entrez une valeur pour d1: "))
a2 = int(input("Entrez une valeur pour a2: "))
b2 = int(input("Entrez une valeur pour b2: "))
c2 = int(input("Entrez une valeur pour c2: "))
d2 = int(input("Entrez une valeur pour d2: "))

def additionpolynome(a1, b1, c1, d1, a2, b2, c2, d2):
    lst = collections.deque()
    lst.append(str(a1 + a2))
    lst.append(str(b1 + b2))
    lst.append(str(c1 + c2))
    lst.append(str(d1 + d2))
    k = len(lst) - 1
    for i in range(len(lst)-1):
        lst[i] = f"{lst[i]}x^{k}"
        k -= 1
    return " + ".join(lst)

print(additionpolynome(a1, b1, c1, d1, a2, b2, c2, d2))

a3 = int(input("Entrez une valeur pour a3: "))
b3 = int(input("Entrez une valeur pour b3: "))
c3 = int(input("Entrez une valeur pour c3: "))
d3 = int(input("Entrez une valeur pour d3: "))
a4 = int(input("Entrez une valeur pour a4: "))
b4 = int(input("Entrez une valeur pour b4: "))
c4 = int(input("Entrez une valeur pour c4: "))
d4 = int(input("Entrez une valeur pour d4: "))

def multiplicationpolynome(a3,b3,c3,d3,a4,b4,c4,d4):
    lst = collections.deque()
    lst.append(str(a3 * a4))
    lst.append(str(b3 * b4))
    lst.append(str(c3 * c4))
    lst.append(str(d3 * d4))
    k = 2*len(lst) - 2
    for i in range(len(lst)-1):
        lst[i] = f"{lst[i]}x^{k}"
        k -= 2
    return " + ".join(lst)

print(multiplicationpolynome(a3, b3, c3, d3, a4, b4, c4, d4))