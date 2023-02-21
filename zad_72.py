class Auto():

    def __init__(self, marka, model, cena, kolor, silnik):
        self.marka = marka
        self.model = model
        self.cena = cena
        self.kolor = kolor
        self.silnik = silnik

audi = Auto("audi", "A6", 1000, "czarny", 2.0)
skoda = Auto("auto", "karoq", 1000, "czerwony", 1.5)
opel = Auto("opel", "astra", 100, "biały", 1.8)

print(audi.marka, audi.model, audi.cena, audi.kolor, audi.silnik)
print(skoda.marka, skoda.model, skoda.cena, skoda.kolor, skoda.silnik)
print(opel.marka, opel.model, opel.cena, opel.kolor, opel.silnik)