class Personel:
    # class variables
    zam_orani = 1.05
    personel_sayisi = 0

    # Consturctor
    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim
        self.maas = maas
        self.email = f"{isim.lower()}.{soyisim.lower()}@firmam.com"
        Personel.personel_sayisi += 1
        #print(f"Yeni Personel Tanımlandı: {isim} {soyisim}")

    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"

    def zam_uygula(self):
        self.maas = int(self.maas * self.zam_orani)

    @classmethod
    def zam_oranini_belirle(cls, oran):
        eski_oran = cls.zam_orani
        cls.zam_orani = oran
        #print(f"Zam oranı değiştirildi eski zam oranı ({eski_oran}). Yeni zam oranı ({cls.zam_orani}) ")

    @classmethod
    def from_string(cls, per_str):
        isim, soyisim, maas = per_str.split("-")
        return cls(isim, soyisim, maas)

    @staticmethod
    def mesai_gunu(gun):
        if gun.weekday == 5 or gun.weekday == 6:
            return "Hafta sonu"
        else:
            return "Hafta içi"
    
    def __repr__(self):
        return f"Personel('{self.isim}','{self.soyisim}','{self.email}')"

    def __str__(self):
        return f"{self.tam_isim()} | {self.email}"

    def __add__(self, other):
        return self.maas + other.maas
    
    def __len__(self):
        return self.tam_isim().__len__()


# Method Resolution Order

class Yazilimci(Personel):
    zam_orani = 1.1

    def __init__(self, isim, soyisim, maas, dil):
        super().__init__(isim, soyisim, maas)
        self.dil = dil
        #print(f"Yeni Personel Yazılımcı Kategorisine Taşındı: {self.isim} {self.soyisim}")


class Mudur(Personel):
    def __init__(self, isim, soyisim, maas, personeller= None):
        super().__init__(isim, soyisim, maas)
        if personeller is None:
            self.personeller = []
        else:
            self.personeller = personeller
     

    def personle_ekle(self, per):
        if per not in self.personeller:
            self.personeller.append(per)
    
    def personle_sil(self, per):
        if per in self.personeller:
            self.personeller.remove(per)
    
    def personelleri_listele(self):
        for e, per in enumerate(self.personeller):
            e += 1
            print(e, per.tam_isim())


yazilimci_1 = Yazilimci(isim="John", soyisim="Smith", maas=12000, dil="python")
yazilimci_2 = Yazilimci("Mary", "Smith", 15000, "Java")

mdr_1 = Mudur('John', 'Wick', 70000, [yazilimci_1])
mdr_2s = Mudur('John', 'Snow', 70000)

personel_1 = Personel(isim="Fatih", soyisim="Tarim", maas=12000)
personel_2 = Personel("Will","Smith",15000)

#personel_1.__add__(personel_2) ==  personel_1 + personel_2

print(personel_1 + personel_2)
print(len(personel_1))







# print(str(personel_1))
# print(repr(personel_1))
# #print(help(personel_1))
# print(personel_1.__str__())
# print(int.__add__(2,3))






# #isinstance()
# print(isinstance(yazilimci_1, Personel))

# #issubclass()
# print(issubclass(Yazilimci, Personel))



# print(mdr_1.tam_isim())
# print("------------------------")
# mdr_1.personelleri_listele()
# print("------------------------")
# mdr_1.personle_ekle(yazilimci_2)
# mdr_1.personelleri_listele()

# print(yazilimci_1.dil)
# yazilimci_1.zam_uygula()
# #print(yazilimci_2.dil)


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

# per_str_1 = "Sam-Winchester-40000"
# per_str_2 = "Dean-Winchester-60000"
# per_str_3 = "Bobby-Singer-60000"

# yeni_per = Personel.from_string(per_str_1)

# print(yeni_per.email)
# print(yeni_per.maas)

# import datetime
# tarih = datetime.date(2022,4,6)
# print(tarih.day)
# print(Personel.mesai_gunu(tarih))
