# boş diziye 0-9 sayıları ekleyip yazdırdı
numbers = []
for x in range(10):
    numbers.append(x)
print(numbers)

# 0-9 listeye atıyor ve yazdırıyor
numbers = [x for x in range(10)]
print(numbers)

# her değerin karesi alındı
numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x**2 for x in range(10) if x % 3 == 0]
print(numbers)     # [0, 9, 36, 81]

# string in harflerini diziye atadı
myString = 'hello'
myList = []
for letters in myString:
    myList.append(letters)
print(myList)       # ['h', 'e', 'l', 'l', 'o']

# string in harflerini diziye atadı (daha kısa)
myList = [letters for letters in myString]
print(myList)       # ['h', 'e', 'l', 'l', 'o']

# yaşları yazdırma
years = [2010,1999,1986,2000]
ages = [2019-age for age in years]
print(ages)          # [9, 20, 33, 19]

# very cool
# x çiftse listeye ekle tekse tek yazdır
results = [x if x % 2 == 0 else 'TEK' for x in range(10)]
print(results)         # [0, 'TEK', 2, 'TEK', 4, 'TEK', 6, 'TEK', 8, 'TEK']

result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))  # çift parantez çünkü bunlar çiftler
print(result)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)] 

# kısa yolu
numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)] 


#indentation=girinti hatası


