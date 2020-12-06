import sys
from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QInputDialog, QMainWindow, QLineEdit, QMessageBox

from kelimeislemleri import YeniKelimeEkle
from silinecekkelimeform import SilinecekKelimeForm
from duzenlenecekkelimeform import DuzenlenecekKelimeForm
from Sinav_coktan_secme import *
from isaret_dili_hafiza_oyunu import HafizaOyunu

from form import *
import sqlite3
from kategoriBLL import KategoriBLL
from kelimeBLL import KelimeBLL
from entity import Kelime
from entity import Kategori
from helper import Helper


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit.textChanged.connect(self.aramaMetniDegistir)
        self.ui.listWidget.itemClicked.connect(self.listedeKiElemanSecildi)
        self.ui.comboBox.currentIndexChanged.connect(self.comboBoxSecim)
        self.ui.actionKategori_Ekle.triggered.connect(self.yeniKategoriEkle)
        self.ui.actionKategori_Sil.triggered.connect(self.kategoriSil)
        self.ui.actionKategori_Duzenle.triggered.connect(self.kategoriDuzenle)
        self.ui.actionCoktanSecmeliSinav.triggered.connect(self.sinavCoktanSecmeli)
        self.ui.actionHafizaOyunu.triggered.connect(self.hafizaOyunuAc)

        self.ui.actionKelime_Ekle.triggered.connect(self.yeniKelimeEkle)
        self.ui.actionKelime_Sil.triggered.connect(self.kelimeSil)
        self.ui.actionKelime_Duzenle.triggered.connect(self.kelimeDuzenle)

        self.secilenKelime=Kelime()
        self.secilenKategori = Kategori()
        self.yeniKategori=Kategori()

        self.silinecekKategori=Kategori()
        self.kelimeListesi = []
        self.kategoriListesi = []
        self.seciliListe = []
        self.listeleriHazirla()

        self.listeyiHazirla()
        self.comboListeHazirla()

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.ui.layout.addWidget(videoWidget)
        self.mediaPlayer.setVideoOutput(videoWidget)
        ##self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("VIDEOLAR/RAHAT.mp4")))
        self.mediaPlayer.play()


        self.show()

    def listeleriHazirla(self):
        try:

            kelimeListesiTupple  = KelimeBLL.KelimeleriListele()
            kategoriListesiTupple = KategoriBLL.KategorileriListele()
            self.kelimeListesi = [item[0] for item in kelimeListesiTupple]
            self.kategoriListesi = [item[0] for item in kategoriListesiTupple]
            self.kategoriListesi.insert(0, "Kategori Seçin")
        except Exception as exp:
            print(exp)


    def yeniKelimeEkle(self):
        try:
            self.yenikelimeEkle = YeniKelimeEkle()
            self.yenikelimeEkle.show()
            if self.yenikelimeEkle.close:
                print("Deneme")
        except Exception as e:
            print(e)
        if self.yenikelimeEkle.exec_() == 1:
            self.listeleriHazirla()
            self.listeyiHazirla()
            QMessageBox.information(self, "Yeni Kelime", "Yeni Kelime Eklendi")

    def kelimeSil(self):
        try:
            self.kelimeSil = SilinecekKelimeForm()
            self.kelimeSil.show()
            if self.kelimeSil.close:
                print("Kelime Sil Kapatıldı")
        except Exception as e:
            print(e)
        if self.kelimeSil.exec_() == 1:
            self.listeleriHazirla()
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(self.kelimeListesi)
            QMessageBox.information(self, "Kelime Sil", "Kelime Silindi")
            self.listeleriHazirla()
            self.listeyiHazirla()



    def kelimeDuzenle(self):

        print("Kelime Düzenle menü basıldı")
        try:
            self.KelimeDuzenle = DuzenlenecekKelimeForm()
            print("Kelime Düzenle yaratıldı")
            self.KelimeDuzenle.show()
            if self.KelimeDuzenle.close:
                print("Kelime Düzenle Kapatıldı")
        except Exception as e:
            print(e)
        if self.KelimeDuzenle.exec_() == 1:
            self.listeleriHazirla()
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(self.kelimeListesi)
            QMessageBox.information(self, "Kelime Düzenle", "Kelime Düzeltildi.")
            self.listeleriHazirla()
            self.listeyiHazirla()




    def kategoriDuzenle(self):
        item, okPressed = QInputDialog.getItem(self, "Kategori Düzenleme", "Düzenlenecek Kategori:", self.kategoriListesi, 0,
                                               False)
        eskiKategori=Kategori()
        eskiKategori.kategori=item
        pass
        if okPressed :
            if item != "Kategori Seçin":
                duzenlenmis, ok = QInputDialog.getText(self, "Kategori Düzenle", f"Düzenlenen Kategori:  {item}",
                                                       QLineEdit.Normal, "")
                yeniKategori = Kategori()
                yeniKategori.kategori = duzenlenmis

                if ok and yeniKategori.kategori:
                    print(eskiKategori.kategori)
                    print(yeniKategori.kategori)
                    guncellendiMi = KategoriBLL.KategoriDuzenle(eskiKategori,yeniKategori)

                    if guncellendiMi :
                        QMessageBox.information(self, "Düzenleme", "Kategori Düzenlendi")
                        self.listeleriHazirla()
                        self.comboListeHazirla()
                        self.listeyiHazirla()

                    else :
                        QMessageBox.warning(self, "Düzenleme", "Kategori Düzenlenmedi")
                else:
                    QMessageBox.information(self, "Düzenleme", "Vazgeçildi.")
            else:
                QMessageBox.warning(self, "Düzenleme", "Kategori seçmediğiniz için iptal edildi.")
        else:
            QMessageBox.information(self, "Düzenleme", "Vazgeçildi.")

    def yeniKategoriEkle(self):
        try:
            yazilanYeniKategori, okPressed = QInputDialog.getText(self, "Kategori Ekleme", "Yeni Kategori:", QLineEdit.Normal, "")
            self.yeniKategori.kategori=Helper.KucukHarfleriBuyukYap(yazilanYeniKategori)
            if okPressed and self.yeniKategori.kategori != '':
                # kategoriler tablosuna yeni kategori eklenecek

                    eklendiMi= KategoriBLL.KategoriEkle(self.yeniKategori)

                    if (eklendiMi):
                        QMessageBox.information(self, "Kategori Ekleme", "Yeni Kategori Eklendi")

                        self.listeleriHazirla()
                        self.comboListeHazirla()
                        self.listeyiHazirla()
                    else:
                        raise Exception("Sql kayıt eklenemedi.")

        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Kategori Ekleme", "Yeni Kategori Eklenemedi.")

    def kategoriSil(self):
        try:
            self.silinecekKategori.kategori, okPressed = QInputDialog.getItem(self, "Kategori Silme İşlemi", "Silinecek Kategoriyi Seçin:",
                                                   self.kategoriListesi, 0, False)
            if okPressed and self.silinecekKategori.kategori:
                if self.silinecekKategori.kategori != "Kategori Seçin":

                    KategoriBLL.KategoriSil(Kategori)

                    self.listeleriHazirla()

                    self.comboListeHazirla()

                    self.ui.listWidget.clear()
                    self.ui.listWidget.addItems(self.kelimeListesi)
                    QMessageBox.information(self, "Kategroi Silme", "Kategori Silindi")
                else :
                    QMessageBox.warning(self, "Kategroi Silme", "Bu seçenek silinemez.")
        except Exception as exp:
            print(exp)


    def comboBoxSecim(self):
        self.secilenKategori.kategori = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())

        if (self.ui.comboBox.currentIndex() != 0):  # düzeltilmesi gerekiyor  bütün hepsinde çıkması lazım
            try:
                kelimeListesi = KategoriBLL.KategoriyeAitKelimeler(self.secilenKategori)
                self.ui.listWidget.clear()
                self.ui.listWidget.addItems(kelimeListesi)
            except Exception as e:
                print(e)

    def comboListeHazirla(self):
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(self.kategoriListesi)

    def listeyiHazirla(self):
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(self.kelimeListesi)

    def videoyuOynat(self, video):
        ##self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("VIDEOLAR/RAHAT.mp4")))
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile(video)))
        self.mediaPlayer.play()

    def listedeKiElemanSecildi(self):
        self.secilenKelime.kelime = self.ui.listWidget.currentItem().text()
        sonuc = KelimeBLL.KelimeVideoBul(self.secilenKelime)
        print(sonuc)
        self.videoyuOynat(sonuc)

    def sinavCoktanSecmeli(self):
        self.Form = QtWidgets.QWidget()
        self.Form.ui = Sinav_coktan_secme()
        self.Form.ui.show()

    def aramaMetniDegistir(self):
        self.ui.listWidget.clear()
        self.seciliListe.clear()
        aramaMetni = self.ui.lineEdit.text()
        for v in self.kelimeListesi:
            if v.startswith(Helper.KucukHarfleriBuyukYap(aramaMetni)):
                self.seciliListe.append(v)

        self.ui.listWidget.addItems(self.seciliListe)

    def hafizaOyunuAc(self):
        h = HafizaOyunu()
        h.oyunuBaslat()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
