from main import *
from random import seed
from random import randint
import sys
from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QInputDialog, QMainWindow, QLineEdit, QMessageBox
from kelimeislemleri import YeniKelimeEkle
from formSinav import *
import sqlite3

conn = sqlite3.connect('Sozluk.db')

def buyukHarfeCevir(metin):
    dizi = ["İ" if m=="i" else m.upper() for m in metin]
    return "".join(dizi)

class MyForm(QMainWindow):
    referansSayi = 0
    puan=0
    def __init__(self) -> MyForm:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.ui.layout.addWidget(videoWidget)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("VIDEOLAR/RAHAT.mp4")))
        self.mediaPlayer.play()
        self.listeHazirla()
        self.sayiUret()
        self.show()
        self.ui.startButton.clicked.connect(self.videoyuOynat)
        self.ui.sonraButon.clicked.connect(self.sonraki)
        self.ui.tahminButton.clicked.connect(self.tahmin)

        self.ui.pushButton_2.clicked.connect(self.cikis)


    def videoyuOynat(self):
        d = self.kelimeListesi[self.referansSayi]
        print(d)
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile("VIDEOLAR/{}.MP4".format(d))))
        self.mediaPlayer.play()



    def listeHazirla(self):
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT KELIME_ADI FROM KELIMELER")
            kelimeListesiTupple = cur.fetchall()
        self.kelimeListesi = [item[0] for item in kelimeListesiTupple]
        print(self.kelimeListesi)

    def sayiUret(self):
        i = int(len(self.kelimeListesi))
        value = randint(0,i)
        print(value)
        print(i)
        self.referansSayi = value
        print(self.referansSayi)

    def sonraki(self):
        self.sayiUret()
        self.videoyuOynat()

    def tahmin(self):
        yazi = buyukHarfeCevir(self.ui.lineEdit_2.text())
        print(yazi)
        d = self.kelimeListesi[self.referansSayi]
        if yazi == d:
            print("aferin")
            self.puan = self.puan +1
        print(self.puan)

        self.ui.label_Puan.setText(str(self.puan))

    def cikis(self):
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

