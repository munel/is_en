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
    def KategoriKelimeIdEkle(eklenenKelimeId,kategori=Kategori()):
        print("Kategori EKleme  başlayacak")
        return KategoriDAL.KategoriKelimeIdEkle(eklenenKelimeId,kategori)


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
    def KategoriKelimeIdGuncelle(kelime=Kelime(), kategori=Kategori()):
        KategoriBLL.KategoriKelimeIdSil(kelime)
        print("Kategori eklenecek : ")
        print(kelime.kelimeId)

        kategori.kategoriler = kategori.duzenlenecekYeniKategoriler
        print(kategori.kategoriler)
        return KategoriDAL.KategoriKelimeIdEkle(kelime.kelimeId, kategori)

    @staticmethod
    def KategoriKelimeIdSil(kelime=Kelime()):
        KategoriDAL.KategoriKelimeIdSil(kelime)

    @staticmethod
    def KategoriyeAitKelimeler(kategori=Kategori()):
        return KategoriDAL.KategoriyeAitKelimeler(kategori)
