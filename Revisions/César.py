
def decalage_cesar(clé,phrase):
    clé = list(clé.upper())
    phrase = list(phrase.upper())
    #print(clé,phrase)
    print("".join(phrase),"-->", end = " ")
    j = 0
    for i in range(len(phrase)):
          if j <= len(clé)-1:
            phrase[i] = chr(ord(phrase[i])+ord(clé[j])- 64)
            j += 1
          else:
            j=0
            phrase[i] = chr(ord(phrase[i])+ord(clé[j])- 64)
            j += 1
    return "".join(phrase)

print(decalage_cesar("ab","bonjour"))

