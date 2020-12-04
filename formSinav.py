# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(714, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 10, 501, 301))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(6)
        self.layout.setObjectName("layout")
        self.frameSinav = QtWidgets.QFrame(self.centralwidget)
        self.frameSinav.setGeometry(QtCore.QRect(10, 320, 681, 131))
        self.frameSinav.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSinav.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSinav.setObjectName("frameSinav")

        self.startButton = QtWidgets.QPushButton(self.frameSinav)
        self.startButton.setGeometry(QtCore.QRect(220, 90, 75, 23))
        self.startButton.setObjectName("startButton")
        self.bitirButton = QtWidgets.QPushButton(self.frameSinav)
        self.bitirButton.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.bitirButton.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frameSinav)
        self.label.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label.setObjectName("label")
        self.label_Puan = QtWidgets.QLabel(self.frameSinav)
        self.label_Puan.setGeometry(QtCore.QRect(10, 70, 71, 21))
        self.label_Puan.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_Puan.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Puan.setWordWrap(False)
        self.label_Puan.setObjectName("label_Puan")
        self.label2 = QtWidgets.QLabel(self.frameSinav)
        self.label2.setGeometry(QtCore.QRect(100, 40, 71, 16))
        self.label2.setObjectName("label")
        self.label_Yanlis = QtWidgets.QLabel(self.frameSinav)
        self.label_Yanlis.setGeometry(QtCore.QRect(100, 70, 71, 21))
        self.label_Yanlis.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_Yanlis.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Yanlis.setWordWrap(False)
        self.label_Yanlis.setObjectName("label_Puan")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frameSinav)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 60, 341, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tahminButton = QtWidgets.QPushButton(self.frameSinav)
        self.tahminButton.setGeometry(QtCore.QRect(350, 90, 75, 23))
        self.tahminButton.setObjectName("tahminButton")
        self.sonraButon = QtWidgets.QPushButton(self.frameSinav)
        self.sonraButon.setGeometry(QtCore.QRect(485, 90, 75, 23))
        self.sonraButon.setObjectName("sonraButon")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 25, 160, 285))
        self.listWidget.setObjectName("listWidget")

        self.labelListe = QtWidgets.QLabel(self.centralwidget)
        self.labelListe.setGeometry(QtCore.QRect(25, 5, 160, 16))
        self.labelListe.setObjectName("label")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 714, 21))
        self.menubar.setObjectName("menubar")
        self.menuKelimeler = QtWidgets.QMenu(self.menubar)
        self.menuKelimeler.setObjectName("menuKelimeler")
        self.menuKategoriler = QtWidgets.QMenu(self.menubar)
        self.menuKategoriler.setObjectName("menuKategoriler")
        self.menuS_nav = QtWidgets.QMenu(self.menubar)
        self.menuS_nav.setObjectName("menuS_nav")
        self.menuHakk_nda = QtWidgets.QMenu(self.menubar)
        self.menuHakk_nda.setObjectName("menuHakk_nda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionKelime_Ekle = QtWidgets.QAction(MainWindow)
        self.actionKelime_Ekle.setObjectName("actionKelime_Ekle")
        self.actionKelime_D_zenle = QtWidgets.QAction(MainWindow)
        self.actionKelime_D_zenle.setObjectName("actionKelime_D_zenle")
        self.actionKelime_Sil = QtWidgets.QAction(MainWindow)
        self.actionKelime_Sil.setObjectName("actionKelime_Sil")
        self.actionKategori_Ekle = QtWidgets.QAction(MainWindow)
        self.actionKategori_Ekle.setObjectName("actionKategori_Ekle")
        self.actionKategori_D_zenle = QtWidgets.QAction(MainWindow)
        self.actionKategori_D_zenle.setObjectName("actionKategori_D_zenle")
        self.actionKategori_Sil = QtWidgets.QAction(MainWindow)
        self.actionKategori_Sil.setObjectName("actionKategori_Sil")
        self.actionRastgele_S_nav_Yap = QtWidgets.QAction(MainWindow)
        self.actionRastgele_S_nav_Yap.setObjectName("actionRastgele_S_nav_Yap")
        self.actionHakk_nda = QtWidgets.QAction(MainWindow)
        self.actionHakk_nda.setObjectName("actionHakk_nda")
        self.actionYard_m = QtWidgets.QAction(MainWindow)
        self.actionYard_m.setObjectName("actionYard_m")
        self.menuKelimeler.addAction(self.actionKelime_Ekle)
        self.menuKelimeler.addAction(self.actionKelime_D_zenle)
        self.menuKelimeler.addAction(self.actionKelime_Sil)
        self.menuKategoriler.addAction(self.actionKategori_Ekle)
        self.menuKategoriler.addAction(self.actionKategori_D_zenle)
        self.menuKategoriler.addAction(self.actionKategori_Sil)
        self.menuS_nav.addAction(self.actionRastgele_S_nav_Yap)
        self.menuHakk_nda.addAction(self.actionHakk_nda)
        self.menuHakk_nda.addSeparator()
        self.menuHakk_nda.addAction(self.actionYard_m)
        self.menubar.addAction(self.menuKelimeler.menuAction())
        self.menubar.addAction(self.menuKategoriler.menuAction())
        self.menubar.addAction(self.menuS_nav.menuAction())
        self.menubar.addAction(self.menuHakk_nda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "İşaret Dili Sözlüğü"))
        self.startButton.setText(_translate("MainWindow", "Başla"))
        self.bitirButton.setText(_translate("MainWindow", "Çıkış"))
        self.label.setText(_translate("MainWindow", "DOĞRU SAYISI"))
        self.label_Puan.setText(_translate("MainWindow", "0"))

        self.label2.setText(_translate("MainWindow", "YANLIŞ SAYISI"))
        self.label_Yanlis.setText(_translate("MainWindow", "0"))

        self.labelListe.setText(_translate("MainWindow", "YANLIŞ CEVAPLANAN SORULAR"))

        self.tahminButton.setText(_translate("MainWindow", "TAHMİN"))
        self.sonraButon.setText(_translate("MainWindow", "SONRAKİ"))
        self.menuKelimeler.setTitle(_translate("MainWindow", "Kelimeler"))
        self.menuKategoriler.setTitle(_translate("MainWindow", "Kategoriler"))
        self.menuS_nav.setTitle(_translate("MainWindow", "Sınav"))
        self.menuHakk_nda.setTitle(_translate("MainWindow", "Hakkında"))
        self.actionKelime_Ekle.setText(_translate("MainWindow", "Kelime Ekle"))
        self.actionKelime_D_zenle.setText(_translate("MainWindow", "Kelime Düzenle"))
        self.actionKelime_Sil.setText(_translate("MainWindow", "Kelime Sil"))
        self.actionKategori_Ekle.setText(_translate("MainWindow", "Kategori Ekle"))
        self.actionKategori_D_zenle.setText(_translate("MainWindow", "Kategori Düzenle"))
        self.actionKategori_Sil.setText(_translate("MainWindow", "Kategori Sil"))
        self.actionRastgele_S_nav_Yap.setText(_translate("MainWindow", "Rastgele Sınav Yap"))
        self.actionHakk_nda.setText(_translate("MainWindow", "Hakkında"))
        self.actionYard_m.setText(_translate("MainWindow", "Yardım"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

