class Matematik:
    def __init__(self,sayi1,sayi2): #constructor-yapıcı blok
        self.s1 = sayi1
        self.s2 = sayi2
        print("Matematik başladı (referansı oluştu)")
    def topla(self):
        return self.s1 + self.s2
    def cikar(self):
        return self.s1 - self.s2
    def bol(self):
        return self.s1 / self.s2
    def carp(self):
        return self.s1 * self.s2
    

matematik = Matematik(14,7)
sonuc = matematik.cikar()
print("Sonuç : " + str(sonuc))

class Istatistik(Matematik):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2) #super dediği matematik yani base class ın kendisi
    def varyansHesapla(self):
        return self.s1 * self.s2
    
# inheritance
    
    
istatistik = Istatistik(5,8)

