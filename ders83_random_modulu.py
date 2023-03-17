# uyarı! dosyanın adı random.py ise ve import random dediğinde hata alırsın
import random

# result = dir(random)   # tum fonkiyonlar
# result = help(random)   # tüm fonkiyonların açıklamaları


result = random.random()   # 0.0 - 1.0  her seferinde farklı sayı. ondalıklı
result = random.random() * 100   # sonuçları 100 ile çarpar
result = int(random.uniform(1,10))   # 1 - 10 arasında integer 
result = random.randint(1,10)       # daha kolayı


names = ['zeynep', 'seyma', 'rumeysa', 'muhammet']
result = names[random.randint(0, len(names) - 1)]   # (0,3) de diyebilirdin ama database den alırsan diye dinamik yapmadık
# listeye isim de eklesen hata almazsın
result = random.choice(names)   # daha kolayı


greeting = 'hello there'
result = random.choice(greeting)


liste = list(range(10))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(liste)   # listenin elemanlarının yerlerini rastgele karıştırır. liste tamamen değişir
result = liste


liste = (range(100))   # list e de çevirebilirsin, 0 dan 100 e kadar 100 dahil değil, liste
result = random.sample(liste, 3)   # 1.parametre liste, 2.parametre eleman sayısı. listeden sayı kadar secer
result = random.sample(names, 2)


print(result) 