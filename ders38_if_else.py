# isLogin = False
# if isLogin:
#     print('Hoşgeldiniz')

# username = 'zeynepaslan'
# password = '1234'
# isLogin = (username == 'zeynepAslan') and (password == '1234')
# if (username == 'zeynepaslan'):
#     if (password == '12345'):
#         print('hoşgeldiniz')
#     else:
#         print('parolanız yanlış')    
# else:
#     print('username iniz yanlış')    


# ders 39-------    

# x = int(input('x: '))
# y = int(input('y: '))

# if (x>y):
#     print('x, y den büyük')
# elif (x == y):
#     print('x, y ye eşit')    
# else:
#     print('y, x den büyük')    

# ders 40----

# isim yaş eğitim al
# ehliyet sınır 18 eğitim lise yada üni olmalı

# isim = input('isminizi giriniz: ')
# yas = int(input('yasinizi giriniz: '))
# egitim = input('mezun oldugunuz son okulu giriniz: ')
# isEgitim = (egitim == 'lise') or (egitim == 'universite')

# if yas<18:
#     print('yasiniz 18 den kucuk oldugu icin size ehliyet veremiyoruz')
# else:
#     if isEgitim:
#         print('ehliyet alabilirsiniz')    
#     else:
#         print('egitim bilginiz yeterli degil')


# trafiğe çıkış tarihi alınan bir aracın servis zamanını bilgilere göre hesapla
# 1.bakım => 1. yıl
# 2.bakım => 2. yıl
# 3.bakım => 3. yıl
# ** süre hesabını alınan gün, ay, yıl bilgilerine göre gün bazlı hesaplayınız
# *** datetime modülünü kullan
# şimdi - (2018/8/8) => gün

# import datetime

# tarih = input('trafige cikis tarihinizi giriniz (2019/8/20): ')
# tarih = tarih.split('/')  # tarih listesine attı
# trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))  # obje haline çevirdik

# simdi = datetime.datetime.now()  # bu bir obje
# fark = simdi - trafigeCikis
# days = fark.days

# if days<=365 and days>0:
#     print('1.servis araligi')
# elif days<=365*2 and days>365:
#     print('2.servis araligi')
# elif days<=365*3 and days>365*2:
#     print('3.servis araligi')
# else:
#     print('hatali sure')

# mert mekatronik datetime kullanımı--------------------
from datetime import datetime

suan = datetime.now()
print(suan)
print(type(suan)) # <class 'datetime.datetime'> datetime modülünün datetime sınıfından bir obje
print(suan.__str__()) # 2 üstteki ile aynı. objeyi çağırdıktan sonra döndürdüğü değer olarak taNIMLnmış
print(suan.year)
print(type(suan.year)) # int

# print(suan.year)
# print(suan.month)
# print(suan.day)
# print(suan.hour)
# print(suan.minute)
# print(suan.second)
print(suan.date()) # bu 2 si obje dönüştürdüğü için metod olarak alıyoruz date() time()   tarih
print(suan.time())  # saat

# print(type(suan.year))    # <class 'int'>
# print(type(suan.date()))  # <class 'datetime.date'>
# print(suan.date().split("-")) # date i stringe çevirmen lazım because split() string metodudur
# tarih = str(suan.date()).split("-")
# print("Yil: {} Ay: {} Gün: {} ".format(tarih[0], tarih[1], tarih[2]))

# import time

# while True:
#     suan = datetime.now()
#     saniye = suan.second
#     if (saniye == 10):
#         print("saniye 10'a geldi!")
#         break

#     print(suan)    
#     time.sleep(1)    # bunu koymazsan değerler çok hızlı döner

# print(datetime.ctime(suan))  # Wed Jun 17 14:21:19 2020 # string dir
# print(datetime.ctime(suan).split(" ")[3].split(":"))   # ['14', '23', '00']

# ders 41---------------




