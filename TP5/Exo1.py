class Rectangle:
    def __init__(self, longueur, largeur, nom = "Rectangle"):
        self.longueur = longueur
        self.largeur = largeur
        self.nom = nom

    def surface(self):
        surface = self.longueur * self.largeur
        return f"la surface est de {surface}cm²."

    def __str__(self):
        return f"La longueur est de {self.longueur}cm et la largeur de {self.largeur}cm."
    
    
rect = Rectangle(15,10,"Rectangle")
print(rect.__str__(),rect.surface())


class  Carre(Rectangle):
    def __init__(self,cote,nom = "carre"):
        self.cote = cote
        self.nom = nom
        super().__init__(cote,cote,nom)

car = Carre(10,"carre")
print(car.__str__(),car.surface())
