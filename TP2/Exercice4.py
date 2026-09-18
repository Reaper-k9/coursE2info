regles = ["x", "+", "D", "C"]
#"x" -- Enregistre un nouveau score de x.
#"+" -- Enregistre un nouveau score qui est la somme des deux scores précédents.
#"D" -- Enregistrez un nouveau score qui est le double du score précédent.
#"C" -- Invalide le score précédent, en le supprimant de l'enregistrement.

def calculScore(regles):
    scores = []
    for regle in regles:
        if regle[0] == "x":
            scores.append(int(regle[1:]))
        elif regle == "+":
            scores.append(scores[-1] + scores[-2])
        elif regle == "D":
            scores.append(scores[-1] * 2)
        elif regle == "C":
            scores.pop()
    return sum(scores)

print(calculScore(["x3", "x2", "+", "D", "C","x5"]))