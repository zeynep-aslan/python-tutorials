# def changeName(n):
#     n = 'Ada'

# name = 'Yigit'
# changeName(name)
# print(name)     # Yigit. ilk tanımladığımız değer fonksiyon tarafından değiştirilemedi.
# # n değişkeninin değerinin bellekte tutulduğu adresle name değişkeninin değerinin tutulduğu adres farklı
# fonksiyon için değişkenin farklı bir kopyası hazırlanoypr

# def change(n):
#     n[0] = 'istanbul'

# sehirler = ['ankara', 'izmir']
# change(sehirler)
# print(sehirler)     # ['istanbul', 'izmir']
# burda value type lardan farklı olarak referans kopyalaması yapıyoruz
# n parametresine sehirler dizisinin adresi gidiyor
# fonksiyonun içine sehirler listenin adresi gönderiliyor


# sehirler = ['ankara', 'izmir']
# n = sehirler
# n[0] = 'istanbul'
# print(sehirler)
# üsttekiyle aynı sonucu aldık


# eğer adres kopyalaması yapmak yerine sadece içindeki elemanları kopyalamak istersek
# sehirler = ['ankara', 'izmir']
# n = sehirler[:]    # slicing = parçalama, dilimleme yöntemi
# n[0] = 'istanbul'
# print(n)
# print(sehirler)
# ilk listenin adresini kopyalmadığımız için onun içindeki elemanlarda değişiklik yapamıyoruz
# string type larda olduğu gibi
# ['istanbul', 'izmir']
# ['ankara', 'izmir']


# def change(n):
#     n[0] = 'istanbul'

# sehirler = ['ankara', 'izmir']
# change(sehirler[:])   # slicing
# print(sehirler)
# sadece kopyaladık


# list() gönderdiğimiz bilgileri listeye çevirir
# sum: python la birlikte hazır gelen 'built in' yani gömülü gelen bir fonksiyon, toplar
# def add(a, b):
#     return sum((a, b))

# print(add(10, 20))


# fonksiyonu bazen 2 parametreli bazen 3 parametreli kullanmak istiyorsak c = 0 deriz
# def add(a, b, c = 0):
#     return sum((a, b))

# print(add(10, 20))
# print(add(10, 20, 30))    # return kısmına c yi yazmadığımız için 3. parametreyi takmadı
# bu şekilde 2 parametreli versiyonu da çalışır 3 parametreli versiyonu da


# def add(a, b, c = 0):
#     return sum((a, b, c))

# print(add(10, 20, 30))


# peki istediğimiz kadar parametre göndermek istersek
# def add(*params):
#     print(params)
#     print(params[0])
#     print(params[1])
#     return sum((params))

# print(add(10, 20, 30))
# print(add(10, 20, 30, 40))
# print(add(10, 20, 30, 40, 50))
# print(add(10, 50, 70))
# print(add(10, 80))
# gönderilen tüm parametreleri tuple listesiyle ekrana yazdırdı
# hepsini topladı


# farklı bir toplama yöntemi
# def add(*params):
#     print(type(params))
#     sum = 0
#     for i in params:
#         sum +=i
#     return sum

# print(add(10, 20))    
# print(add(10, 20, 30)) 
# params ın type ı <class 'tuple'>

# def displayUser(**args):
#     print(type(args))
#     for key, value in args.items():
#         print('{} is {}'.format(key, value))

# displayUser(name = 'Zeynep', age = 19, city = 'istanbul')
# displayUser(name = 'Niran', age = 18, city = 'sakarya', phone = '31723987192')
# displayUser(name = 'Beyza', age = 18, city = 'ankara', phone = '1723987192', email = 'beyza@gmail.com')

# args da gönderebilsin params da yeter ki parametrenin dictionary olduğunu belirten ** işaretini koy
# args ın type ı <class 'dict'>


# def myfunc(a, b, c, *args, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)

# myfunc(10, 20, 30, 40, 50, key1 = 'value1', key2 = 'value2')
# args keywordargs genelde bu şekilde yazılır
# 10
# 20
# 30
# (40, 50)
# {'key1': 'value1', 'key2': 'value2'}



""" uygulama------------- """

# 1- gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yaz
def sendWord(word, repeat):
    print(word*repeat)    
kelime = input('bir kelime giriniz: ')    
tekrar = int(input('girdiginiz kelimenin tekrar edilme sayisini giriniz: '))
sendWord(kelime, tekrar)

# 2- kendine gönderilen sınırsız sayıda parametreyi bir listeye çeviren fonksiyon
# def makeList(*params):
#     sum = list(params)
#     return sum                   # neden sum(list(params)) deyince sayıları topladı
# print(makeList(2,3,12,'zey'))

def makeList(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste

result = makeList(1,2,'zeynep')
print(result)  
  

# 3- gönderilen 2 sayı arasındaki tüm asal sayıları bulun
def asalBul(sayi1, sayi2):  
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi%i==0):
                    break
            else:
                print(sayi)

num1 = int(input('bir sayi giriniz: '))  
num2 = int(input('bir sayi giriniz: '))  
asalBul(num1,num2)

# 4- kendine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyon

def tamBolen(sayi):
    list = []
    for i in range(1,sayi):
        if (sayi%i==0):
            list.append(i)
    list.append(sayi)        
    print(list)        

num = int(input('bir sayi giriniz: '))
print('sayinin tam bolenleri: ')
tamBolen(num)