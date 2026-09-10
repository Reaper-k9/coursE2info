age = int(input("Entrer votre age : "))
if age<=0:
    print("Veuillez naitre avant de fair ce test.")
if age<=2:
    resultat=age*10.5
    print("Votre age cannin est de :",resultat)
else:
    resultat,age=21,age-2
    resultat+=age*4
    print("Votre age cannin est de :",resultat)
    