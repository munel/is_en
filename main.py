import sys

from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QInputDialog, QMainWindow, QLineEdit
from form1 import *

seciliListe = []
kategoriListesi = ["Kategori Seçin", "Harfler", "Renkler", "Aylar", "Günler"]
listem = ["araba", "berbat", "deneme", "falanca", "istanbul", "python", "şeker", "ıspanak", "bilgisayar", "telefon",
          "araba", "acaba", "akran", "çocuk", "bilgisayar", "resim", "seçim", "ülke"]


class Kelime:
    def __init__(self, kelime="", video=""):
        self.kelime = kelime
        self.video = video

    def getKelime(self):
        return self.kelime

    def getVideoName(self):
        return self.video


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
                    # Kategoriler tablosunda düzenleme yapılacak
                    pass



    def yeniKategoriEkle(self):
        yeniKategori, okPressed = QInputDialog.getText(self, "Kategori Ekleme", "Yeni Kategori:", QLineEdit.Normal, "")
        if okPressed and yeniKategori != '':
            # kategoriler tablosuna yeni kategori eklenecek
            kategoriListesi.append(yeniKategori)
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(kategoriListesi)

    def kategoriSil(self):
        item, okPressed = QInputDialog.getItem(self, "Kategori Silme İşlemi", "Silineek Kategoriyi Silin:", kategoriListesi, 0, False)
        if okPressed and item:
            if item != "Kategori Seçin":
                # Kategori tablosundan veri silinecek
                kategoriListesi.remove(item)
                self.ui.comboBox.clear()
                self.ui.comboBox.addItems(kategoriListesi)



    def comboBoxSecim(self):

        kategori = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        if (self.ui.comboBox.currentIndex() != 0):
            print(kategori)

    def comboListeHazirla(self):
        self.ui.comboBox.addItems(kategoriListesi)

    def listeyiHazirla(self):
        self.ui.listWidget.addItems(listem)

    def videoyuOynat(self, video):
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile(video)))
        self.mediaPlayer.play()

    def listedeKiElemanSecildi(self):
        d = self.ui.listWidget.currentItem()

    def rastgeleSinav(self):
        pass

    def aramaMetniDegistir(self):
        self.ui.listWidget.clear()
        seciliListe.clear()
        aramaMetni = self.ui.lineEdit.text()
        for v in listem:
            if v.startswith(aramaMetni):
                seciliListe.append(v)

        self.ui.listWidget.addItems(seciliListe)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
