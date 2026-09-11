résultat = " "
q = int(input("Entrer un nombre : "))
while(q!=0):
    r=q%2
    résultat += str(r)
    q=q//2
print("Vote nombre converti en binair est :",résultat[::-1])