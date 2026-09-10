i = 10
liste=[]
num=0
while(i>=0):
    i=float(input("Entrer une valeur :"))
    if i>=0:
        liste+=[i]
    else:
        break
for y in range(len(liste)):
    for z in range(len(liste)):
        if liste[y]<=liste[z]:
            c=liste[y]
            liste[y],liste[z]=liste[z],c
print("Ordre croissant :",liste,"\nLa plus grande et la plus petite valeur sont :",min(liste),"et",max(liste),'\n')
for h in liste:
    num+=h
den=len(liste)
moyenne=num/den
print("La moyenne est de :",moyenne)