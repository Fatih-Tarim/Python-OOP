class Personel:
    #class variables
    zam_orani = 1.05
    personel_sayisi = 0

    #Consturctor
    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim
        self.maas = maas
        self.email = f"{isim.lower()}.{soyisim.lower()}@firmam.com"
        Personel.personel_sayisi +=1

    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"
    
    def zam_uygula(self):
        self.maas = int(self.maas * self.zam_orani)
    



per_1 = Personel(isim="John", soyisim="Smith", maas=12000)
per_2 = Personel("Mary","Smith",15000)

# print(per_1.isim)
# print(per_1.soyisim)
# print(per_1.mass)
# print(per_1.email)

# print("{} {}".format(per_1.isim, per_1.soyisim))
# print(Personel.tam_isim(per_1))
# print(per_1.tam_isim())


print(per_1.maas)
per_1.zam_uygula()
print(per_1.maas)


# Python Name Space
from pprint import pprint
pprint(per_1.__dict__)
print("--------------------------------------")
pprint(Personel.__dict__)


print(Personel.personel_sayisi)
