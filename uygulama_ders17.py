# ----------metod listesi----------

# metodlarda parametre göndermiycek olsan bile parantez açıp kaparsın
# upper() metodu string ifadenin içindeki tüm harfleri büyük hale getirir
# lower() metodu string ifadenin içindeki tüm harfleri küyük hale getirir
# title() metodu string ifadedeki ilk harfleri büyük yapar
# capitalize() metodu string ifadedeki ilk harfi büyük yapar diğer harfler küçük olur
# strip() metodu stringin başında boşluk karakteri varsa yok eder. şifrede boşluk yazdı mesela kullanıcı sıkıntı elden geçirmek lazım
# strip() metodunun içine yazdığın ifadeleri siler. ders19 2.örnek
# split() metodu her kelimeyi ayırır tırnaklarla. dizi oluşturur.(nokta kelime sayılmaz) içinde stringdeki bir ifadeyi yazarsak parçalarken o elemanı baz alır
# join(buraya stringi tuttuğun değişkenin adını yaz) metodu dizi haline getirdiğin stringi birleştirir " ".join(message)
# find() parametrenin içine yazdığın ifade stringde varsa baş harfinin indeksini verir yoksa -1 verir index() de aynı işe yarıyor(istenilen ifadeyi bulamazsa hata mesajı döndürür ama find() ile arasındaki fark bu)
# rfind() sağ taraftan saymaya başlar mesela 2 tane var son taraftakini bulur
# startswith("H") string ifade H ile başlıyorsa True değerini döndürür
# endswith("n") string ifade n ile bitiyorsa True değerini döndürür
# replace("Sadık","Çınar") sting ifadesinde Sadık yerine Çınar yazar ç leri c falan yaparsın işe yarar
# center(100."*") 100 karakterlik bir alan ayırır ve string ifadesini ortalar. sağ ve solunda * koyar
# (count('a')) kaç tane a varsa sayısını verir
# isalpha() is alpha alfabetik mi true or false
# isdigit() is digit sayı mı true or false
# 'Mercedes' in car_list listeden stringi arar varsa true döner
# car_list.pop() son indisten eleman siler. eğer içine sayı yazarsan o indisteki elemanı siler
# val=min(numbers)
# val = max(numbers)
# val=min(letters)
# val=max(letters) sayı yada string farketmiyor
# numbers.append(59) -> listenin sonuna bu elemanı ekler
# numbers.insert(3, 78)  -> liste.insert(index, eleman)  ->  verilen indisten önce elemanı ekler
# numbers.remove(49) (içine yazdığı eleman. indis değil) -> içine yazıla elemanı siler
# sort() listedeki sayıları küçükten büyüğe, harfleri alfabetik olarak sıralar. içine bir şey yazılmıyor
# reverse() listeyi tersine çevirir
# clear() listeyi temizler boş kalır liste

website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz(40 saat)"
# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır
# length = len(course)
# print(length)

# 2- 'website' içinden www karakterlerini alın
# print(website[7:10])

# 3- 'website' içinden com karakterlerini alın
# print(website[-3:])

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın
# print(course[15:-14])

# 5- 'course' içindeki karakterleri tersten yazdırın
# print(course[:])
# print(course[::-1])

name, surname, age, job = ("Bora", "Yılmaz", 32, "mühendis")
# verilen değişkenler ile aşağıdaki ifadeyi yazdırın
# 6- benim adım Bora Yılmaz. Yaşım 32 ve mesleğim mühendislik
# print(f"I am {name} {surname}. I am {age} years old. I am {job}. This is not ingiliççe")

# 7- "hello world" ifadesindeki 'w' ifadesini 'W' ile değiştirin
# hw = "hello world"           #bayya iyi
# print(hw[:6]+'W'+hw[7:])
# result = hw.replace("w", "W")
# print(result)

# 8- "abc" ifadesini yanyana 3 kere yazdırın
# abc="abc"
# print(abc*3)


# -------------------------ders 18---------------------------


# metodlarda parametre göndermiycek olsan bile parantez açıp kaparsın
# upper() metodu string ifadenin içindeki tüm harfleri büyük hale getirir

sentence = "merhaba ben zeynep"
# print(sentence.upper())

# lower() metodu string ifadenin içindeki tüm harfleri küyük hale getirir

sentence = " merHaBA BeN zEynEp. senin adin ne"
# print(sentence.lower())

# title() metodu string ifadedeki ilk harfleri büyük yapar

# print(sentence.title())

# capitalize() metodu string ifadedeki ilk harfi büyük yapar diğer harfler küçük olur

# print(sentence.capitalize())

# strip() metodu stringin başında ve sonunda boşluk karakteri varsa yok eder. şifrede boşluk yazdı mesela kullanıcı sıkıntı elden geçirmek lazım
# rstrip() -> sadece sağındaki boşluk karakterlerini siler
# lstrip() -> sadece sonundaki boşluk karakterlerini siler
# print(sentence.strip())

# split() metodu her kelimeyi ayırır tırnaklarla. dizi oluşturur. içinde stringdeki bir ifadeyi yazarsak parçalarken o elemanı baz alır

# print(sentence.split(' '))       
# sentence = sentence.split('.')
# print(sentence[1])

# join(buraya stringi tuttuğun değişkenin adını yaz) metodu dizi haline getirdiğin stringi birleştirir " ".join(message)

# sentence = '.'.join(sentence) # birleştirirken nokta ekle
# sentence = '*'.join(sentence) # birleştirirken araya * ekle
# print(sentence)  # normalde esas cümlede olan . yı string saydı

# find() parametrenin içine yazdığın ifade stringde varsa baş harfinin indeksini verir yoksa -1 verir

# print(sentence.find("ZEynEp")) # -1
# print(sentence.find("zeynep"))
# print(sentence.find("zEynEp")) # 13.index

# startswith("H") string ifade H ile başlıyorsa True değerini döndürür

# isFound = sentence.startswith(' ')
# print(isFound)

# endswith("n") string ifade n ile bitiyorsa True değerini döndürür

# print(sentence.endswith('e'))

# replace("Sadık","Çınar") sting ifadesinde Sadık yerine Çınar yazar ç leri c falan yaparsın işe yarar

# sentence = sentence.replace('z', 'Z')
#                    .replace('ç', 'c')
# print(sentence)

# center(100."*") 100 karakterlik bir alan ayırır ve string ifadesini ortalar. sağ ve solunda * koyar

# sentence = sentence.center(100)           # 100 karakterlik conteiner içine alır
# sentence = sentence.center(50, '*')
# print(sentence)

