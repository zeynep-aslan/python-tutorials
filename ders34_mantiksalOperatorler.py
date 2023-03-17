x = 5
# result = 5 < x < 10    # False

hak = 5
devam = 'e'

# # and

# result = (x > 5) and (x < 10)  
# sonuc = (hak > 0) and (devam == 'e')

# # or

# result = (x > 5) or (x < 10)

# # not -> tam tersini yapar false ise true, true ise false olur

# result = not (x > 0)

# # x, 5 ile 10 arasında olan bir çift sayi mi?

# result = ((x<10)or(x>5))and(x%2==0)



# print(result)
# # print(sonuc)


# ------------------------uygulama---------------------

# 1- girilen sayı 0-100 arasına mı?
# num = float(input("bir sayi giriniz: "))
# result = (num > 0) and (num < 100)

# 2- girilen sayı pozitif çift sayı mı?
# result = (num > 0)and(num%2==0)

# 3- email ve parola bilgileri ile giriş kontrolü yapınız
# email = 'slmnbrcnm13@hotmail.com'
# password = 'abc123'
# mail= input('mailinizi giriniz: ')
# parola= input('parolanizi giriniz: ')

# if (email!=mail) or (password!=parola):
#     print("mailiniz veya parolaniz yanlis")
# else:
#     print('girdiginiz bilgiler dogru')


# 4- girilen 3 sayıyı büyüklük olarak karşılaştır
num1 = int(input("a: "))
num2 = int(input("b: "))
num3 = int(input("c: "))
# num = [num1, num2, num3]
# result = num.sort(reverse=True) # küçükten büyüğe sıralayıp ters çevirir
result = (num1>num2) and (num1>num3)
print(f'a en buyuk sayidir: {result}')
result = (num2>num1) and (num2>num3)
print(f'b en buyuk sayidir: {result}')
result = (num3>num2) and (num3>num1)
print(f'c en buyuk sayidir: {result}')

# 5- kullanıcıdan 2 vize (%60) 1 final(%40) notunu alıp ortalama hesapla
#    eğer ort 50 üstüyse geçti yazsın değilse kaldı
# a) ort 50 olsa bile final notu en az 50 olmalıdır
# b) finalden 70 aldığında ortalamanın önemi kalmasın

# vize1 = int(input("1.vize notunu giriniz: "))
# vize2 = int(input("2.vize notunu giriniz: "))
# final = int(input("final notunu giriniz: "))

# ort = ((vize1+vize2)/2*60+(final*40))/100

# if final >= 70:
#     print("gectiniz!")
# elif (ort >= 50) and (final >= 50):
#     print("gectiniz")
# else:
#     print("kaldiniz")    

# 6- kişiden ad, kilo ve boy bilgilerini alıp kilo indexini hesaplayın
#    Formül: (kilo/boyunun karesi)
#    tabloya göre hangi gruba girdiğini söyle
#    0-18.4 =>    Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla kilolu
#    30.0-34.9 => Şişman(obez)

# isim = input("isminizi giriniz: ")
# kilo = int(input("kilonuzu giriniz: "))
# boy = float(input("boyunuzu giriniz(metre cinsinden): "))

# result = kilo / (boy**2)

# if (result>0) and (result<19) :
#     print(f"{isim} vücut kitle indexiniz {result}. Zayifsiniz.")
# elif (result>=19) and (result<25) :
#     print(f"{isim} vücut kitle indexiniz {result}. Normal olculerdesiniz.")
# elif (result>=25) and (result<30) :
#     print(f"{isim} vücut kitle indexiniz {result}. Fazla kilolusunuz.")
# else:
#     print(f"{isim} vücut kitle indexiniz {result}. Sismansiniz.")    

# print(result)