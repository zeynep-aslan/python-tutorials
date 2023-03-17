# x,y,z,t=5,5,10,4
# result = (x==y) # True


# password='1234'
# username='zynpasln'
# result= ('342234' == password)  # False

# result = False + True + 40


# print(result)

# -----------uygulama-----------

# 1- girilen 2 sayıdan hangisi büyüktür?
# num1 = int(input("bir sayi giriniz: "))
# num2 = int(input("bir sayi giriniz: "))
# if num1 > num2:
#     print("1.sayi 2.sayidan buyuktur")
# else:
#     print("2.sayi 1.sayidan buyuktur")

# 2- kullanıcıdan 2 vize(%60) ve final(%40) notunu alıp ort hesapla
#    eğer 50 üstüyse geçti altıysa kaldı yazdır
# vize1 = int(input("1.vize notunu giriniz: "))
# vize2 = int(input("2.vize notunu giriniz: "))
# final = int(input("final notunu giriniz: "))
# ort = ((vize1+vize2)/2*60+(final*40))/100
# if ort < 50:
#     print(f"ortalamaniz: {ort} Kaldiniz")
# else:
#     print(f"ortalamaniz: {ort} Gectiniz")  

# 3- girilen bir sayının tek mi çift mi olduğunu hesaplayın
# num = int(input("bir sayi giriniz: "))
# if num%2==0:
#     print(f"{num} sayisi cifttir.")
# else:
#     print(f"{num} sayisi tektir.")

# 4- girilen bir sayının negatif mi pozitif mi olduğunu hesaplayın
# num = int(input("bir sayi giriniz: "))
# if num<0:
#     print(f"{num} sayisi negatiftir.")
# if num>0:
#     print(f"{num} sayisi pozitiftir.")    
# if num==0:
#     print(f"{num} sayisi notrdur.")    

# 5- parola ve email bilgisini isteyip doğruluğunu kontrol edin
#    (email: email@zeynepaslan.com parola: abc123)

emaill = 'email@zeynepaslan.com'
parolaa = 'abc123'

parola = input("password: ")
email = input("email: ")

# boşluk karakterini sildik başta ve sondaki
isMail = (emaill == email.lower().strip())
isPassword = (parolaa == parola)

print(f'girdiginiz parola {isPassword} ve email adresi {isMail}')
