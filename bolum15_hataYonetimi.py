# error

# error handling

# bazen kullanıcıya açmadan önce hata almayız, açtıktan sonra hata alırız


# x = int(input('x: '))
# y = int(input('y: '))

# print(x+y)
# x: 12
# y: 23a
# ValueError: değer hatası
# invalid literal for int(): int() fonksiyonu gönderdiğimiz 23a değerini çeviremiyor
# kullanıcının bu hataları görmesini istemeyiz

try:    # hata gelebilecek kısım
    x = int(input('x: '))
    y = int(input('y: '))
    print(x+y)
except:    # try daki kod hatalıysa burası çalışır
    print('lutfen sayi girin.')

# mesela bi web uyg yapıyorsun. istenilen şey yoksa aradığınız kaynak bulunamadı diye bi mesaj çıksın istiyorsun  
# yada server la alakalı bi hata oldu. bilinmeyen bir kaynak oldu, tekrar deneyiniz diye bi mesaj çıkar

# ------- hata türleri (exception types) --------
# her hatada kullanıcıya aynı mesajı göndermek yerine 0 girmeyin yada sadece sayı girin gibi mesajlar yayınlamak için

# x = int(input('x: '))
# y = int(input('y: '))

# print(x/y)

# SyntaxError -> yazım yanlışı -> birden fazla ;; gibi

# NameError -> tanımlanmamış bir değişken kullanımı
# print(ad)  # NameError: name 'ad' is not defined

# TypeError -> yanlış parametre gönderme vs.
# len(5)  # TypeError: object of type 'int' has no len()
# 4 + 'a'  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# IndexError -> yanlış index kullanımı
# liste = ['merhaba']  # listede 1 eleman var, 0.index var sadece
# liste[1]  # IndexError: list index out of range

# ValueError -> hatalı tip kullanımı
# int('10a')  # ValueError: invalid literal for int() with base 10: '10a'

# KeyError -> key hatası
# d = {}
# d['ad']  # KeyError: 'ad' , olmayan bir key e ulaşmak istediğinde

# AttributeError -> olmayan bir özelliğe ulaşmak istediğimizde
# "merhaba".upper()  # çalıştı
# "merhaba".Upper()  # AttributeError: 'str' object has no attribute 'Upper'


# python builtin exceptions diyerek arat hata türlerini görmek için




