import random
import unicodedata

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

with open("Z:/Eseo/info/coursE2info/TP3/dic.txt","r", encoding = "utf-8") as f:
    ligne = f.readlines()
    ligne_al = random.choice(ligne)
    ligne_al = strip_accents(ligne_al).strip().upper()
    #print(ligne_al)
mot = list(ligne_al)
#print(mot)
secret = []
secret += mot[0]
for i in range(1,len(mot)):
    secret += "_"
print(secret)
vie =10
lettres = []
print("Vous avez 10 vies !")
while(mot != secret and vie != 0):
    a = input("Entrer une lettre : ")
    a = a.upper()
    if a in lettres:
        print("Cette lettre à déjà été utilisée")
    else:
        if a in mot:
            for i in range(len(mot)):
                if a == mot[i]:
                    secret[i] = mot[i]
                    lettres += a
                    print(secret)
        else:
            vie -= 1
            print(secret)
            print(f"Cette lettre n'est pas dans le mot... Il vous reste plus que {vie} vies...")
            lettres += a

print("Bravo ! vous avez trouvé le mot secret",ligne_al)