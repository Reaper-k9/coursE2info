import random
tab = [random.randint(0,500) for _ in range(random.randint(3,99))]
doublons = []
for i in range(0,len(tab)-1):
    for y in range(i+1,len(tab)):
        if(tab[i]==tab[y]):
            doublons.append(tab[i])
if(len(doublons)==0):
    print("Il n'y a pas de doublons")
else:
    print("Il y a des doublons")
    print(f"Les doublons sont : {doublons}")
