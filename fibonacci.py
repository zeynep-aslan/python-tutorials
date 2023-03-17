# cevap bu
a, b= 0, 1
while a<10:
    print(a, end=',')
    a, b= b, a+b  # bu tek satırda atama işlemleri eşzamanlı olarak atanır
# 0
# 1
# 1
# 2
# 3
# 5
# 8

# hatalı
while a<10:
    print(a)
    a=b
    b=a+b
# 0
# 1
# 2
# 4
# 8    