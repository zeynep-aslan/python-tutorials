# class Person():
#     def __init__(self):
#         print('Person Created')

# class Student(Person):
#     pass

# class Student(Person):
#     def __init__(self):
#         print('Student Created')


# Miras aldığı metodu da çağırması için
# class Student(Person):
#     def __init__(self):
#         Person.__init__(self)
#         print('Student Created')

# p1 = Person()
# s1 = Student()   # Person Created

# s1 = Student()   # Student Created

# s1 = Student()
# Person Created
# Student Created

# ------------

class Person():
    def __init__(self, fName, lName):
        self.firstName = fName
        self.lastName = lName
        print('Person Created')
    def who_am_i(self):
        print('i am a person')    
    def eat(self):
        print('i am a eating')    

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)  # person ın özelliklerini aldık
        self.studentNumber = number
        print('Student Created')

    # override -> aynı isimde bir metod, temel sınıftaki metodu ezer
    def who_am_i(self):
        print('i am a student')  
    def sayHello(self):
        print('Heloooooo')      
    
class Teacher(Person):
    def __init__(self, fName, lName, branch):
        super().__init__(fName, lName)
        self.branch = branch
    def who_am_i(self):
        print(f'i am a {self.branch} teacher')

p1 = Person('Zeynep', 'Aslan')
s1 = Student('Ali', 'Aydin', 1223423)
t1 = Teacher('Serkan', 'Kaya', 'Math')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()  # override lı fonksiyon yazılmadan önce
p1.eat()
s1.eat()
s1.sayHello()
# i am a person
# i am a person
# i am a eating
# i am a eating
t1.who_am_i()




