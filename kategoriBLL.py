from kategoriDAL import KategoriDAL
from kelimeBLL import  KelimeBLL
from entity import Kategori
from entity import Kelime

class KategoriBLL:

    @staticmethod
    def KategorileriListele():
        print("Kategori Listele Bll Çalıştı")
        return KategoriDAL.KategorileriListele()

    @staticmethod
    def KategoriIdBul(kategori=Kategori()):
        KategoriDAL.KategoriIdBul(kategori)

    @staticmethod
    def KategoriKelimeIdEkle(eklenenKelimeId,kategori=Kategori()):
        print("Kategori EKleme  başlayacak")
        return KategoriDAL.KategoriKelimeIdEkle(eklenenKelimeId,kategori)

    @staticmethod
    def KategoriIdKelimeEkle(eklenenKategoriId, kelime=Kelime()):
        print("KategoriId Kelime EKleme  başlayacak")
        return KategoriDAL.KategoriIdKelimeEkle(eklenenKategoriId, kelime)

    @staticmethod
    def KategoriEkleSadece(kategori=Kategori()):
        eklenenKategoriId=  KategoriDAL.KategoriEkle(kategori)
        if eklenenKategoriId>0:
            return True
        else:
            return False

    @staticmethod
    def KategoriEkleKelimeAta(kategori=Kategori(),secilenKelimeler=Kelime()):
        eklenenKategoriId=KategoriDAL.KategoriEkle(kategori)
        return KategoriDAL.KelimelerKategoriIdEkle(eklenenKategoriId,secilenKelimeler)

    @staticmethod
    def KategoriSil(kategori=Kategori()):
        return KategoriDAL.KategoriSil(kategori)

    @staticmethod
    def KategoriDuzenle(eskiKategori=Kategori(), yeniKategori=Kategori()):
        return KategoriDAL.KategoriDuzenle(eskiKategori,yeniKategori)


    @staticmethod
    def KelimeyeAitKategoriBul(Kelime=Kelime()):
        print("Kategori Bul Bll Çalıştı")
        KelimeBLL.KelimeIDBul(Kelime)
        print("Kelime ID BUl Bitti")
        print("Kategori Id bul Bitti:")
        print(Kelime.kelime)
        print(Kelime.kelimeId)
        print("kelimeye ait Kategoriler bulunacak")

        return  KategoriDAL.KelimeyeAitKategoriBul(Kelime)



    @staticmethod
    def KategoriKelimeIdSil(kelime=Kelime()):
        KategoriDAL.KategoriKelimeIdSil(kelime)

    @staticmethod
    def KategoriIdKelimeSil(kategori=Kategori()):
        KategoriDAL.KategoriIdKelimeSil(kategori)

    @staticmethod
    def KategoriyeAitKelimeler(kategori=Kategori()):
        return KategoriDAL.KategoriyeAitKelimeler(kategori)

    @staticmethod
    def KategoriKelimeIdGuncelle(kelime=Kelime(), kategori=Kategori()):
        KategoriBLL.KategoriKelimeIdSil(kelime)
        print("Kategori eklenecek : ")
        print(kelime.kelimeId)

        kategori.kategoriler = kategori.duzenlenecekYeniKategoriler
        print(kategori.kategoriler)
        return KategoriDAL.KategoriKelimeIdEkle(kelime.kelimeId, kategori)


    @staticmethod
    def KategoriIdKelimeGuncelle(kelime=Kelime(), eskiKategori=Kategori(),yeniKategori=Kategori()):
        try:
            print("Kategori düzenlenecek : ")
            KategoriBLL.KategoriDuzenle(eskiKategori, yeniKategori)
            print("KategoriId bulunacak")
            kategoriId = KategoriDAL.KategoriIdBul(yeniKategori)
            print("Kategori Id: ", kategoriId)
            yeniKategori.kategoriId = kategoriId

            silindiMi = KategoriBLL.KategoriIdKelimeSil(yeniKategori)
            print(silindiMi)
            KategoriBLL.KategoriIdKelimeEkle(yeniKategori.kategoriId,kelime)
            return True

        except Exception as exp:
            print(exp)
            return False
