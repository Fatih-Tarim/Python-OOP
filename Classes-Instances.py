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
    
    @classmethod
    def zam_oranini_belirle(cls, oran):
        eski_oran= cls.zam_orani
        cls.zam_orani = oran
        print(f"Zam oranı değiştirildi eski zam oranı ({eski_oran}). Yeni zam oranı ({cls.zam_orani}) ")
    
    @classmethod
    def from_string(cls, per_str):
        isim,soyisim,maas = per_str.split("-")
        return cls(isim, soyisim, maas)

    @staticmethod
    def mesai_gunu(gun):
        if gun.weekday == 5 or gun.weekday == 6:
            return "Hafta sonu"
        else:
            return "Hafta içi"

    

per_1 = Personel(isim="John", soyisim="Smith", maas=12000)
per_2 = Personel("Mary","Smith",15000)

# print(per_1.isim)
# print(per_1.soyisim)
# print(per_1.mass)
# print(per_1.email)

# print("{} {}".format(per_1.isim, per_1.soyisim))
# print(Personel.tam_isim(per_1))
# print(per_1.tam_isim())


# print(per_1.maas)
# per_1.zam_uygula()
# print(per_1.maas)


# Python Name Space
# from pprint import pprint
# pprint(per_1.__dict__)
# print("--------------------------------------")
# pprint(Personel.__dict__)

# print(Personel.personel_sayisi)

# Personel.zam_oranini_belirle(1.1)
# print(Personel.zam_orani)
# print(per_1.zam_orani)
# print(per_2.zam_orani)

per_str_1 = "Sam-Winchester-40000"
per_str_2 = "Dean-Winchester-60000"
per_str_3 = "Bobby-Singer-60000"

yeni_per = Personel.from_string(per_str_1)

print(yeni_per.email)
print(yeni_per.maas)

import datetime
tarih = datetime.date(2022,4,6)
print(tarih.day)
print(Personel.mesai_gunu(tarih))

