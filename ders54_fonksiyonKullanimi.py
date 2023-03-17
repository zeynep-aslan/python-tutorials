# parametre göndermediysen user ismini parametre kabul eder
def sayHello(name = 'user'):
    print('HELLO '+ name )

sayHello('Zeynep')    
sayHello('Veli')
sayHello()
#------------

def sayHello(name = 'user'):
    return 'Hello ' + name

message = sayHello('Rumeysa')
print(message)
#------------

def total(num1, num2):
    return num1 + num2

result = total(2, 3)
result = total(15, 10)
print(result)
#------------

def yasHesapla(dogumYili):
    return 2020 - dogumYili

# ageZey = yasHesapla(2000)
# ageDad = yasHesapla(1969)
# ageMom = yasHesapla(1971)
# print(ageZey, ageDad, ageMom)

def emekliliginizeKacYilKaldi(dogumYili, isim):
    """ 
        DOCSTRING = emekliliginize kac yil kaldigini gosteren fonksiyon
        INPUT = dogum yili
        OUTPUT = hesaplanan yil bilgisi
    """
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f'{isim} emekliliğinize {emeklilik} yıl kaldı.')
    else:
        print(f'{isim} emeklilik yaşınızı doldurdunuz')    

emekliliginizeKacYilKaldi(1969, 'Muhammet') 
help(emekliliginizeKacYilKaldi)
""" 
    DOCSTRING = emekliliginize kac yil kaldigini gosteren fonksiyon
    INPUT = dogum yili
    OUTPUT = hesaplanan yil bilgisi   
"""
#------------

liste = [1,2,3]
print(help(liste.append))  # fonksiyonun nasıl kullanıldığını açıklıyor
""" 
Help on built-in function append:     

append(object, /) method of builtins.list instance
    Append object to the end of the list.

listenin sonuna obje eklemek için kullanılan bir metod olduğunu söylüyor    
"""