import random

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QDialog, QWidget, QFileDialog

import sqlite3
import shutil
import string
conn = sqlite3.connect('Sozluk.db')



class YeniKelimeEkle(QDialog):
    def __init__(self):
        super(YeniKelimeEkle, self).__init__()
        self.setWindowTitle("Yeni Kelime Ekle")
        self.setFixedSize(400, 300)
        self.secilenler = []
        self.kelime = ""
        self.orjinalYol = ""
        self.hedef = ""
        self.uiHazirla()

    def uiHazirla(self):
        self.yeniKelimeWidget = QWidget(self)
        self.yeniKelimeWidget.setObjectName("yeniKelimeWidget")
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

        with conn:
            cur = conn.cursor()
            cur.execute("SELECT GRUP_ADI FROM GRUPLAR")
            kategoriListesiTupple = cur.fetchall()
            self.kategoriListesi = [item[0] for item in kategoriListesiTupple]
        self.listWidgetYKelime.addItems(self.kategoriListesi)



    def actionsHazirla(self):
        self.pushButtonYKKaydet.clicked.connect(self.yeniKelimeyiKaydetFonk)
        self.listWidgetYKelime.itemSelectionChanged.connect(self.listedenSecimleriAyarlar)
        self.pushButtonYKVideoEkle.clicked.connect(self.videoSec)

    def videoSec(self):
        self.orjinalYol, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if self.orjinalYol != '':

            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.orjinalYol)))
            self.mediaPlayer.play()
            dosyaAdiHam = self.orjinalYol.split("/")[-1]
            ad = ''.join([random.choice(string.ascii_letters
                                           ) for n in range(6)])
            print(ad)
            aduzanti = ad + "." + dosyaAdiHam.split(".")[-1]
            self.hedef = "VIDEOLAR/" + aduzanti
   



    def yeniKelimeyiKaydetFonk(self):
        self.kelime = self.yeniKelimeEkleText.text()
        if self.kelime == "" or len(self.secilenler)==0 or self.orjinalYol == "":
            print("Boş Bırakıldı")
        else:
            shutil.copy(self.orjinalYol, self.hedef)
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO KELIMELER (KELIME_ADI,KELIME_YOLU) VALUES(?,?)",[self.kelime.upper(),self.hedef])
                kelimeId = cur.lastrowid
                for g in self.secilenler:
                    cur.execute("SELECT ID FROM GRUPLAR WHERE GRUP_ADI=(?)",[g])
                    idH = cur.fetchone()
                    groupId = idH[0]
                    cur.execute("INSERT INTO GRUP_KELIMELERI (GRUP_ID,KELIME_ID) VALUES(?,?)",[groupId,kelimeId])
                self.done(1)





    def listedenSecimleriAyarlar(self):
        sectim = self.listWidgetYKelime.selectedItems()
        self.secilenler = [s.text() for s in sectim]
        print(self.secilenler)



