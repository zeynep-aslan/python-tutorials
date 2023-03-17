# key : value

sehirler=["kocaeli", "istanbul"]
plakalar=[41, 34]

print(plakalar[sehirler.index("kocaeli")])   # ismi kocaeli olan şehrin indexindeki plakayı yazdır

# onun yerine bu daha kullanışlı

plakalarr = { "kocaeli" : 41, "istanbul" : 34 }
print(plakalarr["istanbul"])
print(plakalarr["kocaeli"])

# ankara'yı plakaların üstüne ekledi, olan bir elemanı bu şekilde değiştirebilirsin de
plakalarr["ankara"] = 6
print(plakalarr["ankara"])

print(plakalarr)


users = {
    "zeynepaslan": {
        "age":19,
        "roles":["user"],
        "email":"zeynep@gmail.com",
        "address":"sakarya",
        "phone":7249872943
    },

    "hulyaaslan": {
        "age":49,
        "roles":["user", "mom"],
        "email":"hulya@gmail.com",
        "address":"istanbul",
        "phone":1249872943
    }
}

print(users["hulyaaslan"])
print(users["zeynepaslan"]["age"])
print(users["zeynepaslan"]["email"])
print(users["hulyaaslan"]["roles"][1])

animals = {
    "foot4" : {
        "a1" : "cat",
        "a2" : "dog",
        "a3" : "horse"
    },

    "foot2" : {
        "a1" : "chicken",
        "a2" : "duck",
        "a3" : "bird"
    }
}

print(animals["foot2"]["a2"])

# --------------------uygulama---------------------

# 1- kullanıcıdan bilgi alarak yeni öğrenci oluştur
# 2- numarası girilen öğrencinin bilgilerini getir

students = {}
number=input("ogrenci numarasi: ")
name=input("ogrenci adi: ")
surname=input("ogrenci soyadi: ")
phone=input("ogrenci telefon numarasi: ")

# students[number] = {
#     "isim": name,
#     "soyisim":surname,
#     "telefon":phone
# }

# bu daha pratik, update() metodu ile
students.update({
    number: {
        "isim": name,
        "soyisim":surname,
        "telefon":phone
    }
})

number=input("ogrenci numarasi: ")
name=input("ogrenci adi: ")
surname=input("ogrenci soyadi: ")
phone=input("ogrenci telefon numarasi: ")

students.update({
    number: {
        "isim": name,
        "soyisim":surname,
        "telefon":phone
    }
})

number=input("ogrenci numarasi: ")
name=input("ogrenci adi: ")
surname=input("ogrenci soyadi: ")
phone=input("ogrenci telefon numarasi: ")

students.update({
    number: {
        "isim": name,
        "soyisim":surname,
        "telefon":phone
    }
})

print(students)

print("*"*50)
num=input("bilgilerinin getirilmesini istediğiniz kullacının numarasını girin: ")

if num==number:
    print(students[num])
else:
    print("veritabanimizda boyle bir ogrenci bulunmamaktadir")    

ogrenci = students[num]
print(f'aradiginiz {num} nolu ogrencinin adi {ogrenci["isim"]} soyadi {ogrenci["soyisim"]} ve telefonu {ogrenci["telefon"]} dir')


# -----------sadık turan web sitesi---------------

# zeynepaslan ve hulyaaslan ın altındakiler obje
users = {
    "zeynepaslan": {
        "age":19,
        "roles":["user"],
        "email":"zeynep@gmail.com",
        "address":"sakarya",
        "phone":7249872943
    },

    "hulyaaslan": {
        "age":49,
        "roles":["user", "mom"],
        "email":"hulya@gmail.com",
        "address":"istanbul",
        "phone":1249872943
    }
}

for i in users:           # sadece key leri getirir
    print(i)

for i in users:           # key ve value ları getirir
    print(users[i])

for i in users.values():  # key ve value ları getirir
    print(i)    

for a,b in users.items(): # key ve value ları getirir
    print(a,b) 

users["zeynepaslan"].pop("address") # silme şeysi
users.pop()
for i in users.values():  # key ve value ları getirir
    print(i)      

del users["zeynepaslan"]
print(users)

users.clear()
print(users)  # {} verir

users.popitem() # son elemanı siler users in
print(users)

