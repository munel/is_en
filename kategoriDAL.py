import sqlite3
from entity import Kategori
from entity import Kelime

conn = sqlite3.connect('Sozluk.db')



class KategoriDAL:

    @staticmethod
    def KategorileriListele():
        print("dal çalıştı")
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT GRUP_ADI FROM GRUPLAR")
            kategoriListesiTupple = cur.fetchall()
            return kategoriListesiTupple

    @staticmethod
    def KategoriIdBul(kategori=Kategori()):
        print("KategoriId bul dal çalıştı")
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT ID FROM GRUPLAR where GRUP_ADI=?",[kategori.kategori])
            bulunacakKategoriId = cur.fetchone()[0]
            return bulunacakKategoriId

    @staticmethod
    def KelimeyeAitKategoriBul(kelime=Kelime()):
        kelimeKategoriListesiTupple=""
        try:
            print("Kelimeye ait kategorileri bul çalışıyorç")


            with conn:

                cur = conn.cursor()
                print(Kelime.kelimeId)

                cur.execute("select GRUP_ID from GRUP_KELIMELERI where KELIME_ID = ? ",[kelime.kelimeId])


                kelimeKategoriIdListesiTupple = cur.fetchall()
            kelimeKategoriIdListesi=""
            kelimeKategoriIdListesi= [item[0] for item in kelimeKategoriIdListesiTupple]

            print("Gruplar: ")
            print(kelimeKategoriIdListesi)

            print("Gruplar bitti")
            with conn:
                cur = conn.cursor()
                soruIsareti= '?' * len(kelimeKategoriIdListesi)
                sql = 'select GRUP_ADI from GRUPLAR where ID In({}) '.format(', '.join(soruIsareti))
                cur.execute(sql, kelimeKategoriIdListesi)
                kelimeKategoriListesiTupple = cur.fetchall()

            print(kelimeKategoriListesiTupple)
        except Exception as exp:
            print(exp)
        return kelimeKategoriListesiTupple


    @staticmethod
    def KategoriSil(kategori=Kategori()):
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM GRUPLAR Where GRUP_ADI=(?)", [kategori.kategori])
            return  True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def KategoriKelimeIdEkle(eklenenKelimeId, kategori=Kategori()):
        print("Kategori EKlenecek")
        yeniKategori= kategori
        try:
            with conn:
                print("Kategori Eklenmeye başlandı")
                cur = conn.cursor()
                print("conn açıldı")
                for g in yeniKategori.kategoriler:
                    print(g)
                    cur.execute("SELECT ID FROM GRUPLAR WHERE GRUP_ADI=(?)", [g])
                    print("fetch yapılacak.")
                    idH = cur.fetchone()
                    groupId = idH[0]
                    print("execute yapılacak.")
                    cur.execute("INSERT INTO GRUP_KELIMELERI (GRUP_ID,KELIME_ID) VALUES(?,?)", [groupId, eklenenKelimeId])
            print ("Bitti")
            return True
        except Exception as exp:
            print(exp)
            return False



    @staticmethod
    def KategoriIdKelimeEkle(eklenenKategoriId, kelime=Kelime()):
        print("Kategori Id Kelime EKlenecek Dal")

        try:
            with conn:
                print("Kategori Eklenmeye başlandı")
                cur = conn.cursor()
                print("conn açıldı")
                print(kelime.kelimeler)
                for g in kelime.kelimeler:
                    print(g)
                    cur.execute("SELECT ID FROM KELIMELER WHERE KELIME_ADI=(?)", [g])
                    print("fetch yapılacak.")
                    idH = cur.fetchone()
                    kelimeId = idH[0]
                    print("execute yapılacak.")
                    cur.execute("INSERT INTO GRUP_KELIMELERI (GRUP_ID,KELIME_ID) VALUES(?,?)",
                                [eklenenKategoriId, kelimeId])
            print("Bitti")
            return True
        except Exception as exp:
            print(exp)
            return False

    @staticmethod
    def KelimelerKategoriIdEkle(eklenecekKategoriId, kelime=Kelime()):
        print("Kategori EKlenecek")
        yeniKelime = kelime
        try:

            with conn:
                print("Kategori Eklenmeye başlandı")
                cur = conn.cursor()
                print("conn açıldı")
                for g in yeniKelime.kelimeler:
                    print(g)
                    cur.execute("SELECT ID FROM KELIMELER WHERE KELIME_ADI=(?)", [g])
                    print("fetch yapılacak.")
                    idH = cur.fetchone()
                    kelimeId = idH[0]
                    print("execute yapılacak.")
                    cur.execute("INSERT INTO GRUP_KELIMELERI (GRUP_ID,KELIME_ID) VALUES(?,?)",
                                [eklenecekKategoriId, kelimeId])
            print("Bitti")
            return True
        except Exception as exp:
            print(exp)
            return False

    @staticmethod
    def KategoriIdKelimeSil(silinecekKategori):
        try:

            with conn:
                print("Kategoriler kategori Id ye göre silinmeye başlandı")
                cur = conn.cursor()
                print("conn açıldı ")
                cur.execute("delete from GRUP_KELIMELERI WHERE GRUP_ID=(?)", [silinecekKategori.kategoriId])
                print("fetch yapılacak.")
                print("Bitti")
            return True
        except Exception as exp:
            print(exp)
            return False

    @staticmethod
    def KategoriKelimeIdSil(kelime=Kelime()):
        try:
            with conn:
                print("Kategoriler silinmeye başlandı")
                cur = conn.cursor()
                print("conn açıldı")

                cur.execute("delete from GRUP_KELIMELERI WHERE KELIME_ID=(?)", [kelime.kelimeId])
                print("fetch yapılacak.")



                print("Bitti")
            return True
        except Exception as exp:
            print(exp)
            return False




    @staticmethod
    def KategoriyeAitKelimeler(kategori=Kategori()):
        sonuc=""
        print("kategoriye ait kelimeler")
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT KELIME_ADI FROM WR_GRUP_KELIMELERI WHERE GRUP_ADI=(?)", [kategori.kategori])
            sonuc = cur.fetchall()

        kelimeListesi = [item[0] for item in sonuc]
        print(kelimeListesi)
        return kelimeListesi


    @staticmethod
    def KategoriEkle(kategori=Kategori()):
        kategoriId=-1
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO GRUPLAR (GRUP_ADI) VALUES (?)",
                            [kategori.kategori])
                kategoriId = cur.lastrowid
                print("Kategori eklendi")
            return kategoriId
        except Exception as exp:
            print(exp)
            return  kategoriId

    @staticmethod
    def KategoriDuzenle(eskiKategori=Kategori(), yeniKategori=Kategori()):
        try:
            print(eskiKategori.kategori)
            print(yeniKategori.kategori)
            print("Kategori dal düzenlenecek.")
            with conn:
                cur = conn.cursor()
                cur.execute("UPDATE GRUPLAR SET GRUP_ADI = (?) WHERE GRUP_ADI=(?)", [yeniKategori.kategori,eskiKategori.kategori])
            return True
        except Exception as exp:
            print(exp)
            return False


