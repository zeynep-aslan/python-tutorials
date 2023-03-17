fruits = {'orange', 'apple', 'banana', 'orange' }
# print(fruits)
# print(fruits[0])  # indexlenemez

# elemanlara döngü kullanarak ulaşabiliriz
# karışık bir şekilde
# ama sıralama yapamazsın alfabetik vs
# for i in fruits:
#     print(i)

# ekleme yapma
# fruits.add('cherry')
# print(fruits)

# update() metoduna liste göndererek ekleme
# listede zaten olan bir elemanı bir daha eklemez
# fruits.update(['grape', 'mango', 'apple'])
# print(fruits)

# set() ile tekrarlayan elemanları çıkarma
# myList = [1,2,3,4,2,4,7]
# print(myList)
# print(set(myList))

# print(set(fruits))

# eleman silme şeyleri
# fruits.remove('banana')
# fruits.discard('apple')
# fruits.pop()  # kafasına göre siliyor
# fruits.clear()  # ne var ne yok siler

# print(fruits)

# setler union() metodu ile rastgele birleştirilir
# set1 = {1,2,3}
# set2={'a','b','c'}

# set3 = set1.union(set2)
# print(set3)

# update() metodu ile bir set'i diğer set içerisine eklemiş oluyoruz yeni bir set objesi oluşturulmaz.
# set1.update(set2)
# print(set1)

# ----------ders28 value & referans veri tipleri----------

# value types => int, string
# farklı alanlarda tanımlanan değerler oldukları için y de yapılan değişiklik x i etkilemedi
# verinin kendisiyle ilgileniriz
x = 5
y = 25

x = y
y = 10
print(x,y)  # 25,10

# reference types => list, class
# listeleri 1-1ine eşitledikten sonra değerlerin tutulduğu adres aynı oluyor
# 500 tane eşitleme işlemlerinde sürekli 500 tane yeni bir adres oluşmaz. adres kopyalanır, o adrese gider
# verinin adresiyle ilgileniriz
a=["apple", "banana"]
b=["apple", "banana"]

a=b

b[0]="grape"

# print(a,b)



