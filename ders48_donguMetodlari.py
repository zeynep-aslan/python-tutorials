# range-----------------------
# 0.indexi 0 son indexi içindeki sayı ama içindeki sayı dahil değil
for item in range(10):
    print(item)

# 2 den başlar 10 a kadar (10 dahil değil)
for item in range(2,10):
    print(item)

# 3 er 3 er ritmiq
for item in range(2,10,3):
    print(item)

print(list(range(10,90,10)))    # [10, 20, 30, 40, 50, 60, 70, 80]  


# enumerate-----------------------
index = 0
greeting = 'hello'
for letter in greeting:
    print(f'index: {index} letter: {letter}')
    index += 1

for item in enumerate(greeting):
    print(item)
    
# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')    

for index,letter in enumerate(greeting):
    print(f'index: {index} letter: {letter}')
# index: 0 letter: h
# index: 1 letter: e
# index: 2 letter: l
# index: 3 letter: l
# index: 4 letter: o


# zip-----------------------
list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [100,200,300,400,500]
# dictionary yle de birleştirebiliriz
# isim listesi ve telefon listesi olabilir her kişinin telefonuyla eşleştirir

print(list(zip(list1, list2)))    # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

# 3 taneyi de birleştirir, her bir tanesi bir tuple'a karşılık geliyor
print(list(zip(list1, list2, list3)))  # [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300), (4, 'd', 400), (5, 'e', 500)]

for item in zip(list1, list2, list3):
    print(item)
# (1, 'a', 100)
# (2, 'b', 200)
# (3, 'c', 300)
# (4, 'd', 400)
# (5, 'e', 500)

for a,b,c in zip(list1, list2, list3):
    print(a)

for a,b,c in zip(list1, list2, list3):
    print(a,b,c)
