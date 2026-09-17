test=0
plaque= ""
while(test!=1):
    import string
    a = string.ascii_uppercase
    import random
    plaque += str(random.choice(a))
    b2 = random.choice(a)
    b3 = random.choice(a)
    b4 = random.choice(a)
    c = random.randrange(0,10)
    c2 = random.randrange(0,10)
    c3 = random.randrange(0,10)
    plaque
    for i in range(len(plaque)):
        if(plaque[i]=="I" or plaque[i]=="O" or plaque[i]=="U"):
            test=0
        else:
            test = 1

for i in range(len(plaque)):
    print(plaque[i])

            

