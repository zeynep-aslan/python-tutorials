# sıfıra bölme hatası olduğunda except bloğu çalışır
# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except ZeroDivisionError:
#     print('y sifir olamaz')
# except ValueError:
#     print('x ve y sayisal bir deger olmalidir')
# except:
#     print('bilinmeyen bir hata olustu')  # çalışma zamanında oluşan hatalar için


# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError, ValueError) as e:  # paranteze almazsan syntax error
#     print('hata olustu')    # hataları ortak kümede genelleyebiliriz
#     print(e)  # hata mesajını sadece bizim görebileceğimiz şekilde gösterir


# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except Exception as e:
#     print('bilinmeyen bir hata olustu.')
#     print(e)  # hata ne olursa olsun hatanın sebebini sadece bizim görebileceğimiz şekilde gösterir
# else:
#     print('her sey yolunda')  # except bloğu çalışmazsa burası çalışır


# bu daha mantıklı
# döngü hata vermeyene kadar değer almaya devam eder
# while True:
#     try:
#         x = int(input('x: '))
#         y = int(input('y: '))
#         print(x/y)
#     except Exception as e:
#         print('bilinmeyen bir hata olustu.')
#         print(e)  # hata ne olursa olsun hatanın sebebini sadece bizim görebileceğimiz şekilde gösterir
#     else:
#         break
#     finally:  # döngü her çalıştığında finally bloğu çalışır
#         print(print('finally blogu calisti'))  # kullandığın kaynakları kapatma işlemlerini burada yapabilirsin  


# uygulama-------------

liste = ["1","2","5a","10b","abc","10","50"]

# 1: Liste elemanları içerisindeki sayısal değerleri bulunuz.
try:
    for num in liste:
        int(num)



# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın

# 3: Dictionary ve key bilgilerini parametre olan get(d, key)
# fonksiyonu hazırlayın

# d = {"urunAdi":"samsung s10"}

# d["price"] => KeyError

# get(d, "price") => None

# get(d, "urunAdi") => samsung s10







