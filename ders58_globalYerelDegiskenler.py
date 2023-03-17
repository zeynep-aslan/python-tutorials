# # global scope
x = 'Global x'

def function():
    # local scope : burada fonksiyon için ayrı çalışma alanı hazırlıyorsun.
    # burada hazrıladığın değişkenler dışardakileri etkilemiyor
    x = 'Local x'
    print(x)

function()
print(x)
# Local x
# Global x
#------------

x = 'Global x'

def function():
    print(x)

function()
print(x)
# fonksiyonda tanımlama olmadığı için kendisi için 1 üst kapsamı kullanıyor
# Global x
# Global x
#------------

# global
name = 'Zeynep'
def changeName(new_name):
    # local
    name = new_name   # sadece local name i değiştirdi
    print(name)

changeName('Ada')
print(name)
# Ada
# Zeynep
#------------

name = 'global string'
def greeting():
    name = 'Zeynep'
    def hello():
        name = 'Sena'
        print('hello', name)
    hello()

greeting()
# hello Sena
# name değişkenini kendi globalinde arar yoksa bir üst globalinden alır
# hello() daki name değişkeni kalkarsa çıktı: hello Zeynep
# greeting() deki name değişkenleri kalkarsa çıktı: hello global string
#------------

x = 50
def test(x):
    print(f'x: {x}')
    x = 100
    print(f'changed x to {x}')
test(x)
print(x)
# x: 50
# changed x to 100
# 50
#------------

# dışarda tanımlanan x değişkenini fonksiyon içinde değiştirmek istiyorsak fonk içinde global olarak tanımlamalıyız
x = 50
def test():
    global x      # bu sayede içeride x i değiştirebildik
    print(f'x: {x}')
    x = 100
    print(f'changed x to {x}')
test()
print(x)
# x: 50
# changed x to 100
# 100
#------------

name = 'Zeynep'
def changeName(new_name):
    global name     # name e değişiklik yapma yetkisi verdik gibi bir şey
    name = new_name
    print(name)

changeName('Ada')
print(name)
# Ada
# Ada

