class Personel:
    #Consturctor
    
    def __init__(self, isim, soyisim, maas):
        self.isim = isim.title()
        self.soyisim = soyisim
        self.mass = maas
        self.email = f"{isim.lower()}.{soyisim.lower()}@firmam.com"

    def tam_isim(self):
        return f"{self.isim} {self.soyisim}"
    

per_1 = Personel(isim="John", soyisim="Smith", maas=12000)
per_2 = Personel("Mary","Smith",15000)

# print(per_1.isim)
# print(per_1.soyisim)
# print(per_1.mass)
# print(per_1.email)

print("{} {}".format(per_1.isim, per_1.soyisim))
print(Personel.tam_isim(per_1))
print(per_1.tam_isim())