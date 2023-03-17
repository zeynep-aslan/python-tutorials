# lambda fonksiyonları
# map() in yaptığı şey dizinin elemanlarını fonksiyona tek tek göndermek
# filter() mesela sadece çift olanları döndürmek istersek bir koşul varsa

# kare alma fonksiyonu
def square(num): return num ** 2

result = square(13)
print(result)
#------------

def square(num): return num ** 2

number = [1,23,4,56,7,89]
for num in number:
    print(square(num))
#------------

def square(num): return num ** 2
number = [1,23,4,56,7,89]
result = map(square, number)   # ilk parametre çağırılacak fonksiyon, 
print(result)                   # 2.parametre elemanları fonksiyona atılacak liste olmalı        
# <map object at 0x000001FD0C474C70>    
#------------

def square(num): return num ** 2
number = [1,23,4,56,7,89]
result = list(map(square, number))
print(result)
# ya liste metodu aracılığıyla ya da for döngüsüyle yazılmalı
# en mantıklısı i think
#------------

def square(num): return num ** 2
number = [1,23,4,56,7,89]
for item in map(square, number):
    print(item)
# 1
# 529
# 16
# 3136
# 49
# 7921    
#------------

square = lambda num: num ** 2
number = [1,23,4,56,7,89]
result = list(map(square, number))
print(result)
# gene aynı sonucu alırız
#------------

# bu şekilde fonksiyonmuş gibi kullanabiliriz
square = lambda num: num ** 2
result = square(3)
print(result)    # 9
#------------

# çift olanları döndürdü
def check_even(num): return num%2==0
numbers = [1,23,4,56,7,89]
result = list(filter(check_even, numbers))    # [4, 56]
result = list(filter(lambda num: num%2==0, numbers))    # [4, 56] gene aynı sonucu aldık
print(result)
#------------

check_even = lambda num: num%2==0
numbers = [1,23,4,56,7,89]
result = list(filter(check_even, numbers))    # [4, 56] gene aynı sonucu aldık
print(result)
#------------

check_even = lambda num: num%2==0
numbers = [1,23,4,56,7,89]
result = check_even(numbers[0])
print(result)     # False
# çünkü koşulu sağlamadı



# -----------------------
# sonradan eklenen dersler

# -------------------------------- any - all

# sonuc = all([True, True, False])  # hepsi true ise true, yoksa false döndürür
# sonuc = any([True, True, False])  # herhangi biri true ise true döndürür
# print(sonuc)
#------------

# sayilar = [0,1,2,3,4,5,10]
# sonuc = all([bool(sayi) for sayi in sayilar])  # [False, True, True, True, True, True, True], all eklenince false, 0 ı silersek true
# sonuc = any([bool(sayi) for sayi in sayilar])  # True
# sonuc = all([bool(sayi) for sayi in sayilar if sayi%2==0])  # False
# sonuc = [sayi%2==0 for sayi in sayilar]  # [True, False, True, False, True, False, True] teklik çiftliğe bakar
# print(sonuc)

# -------------------------------- sorted()

# sayilar = [0,34,1,123,4,76]
# sayilar.sort()  # [0, 1, 4, 34, 76, 123]
# print(sayilar)

# sonuc = sorted(sayilar)  # [0, 1, 4, 34, 76, 123] sıralar
# sonuc = sorted(sayilar, reverse = True)  # [123, 76, 34, 4, 1, 0] ters sıralar

# tuple listesinde normalde değişiklik yapamıyoruz ama sorted() fonk ile sıralayabiliriz
# sonuc = sorted((0,1,4,34,76,123))  # [0, 1, 4, 34, 76, 123]

# users = [
#     {"username":"sadikturan", "tweets":["tweet1", "tweet2"], "email":"info@gmail.com"},
#     {"username":"zeynepaslan", "tweets":[]},
#     {"username":"hulyaaslan", "tweets":["tweet1"], "name":"", "phone":"284509824"}
# ]

# sonuc = sorted(users, key=len)  # key bilgisi az olandan çok olana sıralar
# sonuc = sorted(users, key=len, reverse=True)  # tam tersi sıralar
# sonuc = sorted(users, key=lambda user: user["username"])  # username in baş harflarine göre sıraladı
# sonuc = sorted(users, key=lambda user: len(user["tweets"]))  # tweets leri az olandan çok olana sıraladı


# kurslar = [
#     {"title:": "python kursu", "students": 5000},
#     {"title:": "web gelistirme kursu", "students": 3000},
#     {"title:": "javascript kursu", "students": 7000}
# ]

# sonuc = sorted(kurslar, key=lambda kurs: kurs["students"])  # öğrenci az olandan çok olana sıralandı komple {} ile
# sonuc = sorted(kurslar, key=lambda kurs: kurs["students"], reverse=True)  # tam tersi

# sonuc = map(lambda kurs: kurs["title"], sorted(kurslar, key=lambda kurs: kurs["students"], reverse=True)) # hata veriyor nedenini anlamadım

# print(list(sonuc))


# -------------------------------- min - max
# uyg 22 de de vardı

# sayilar = [1,2,7,23,654]
# harfler = ['a', 'v', 'h', 's']


# sonuc = min(sayilar)  # 1
# sonuc = max(sayilar)  # 654

# sonuc = min(harfler)  # a
# sonuc = max(harfler)  # v

# isimler = ["zeynep", "ali", "seyma", "rumeysa"]
# sonuc = [len(isim) for isim in isimler ]  # [6, 3, 5, 7]
# sonuc = max([len(isim) for isim in isimler ]) # 7 
# sonuc = max(isimler, key=lambda n: len(n))  # rumeysa

# urunler = [
#     {"title":"iphone x", "price":5000},
#     {"title":"iphone xr", "price":6000},
#     {"title":"iphone 11", "price":7000}
# ]

# sonuc = min(urunler, key=lambda urun: urun["price"])
# {'title': 'iphone x', 'price': 5000}
# sonuc = max(urunler, key=lambda urun: urun["price"])["title"]
# iphone 11

# print(sonuc)

# üstteki gibi yapmaycak olursak
# max = 0
# for urun in urunler:
#     if urun["price"]>max:
#         max = urun["price"]

# print(max)  # 7000

# -------------------------------- abs - sum - round=yuvarlama
# ! metodların içine liste gönder [], sum([]), len([])

sayilar = [34,1,123,4,76]
# sonuc = sum(sayilar)  # 238
# sonuc = sum(sayilar, 10)  # 248

urunler = [
    {"title":"iphone x", "price":5000},
    {"title":"iphone xr", "price":6000},
    {"title":"iphone 11", "price":7000},
    {"title":"iphone 11 Pro", "price":0, "isactive":False}
]

# dict deki fiyatları toplar
# sonuc = sum([urun["price"] for urun in urunler])  # 18000

# 4.ürünü ekledikten sonra fiyat ort. bulmak istiyoruz ama fiyatı 0 olanı katmak istemiyoruz
# toplamFiyat = sum([urun["price"] for urun in urunler])
# urunAdedi = len([urun for urun in urunler if urun["price"]>0])
# sonuc = toplamFiyat/urunAdedi  # 6000.0
# yada isactive i false olan ürünü eklemezsin if bloğuyla


# round() = yuvarlama fonk

sonuc = round(10.2)  # 10
sonuc= round(10.5)  # 10, buçukları aşağı yuvarlar
sonuc = round(1.4242424242, 2)  # 1.42 , virgülden sonra 2 basamak aldık
sonuc = round(1.42626262, 2)  # 1.43 , 1.426 sayısı 1.43 e yuvarlanır



# print(sonuc)


