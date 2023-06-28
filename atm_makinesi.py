print("""
******************

Hoşgeldiniz...

İşlemler:

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Çıkmak için 'q' ya basınız.

******************
""")

bakiye = 10000

while True:
    islem = int(input("İşlemi Seçiniz:"))

    if islem == "q":
        break
    elif (islem == 1):
        print("Bakiyeniz: {} TL".format(bakiye))
        islem_devam = input("Başka İşlem Yapmak İster misiniz? Evet/Hayır:")
        if islem_devam == "Evet":
            continue
        else:
            print("Çıkış Yapılıyor...")
            break
    elif (islem == 2):
        yatirma_miktari = float(input("Yatırmak İstediğiniz Miktarı Giriniz:"))
        bakiye += yatirma_miktari
        print("Yeni Bakiyeniz:{} TL".format(bakiye))
        islem_devam = input("Başka İşlem Yapmak İster misiniz? Evet/Hayır:")
        if islem_devam == "Evet":
            continue
        else:
            print("Çıkış Yapılıyor...")
            break
    elif islem == 3:
        cekme_miktari = float(input("Çekmek İstediğiniz Miktarı Giriniz:"))
        bakiye -= cekme_miktari
        print("Yeni Bakiyeniz:{} TL".format(bakiye))
        islem_devam = input("Başka İşlem Yapmak İster misiniz? Evet/Hayır:")
        if islem_devam == "Evet":
            continue
        else:
            print("Çıkış Yapılıyor...")
            break
    else:
        print("Lütfen Geçerli Bir İşlem Seçiniz...")
        continue