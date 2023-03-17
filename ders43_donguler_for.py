numbers = [1, 2, 3, 4, 5]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

for num in numbers:   # listenin içerisinden tek tek elemanları al num değişkeninin içerisine at, her for döngüsü döndüğünde dönen num içeriğini ekrana yazdır
    print(num)

for num in numbers:  # listedeki eleman sayısı kadar hello yazar(for döngüsü listenin eleman sayısı kadar döner)
    print('hello')    

names = ['zeynep', 'sena', 'ali']
for name in names:
    print(f'my name is {name}')

name = 'Zeynep' # string ifadenin her elemanını bir dizi elemanı şeklinde değerlendirilir
for n in name:  # string ifadenin harflerini tek tek yazdırır
    print(n)

tupleeee = [(1, 2), (3, 4), (5, 6), (7, 8)]
for a,b in tupleeee: # 1 3 5 7
    print(a)

for a,b in tupleeee: 
    print(a,b)    
# 1 2
# 3 4
# 5 6
# 7 8

# dictionary listesi key - value
d = {'k1':1, 'k2':2, 'k3':3, 'k4':4}

# sadece key bilgilerini verir
for item in d:   
    print(item)

# # eleman gruplarına ulaşmak istiyorsak
for item in d.items():
    print(item)
# ('k1', 1)    
# ('k2', 2)    
# ('k3', 3)    

for key,value in d.items():
    print(value)
# bu 2 si aynı anlama geliyor
for a,b in d.items():
    print(b)    
# k1 1  
# k2 2    
# k3 3    


# uygulama---------------------------

sayilar = [1,3,5,7,9,12,19,21]

# 1- listedeki hangi sayılar 3 ün katıdır
for sayi in sayilar:
    if sayi%3==0:
        print(sayi)

# 2- listedeki sayıların toplamı
temp = 0
for sayi in sayilar:
    temp+=sayi
print(temp)

# 3- listedeki tek sayıların karesini alınız
for sayi in sayilar:
    if sayi%2==1:
        print(sayi**2)

sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

# 4- sehirlerden hangileri en fazla 5 karakterlidir
for i in sehirler:
    if (len(i)<=5):
        print(i)

urunler = [
    {'name':'samsung s6', 'price':'3000' },
    {'name':'samsung s7', 'price':'4000' },
    {'name':'samsung s8', 'price':'5000' },
    {'name':'samsung s9', 'price':'6000' },
    {'name':'samsung s10', 'price':'7000' }
]

# 5- ürünlerin fiyatları toplamı nedir
toplam = 0
for urun in urunler:
    toplam += int(urun['price'])
print(toplam)

# 6- ürünlerin fiyatı en fazla 5000 olan ürünleri gösteriniz
for urun in urunler:
    if (int(urun['price'])<=5000):
        print(urun['name'])
