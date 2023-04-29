class Personel:
    
    # Consturctor
    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title() #Global
        self.soyisim = soyisim.title()
        self.maas = maas
        self.__zam_orani = 1.05 #Private
    
    def getZamOrani(self):
        return self.__zam_orani

    # def setZamOrani(self, oran):
    #     self.__zam_orani = oran

    def zam_uygula(self):
        self.maas = int(self.maas * self.__zam_orani)

per_1 = Personel("Dean","Winchester",15000)

print(per_1.getZamOrani())
per_1.setZamOrani(oran=1.2)
print(per_1.getZamOrani())



# print(per_1.maas)
# per_1.zam_uygula()
# print(per_1.maas)

