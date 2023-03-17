# uygulama1------------------

"""
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri
    ile bulmaya çalışın. (hak = 5)
    * random modülü kullan
    ** her soru 20 puan. 100 üzerinden puanlama yapmaya çalışın
    *** hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın
"""
import random

while True:
    sayi = random.randint(1,10)
    can = int(input('kaç hakkınızın olmasını istersiniz: '))
    hak = can
    sayac = 0
    while 0 < hak:
        tahmin = int(input("bir sayi tahmin ediniz: "))
        hak -= 1
        if sayi == tahmin:
            print(f'Tebrikler bildiniz! {sayac+1}. defada bildiniz. Toplam puanınız: {100-(100/can)*sayac}')
            break
        elif sayi > tahmin:
            sayac +=1
            print('yukarı')
        elif sayi < tahmin:
            sayac +=1
            print('aşağı')    
        if hak == 0:
            print(f'hakkınız bitti. tutulan sayi: {sayi}')    
            
# uygulama2--------------------

"""
    girilen bir sayının asal sayı olup olmadığını bulunuz
    asal sayı: 1 ve kendisi hariç başka böleni olmayan sayı
"""
# while True:
#     sayi = int(input('bir sayi giriniz: '))
#     if sayi == 1:
#         print('girdiğiniz sayı asal değildir.')
#         sorgu = int(input('başka sayı sorgulamak ister misiniz?\n1-EVET\n2-HAYIR\n'))        
#     i = 2
#     while i < sayi:
#         if sayi%i==0:
#             print('girdiğiniz sayı asal değildir.')
#             break
#         else:
#             i += 1
#             if i == sayi:
#                 print('girdiğiniz sayı asaldır')
#     sorgu = int(input('başka sayı sorgulamak ister misiniz?\n1-EVET\n2-HAYIR\n'))    
#     if sorgu == 1:
#         True
#     elif sorgu == 2:
#         False        
    
sayi = int(input('bir sayi giriniz: '))  
asalmi = True  

if sayi == 1:
    asalmi = False 
    
for i in range(2, sayi):
    if (sayi % i == 0):    
        asalmi = False   
        break    

if asalmi:
    print('sayı asaldır')
else:
    print('sayı asal değildir')      


""" 
sayi = int(input('bir sayi giriniz: '))    
if sayi == 1:
    print('girdiğiniz sayı asal değildir.')        
for i in range(2, sayi):
    if (sayi % i == 0):    
        print('girdiğiniz sayı asal değildir.')        
        break    
    else:
        if (i + 1 == sayi):    
            print('girdiğiniz sayı asaldır')   
""" 