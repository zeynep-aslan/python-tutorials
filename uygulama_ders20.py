# my_list = [True, 2.5, 6, "Zeynep", 'A']
# print(my_list[2])

# list1=["one", "two", "three"]
# list2=["four", "five", "six"]
# numbers=list1+list2
# print(numbers)

# message="hey there. I am using WhatsApp".split()
# print(message[5])

# user1 user2 users

# user1=["Zeynep", 19]
# user2=["Zöhre", 1]
# users=[user1, user2]
# print(users)  #liste içinde liste adamım
# print(users[1][0])


# ---------------uygulama----------------

# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz
car_list=["Bmw", "Mercedes", "Opel", "Mazda"]

# 2- Liste kaç elemanlıdır?
result=len(car_list)

# 3- Listenin ilk ve son elemanı?
result=car_list[0]+car_list[-1]

# 4- Mazda değerini Toyota ile değiştirin
car_list[-1]='Toyota'
result=car_list

# 5- Mercedes listenin bir elemanı mıdır?
result= 'Mercedes' in car_list

# 6- Listenin -2. indexindeki değer?
result=car_list[-2]

# 7- Listenin ilk 3 elemanını alın
result=car_list[0:3]

# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin
car_list[-2:]=["Toyota", "Renault"]
result=car_list

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin
result=car_list+["Audi", "Nissan"]

# 10- Listenin son elemanını silin
del car_list[-1]
result=car_list

# 11- Liste elemanlarını tersten yazdırın
result=car_list[::-1]

# 12- Aşağıdaki verileri bir liste içinde saklayın
        # StudentA: Yiğit Bilgi 2010, (70,60,70)
student_a=["Yiğit", "Bilgi", 2010, [70,60,70]]
        # StudentB: Sena Turan 1999, (80,80,70)
student_b=["Sena", "Turan", 1999, [80,80,70]]
        # StudentC: Ahmet Turan 1998, (80,70,90)
student_c=["Ahmet", "Turan", 1998, [80,70,90]]
students=[student_a, student_b, student_c]
# 13- Liste elemanlarını ekrana yazdırın
result=students[2][3][2]
result=student_c[3][1]

print(result)