import sys

from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QInputDialog, QMainWindow, QLineEdit
from form1 import *
import sqlite3

conn = sqlite3.connect('Sozluk.db')
cur = conn.cursor()
cur.execute("SELECT KELIME_ADI FROM KELIMELER")
kelimeListesiTupple = cur.fetchall()
kelimeListesi = [item[0] for item in kelimeListesiTupple]
cur.execute("SELECT GRUP_ADI FROM GRUPLAR")
kategoriListesiTupple = cur.fetchall()
kategoriListesi = [item[0] for item in kategoriListesiTupple]
kategoriListesi.insert(0,"Kategori Seçin")

seciliListe = []
# kategoriListesi = ["Kategori Seçin", "Harfler", "Renkler", "Aylar", "Günler"]
# kelimeListesi = ["araba", "berbat", "deneme", "falanca", "istanbul", "python", "şeker", "ıspanak", "bilgisayar", "telefon",
#           "araba", "acaba", "akran", "çocuk", "bilgisayar", "resim", "seçim", "ülke"]


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
        self.ui.actionRastgele_S_nav_Yap.triggered.connect(self.rastgeleSinav)

        self.listeyiHazirla()
        self.comboListeHazirla()

        # Video Göstericinin Kodları. layout isimli bir widgeta ekleniyor.
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.ui.layout.addWidget(videoWidget)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile("2.mp4")))
        self.mediaPlayer.play()

        self.show()

    def kategoriDuzenle(self):
        item, okPressed = QInputDialog.getItem(self, "Kategori Düzenleme", "Düzenlenecek Kategori:", kategoriListesi, 0, False)
        if okPressed and item:
            if item != "Kategori Seçin":
                duzenlenmis, ok = QInputDialog.getText(self, "Kategori Düzenle", f"Düzenlenen Kategori:  {item}", QLineEdit.Normal, "")
                if ok and item:
                    with conn:
                        cur.execute("UPDATE GRUPLAR SET GRUP_ADI = (?) WHERE GRUP_ADI=(?)", [duzenlenmis, item])
                    kategoriListesi.remove(item)
                    kategoriListesi.append(duzenlenmis)
                    self.ui.comboBox.clear()
                    self.ui.comboBox.addItems(kategoriListesi)
                    self.ui.listWidget.clear()
                    self.ui.listWidget.addItems(kelimeListesi)




    def yeniKategoriEkle(self):
        yeniKategori, okPressed = QInputDialog.getText(self, "Kategori Ekleme", "Yeni Kategori:", QLineEdit.Normal, "")
        if okPressed and yeniKategori != '':
            # kategoriler tablosuna yeni kategori eklenecek
            try:
                with conn:
                    cur.execute("INSERT INTO GRUPLAR (GRUP_ADI) VALUES (?)",
                                [yeniKategori])
                print(yeniKategori)
                kategoriListesi.append(yeniKategori)
                self.ui.comboBox.clear()
                self.ui.comboBox.addItems(kategoriListesi)
                self.ui.listWidget.clear()
                self.ui.listWidget.addItems(kelimeListesi)
            except Exception as e:
                print(e)

    def kategoriSil(self):
        item, okPressed = QInputDialog.getItem(self, "Kategori Silme İşlemi", "Silineek Kategoriyi Silin:", kategoriListesi, 0, False)
        if okPressed and item:
            if item != "Kategori Seçin":
                try:
                    with conn:
                        cur.execute("DELETE FROM GRUPLAR Where GRUP_ADI=(?)", [item])

                    kategoriListesi.remove(item)
                    self.ui.comboBox.clear()
                    self.ui.comboBox.addItems(kategoriListesi)
                    self.ui.listWidget.clear()
                    self.ui.listWidget.addItems(kelimeListesi)
                except Exception as e:
                    print(e)



    def comboBoxSecim(self):

        kategori = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        if (self.ui.comboBox.currentIndex() != 0):
            try:
                cur.execute("SELECT KELIME_ADI FROM WR_GRUP_KELIMELERI WHERE GRUP_ADI=(?)", [kategori])
                sonuc = cur.fetchall()
                seciliListe = [item[0] for item in sonuc]
                self.ui.listWidget.clear()
                self.ui.listWidget.addItems(seciliListe)
            except Exception as e:
                print(e)

    def comboListeHazirla(self):
        self.ui.comboBox.addItems(kategoriListesi)

    def listeyiHazirla(self):
        self.ui.listWidget.addItems(kelimeListesi)

    def videoyuOynat(self, video):
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile(video)))
        self.mediaPlayer.play()

    def listedeKiElemanSecildi(self):
        d = self.ui.listWidget.currentItem()
        cur.execute("SELECT KELIME_YOLU FROM KELIMELER Where KELIME_ADI=(?)", [d.text()])
        sonuc = cur.fetchone()[0]
        print(sonuc)
        self.videoyuOynat(sonuc)

    def rastgeleSinav(self):
        pass

    def aramaMetniDegistir(self):
        self.ui.listWidget.clear()
        seciliListe.clear()
        aramaMetni = self.ui.lineEdit.text()
        for v in kelimeListesi:
            if v.startswith(aramaMetni.upper()):
                seciliListe.append(v)

        self.ui.listWidget.addItems(seciliListe)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
