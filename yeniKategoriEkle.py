
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QWidget, QFileDialog
from PyQt5.QtCore import Qt
from entity import Kelime
from entity import Kategori
from kelimeBLL import KelimeBLL
from kategoriBLL import KategoriBLL

from helper import Helper


class YeniKategoriEkle(QDialog):

    def __init__(self):

        self.kelimeListesi=[]
        self.yeniKategori =Kategori()
        self.secilenKelimeler= Kelime()
        super(YeniKategoriEkle, self).__init__()
        self.setFixedSize(492, 556)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setupUi(self)

    def setupUi(self, DialogYeniKategoriEkle):

        qss = "sablon.qss"
        with open(qss, "r") as fh:
            self.setStyleSheet(fh.read())

        DialogYeniKategoriEkle.setObjectName("DialogYeniKategoriEkle")
        DialogYeniKategoriEkle.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogYeniKategoriEkle.resize(492, 556)
        DialogYeniKategoriEkle.setSizeGripEnabled(False)

        self.groupBox = QtWidgets.QGroupBox(DialogYeniKategoriEkle)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 251, 91))
        self.groupBox.setObjectName("groupBox")

        self.txtYeniKategoriAdi = QtWidgets.QLineEdit(self.groupBox)
        self.txtYeniKategoriAdi.setGeometry(QtCore.QRect(10, 30, 221, 41))
        self.txtYeniKategoriAdi.setObjectName("txtYeniKategoriAdi")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.txtYeniKategoriAdi.setFont(font)


        self.groupBox_2 = QtWidgets.QGroupBox(DialogYeniKategoriEkle)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 251, 391))
        self.groupBox_2.setObjectName("groupBox_2")

        self.listKelimeler = QtWidgets.QListWidget(self.groupBox_2)
        self.listKelimeler.setGeometry(QtCore.QRect(10, 20, 221, 351))
        self.listKelimeler.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.listKelimeler.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listKelimeler.setObjectName("listKelimeler")
        self.listKelimeler.setSortingEnabled(True)

        self.btnKategoriEkle = QtWidgets.QCommandLinkButton(DialogYeniKategoriEkle)
        self.btnKategoriEkle.setGeometry(QtCore.QRect(280, 70, 181, 51))
        self.btnKategoriEkle.setObjectName("btnKategoriEkle")

        self.label = QtWidgets.QLabel(DialogYeniKategoriEkle)
        self.label.setGeometry(QtCore.QRect(170, 0, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.groupBox_3 = QtWidgets.QGroupBox(DialogYeniKategoriEkle)
        self.groupBox_3.setGeometry(QtCore.QRect(280, 150, 191, 391))
        self.groupBox_3.setObjectName("groupBox_3")
        self.listSecilenKelimeler = QtWidgets.QListWidget(self.groupBox_3)
        self.listSecilenKelimeler.setGeometry(QtCore.QRect(10, 20, 161, 351))
        self.listSecilenKelimeler.setObjectName("listSecilenKelimeler")
        self.listSecilenKelimeler.setSortingEnabled(True)

        self.retranslateUi(DialogYeniKategoriEkle)
        QtCore.QMetaObject.connectSlotsByName(DialogYeniKategoriEkle)

        self.actionsHazirla()
        self.listeleriHazirla()
        self.listeyiHazirla()

    def retranslateUi(self, DialogYeniKategoriEkle):
        _translate = QtCore.QCoreApplication.translate
        DialogYeniKategoriEkle.setWindowTitle(_translate("DialogYeniKategoriEkle", "Yeni Kategori Ekle"))
        self.groupBox.setTitle(_translate("DialogYeniKategoriEkle", "Yeni Kategori Adı"))
        self.groupBox_2.setTitle(
            _translate("DialogYeniKategoriEkle", "Yeni Kategoriye Dahil Olacak Kelimeleri Seçiniz"))
        self.btnKategoriEkle.setText(_translate("DialogYeniKategoriEkle", "Kategoriyi Ekle"))
        self.label.setText(_translate("DialogYeniKategoriEkle", "Yeni Kategori Ekle"))
        self.groupBox_3.setTitle(_translate("DialogYeniKategoriEkle", "Seçilen Kelimeler"))



    def actionsHazirla(self):
        self.btnKategoriEkle.clicked.connect(self.KelimeEkle)
        self.listKelimeler.itemSelectionChanged.connect(self.listedenSecilenKelimeleriAl)




    def KelimeEkle(self):
        yazilanYeniKategori = self.txtYeniKategoriAdi.text()
        self.yeniKategori.kategori = Helper.KucukHarfleriBuyukYap(yazilanYeniKategori)
        print(self.yeniKategori.kategori)

        if self.yeniKategori.kategori != '':
            # kategoriler tablosuna yeni kategori eklenecek

            if len(self.secilenKelimeler.kelimeler) == 0:
                self.eklendiMi = KategoriBLL.KategoriEkleSadece(self.yeniKategori)
            else:
                self.eklendiMi = KategoriBLL.KategoriEkleKelimeAta(self.yeniKategori, self.secilenKelimeler)



            if (self.eklendiMi):
                print("Kategori eklendi.")
                self.done(1)
            else:
                self.done(-1)



    def listeleriHazirla(self):
        try:
            kelimeListesiTupple = KelimeBLL.KelimeleriListele()
            self.kelimeListesi = [item[0] for item in kelimeListesiTupple]

        except Exception as exp:
            print(exp)

    def listeyiHazirla(self):
        self.listKelimeler.clear()
        self.listKelimeler.addItems(self.kelimeListesi)


    def listedenSecilenKelimeleriAl(self):
        sectim = self.listKelimeler.selectedItems()
        self.secilenKelimeler.kelimeler= [s.text() for s in sectim]
        self.listSecilenKelimeler.clear()
        self.listSecilenKelimeler.addItems(self.secilenKelimeler.kelimeler)
        print(self.secilenKelimeler.kelimeler)
