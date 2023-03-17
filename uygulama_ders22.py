# listeler değiştirilemez, sadece kopyaları oluşturulur
numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val=min(numbers)
val = max(numbers)
val=min(letters)
val=max(letters)

# print(val)
# val = numbers[3:6]
# print(val)

# numbers[4] = 40

# numbers.append(49)
# numbers.append(59)
# numbers.insert(3, 78)
# numbers.insert(-1, 52)  # -1. indisten önce elemanı ekler yani -2.indise
# numbers.pop()           # en sondaki elemanı siler
# numbers.remove(49)
# numbers.sort()        # küçükten büyüğe sıralar
# numbers.reverse()    # listeyi tersine çevirir
# letters.sort()
# letters.reverse()

# print(numbers.count(10)) # 10 dan kaç tane var yada s harfinden kaç tane var?
# print(letters.count('s'))

# numbers.clear() 

# print(letters)
# print(numbers)

# list method in python

# -----------uygulama-------------

names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz
# names.append("Cenk")
# var = names

# 2- "Sena" değerini listenin başına ekleyiniz
# names.insert(0, "Sena")
# var=names

# 3- "Deniz" ismini listeden siliniz
# names.remove("Deniz")
# var=names

# 4- "Deniz" isminin indisi nedir
# var = names.index("Deniz")

# 5- "Ali" listenin bir elemanı mıdır
# var = "Ali" in names

# 6- Liste elemanlarını ters çevirin
# var = names.reverse()

# 7- Liste elemanlarını alfabetik sıralayın
# names.sort()
# var=names

# 8- years listesini rakamsal büyüklüğe göre sıralayın
# years.sort()
# var=years

# 9- str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz
# str = "Chevrolet, Dacia"
# var=str.split(',')

# 10- years dizisinin en büyük ve en küçük elemanı nedir
# mini=min(years)
# print(mini)
# var=max(years)

# 11- years dizisinde kaç tane 1998 değeri vardır
# var=years.count(1998)

# 12- years dizisinin tüm elemanlarını silin
# var = years.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız
# markalar=[]
# marka = input("marka: ")
# markalar.append(marka)

# marka = input("marka: ")
# markalar.append(marka)

# marka = input("marka: ")
# markalar.append(marka)

# print(markalar)


# print(var)

# -------------tuple----------------

liste=[1,2,3]
tuplee=(1,2,3)
tupleeee=1,2,3    # bu da bir tuple listesi ama okunabilirlik açısından parantez kullan
# print(type(liste))
# print(type(tuplee))

# liste[0]=0
# print(liste)

# tuplee[0]=0      # tuple de atadıktan sonra eleman değişikliği yapamıyorsun ama liste elemanı atabilirsin
# print(tuplee)

a=list(tuplee)     # Tuple liste elemanları değiştirilemez ancak başka bir liste türüne çevrilerek güncelleme yapılabilir.
a[0]="armut"      # list() metodu ile list objesine çevirip güncellemeyi yapıyoruz
tuplee=tuple(a)    # güncellenmiş listeyi tekrar tuple() metodu ile tuple objesine çeviriyoruz.
# print(tuplee)

message=("hey", "there", "I", "am", "using", "whatsapp")
# print(message[:2])

# döngüyle yazdırma
# names=("Ali", "Veli", "Zeynep", "Nazlı")
# for name in names:
#     print(name)

# 2 tane tumple metodu vardır count(), index()

# count(eleman) -> seçili elemandan kaç tane var
numbers=(10,2,5,2,12,7,34)
letters=('a', 'b', 'c', 'a')
# print(numbers.count(10))
# print(letters.count('a'))

# index(eleman) -> seçili eleman kaçıncı indexte
# print(letters.index('b'))