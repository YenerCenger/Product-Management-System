import sqlite3

class Ürün():

    def __init__(self,isim,kategori,alış_fiyat,satış_fiyat,stok):
        self.isim = isim
        self.kategori = kategori
        self.alış_fiyat = alış_fiyat
        self.satış_fiyat = satış_fiyat
        self.stok = stok

    def __str__(self):
        return """\nÜrün: {}\nKategori: {}\nAlış Fiyatı: {}\nSatış Fiyatı: {}\nStok: {}""".format(self.isim,self.kategori,self.alış_fiyat,self.satış_fiyat,self.stok)

class Dükkan():

    def __init__(self):
        self.bağlantı_oluştur()

    def bağlantı_oluştur(self):

        self.bağlantı = sqlite3.connect("Dükkan.db")

        self.cursor = self.bağlantı.cursor()

        sorgu = "Create Table IF NOT EXISTS ürünler (isim TEXT,kategori TEXT,alış_fiyat INT,satış_fiyat INT,stok INT)"

        self.cursor.execute(sorgu)

        self.bağlantı.commit()

    def bağlantı_kes(self):
        self.bağlantı.close()

    def ürünleri_göster(self):
        sorgu = "Select * From ürünler"

        self.cursor.execute(sorgu)

        ürünler = self.cursor.fetchall()

        if ( len(ürünler)== 0 ):
            print("Herhangi bir ürün bulunmuyor.")
        else:
            for i in ürünler:
                ürün = Ürün(i[0],i[1],i[2],i[3],i[4])
                print(ürün)

    def ürün_sorgula(self,isim):

        sorgu = "Select * From ürünler where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        ürünler = self.cursor.fetchall()

        if ( len(ürünler)== 0 ):
            print(isim,"adlı bir ürün bulunmuyor..")
        else:
            ürün = Ürün(ürünler[0][0],ürünler[0][1],ürünler[0][2],ürünler[0][3],ürünler[0][4])
            print(ürün)

    def ürün_ekle(self,ürün):

        sorgu = "Insert into ürünler Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(ürün.isim,ürün.kategori,ürün.alış_fiyat,ürün.satış_fiyat,ürün.stok))

        self.bağlantı.commit()

    def ürün_kaldır(self,isim):

        sorgu = "Select * From ürünler where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        ürünler = self.cursor.fetchall()

        if (len(ürünler) == 0):
            print(isim, "adlı bir ürün bulunmuyor..")
        else:
            soru = input("Bu ürünü kaldırmak istediğinize emin misiniz? (E/H)").upper()

            if soru == "E":
                sorgu = "Delete From ürünler where isim = ?"
                self.cursor.execute(sorgu,(isim,))
                print("ürün kaldırıldı.")
                self.bağlantı.commit()

    def stok_arttır(self,isim,miktar):

        sorgu = "Select * From ürünler where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        ürünler = self.cursor.fetchall()

        if (len(ürünler) == 0):
            print(isim, "adlı bir ürün bulunmuyor..")
        else:
            stok = ürünler[0][4]

            stok += miktar

            sorgu2 = "Update ürünler set stok = ? where isim = ?"

            self.cursor.execute(sorgu2, (stok,isim))

            print(stok-miktar,"olan stok",stok,"olarak güncellendi.")

            self.bağlantı.commit()


    def ürün_sat(self,isim):

        sorgu = "Select * From ürünler where isim = ?"

        self.cursor.execute(sorgu, (isim,))

        ürünler = self.cursor.fetchall()

        if (len(ürünler) == 0):
            print(isim, "adlı bir ürün bulunmuyor..")
        else:
            stok = ürünler[0][4]

            stok -= 1

            sorgu2 = "Update ürünler set stok = ? where isim = ?"

            self.cursor.execute(sorgu2, (stok, isim))

            print("Güncel Stok:",stok)

            self.bağlantı.commit()

    def toplu_sat(self,isim,miktar):

        sorgu = "Select * From ürünler where isim = ?"

        self.cursor.execute(sorgu, (isim,))

        ürünler = self.cursor.fetchall()

        if (len(ürünler) == 0):
            print(isim, "adlı bir ürün bulunmuyor..")
        else:
            stok = ürünler[0][4]

            stok -= miktar

            sorgu2 = "Update ürünler set stok = ? where isim = ?"

            self.cursor.execute(sorgu2, (stok, isim))

            print(stok + miktar, "olan stok", stok, "olarak güncellendi.")

            self.bağlantı.commit()

    def zam_yap(self,isim,zam_oranı):

        sorgu = "Select * From ürünler where isim = ?"

        self.cursor.execute(sorgu, (isim,))

        ürünler = self.cursor.fetchall()

        if (len(ürünler) == 0):
            print(isim, "adlı bir ürün bulunmuyor..")
        else:
            sorgu2 = "Update ürünler set satış_fiyat = ? where isim = ?"

            zam_oranı = zam_oranı/100 + 1

            self.cursor.execute(sorgu2, (int(ürünler[0][3]*zam_oranı),isim))

            print(ürünler[0][3],"olan satış fiyatı", int(ürünler[0][3]*zam_oranı),"olarak güncellendi.")

            self.bağlantı.commit()

    def alış_fiyat_değiştir(self,isim,fiyat):

        sorgu = "Select * From ürünler where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        ürünler = self.cursor.fetchall()

        if (len(ürünler) == 0):
            print(isim, "adlı bir ürün bulunmuyor..")
        else:
            alış_fiyat = ürünler[0][2]

            alış_fiyat = fiyat

            sorgu2 = "Update ürünler set alış_fiyat = ? where isim = ?"

            self.cursor.execute(sorgu2, (alış_fiyat, isim))

            print("alış fiyatı", alış_fiyat, "olarak güncellendi.")

            self.bağlantı.commit()

    def satış_fiyat_değiştir(self,isim,fiyat):

        sorgu = "Select * From ürünler where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        ürünler = self.cursor.fetchall()

        if (len(ürünler) == 0):
            print(isim, "adlı bir ürün bulunmuyor..")
        else:
            satış_fiyat = ürünler[0][3]

            satış_fiyat = fiyat

            sorgu2 = "Update ürünler set satış_fiyat = ? where isim = ?"

            self.cursor.execute(sorgu2, (satış_fiyat, isim))

            print("satış fiyatı", satış_fiyat, "olarak güncellendi.")

            self.bağlantı.commit()

    def toplu_zam(self, zam_oranı):

        sorgu = "SELECT * FROM ürünler"

        self.cursor.execute(sorgu)

        ürünler = self.cursor.fetchall()

        for ürün in ürünler:
            yeni_fiyat = ürün[3] * (1 + zam_oranı / 100)

            sorgu2 = "UPDATE ürünler SET satış_fiyat = ? WHERE isim = ?"
            self.cursor.execute(sorgu2, (int(yeni_fiyat), ürün[0]))

        self.bağlantı.commit()

