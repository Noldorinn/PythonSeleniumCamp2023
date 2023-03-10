#1) Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

str="Hello World" #String, metinsel ifadelerin yer aldığı bir veri tipidir.

int=20 #Integer, tam sayı şeklinde veri tipidir.

float=15.5 #Float, ondalıklı sayı şeklinde veri tipidir.

complex=1j #Complex, karışık olarak verinin bulunduğu veri tipidir.

list=["bmw","mercedes","audi",5,6,7] #List, içerisinde eleman barındırabilen listeyi ifade eder.
#Liste elamanları güncellenebilir.

tuple1=1,"iki",3 #Tuple, liste gibi elemanlar bulunduran veri tipidir.
tuple2=(5,6,"yedi") #Tuple'da eleman güncellemesi yapamayız.

range=range(10) #Range, aralık,uzunluk(mesafe) belirten veri tipidir.

dict={"kocaeli":41 , "istanbul":34} #Dictionary, liste benzeri her metinin bir değeri olması gereken veri tipidir.
#Dictionary'de güncelleme yapapbliriz. key:value

set={"Germany","France","Netherlands"} #Set, liste benzeri veri tipidir.
#Set'de elemanlar indexlenemez, sıralanamaz, birden fazla aynı eleman eklenemez.

bool=True #Boolean, sadece 2 çeşit değer alan veri tipidir(True ya da False).


# 2) Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

# Ana Sayfada kurslar Liste şeklindedir.
# Kurs isimleri, açıklamaları, eğitmen ismi String şeklindedir.
# Kursun tamamlama yüzdesi Float türündedir.
# Ödevlerin tamamlanmış olup olmadığı Boolean türündedir.
# Yorum sayıları Integer şeklindedir.


# 3) Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

# Öğrenci tüm ödevleri tamamlayıp bitir ve devam et butonuna tıkladığında Checkmark(tik işareti) aktif olur.

# Login ekranında doğru kullanıcı adı ve şifre girildiğinde kullanıcı sisteme giriş yapar.

email="abc@gmail.com"
password="123"

if(email=="abc@gmail.com"):
    if(password=="123"):
        print("Giriş başarılı")
    else:
        print("Şifre hatalı")
else:
    print("email hatalı")



