import random

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QDialog, QWidget, QFileDialog
from pathlib import Path
import sqlite3

import string

conn = sqlite3.connect('Sozluk.db')
from entity import Kelime
from entity import Video
from entity import Kategori
from kelimeBLL import KelimeBLL
from kategoriBLL import KategoriBLL
from videoBLL import VideoBLL
from helper import Helper

class YeniKelimeEkle(QDialog):
    def __init__(self):
        self.yeniKelimObj= Kelime()
        self.yeniVideoObj=Video()
        self.yeniKategoriObj = Kategori()
        super(YeniKelimeEkle, self).__init__()
        self.setWindowTitle("Yeni Kelime Ekle")
        self.setFixedSize(400, 300)
        self.uiHazirla()

    def uiHazirla(self):
        self.yeniKelimeWidget = QWidget(self)
        self.yeniKelimeWidget.setObjectName("yeniKelimeWidget")

        qss = "sablon.qss"
        with open(qss, "r") as fh:
            self.setStyleSheet(fh.read())



        self.yeniKelimeEkleText = QtWidgets.QLineEdit(self.yeniKelimeWidget)
        self.yeniKelimeEkleText.setGeometry(QtCore.QRect(10, 20, 131, 20))
        self.yeniKelimeEkleText.setToolTip("")
        self.yeniKelimeEkleText.setObjectName("yeniKelimeEkleText")

        self.labelyk = QtWidgets.QLabel(self.yeniKelimeWidget)
        self.labelyk.setGeometry(QtCore.QRect(10, 56, 131, 41))
        self.labelyk.setAlignment(QtCore.Qt.AlignCenter)
        self.labelyk.setWordWrap(True)
        self.labelyk.setObjectName("labelyk")

        self.listWidgetYKelime = QtWidgets.QListWidget(self.yeniKelimeWidget)
        self.listWidgetYKelime.setGeometry(QtCore.QRect(10, 100, 131, 171))
        self.listWidgetYKelime.setObjectName("listWidgetYKelime")
        self.listWidgetYKelime.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidgetYKelime.setSortingEnabled(True)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.yeniKelimeWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(159, 99, 211, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.layoutYeniKelime = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layoutYeniKelime.setContentsMargins(0, 0, 0, 0)
        self.layoutYeniKelime.setObjectName("layoutYeniKelime")

        self.pushButtonYKKaydet = QtWidgets.QPushButton(self.yeniKelimeWidget)
        self.pushButtonYKKaydet.setGeometry(QtCore.QRect(210, 20, 111, 41))
        self.pushButtonYKKaydet.setObjectName("pushButtonYKKaydet")

        self.pushButtonYKVideoEkle = QtWidgets.QPushButton(self.yeniKelimeWidget)
        self.pushButtonYKVideoEkle.setGeometry(QtCore.QRect(200, 250, 131, 23))
        self.pushButtonYKVideoEkle.setObjectName("pushButtonYKVideoEkle")
        self.yeniKelimeEkleText.setPlaceholderText("YeniKelime")

        self.labelyk.setText("Kategori Seçin.\n"
                                                  " Birden Fazla Seçim Yapabilirsiniz. ")
        self.pushButtonYKKaydet.setText("Kaydet")
        self.pushButtonYKVideoEkle.setText("Kelime Video Seç")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.layoutYeniKelime.addWidget(videoWidget)
        self.mediaPlayer.setVideoOutput(videoWidget)


        self.actionsHazirla()


        kategoriListesiTupple = KategoriBLL.KategorileriListele()
        self.kategoriListesi = [item[0] for item in kategoriListesiTupple]
        self.listWidgetYKelime.addItems(self.kategoriListesi)



    def actionsHazirla(self):
        self.pushButtonYKKaydet.clicked.connect(self.yeniKelimeyiKaydetFonk)
        self.listWidgetYKelime.itemSelectionChanged.connect(self.listedenSecimleriAyarlar)
        self.pushButtonYKVideoEkle.clicked.connect(self.videoSec)

    def videoSec(self):
        baslangicYol = str(Path.home()) + "\Desktop"
        self.orjinalYol, _ = QFileDialog.getOpenFileName(self, "Video Seçiniz", baslangicYol, "Video dosyası (*.mp4);;Tüm dosyalar (*.*)")
        if self.orjinalYol != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.orjinalYol)))
            self.mediaPlayer.play()
            dosyaAdiHam = self.orjinalYol.split("/")[-1]
            ad = ''.join([random.choice(string.ascii_letters
                                           ) for n in range(6)])
            print(ad)
            aduzanti = ad + "." + dosyaAdiHam.split(".")[-1]
            self.hedef = "VIDEOLAR/" + aduzanti

            self.yeniVideoObj.secilenvideoAdi = dosyaAdiHam
            self.yeniVideoObj.kaydedilecekVideoAdi = aduzanti
            self.yeniVideoObj.videoKaynakYol = self.orjinalYol
            self.yeniVideoObj.videoHedefYol = self.hedef



    def yeniKelimeyiKaydetFonk(self):
        print("Kaydet Başladı")
        self.yeniKelimObj.kelime=Helper.KucukHarfleriBuyukYap(self.yeniKelimeEkleText.text())
        print("if çalışacak")
        if self.yeniKelimObj.kelime == "" or len(self.yeniKategoriObj.kategoriler)==0 or self.yeniVideoObj.videoKaynakYol == "":
            print("Boş Bırakıldı")
        else:
            print("Video BLL başlayacak")
            sonucVideo = VideoBLL.VideoKopyala(self.yeniVideoObj)
            print("Kelime BLL başlayacak")
            eklenenKayitId = KelimeBLL.YeniKelimeEkle(self.yeniKelimObj,self.yeniVideoObj)
            print("Kategori BLL başlayacak")

            sonucKategori =KategoriBLL.KategoriKelimeIdEkle(eklenenKayitId,self.yeniKategoriObj)

            if (sonucVideo and sonucKategori and eklenenKayitId!=-1) :
                print("self done 1")
                self.done(1)
            else:
                print("self done 0")
                print(sonucVideo)
                print(eklenenKayitId)
                print(sonucKategori)
                self.done(-1)


    def listedenSecimleriAyarlar(self):
        sectim = self.listWidgetYKelime.selectedItems()
        self.yeniKategoriObj.kategoriler = [s.text() for s in sectim]
        print(self.yeniKategoriObj.kategoriler)



