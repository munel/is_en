import sqlite3
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from random import randint
from kisacevap import *
from PyQt5.QtCore import Qt
conn = sqlite3.connect('Sozluk.db')

def buyukHarfeCevir(metin):
    dizi = ["İ" if m=="i" else m.upper() for m in metin]
    return "".join(dizi)

class KisaCevapFrom(QDialog):
    referansSayi = 0 # kelimeler listesinde istenlen kelimenin indsi için
    puan=0  # doğru cevap sayısını bulmak için
    yanlisSayisi = 0 # yanlış cevap sayısını bulmak için
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(662, 348)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget(self)
        self.ui.layout.addWidget(videoWidget)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("VIDEOLAR/RAHAT.mp4")))
        self.mediaPlayer.play()

        self.listeHazirla()
        self.sayiUret()

        self.ui.sonraButon.clicked.connect(self.sonraki)
        self.ui.tahminButton.clicked.connect(self.tahmin)
        self.videoyuOynat()
        self.show()
        self.exec_()


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
        if self.ui.lineEdit_2.text()=="":
            d = self.kelimeListesi[self.referansSayi]
            self.ui.listWidget.addItem("      / {} ".format(d))
        self.sayiUret()
        self.videoyuOynat()
        
    def tahmin(self):
        yazi = buyukHarfeCevir(self.ui.lineEdit_2.text())
        print(yazi)
        d = self.kelimeListesi[self.referansSayi]
        if yazi == d:
            print("aferin")
            self.puan = self.puan +1
            self.ui.listWidget.addItem("{} / {} ".format(yazi, d))
        else:
            self.ui.listWidget.addItem("{} / {} ".format(yazi,d))
            print("yanlış cevap") #yanlış cevap verilirse
            self.yanlisSayisi +=1

        print("Doğru Cevap Sayısı = {} / Yanlış Cevap Sayısı = {}".format(self.puan,self.yanlisSayisi))
        self.sonraki()
        # tahmin doğru olsa da yanlış olsa da yeni kelime üretiyoruz
        self.ui.label_Puan.setText(str(self.puan))
        self.ui.label_Yanlis.setText(str(self.yanlisSayisi))
        self.ui.lineEdit_2.setText("")

    def videoyuOynat(self):
        d = self.kelimeListesi[self.referansSayi]
        print(d)
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile("VIDEOLAR/{}.MP4".format(d))))
        self.mediaPlayer.play()



