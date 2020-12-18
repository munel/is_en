
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QInputDialog, QMainWindow, QLineEdit, QMessageBox,QWidget
from PyQt5.QtCore import Qt
from entity import Kelime
from entity import Video
from kelimeBLL import KelimeBLL
from helper import Helper

class SilinecekKelimeForm(QDialog):

    def __init__(self):
        self.silienecekKelimObj= Kelime ()
        self.silinecekVideoObj=Video ()
        self.seciliListe =[]
        super(SilinecekKelimeForm, self).__init__()
        self.setWindowTitle("Kelime Silme")
        self.setFixedSize(400, 300)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setupUi()

    def setupUi(self):

        self.kelimeSilWidget = QWidget(self)
        self.kelimeSilWidget.setGeometry(QtCore.QRect(10, 0, 381, 281))
        self.kelimeSilWidget.setObjectName("kelimeSilWidget")

        qss = "sablon.qss"
        with open(qss, "r") as fh:
            self.setStyleSheet(fh.read())

        self.silinecekKelimeText = QtWidgets.QLineEdit(self.kelimeSilWidget)
        self.silinecekKelimeText.setGeometry(QtCore.QRect(20, 20, 131, 20))
        self.silinecekKelimeText.setToolTip("")
        self.silinecekKelimeText.setObjectName("silinecekKelimeText")

        self.labelyk = QtWidgets.QLabel(self.kelimeSilWidget)
        self.labelyk.setGeometry(QtCore.QRect(20, 220, 131, 41))
        self.labelyk.setAlignment(QtCore.Qt.AlignCenter)
        self.labelyk.setWordWrap(True)
        self.labelyk.setObjectName("labelyk")

        self.listWidgetSilenecekKelimeler = QtWidgets.QListWidget(self.kelimeSilWidget)
        self.listWidgetSilenecekKelimeler.setGeometry(QtCore.QRect(20, 50, 131, 171))
        self.listWidgetSilenecekKelimeler.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidgetSilenecekKelimeler.setSortingEnabled(True)
        self.listWidgetSilenecekKelimeler.setObjectName("listWidgetSilenecekKelimeler")

        self.pushButtonKelimeSil = QtWidgets.QPushButton(self.kelimeSilWidget)
        self.pushButtonKelimeSil.setGeometry(QtCore.QRect(160, 230, 201, 41))
        self.pushButtonKelimeSil.setObjectName("pushButtonKelimeSil")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.kelimeSilWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 20, 211, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.layoutKelimeSil = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layoutKelimeSil.setContentsMargins(0, 0, 0, 0)
        self.layoutKelimeSil.setObjectName("layoutYeniKelime")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()

        self.layoutKelimeSil.addWidget(videoWidget)
        self.mediaPlayer.setVideoOutput(videoWidget)

        self.listeleriHazirla()
        self.listeyiHazirla()
        self.retranslateUi(self)

        self.actionsHazirla()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kelime Sil"))
        self.silinecekKelimeText.setPlaceholderText(_translate("Dialog", "Silinecek kelime"))
        self.labelyk.setText(_translate("Dialog", "Silinecek kelimeyi üstten seçmeniz gerekir."))
        self.pushButtonKelimeSil.setText(_translate("Dialog", "Sil"))


    def actionsHazirla(self):
        self.pushButtonKelimeSil.clicked.connect(self.kelimeSil)
        self.silinecekKelimeText.textChanged.connect(self.aramaMetniDegistir)
        self.listWidgetSilenecekKelimeler.itemClicked.connect(self.listedeKiElemanSecildi)


    def kelimeSil(self):
        print(self.silienecekKelimObj.kelime)
        sonuc = KelimeBLL.KelimeSil(self.silienecekKelimObj,self.silinecekVideoObj)
        if(sonuc):
            QMessageBox.information(self, "Kelime Silme", "Kelime silindi")
            self.listeleriHazirla();
            self.listeyiHazirla()
            self.videoyuOynat(None)
        else:
            QMessageBox.information(self, "Kelime Silme", "Kelime silinmedi")
        self.listeleriHazirla()
        self.listeyiHazirla()

    def listeleriHazirla(self):
        kelimeListesiTupple  = KelimeBLL.KelimeleriListele()
        self.silienecekKelimObj.kelimeler= [item[0] for item in kelimeListesiTupple]

    def listeyiHazirla(self):
        self.listWidgetSilenecekKelimeler.clear()
        self.listWidgetSilenecekKelimeler.addItems(self.silienecekKelimObj.kelimeler)

    def listedenSecimleriAyarlar(self):
        self.silienecekKelimObj.kelime = self.listWidgetYKelime.selectedItems()

    def videoyuOynat(self, video):
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile(video)))
        self.mediaPlayer.play()

    def listedeKiElemanSecildi(self):
        self.silienecekKelimObj.kelime = self.listWidgetSilenecekKelimeler.currentItem().text()
        sonuc = KelimeBLL.KelimeVideoBul(self.silienecekKelimObj)
        if(sonuc==None):
            pass
        else:
            self.silinecekVideoObj.videoHedefYol=sonuc
            self.videoyuOynat(self.silinecekVideoObj.videoHedefYol)

    def aramaMetniDegistir(self):
        self.listWidgetSilenecekKelimeler.clear()
        self.seciliListe.clear()
        aramaMetni = self.silinecekKelimeText.text()
        for v in self.silienecekKelimObj.kelimeler:
            if v.startswith(Helper.KucukHarfleriBuyukYap(aramaMetni)):
                self.seciliListe.append(v)

        self.listWidgetSilenecekKelimeler.addItems(self.seciliListe)
