from kelimeDAL import KelimeDAL
from kategoriDAL import KategoriDAL
from videoBLL import VideoBLL
from entity import Kelime
from entity import Kategori
from entity import Video



class KelimeBLL:

    @staticmethod
    def KelimeleriListele():
        print("kelime bll çalıştı")

        return KelimeDAL.KelimeleriListele()

    @staticmethod
    def YeniKelimeEkle(kelime=Kelime(),video=Video()):
        print("Kelime BLL başladı")
        return KelimeDAL.KelimeEkle(kelime,video)

    @staticmethod
    def KelimeVideoGuncelle(kelime=Kelime(),video=Video()):
        print("kelimvideogüncelle bll çalıştı.")
        KelimeDAL.KelimeVideoGuncelle(kelime,video)

    @staticmethod
    def KelimeSil(kelime=Kelime(),video=Video()):

        VideoBLL.VideoSil(video)
        KategoriDAL.KategoriKelimeIdSil(kelime)
        return KelimeDAL.KelimeSil(kelime)

    @staticmethod
    def KelimeVideoBul(kelime=Kelime()):
        return KelimeDAL.KelimeVideoBul(kelime)

    @staticmethod
    def KelimeIDBul(kelime=Kelime()):
        return KelimeDAL.KelimeIDBul(kelime)