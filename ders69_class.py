# class
# instance (object)

lst1 = [1,2,3]
lst2 = [1,2,3,4]

# print(type(lst1))  
# print(type(lst2))

# Class -> Person(name, surname, birthday, calculateAge())

# ----------
# ders 70-71

# boş class da pass yazmazsak hata alırız

class Person:
    # class attributes
    address = 'no information'

    # constructor(yapıcı metod) içinde tanımlanır
    # self = class dan türetilen p1 veya p2 objesi demek. self yerine this de diyebiliriz hiç farketmez
    # obje üzerine bir değer aktarmak istiyorsak self i kullanırız
    # self in üzerine eklemek istediğimiz attribute(özellik) ları parametre olarak veririz
    def __init__(self, name, year):  # oluşturulan her obje için(p1, p2 vs.) çalıştırılır
        # object attributes
        self.name = name
        self.birthYear = year
        print('init metodu calisti.')
    
    # instance methods
    def intro(self):  # oluşturulan objelere hizmet edecek olan bir metod olacağı için self parametresi ile başlıyor
        print('Hello There! I am '+ self.name)

    # instance methods
    def calculateAge(self):
        return 2020 - self.birthYear


# object (instance)
p1 = Person('zeynep', 2000)  # farklı adreslerde tanımlanmış 2 tane obje, 2 sinin de tipi Person
p2 = Person(name='rumeysa', year=1971)  # 2 tane parametre göndermemiz lazım. self sayılmıyor
# bu şekilde okunabilirliği çok daha kolay

p1.intro()
p2.intro()

print(f'adim {p1.name} ve yasim {p1.calculateAge()}')
print(f'adim {p2.name} ve yasim {p2.calculateAge()}')

# updating
p1.name = 'ali'   # sonradan değiştirme

# accessing object attributes
print(f'p1: name: {p1.name} year: {p1.birthYear} address: {p1.address}')
print(f'p2: name: {p2.name} year: {p2.birthYear} address: {p2.address}')

print(p1)   # <__main__.Person object at 0x000002C4F3374C40>
print(p2)   # farklı adreslerde tanımlanmış 2 tane obje, 2 sinin de tipi Person

print(type(p1))   # <class '__main__.Person'>
print(type(p2))   # 2 si de Person tipinde class

print(p1 == p2)  # False


# --------
# 71.video 2.yarısı

class Circle:
    # class attributes
    pi = 3.14

    # constructor
    def __init__(self, yaricap=1):   # hiçbir parametre verilmezse yarıçap 1 
        self.yaricap = yaricap

    # instance methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap

    # instance methods
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2) 

c1 = Circle()  # yaricap=1 
print(c1.cevre_hesapla())   # 6.28
print(c1.alan_hesapla())   # 3.14

c2 = Circle(5)
print(c2.cevre_hesapla())   # 31.400000000000002
print(c2.alan_hesapla())   # 78.5

