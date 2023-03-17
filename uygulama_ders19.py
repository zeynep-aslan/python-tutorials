website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz(40 saat)"

# 1- " Hello World " karakter dizisinin baş ve sonraki karakterlerini silin.
# hw = " Hello World "
# result = hw.strip()

# 2- "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin.
temp = "www.sadikturan.com"
result = temp.strip("w.com")

# 3- 'course' karakter dizisinin tüm karakterlerini küçük yapın.
# result = course.lower()

# 4- 'website' içinde kaç tane a karakteri vardır? (count('a'))
# result = website.count(('a'))
# result=course.count(('a'), 0, 20)   # 0.indexten 20.intexe kadar olanları kapsar

# 5- 'website' www ile başlayıp com ile bitiyor mu?
# result = website.startswith("www")
# print(result)                
# result = website.endswith("com")
# print(result) 

# 6- 'website' içinde '.com' ifadesi var mı?
# result=website.find(".com")

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
# result=course.isalpha()

# 8- 'Content' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz
# result="content"
# result=result.center(50,'*')

# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin
# result=course.replace(" ", "-")

# 10- "hello world " karakter dizisinin "World " ifadesini "There" ile değiştirin
#result="hello world ".replace("world ", "There")

# 'course' karakter dizisini boşluk karakterlerinden ayırın
# result=course.split(" ")
# result=result[2]

print(result) 