import mod

# result = help(mod)
# result = help(mod.func)
# result = mod.number
# result = mod.person["age"]
# result = mod.person["name"]
# result = mod.func(10)

p = mod.Person()
result = p.speak()  # i am speaking...


# python ın içinde olan modüllerin içine yazdığımız modülü eklemeyi gösterdi

from mod import person,numbers
sonuc=person

from mod import *
# bu şekilde her seferinde mod. demeden mod daki yaılanlara ulaşabiliriz
sonuc=numbers

print(sonuc)

print(result)