def Syraccus(a):
    int(a)
    print(a)
    while a != 1:
        r = a%2
        if r == 0: 
            a = a/2
            print(a)
        else: 
            a = a*3 + 1
            print(a)
    return a
    
print(Syraccus(1243))
