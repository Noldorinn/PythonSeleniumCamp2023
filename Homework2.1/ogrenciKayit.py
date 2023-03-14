ogrenciler=["Ali Aygün","Arda Aygün"]

def ogrenciEkle():
    isim=input("Ogrenci adi: ")
    if (isim.isalpha()==True): 
        soyisim=input("Ogrenci soyadi: ")
        if (soyisim.isalpha()==True):
            print(f"{isim} {soyisim} adlı kişiyi eklemek istiyor musunuz? evet/hayır")
            if str(input())=="evet":
                ogrenciler.append(f"{isim} {soyisim}")
                print("öğrenci eklendi")
                print(ogrenciler)
                return
            else:
                print("öğrenci eklenmedi") 
        else :
            print("geçerli bir isim giriniz!")   
    else:
        print("geçerli bir isim giriniz!") 
        return

def  ogrenciSil():
    isim=input("Silinecek ogrenci adi: ")
    if (isim.isalpha()==True):
        soyisim=input("Silinecek ogrenci soyadi: ")
        if (soyisim.isalpha()==True):
            for varmi in ogrenciler:
                if (varmi==(f"{isim} {soyisim}")):
                    print(f"{isim} {soyisim} adlı kişiyi silmek istiyor musunuz? evet/hayır")
                    if str(input())=="evet":
                        ogrenciler.remove(varmi)
                        print("Öğrenci silindi")
                        print(ogrenciler)
                    else:
                         return
                else:
                    print("Aradığınız öğrenci listede bulunamadı!")
                    return
        else:
            print("geçerli bir isim giriniz!") 
    else:
        print("geçerli bir isim giriniz!")

def ogrencilerEkle():
    eklemeSayisi=int(input("Eklemek istediğiniz öğrenci sayısını giriniz: "))
    i=0
    while (i<eklemeSayisi):
        isim=str(input("Öğrenci adı: "))
        soyisim=str(input("Öğrenci soyadı: "))
        print(f"{isim} {soyisim} isimli öğrenci eklensin mi? evet/hayır")
        if (input()=="evet"):
            ogrenciler.append(f"{isim} {soyisim}")
            print(ogrenciler)
            i+=1
        else:
            i=i
        
def tumOgrenciler():
    for tum in ogrenciler:
        print(tum)

def ogrenciNoOgren():
    print("Numarasını öğrenmek istediğiniz öğrencinin")
    isim=str(input("Adı: "))
    soyisim=str(input("Soyadi: "))

    for ara in range(len(ogrenciler)):
        if ogrenciler[ara]==(f"{isim} {soyisim}"):
            print(f"{isim} {soyisim} adlı öğrencinin numarası: {ara}")
            return
        else:
            print("Öğrenci listede bulunamamıştır.")
            return
        
def ogrencileriSil():
    silinecekSayi = int(input("Silinecek öğrenci sayısını giriniz: "))
    for s in range(silinecekSayi):
        isim=str(input("Silinecek öğrenci adı: "))
        soyisim=str(input("Silinecek öğrenci soyadı: "))
        ogrenciler.remove(f"{isim} {soyisim}")
    print(ogrenciler)

