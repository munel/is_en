
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import string
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QUrl, QModelIndex
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QInputDialog, QMainWindow, QLineEdit, QMessageBox,QWidget
from pathlib import Path
from entity import Kelime
from entity import Video
from entity import Kategori

from kelimeBLL import KelimeBLL
from videoBLL import VideoBLL
from kategoriBLL import KategoriBLL
from helper import Helper


class DuzenlenecekKelimeForm(QDialog):

    def __init__(self):
        self.duzenlenecekKelimObj = Kelime()
        self.duzenlenecekVideoObj = Video ()
        self.duzenlenecekKategoriObj = Kategori()

        self.seciliListe = []
        super(DuzenlenecekKelimeForm, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.kelimeDuzenleWidget = QWidget(self)
        self.kelimeDuzenleWidget.setGeometry(QtCore.QRect(10, 10, 751, 331))
        self.kelimeDuzenleWidget.setObjectName("kelimeDuzenleWidget")

        self.duzenlenecekKelimeText = QtWidgets.QLineEdit(self.kelimeDuzenleWidget)
        self.duzenlenecekKelimeText.setGeometry(QtCore.QRect(20, 20, 131, 20))
        self.duzenlenecekKelimeText.setToolTip("")
        self.duzenlenecekKelimeText.setObjectName("duzenlenecekKelimeText")

        self.labelyk = QtWidgets.QLabel(self.kelimeDuzenleWidget)
        self.labelyk.setGeometry(QtCore.QRect(10, 220, 131, 41))
        self.labelyk.setAlignment(QtCore.Qt.AlignCenter)
        self.labelyk.setWordWrap(True)
        self.labelyk.setObjectName("labelyk")

        self.listWidgetDuzenlenecekKelimeler = QtWidgets.QListWidget(self.kelimeDuzenleWidget)
        self.listWidgetDuzenlenecekKelimeler.setGeometry(QtCore.QRect(20, 50, 131, 171))
        self.listWidgetDuzenlenecekKelimeler.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidgetDuzenlenecekKelimeler.setObjectName("listWidgetDuzenlenecekKelimeler")
        self.listWidgetDuzenlenecekKelimeler.setSortingEnabled(True)

        self.pushButtonKelimeDuzenle = QtWidgets.QPushButton(self.kelimeDuzenleWidget)
        self.pushButtonKelimeDuzenle.setGeometry(QtCore.QRect(80, 280, 201, 41))
        self.pushButtonKelimeDuzenle.setObjectName("pushButtonKelimeDuzenle")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.kelimeDuzenleWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(350, 50, 381, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.layoutKelimeDuzenlne = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layoutKelimeDuzenlne.setContentsMargins(0, 0, 0, 0)
        self.layoutKelimeDuzenlne.setObjectName("layoutYeniKelime")

        self.labelyk_2 = QtWidgets.QLabel(self.kelimeDuzenleWidget)
        self.labelyk_2.setGeometry(QtCore.QRect(170, 220, 161, 41))
        self.labelyk_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelyk_2.setWordWrap(True)
        self.labelyk_2.setObjectName("labelyk_2")

        self.listWidgetYKategoriler = QtWidgets.QListWidget(self.kelimeDuzenleWidget)
        self.listWidgetYKategoriler.setGeometry(QtCore.QRect(170, 50, 161, 171))
        self.listWidgetYKategoriler.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidgetYKategoriler.setObjectName("listWidgetYKelime")
        self.listWidgetYKategoriler.setSortingEnabled(True)

        self.yeniKelimeEkleText = QtWidgets.QLineEdit(self.kelimeDuzenleWidget)
        self.yeniKelimeEkleText.setGeometry(QtCore.QRect(170, 20, 161, 20))
        self.yeniKelimeEkleText.setToolTip("")
        self.yeniKelimeEkleText.setObjectName("yeniKelimeEkleText")

        self.pushButtonYeniVideoSec = QtWidgets.QPushButton(self.kelimeDuzenleWidget)
        self.pushButtonYeniVideoSec.setGeometry(QtCore.QRect(350, 0, 151, 41))
        self.pushButtonYeniVideoSec.setObjectName("pushButtonYeniVideoSec")

        self.labelyk_3 = QtWidgets.QLabel(self.kelimeDuzenleWidget)
        self.labelyk_3.setGeometry(QtCore.QRect(510, 0, 151, 41))
        self.labelyk_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelyk_3.setWordWrap(True)
        self.labelyk_3.setObjectName("labelyk_3")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.layoutKelimeDuzenlne.addWidget(videoWidget)
        self.mediaPlayer.setVideoOutput(videoWidget)

        self.listeleriHazirla()
        self.listeyiHazirla()
        kategoriListesiTupple = KategoriBLL.KategorileriListele()
        self.kategoriListesi = [item[0] for item in kategoriListesiTupple]
        self.listWidgetYKategoriler.addItems(self.kategoriListesi)

        self.retranslateUi(self)
        self.actionsHazirla()



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kelime Düzenle"))
        self.duzenlenecekKelimeText.setPlaceholderText(_translate("Form", "Düzenlenecek kelime"))
        self.labelyk.setText(_translate("Form", "Düzenlenecek kelimeyi üstten seçmeniz gerekir."))
        self.pushButtonKelimeDuzenle.setText(_translate("Form", "Düzenle"))
        self.labelyk_2.setText(_translate("Form", "KategoriSeçin.\n"
" Birden Fazla Seçim Yapabilirsiniz. "))
        self.yeniKelimeEkleText.setPlaceholderText(_translate("Form", "Yeni Kelime"))
        self.pushButtonYeniVideoSec.setText(_translate("Form", "Kelime Yeni Video Seç"))
        self.labelyk_3.setText(_translate("Form", "Videoyu değiştirmek istiyorsanız yeni video seçiniz."))

    def actionsHazirla(self):
        self.pushButtonKelimeDuzenle.clicked.connect(self.kelimeDuzenle)
        self.duzenlenecekKelimeText.textChanged.connect(self.aramaMetniDegistir)
        self.listWidgetDuzenlenecekKelimeler.itemClicked.connect(self.KelimeListesindenSecimYapildi)
        self.listWidgetYKategoriler.itemSelectionChanged.connect(self.listeSecilenKategorileriAl)
        self.pushButtonYeniVideoSec.clicked.connect(self.videoSec)



    def aramaMetniDegistir(self):
        try:
            self.listWidgetDuzenlenecekKelimeler.clear()
            self.seciliListe.clear()
            aramaMetni = self.duzenlenecekKelimeText.text()
            for v in self.duzenlenecekKelimObj.kelimeler:
                if v.startswith(Helper.KucukHarfleriBuyukYap(aramaMetni)):
                    self.seciliListe.append(v)

            self.listWidgetDuzenlenecekKelimeler.addItems(self.seciliListe)
        except Exception as exp:
            print(exp)

    def videoyuOynat(self, video):
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile(video)))
        self.mediaPlayer.play()

    def KelimeListesindenSecimYapildi(self):
        try:

            self.duzenlenecekKelimObj.kelime = self.listWidgetDuzenlenecekKelimeler.currentItem().text()
            sonuc = KelimeBLL.KelimeVideoBul(self.duzenlenecekKelimObj)
            print("Listedeki eleman seçildi.----------------------------------")
            gruplarTuple = KategoriBLL.KelimeyeAitKategoriBul(self.duzenlenecekKelimObj)
            print("Listedeki elemana ait gruplar.----------------------------------")
            gruplar  = [item[0] for item in gruplarTuple]
            #print(gruplar)
            #print(self.kategoriListesi)
            sayi=0
            self.listWidgetYKategoriler.clear()
            print()
            while (sayi < len(self.kategoriListesi)):
                it = QtWidgets.QListWidgetItem(str(self.kategoriListesi[sayi]))
                self.listWidgetYKategoriler.addItem(it)
                if self.kategoriListesi[sayi] in gruplar:
                    it.setSelected(True)
                sayi +=1
        except Exception as exp:
            print(exp)


        if(sonuc==None):
            pass
        else:
            print(sonuc)
            self.duzenlenecekVideoObj.secilenKelimeVideoYol=sonuc
            self.videoyuOynat(self.duzenlenecekVideoObj.secilenKelimeVideoYol)
    def listeleriHazirla(self):
        kelimeListesiTupple  = KelimeBLL.KelimeleriListele()
        self.duzenlenecekKelimObj.kelimeler= [item[0] for item in kelimeListesiTupple]

    def listeyiHazirla(self):
        self.listWidgetDuzenlenecekKelimeler.clear()
        self.listWidgetDuzenlenecekKelimeler.addItems(self.duzenlenecekKelimObj.kelimeler)

    def listeSecilenKategorileriAl(self):
        try:

            sectim = self.listWidgetYKategoriler.selectedItems()
            self.duzenlenecekKategoriObj.duzenlenecekYeniKategoriler = [s.text() for s in sectim]
            print(self.duzenlenecekKategoriObj.duzenlenecekYeniKategoriler )
        except Exception as exp:
            print(exp)

    def videoSec(self):
        try:
            baslangicYol = str(Path.home()) + "\Desktop"
            orjinalYolu, _ = QFileDialog.getOpenFileName(self, "Video Seçiniz", baslangicYol, "Video dosyası (*.mp4);;Tüm dosyalar (*.*)")

            if orjinalYolu != '':

                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(orjinalYolu)))
                print("orjinalYolu")
                self.mediaPlayer.play()
                dosyaAdiHam = orjinalYolu.split("/")[-1]
                ad = ''.join([random.choice(string.ascii_letters
                                               ) for n in range(6)])
                print(ad)
                aduzanti = ad + "." + dosyaAdiHam.split(".")[-1]
                hedef = "VIDEOLAR/" + aduzanti

                self.duzenlenecekVideoObj.duzenlenecekVideoAdi = dosyaAdiHam
                self.duzenlenecekVideoObj.kaydedilecekVideoAdi = aduzanti
                self.duzenlenecekVideoObj.videoKaynakYol = orjinalYolu
                self.duzenlenecekVideoObj.videoHedefYol = hedef



        except Exception as exp:
            print(exp)


    def kelimeDuzenle(self):
        print("Düzenle Başladı")
        self.duzenlenecekKelimObj.duzenlenecekYeniKelime = Helper.KucukHarfleriBuyukYap(self.yeniKelimeEkleText.text())
        print("if çalışacak")
        if self.duzenlenecekKelimObj.duzenlenecekYeniKelime == "" or len(
                self.duzenlenecekKategoriObj.duzenlenecekYeniKategoriler) == 0:
            print("Boş Bırakıldı")
        else:
            print("Video BLL başlayacak")
            if (self.duzenlenecekVideoObj.duzenlenecekVideoAdi != ""):
                print("video Kopyala")
                sonucVideo = VideoBLL.VideoKopyala(self.duzenlenecekVideoObj)
                print(sonucVideo)

                sonucSilVideo = VideoBLL.VideoSil(self.duzenlenecekVideoObj)
                #sonuc 1 silindi, 0 silerken hata oldu, -1 video bulanamadı
                print("Video silindi.")
                print(sonucSilVideo)
                #Video silinemezse sonuç üzerinden işlem yapılabilir.
            else:
                print("yeni video seçilmedi")

            print("kelime güncellenecek.")
            KelimeBLL.KelimeVideoGuncelle(self.duzenlenecekKelimObj,self.duzenlenecekVideoObj)
            print(self.duzenlenecekKelimObj.kelimeId)

            KategoriBLL.KategoriKelimeIdGuncelle(self.duzenlenecekKelimObj, self.duzenlenecekKategoriObj)
            self.listeleriHazirla()
            self.listeyiHazirla()



