"""
    daire alanı = PI*r*r
    daire çevresi = 2*PI*r
    r = 3.14

    yarıçapı verilen bir dairenin alan ve çevresini hesapla
"""

""" PI = 3.14
r = float(input("yaricapi giriniz: "))
alan = PI*(r**2)
cevre = 2*PI*r
print("alan: ",alan)
print("cevre ", cevre)
print("alan: "+ str(alan) + " cevre "+ str(cevre)) """

#----------

name="zeynep"
surname=" aslan"
age=19
greeting = ("my name is {}{}. \nI am {} years old".format(name, surname, age))
length=len(greeting)
print(greeting[-1])
# print(length)  # kapladığı birim sayısı
# print(greeting[length-1])  # index
print(greeting[2:])
# print(greeting[2:5])  # son index dahil değil
# print(greeting[3:7])
# print(greeting[:17])
print(greeting[3:17:2]) #2 karakterde bir alır

sentence = ("my name is {n}{s}. \nI am {a} years old".format(n=name, s=surname, a=age))
# print(sentence)

result = 200 / 700
print(result)
print("the result is {r:1.3}".format(r=result))
print("the result is {r:10.3}".format(r=result)) # 6 karakterlik boşluk bırakır

# print(f"my name is {name}{surname}. \nI am {age} years old")