# yapılacaklar:
# paraYatir() isminde bir fonksiyonla hesaba para yatırma(fonksiyon dışardan hesap bilgisi alır(obje) yani hangi hesaba yatıracağını)
# bakiye = 0 sa ve ekHesabında da para bitmişse para ekleyince ilk ekHesaba aktarılır ekHesap limiti belirlenir. limit dolunca hesaba para aktarılmaya başlanır
# ek hesaptan parayı kullandığın tarihi obje içerisine kayıt edip tekraren ekHesaba para aktarırken faiz olup onu bakiyeden eksiltme
# yani %5 faiz varsa 20 gün sonra ek hesaba yatırdıysan yatırdığın paranın %5 ini ana hesaptan düşersin

""" 
    ZeynepHesap, RumeysaHesap bunlar birer obje. fonksiyona gönderdiğinde içinde değişiklik yapılabilir.
    bilgileri obje içinde tanımlamak yerine 
    ad = 'Zeynep' 
    hesapNo = '12414212412'
    bakiye = 3000
    diye ayrı ayrı tanımlasaydık değişkenlerin adreslerindeki değerleri fonksiyonla değiştiremediğimiz için bi bok yapamazdık
    fonksiyonla değişiklik yapmak istediğin bir şey varsa içine obje gönder
"""

ZeynepHesap = {
    'ad': 'Zeynep Aslan',
    'hesapNo': '1341242334',
    'bakiye': 3000,
    'ekHesap': 2000
    'ekHesapLimiti': 3000
}

# obje
RumeysaHesap = {
    'ad': 'Rumeysa Aslan',
    'hesapNo': '2141242334',
    'bakiye': 2000,
    'ekHesap': 1000
    'ekHesapLimiti': 2000
}

def paraCek(hesap, miktar):
    print(f"merhaba {hesap['ad']}")
    if (hesap['bakiye']>=miktar):
        hesap['bakiye'] -= miktar
        print('paranizi alabilirsiniz.')
        bakiyeSorgu(hesap)
    else:
        if (hesap['bakiye']+hesap['ekHesap']>=miktar):
            ekHesapKullanimi = input('ek hesabinizi kullanmak istiyor musunuz?(e/h)')
            if ekHesapKullanimi == 'e':
                hesap['ekHesap'] -= (miktar - hesap['bakiye'])
                hesap['bakiye'] = 0
                print('paranizi alabilirsiniz.')
                bakiyeSorgu(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} bulundugundan dolayi islemi gerceklestiremiyoruz.")    
        else:
            print('uzgunuz, bakiye yetersiz')
            bakiyeSorgu(hesap)

def paraYatir(hesap, miktar):
    print(f"merhaba {hesap['ad']}")
    if (hesap['ekHesapLimiti']>hesap['ekHesap']):
        ekHesapKullanimi = input('ek hesabinizdaki miktar ek hesap liminizin altinda. once ek hesabiniza para yatirmak istiyor musunuz?(e/h)')
        if ekHesapKullanimi == 'e':
            miktar -= (hesap['ekHesapLimiti'] - hesap['ekHesap'])
            hesap['ekHesap'] += (hesap['ekHesapLimiti'] - hesap['ekHesap'])
            hesap['bakiye'] += miktar
            print('isleminiz tamamlanmistir.')
            bakiyeSorgu(hesap)
        else:
            print(f"{hesap['hesapNo']} nolu ek hesabinizda {hesap['ekHesapLimiti'] - hesap['ekHesap']} TL eksik oldugundan dolayi islemi gerceklestiremiyoruz.")
    else:
        hesap['bakiye'] += miktar
        bakiyeSorgu(hesap)

def bakiyeSorgu(hesap):
    print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir. Ek hesap limitiniz ise {hesap['ekHesap']} TL dir.")


secilenHesap = input('islem yapmak istediginiz hesap numarasini giriniz: ')    
islem = int(input('yapmak istediginiz islemi sacin:\n1- Para Cekme\n2- Para Yatirma\n3-Bakiye Sorgulama '))
if islem == 1:
    secilenMiktar = int(input('cekmek istediginiz miktari giriniz: '))
    paraCek(secilenHesap, secilenMiktar)
elif islem == 2:
    secilenMiktar = int(input('yatirmak istediginiz miktari giriniz: '))
    paraYatir(secilenHesap, secilenMiktar)    
elif islem == 3:
    bakiyeSorgu(secilenHesap)    
else:
    break    



