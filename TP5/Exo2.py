class Airplane:
    def __init__(self,name : str):
        self.fly = False
        self.name = name

    def take_off(self):
        self.fly = True

    def land(self):
        self.fly = False
    
    def __str__(self):
        if self.fly:
            return f"{self.name} - flying"
        else:
            return f"{self.name} - ground"

class CivilAircraft(Airplane):
    def __init__(self,nb_passenger : int = 0, name = "CivilAircraft"):
        self.nb_passenger = nb_passenger
        super().__init__(name)
    
    def passenger_enter(self,nb : int):
        self.nb_passenger = nb + self.nb_passenger

    def passenger_leave(self, nb : int):
        self.nb_passenger = self.nb_passenger - nb

    def __str__(self):
        if self.nb_passenger != 0:
            return f"{super().__str__()} - {self.nb_passenger} passengers"
        else:
            return f"{super().__str__()} - no passengers"

    

p1,p2 = CivilAircraft(120, "Civil aircraft Airbus A380"),\
CivilAircraft(120,"Civil aircraft Airbus A380")
p2.passenger_leave(120)
p1.take_off()
p2.land()
print(p1)
print(p2)


