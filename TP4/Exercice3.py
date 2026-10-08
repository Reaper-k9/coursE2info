

class CardValue:

    def __init__(self,value_txt,value_pts):
        self.value_txt = value_txt
        self.value_pts = value_pts

    def __str__(self):
      return f"La carte est {self.value_txt} et vaut {self.value_pts} points"

car = CardValue("Q",12)
#print(car.value_txt, car.value_pts)
print(car.__str__())



class CardColor:
    def __init__(self, shade, shade_name, foreground_color, background_color):
        self.shade = shade
        self.shade_name = shade_name
        self.foreground_color = foreground_color
        self.background_color = background_color
    
    def __str__(self):
        return f"La forme est {self.shade} soit le {self.shade_name}\
 de couleur {self.foreground_color} et la carte est {self.background_color}"


cart = CardColor("♣","trèfle","Black","White")
print(cart.__str__())

#class Card:

