# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Salih\Desktop\Python Eğitici Eğitimi\Proje\munel\is_en\ui\kategoriDuzenle.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtWidgets import QDialog, QWidget, QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from helper import Helper
from entity import Kelime
from entity import Kategori
from kelimeBLL import KelimeBLL
from kategoriBLL import KategoriBLL

class KategoriDuzenle(QDialog):

    def __init__(self):

        self.kategoriListesi=[]
        self.seciliKategoriyeAitKelimelerListesi = []
        self.duzenlenecekKategori =Kategori()
        self.secilenKelimeler= Kelime()
        super(KategoriDuzenle, self).__init__()
        self.setFixedSize(464, 327)
        self.setupUi(self)

    def setupUi(self, formKategoriDuzenle):
        formKategoriDuzenle.setObjectName("formKategoriDuzenle")
        self.label = QtWidgets.QLabel(formKategoriDuzenle)
        self.label.setGeometry(QtCore.QRect(80, 0, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.grboxKategoriler = QtWidgets.QGroupBox(formKategoriDuzenle)
        self.grboxKategoriler.setGeometry(QtCore.QRect(10, 30, 261, 201))
        self.grboxKategoriler.setObjectName("grboxKategoriler")
        self.listKategoriler = QtWidgets.QListWidget(self.grboxKategoriler)
        self.listKategoriler.setGeometry(QtCore.QRect(10, 20, 241, 171))
        self.listKategoriler.setObjectName("listKategoriler")
        self.grboxYeniKategoriAdi = QtWidgets.QGroupBox(formKategoriDuzenle)
        self.grboxYeniKategoriAdi.setGeometry(QtCore.QRect(10, 230, 261, 91))
        self.grboxYeniKategoriAdi.setObjectName("grboxYeniKategoriAdi")
        self.txtYeniKategoriAdi = QtWidgets.QLineEdit(self.grboxYeniKategoriAdi)
        self.txtYeniKategoriAdi.setGeometry(QtCore.QRect(10, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.txtYeniKategoriAdi.setFont(font)
        self.txtYeniKategoriAdi.setObjectName("txtYeniKategoriAdi")
        self.chbKelimelerAcilsinMi = QtWidgets.QCheckBox(self.grboxYeniKategoriAdi)
        self.chbKelimelerAcilsinMi.setGeometry(QtCore.QRect(20, 60, 211, 17))
        self.chbKelimelerAcilsinMi.setObjectName("chbKelimelerAcilsinMi")
        self.verticalLayoutWidget = QtWidgets.QWidget(formKategoriDuzenle)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 40, 171, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.listKelimeler = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listKelimeler.setInputMethodHints(QtCore.Qt.ImhNone)
        self.listKelimeler.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listKelimeler.setObjectName("listKelimeler")
        self.listKelimeler.setVisible(False)
        self.verticalLayout.addWidget(self.listKelimeler)

        self.btnDuzenle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDuzenle.sizePolicy().hasHeightForWidth())
        self.btnDuzenle.setSizePolicy(sizePolicy)
        self.btnDuzenle.setMinimumSize(QtCore.QSize(0, 50))
        self.btnDuzenle.setObjectName("btnDuzenle")
        self.verticalLayout.addWidget(self.btnDuzenle)

        self.retranslateUi(formKategoriDuzenle)
        QtCore.QMetaObject.connectSlotsByName(formKategoriDuzenle)

        self.actionsHazirla()
        self.listeleriHazirla()
        self.listeyiHazirla()



    def retranslateUi(self, formKategoriDuzenle):
        _translate = QtCore.QCoreApplication.translate
        formKategoriDuzenle.setWindowTitle(_translate("formKategoriDuzenle", "Kategori Düzenleme"))
        self.label.setText(_translate("formKategoriDuzenle", "Kategori Düzenleme Modülü"))
        self.grboxKategoriler.setTitle(_translate("formKategoriDuzenle", "Kategoriler"))
        self.listKategoriler.setSortingEnabled(True)
        self.grboxYeniKategoriAdi.setTitle(_translate("formKategoriDuzenle", "Yeni Kategori Adı"))
        self.chbKelimelerAcilsinMi.setText(_translate("formKategoriDuzenle", "Kelimeleri Düzenlemek İstiyor musunuz?"))
        self.listKelimeler.setSortingEnabled(True)
        self.btnDuzenle.setText(_translate("formKategoriDuzenle", "Düzenle"))


    def actionsHazirla(self):

        self.listKategoriler.itemSelectionChanged.connect(self.listedenSecilenKategoriyiAl)
        self.listKelimeler.itemSelectionChanged.connect(self.secilenKelimeleriAl)
        self.chbKelimelerAcilsinMi.toggled.connect(self.KelimelerListesiniAc)
        self.btnDuzenle.clicked.connect(self.KategoriDuzenle)


    def listeleriHazirla(self):
        try:
            kategoriListesi = KategoriBLL.KategorileriListele()
            self.duzenlenecekKategori.kategoriler = [item[0] for item in kategoriListesi]
            print(self.duzenlenecekKategori.kategoriler)
        except Exception as exp:
            print(exp)

    def listeyiHazirla(self):
        self.listKelimeler.clear()
        self.listKategoriler.clear()
        self.listKategoriler.addItems(self.duzenlenecekKategori.kategoriler)


    def listedenSecilenKategoriyiAl(self):
        try:
            print(self.listKategoriler.selectedItems())
            secim = self.listKategoriler.selectedItems()[0].text()
            self.duzenlenecekKategori.kategori=secim
            self.txtYeniKategoriAdi.setText(secim)

            if self.chbKelimelerAcilsinMi.isChecked():

                self.KategoriyeAitKelimeleriListele()
                self.listKelimeler.setVisible(True)
        except Exception as exp:
            print(exp)

    def KategoriDuzenle(self):
        yeniKategori = Kategori()
        yeniKategori.kategori = Helper.KucukHarfleriBuyukYap( self.txtYeniKategoriAdi.text())
        guncellendiMi=False
        if self.chbKelimelerAcilsinMi.isChecked():
            print("Kategori adı ve kelime listesi güncellenecek")

            if set(self.secilenKelimeler.kelimeler) != set(self.seciliKategoriyeAitKelimelerListesi):
                guncellendiMi = KategoriBLL.KategoriIdKelimeGuncelle(self.secilenKelimeler, self.duzenlenecekKategori, yeniKategori)
            else:
                guncellendiMi = KategoriBLL.KategoriDuzenle(self.duzenlenecekKategori, yeniKategori)

        else:
            print("Sadece Kategori Adı güncellenecek")
            guncellendiMi = KategoriBLL.KategoriDuzenle(self.duzenlenecekKategori, yeniKategori)
        if guncellendiMi:
            print("Güncellendi.")
            self.done(1)
        else:
            print("Güncellenemedi.")
            self.done(-1)





    def KelimelerListesiniAc(self):
        if self.chbKelimelerAcilsinMi.isChecked():
            print("Listeyi Aç")
            self.KategoriyeAitKelimeleriListele()
            self.listKelimeler.setVisible(True)
        else:
            print("listeyi kapat")
            self.listKelimeler.setVisible(False)

    def KategoriyeAitKelimeleriListele(self):
        print(self.duzenlenecekKategori.kategori)
        self.seciliKategoriyeAitKelimelerListesi = KategoriBLL.KategoriyeAitKelimeler(self.duzenlenecekKategori)
        tumKelimeler = []
        kelimeListesiTupple = KelimeBLL.KelimeleriListele()
        tumKelimeler = [kelime[0] for kelime in kelimeListesiTupple]
        print(tumKelimeler)
        self.listKelimeler.clear()


        sayi = 0

        while (sayi < len(tumKelimeler)):
            it = QtWidgets.QListWidgetItem(str(tumKelimeler[sayi]))
            self.listKelimeler.addItem(it)
            if tumKelimeler[sayi] in self.seciliKategoriyeAitKelimelerListesi:
                it.setSelected(True)
            sayi += 1


    def secilenKelimeleriAl(self):
        try:
            listedenSecilenKelimeler = self.listKelimeler.selectedItems()

            self.secilenKelimeler.kelimeler = [kelime.text() for kelime in listedenSecilenKelimeler]
            print("seçilen keliemler")
            print(self.secilenKelimeler.kelimeler )
        except Exception as exp:
            print(exp)
