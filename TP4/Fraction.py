class Fraction:

    def __init__(self, nume: int, deno: int):
        self.nume = nume
        self.deno = deno

    def __str__(self):
        return f"{self.nume}/{self.deno}"

    def __add__(self, other):
        newnume = self.nume * other.deno + self.demo * other.nume
        newdeno = self.deno * other.deno
        return Fraction(newnume,newdeno)
    
ob1 = Fraction(5,4)
ob2 = Fraction(4,3)
print()
    
