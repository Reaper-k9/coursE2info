a=1
while(a!=0):
    a = int(input("Un calcul ? Si non taper 0 si oui taper 1 :"))
    if(a==0):
        break
    else:
        a = int(input("Quelle est l'opération souhaitée, addition(1), soustraction(2), multiplication(3) ou division(4) :"))
        print("\nTrès bien maintenant 2 nombres")
        b = float(input("Premier chiffre :"))
        c = float(input("Deuxième chiffre :"))
        if(a==1):
            a=b+c
            print("Le résultat est :",a)
        elif(a==2):
            a=b-c
            print("Le résultat est :",a)
        elif(a==3):
            a=b*c
            print("Le résultat est :",a)
        elif(a==4):
            if(c==0):
                print("On ne peut pas diviser par 0")                              
            else:
                a=b/c
                print("Le résultat est :",a)
        
