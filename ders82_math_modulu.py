# **************** yöntem 1 ****************
# import math

# value = dir(math)   # tüm fonksiyonları yazdırır

# value = help(math)   # modülün yardım dökümanı. enter la aşağı iner

# value = help(math.factorial)   # yazılan modülü açıklar

# value = math.sqrt(49)   # 7.0
# value = math.factorial(5)   # 120
# value = math.floor(9.9)   # 9
# value = math.ceil(3.3)   # 4


# **************** yöntem 2 ****************
# import math as islem

# value = islem.ceil(4.4)   # 5



# **************** yöntem 3 ****************
# from math import *
# from math import factorial, ceil
# math. demeden direkt fonksiyonmuş gibi modüldeki fonksiyonları kullanırız
# her şeyi import etmiş oluruz
# sadece yazılanları import etmiş oluruz

# value = factorial(5)   # 120
# value = ceil(3.3)   # 4

# ------


def sqrt(x):
    print('x: '+ str(x))

from math import factorial, ceil, sqrt


value = sqrt(4)   # alta hangisini yazarsak onun dediği olur

print(value)
# pow : üs alma
# sqrt : karekök
# floor : aşağı yuvarlama
# ceil : yukarı yuvarlama

