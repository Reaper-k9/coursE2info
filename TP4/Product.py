class Product:
    def __init__(self, priceET, code, name):
        self.code = code
        self.name = name
        self.priceET = priceET

    def get_price_it(self):
        prixTTC = self.priceET+self.priceET*0.2
        return print(prixTTC)
    
produit = Product(10.99,"A12Dcf54","boite")
print(produit.code, produit.name)
produit.get_price_it()

    