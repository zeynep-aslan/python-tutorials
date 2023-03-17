#  iterable, içerisinde gezilebilir
# iterator

# sayilar = [1,2,3,4,5]  #  iterable object
# isim = "Sadik"  #  iterable object
# a = 10    #  not iterable object

# for i in sayilar:  # sayilar yerine a yazamayiz, iterable degil cunku
#     print(i)

# # metodlarini dondurur
# print(dir(sayilar))  #  '__iter__' de bulunur

#  __iter__ metodunu cagirir
# iterator = iter(sayilar)  #  <list_iterator object at 0x000002617FA56100>
# print(iterator)
# print(next(iterator))  #  1
# print(next(iterator))  #  2
# print(next(iterator))  #  3
# print(next(iterator))  #  4
# print(next(iterator))  #  5
# print(next(iterator))  #  hata verir, next metodu nerede duracagini bilemez

# while True:
#     try:
#         sayi = next(iterator)
#         print(sayi)
#     except StopIteration:
#         break


# costum iterator #############

# sayilar = [1,2,3,4,5]
# s = "hello"

# def my_for(iterable, func):
#     iterator = iter(iterable)
#     while True:
#         try:
#             sayi = next(iterator)
#             func(sayi)
#         except StopIteration:
#             break    

# my_for(sayilar, print)
# my_for(s, print)

#######

# class Counter():
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.start <= self.stop:
#             x = self.start
#             self.start += 1
#             return x
#         else:
#             raise StopIteration            

# dongu kullanmadan
# iterator = iter(Counter(20, 30))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# 20
# 21
# 22
# 23

# dongu ile
# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break

# farkli cesit dongu
# for i in Counter(10, 20):
#     print(i)
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20


# generators #############

# generator: iterable nesne olusturan fonksiyon

# def sayi_say(max):
#     sayi = 1
#     sayilar = []
#     while sayi <= max:
#         sayilar.append(sayi)
#         sayi += 1
#     return sayilar    

# sonuc = sayi_say(10)
# print(sonuc)
# eger buyuk bir dosyadan bir miktar veri lazımsa tum dosyayi bi listeye atmak performans kaybi, alan kaybi
# bi iterator olusturup next metodu araciligiyla her seferinde ihtiyacim old. kadarini alirim
# bellekte yer isgal eden bi liste olusturmamis olurum

def sayi_say(max):
    sayi = 1
    while sayi <= max:
        yield sayi  # iter ve next iplement edilmis
        sayi += 1

iterator = sayi_say(10)
# print(help(iterator))
# print(next(iterator))  # bi kere next e giderse geri donemez
# print(next(iterator))
# for i in iterator:
#     print(i)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

sonuc = list(iterator)  #  elemanlarin hepsi iterate edildi
print(sonuc)  #  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
