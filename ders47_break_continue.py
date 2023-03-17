name = 'zeynep'
for letter in name:
    if letter == 'e':
        break   # döngüyü durdurur ve diğer harfler ekrana yazdırılmaz
    print(letter)

for letter in name:
    if letter == 'e':
        continue   # döngüyü bu seferliğine durdurur ve diğer harfler ekrana yazdırılır
    print(letter)    

x=0
while x<5:
    x+=1
    if x==2:
        break   # döngüden komple çıktı
    print(x)

while x<5:
    if x==2:
        x+=1
        continue  # döngüden tek seferliğine çıktı
    print(x)
    x+=1


while True: # Sonsuz döngü. Nasıl sonlandırabiliriz ? 
    isim = input("İsminiz(Çıkmak için q tuşuna basın.):")
    if (isim == "q"): # break ile tabii ki.
        print("Çıkış yapılıyor...")
        break
    print(isim)