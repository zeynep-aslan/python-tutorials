x=0
while x<10:
    if x%2==1:
        print(x)
    x +=1

# mecburen isim girdirtme kodu
name = '' # boş olduğu için False
while not name: # False tersi yani True döner
    name = input('isiminiz giriniz: ')
print(f'merhaba {name}') # değer girmek istemeyip enter a tıklarsan sen değer girene kadar aynı soruyu sorar
# ama boşluk tuşuna bastığında da true döndürür ' ' olur merhaba boşluk

# boşluk önleme kodu
while not name.strip():
    name = input('isiminiz giriniz: ')
print(f'merhaba {name}')


# uygulama-------------------

sayilar = [1,3,5,7,9,12,19,21]
# 1- listeyi while ile ekrana yazdır
temp = 0
while temp < len(sayilar):
    print(sayilar[temp])
    temp +=1

# 2- başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
ilk = int(input('baslangic değerini giriniz: '))
bitis = int(input('bitis değerini giriniz: '))
while ilk < bitis-1:
    ilk +=1
    print(ilk)
    
# 3- 1-100 arasındaki sayıları azalan bir şekilde ekrana yazdırın
temp = 0
while temp < 99:
    if temp == 98:
        break
    else:
        print(99-temp)
    temp += 1
    
# 4- kullanıcıdan alacağınız 5 sayıyı ekrana sıralı bir şekilde yazdırın
liste = []
while len(liste)<5:
    sayi = int(input('bir sayi giriniz: '))
    liste.append(sayi)
liste.sort()     # değer döndürüyor  
print(liste)

# 5- kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız
#  * ürün sayısını kullanıcıya sorun
#  ** dictionary listesi yapısı(name, price) şeklinde olsun
#  *** ürün ekleme işlemi bittiğinde ürünleri ekrana while ile listeleyin

number = int(input('ürün sayisi giriniz: '))
urunler = []
temp = 0
while temp < number:
    name = input('urun adini giriniz: ')
    price = input('ürünün fiyatini giriniz: ')
    urunler.append({
        'name':name,
        'price':price
    })
    temp += 1

for urun in urunler:
    print(f'urun adi: {urun["name"]} urun fiyati: {urun["price"]} ')
   
