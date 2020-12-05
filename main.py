import sys
from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QInputDialog, QMainWindow, QLineEdit, QMessageBox
from kelimeislemleri import YeniKelimeEkle
from Sinav_coktan_secme import *
from form import *
import sqlite3



conn = sqlite3.connect('Sozluk.db')

def buyukHarfeCevir(metin):
    dizi = ["İ" if m=="i" else m.upper() for m in metin]
    return "".join(dizi)


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
        self.ui.actionKategori_D_zenle.triggered.connect(self.kategoriDuzenle)
        self.ui.actionRastgele_S_nav_Yap.triggered.connect(self.sinavCoktanSecmeli)
        self.ui.actionKelime_Ekle.triggered.connect(self.yeniKelimeEkle)
        self.ui.actionKelime_Sil.triggered.connect(self.kelimeSil)

        self.kelimeListesi = []
        self.kategoriListesi = []
        self.seciliListe = []
        self.listeleriHazirla()

        self.listeyiHazirla()
        self.comboListeHazirla()

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget(self)
        self.ui.layout.addWidget(videoWidget)



        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("VIDEOLAR/RAHAT.mp4")))
        self.mediaPlayer.play()




        self.show()
    def sinavCoktanSecmeli(self):
        self.s = Sinav_coktan_secme()





    def listeleriHazirla(self):
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT KELIME_ADI FROM KELIMELER")
            kelimeListesiTupple = cur.fetchall()
            cur.execute("SELECT GRUP_ADI FROM GRUPLAR")
            kategoriListesiTupple = cur.fetchall()
        self.kelimeListesi = [item[0] for item in kelimeListesiTupple]
        self.kategoriListesi = [item[0] for item in kategoriListesiTupple]
        self.kategoriListesi.insert(0, "Kategori Seçin")


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
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(self.kelimeListesi)
            QMessageBox.information(self, "Yeni Kelime", "Yeni Kelime Eklendi")

    def kelimeSil(self):
        self.listeleriHazirla()
        item, okPressed = QInputDialog.getItem(self, "Kelime Silme İşlemi", "Silineek Kelimeyi Seçin:",
                                               self.kelimeListesi, 0, False)
        if okPressed and item:

            try:
                with conn:
                    cur = conn.cursor()
                    cur.execute("DELETE FROM KELIMELER Where KELIME_ADI=(?)", [item])


                self.ui.comboBox.clear()
                self.ui.listWidget.clear()
                self.listeleriHazirla()
                self.ui.comboBox.addItems(self.kategoriListesi)
                self.ui.listWidget.addItems(self.kelimeListesi)
                QMessageBox.information(self, "Kelime Silme", "Kelime Silindi")
            except Exception as e:
                print(e)

    def kategoriDuzenle(self):
        item, okPressed = QInputDialog.getItem(self, "Kategori Düzenleme", "Düzenlenecek Kategori:", self.kategoriListesi, 0,
                                               False)
        if okPressed and item:
            if item != "Kategori Seçin":
                duzenlenmis, ok = QInputDialog.getText(self, "Kategori Düzenle", f"Düzenlenen Kategori:  {item}",
                                                       QLineEdit.Normal, "")
                if ok and item:
                    with conn:
                        cur = conn.cursor()
                        cur.execute("UPDATE GRUPLAR SET GRUP_ADI = (?) WHERE GRUP_ADI=(?)", [duzenlenmis, item])
                    self.kategoriListesi.remove(item)
                    self.kategoriListesi.append(duzenlenmis)
                    self.ui.comboBox.clear()
                    self.ui.comboBox.addItems(self.kategoriListesi)
                    self.ui.listWidget.clear()
                    self.ui.listWidget.addItems(self.kelimeListesi)
                    QMessageBox.information(self, "Düzenleme", "Kategori Düzenlendi")

    def yeniKategoriEkle(self):
        yeniKategori, okPressed = QInputDialog.getText(self, "Kategori Ekleme", "Yeni Kategori:", QLineEdit.Normal, "")
        if okPressed and yeniKategori != '':
            # kategoriler tablosuna yeni kategori eklenecek
            try:
                with conn:
                    cur = conn.cursor()
                    cur.execute("INSERT INTO GRUPLAR (GRUP_ADI) VALUES (?)",
                                [yeniKategori])
                print(yeniKategori)
                self.kategoriListesi.append(yeniKategori)
                self.ui.comboBox.clear()
                self.ui.comboBox.addItems(self.kategoriListesi)
                self.ui.listWidget.clear()
                self.ui.listWidget.addItems(self.kelimeListesi)
                QMessageBox.information(self, "Kategori Ekleme", "Yeni Kategori Eklendi")
            except Exception as e:
                print(e)

    def kategoriSil(self):
        item, okPressed = QInputDialog.getItem(self, "Kategori Silme İşlemi", "Silineek Kategoriyi Seçin:",
                                               self.kategoriListesi, 0, False)
        if okPressed and item:
            if item != "Kategori Seçin":
                try:
                    with conn:
                        cur = conn.cursor()
                        cur.execute("DELETE FROM GRUPLAR Where GRUP_ADI=(?)", [item])

                    self.kategoriListesi.remove(item)
                    self.ui.comboBox.clear()
                    self.ui.comboBox.addItems(self.kategoriListesi)
                    self.ui.listWidget.clear()
                    self.ui.listWidget.addItems(self.kelimeListesi)
                    QMessageBox.information(self, "Kategroi Silme", "Kategori Silindi")
                except Exception as e:
                    print(e)

    def comboBoxSecim(self):

        kategori = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        if (self.ui.comboBox.currentIndex() != 0):
            try:
                with conn:
                    cur = conn.cursor()
                    cur.execute("SELECT KELIME_ADI FROM WR_GRUP_KELIMELERI WHERE GRUP_ADI=(?)", [kategori])
                    sonuc = cur.fetchall()
                seciliListe = [item[0] for item in sonuc]
                self.ui.listWidget.clear()
                self.ui.listWidget.addItems(seciliListe)
            except Exception as e:
                print(e)

    def comboListeHazirla(self):
        self.ui.comboBox.addItems(self.kategoriListesi)

    def listeyiHazirla(self):
        self.ui.listWidget.addItems(self.kelimeListesi)

    def videoyuOynat(self, video):
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile(video)))
        self.mediaPlayer.play()

    def listedeKiElemanSecildi(self):
        d = self.ui.listWidget.currentItem()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT KELIME_YOLU FROM KELIMELER Where KELIME_ADI=(?)", [d.text()])
            sonuc = cur.fetchone()[0]
        print(sonuc)
        self.videoyuOynat(sonuc)

    def rastgeleSinav(self):
        pass

    def aramaMetniDegistir(self):
        self.ui.listWidget.clear()
        self.seciliListe.clear()
        aramaMetni = self.ui.lineEdit.text()
        for v in self.kelimeListesi:
            if v.startswith(buyukHarfeCevir(aramaMetni)):
                self.seciliListe.append(v)

        self.ui.listWidget.addItems(self.seciliListe)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
