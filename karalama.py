# ctrl + Enter = 1 satır boşluk bırakır
# Alt + Shift + A = toplu yorum satırı

# liste = ['selam', 'ben', 'zeynep']
# ifade = 'selam ben zeynep'
# ifade.upper() # döndürüyor
# print(ifade)

# liste = [1,2,42,0]
# print(sorted(liste)) # sorted() döndürmüyor

def square(num): return num ** 2
number = [1,23,4,56,7,89]
for item in map(square, number):
    print(item)