# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Salih\Desktop\Python Eğitici Eğitimi\Proje\munel\is_en\ui\kategoriSil.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtWidgets import QDialog, QWidget, QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from entity import Kelime
from entity import Kategori
from kelimeBLL import KelimeBLL
from kategoriBLL import KategoriBLL

class KategoriSil(QDialog):
    def __init__(self):
        self.kategoriListesi = []
        self.seciliKategoriyeAitKelimelerListesi = []
        self.silinecekKategori = Kategori()
        self.secilenKelimeler = Kelime()
        super(KategoriSil, self).__init__()
        self.setFixedSize(521, 408)
        self.setupUi(self)

    def setupUi(self, formKategoriSil):
        formKategoriSil.setObjectName("formKategoriSil")
        self.lblKategoriSil = QtWidgets.QLabel(formKategoriSil)
        self.lblKategoriSil.setGeometry(QtCore.QRect(190, 0, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblKategoriSil.setFont(font)
        self.lblKategoriSil.setObjectName("lblKategoriSil")
        self.btnKategoriSil = QtWidgets.QPushButton(formKategoriSil)
        self.btnKategoriSil.setGeometry(QtCore.QRect(40, 50, 181, 41))
        self.btnKategoriSil.setObjectName("btnKategoriSil")
        self.grboxKategoriler = QtWidgets.QGroupBox(formKategoriSil)
        self.grboxKategoriler.setGeometry(QtCore.QRect(10, 100, 251, 301))
        self.grboxKategoriler.setObjectName("grboxKategoriler")
        self.listKategoriler = QtWidgets.QListWidget(self.grboxKategoriler)
        self.listKategoriler.setGeometry(QtCore.QRect(10, 20, 231, 271))
        self.listKategoriler.setObjectName("listKategoriler")
        self.grpboxKelimeler = QtWidgets.QGroupBox(formKategoriSil)
        self.grpboxKelimeler.setGeometry(QtCore.QRect(270, 40, 241, 361))
        self.grpboxKelimeler.setObjectName("grpboxKelimeler")
        self.listKelimeler = QtWidgets.QListWidget(self.grpboxKelimeler)
        self.listKelimeler.setGeometry(QtCore.QRect(10, 20, 221, 331))
        self.listKelimeler.setObjectName("listKelimeler")

        self.retranslateUi(formKategoriSil)
        QtCore.QMetaObject.connectSlotsByName(formKategoriSil)

        self.actionsHazirla()
        self.listeleriHazirla()
        self.listeyiHazirla()



    def retranslateUi(self, formKategoriSil):
        _translate = QtCore.QCoreApplication.translate
        formKategoriSil.setWindowTitle(_translate("formKategoriSil", "Kategori Sil"))
        self.lblKategoriSil.setText(_translate("formKategoriSil", "Kategori Sil"))
        self.btnKategoriSil.setText(_translate("formKategoriSil", "Seçili Kategoriyi Sil"))
        self.grboxKategoriler.setTitle(_translate("formKategoriSil", "Silinecek Ketegoriyi Seçiniz"))
        self.grpboxKelimeler.setTitle(_translate("formKategoriSil", "Silinecek kategoriyle ilişkisi kaldırılacak kelimeler"))

    def actionsHazirla(self):
        self.listKategoriler.itemSelectionChanged.connect(self.listedenSecilenKategoriyiAl)
        self.btnKategoriSil.clicked.connect(self.KategoriyiSil)

    def listeleriHazirla(self):
        try:
            kategoriListesi = KategoriBLL.KategorileriListele()
            self.silinecekKategori.kategoriler = [item[0] for item in kategoriListesi]
            print(self.silinecekKategori.kategoriler)
        except Exception as exp:
            print(exp)

    def listeyiHazirla(self):
        self.listKelimeler.clear()
        self.listKategoriler.clear()
        self.listKategoriler.addItems(self.silinecekKategori.kategoriler)


    def listedenSecilenKategoriyiAl(self):
        try:
            secim = self.listKategoriler.selectedItems()[0].text()
            self.silinecekKategori.kategori=secim

            print(self.silinecekKategori.kategori)
            self.seciliKategoriyeAitKelimelerListesi = KategoriBLL.KategoriyeAitKelimeler(self.silinecekKategori)
            self.listKelimeler.clear()
            self.listKelimeler.addItems(self.seciliKategoriyeAitKelimelerListesi)

        except Exception as exp:
            print(exp)

    def KategoriyiSil(self):
        silindiMi = KategoriBLL.KategoriSil(self.silinecekKategori)
        if silindiMi:
            print("silinmişşşşş")
            self.done(1)
        else:
            print("silinmemişşşş")
            self.done(-1)
