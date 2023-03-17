class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi olusturuldu')

    def __str__(self):   # print veya str fonksiyonları çağrıldığında otmatik çalışır
        return f'{self.title} by {self.director} '

    def __len__(self):
        return self.duration  

    def __del__(self):
        print('film objesini sileceğimizi haber ediyoruz')      

m = Movie('filmin adi', 'filmin yönetmeni', 120)        

myList = [1,2,3]

# print(m)   # ram deki yerini yazdırır
# print(myList)  # listeyi normal yazdırır

# print(str(m))
# print(str(myList))
# gene aynı sonuç
# demek ki bir bir objeyi printle yazdırdığımızda veya str metoduyla yazdırdığımızda 
# arka tarafta çalışan metodumuz __str__

# fonksiyonu yazdıktan sonra
# print(m)

# print(len(m))  # len motodu bu obje için tanımlanmamış 
# class ın içine __len__ ekledikten sonra filmin süresini yazdırır

del m
print(m)  # bulamadı çünkü sildik
# biz objeyi del le silmesek bile bellekten bir süre sonra otomatik olarak silinir 
# ve silindikten sonra zaten mesajı gösterir

# python special methods list