from dükkan import *

import time
print("""***********************************

İşlemler:

1-Ürünleri Göster

2-Ürün Sorgula

3-Ürün Ekle

4-Ürün Kaldır

5-Stok Arttır

6-Ürün Sat

7-Toplu Ürün Sat

8-Zam Yap

9-Alış fiyatı güncelle

10-Satış fiyatı güncelle

11-Toplu zam yap

çıkış içim 'q' ya basın
***********************************
""")

dükkan = Dükkan()

while True:
    işlem = input("İşlem Seçin:")

    if işlem == "q":
        print("Programdan Çıkılıyor...")
        dükkan.bağlantı_kes()
        break

    elif işlem == "1":
        dükkan.ürünleri_göster()

    elif işlem == "2":
        ürün = input("Aradığınız Ürünü Girin:").upper()
        dükkan.ürün_sorgula(ürün)

    elif işlem == "3":
        isim = input("Ürünün Adı:").upper()
        kategori = input("Kategori:").upper()
        alış_fiyat = int(input("Ürünün alış fiyatı:"))
        satış_fiyat = int(input("Ürünün satış fiyatı:"))
        stok = int(input("Ürün Stok:"))

        yeni_ürün = Ürün(isim,kategori,alış_fiyat,satış_fiyat,stok)
        print("Ürün Ekleniyor...")
        time.sleep(1)
        dükkan.ürün_ekle(yeni_ürün)
        print("Ürün Eklendi.")

    elif işlem == "4":
        isim = input("Silmek İstediğiniz Ürünün adını girin:").upper()
        dükkan.ürün_kaldır(isim)


    elif işlem == "5":
        isim = input("Stoğunu arttıracağınız ürünün adı: ").upper()
        miktar = int(input("Kaç Adet Aldınız: "))
        dükkan.stok_arttır(isim,miktar)

    elif işlem == "6":
        isim = input("Sattığınız ürünün adı: ").upper()
        dükkan.ürün_sat(isim)

    elif işlem == "7":
        isim = input("Sattıpınız ürünün adı: ").upper()
        miktar = int(input("Kaç Adet Sattınız: "))
        dükkan.toplu_sat(isim,miktar)

    elif işlem == "8":
        isim = input("Zam yapacağınız ürünün adı: ").upper()
        zam_miktarı = int(input("Zam oranını girin: "))
        dükkan.zam_yap(isim,zam_miktarı)

    elif işlem == "9":
        isim = input("alış fiyatı değişecek ürünün adı: ").upper()
        yeni_fiyat = int(input("Yeni fiyatı girin: "))
        dükkan.alış_fiyat_değiştir(isim,yeni_fiyat)

    elif işlem == "10":
        isim = input("satış fiyatı değişecek ürünün adı: ").upper()
        yeni_fiyat = int(input("Yeni fiyatı girin: "))
        dükkan.satış_fiyat_değiştir(isim, yeni_fiyat)

    elif işlem == "11":
        zam_oranı = int(input("Zam oranını giriniz:"))
        dükkan.toplu_zam(zam_oranı)

    else:
        print("Geçersiz İşlem...")