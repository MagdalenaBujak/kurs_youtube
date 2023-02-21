class zawodnik():
    def __init__(self, imie, wzrost, waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga

    def bmi(self):
        bmi = self.waga / (self.wzrost * self.wzrost) * 100
        print(bmi)

zawodnikM = zawodnik("magda", 165, 50)
zawodnikM.bmi()



