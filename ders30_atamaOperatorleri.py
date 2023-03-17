# x, y, z = 5, 10, 20
# x yerine y, y yerine x değerini getirir
# x, y = y, x
# x += 2
# print(x,y,z)

# values = 1,2,3
# print(values)
# print(type(values))
# x, y, z = values # values da 2 değer olsaydı hata alırdık, fazla eleman olsa da hata alırsın
# print(x, y, z)

# degerler = 1,2,3,4,5,6
# a, b, *c = degerler    # fazladan kalan tüm değerleri c ye dizi olarak atar 
# print(a, b, c)
# print(a, b, c[2])


# --------------------uygulama-------------------

x, y, z = 2, 5, 107
numbers = 1, 5, 7, 10, 6

# 1- kullanıcıdan aldığınız 2 sayının çarpımı ile x, y, z toplamının farkı nedir?
# num1 = int(input("bir sayi giriniz: "))
# num2 = int(input("bir sayi giriniz: "))
# multiply = num1*num2
# fark = multiply-(x+y+z)
# print(fark)

# 2- y'nin x'e kalansız bölümü?
# bolum = y//x
# print(bolum)

# 3- (x,y,z) toplamının mod 3 ü?
# toplam = x+y+z
# print(toplam%3)

# 4- y nin x. kuvveti?
# print(y**x)

# 5- x, *y, z = numbers işlemine göre x'nin küpü kaçtır?
x, *y, z = numbers
# print(x**3)

# 5- x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?
top = y[0]+y[1]+y[2]
print(top)


