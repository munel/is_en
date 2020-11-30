# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 371)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 70, 161, 241))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 10, 421, 301))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(6)
        self.layout.setObjectName("layout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 21))
        self.menubar.setObjectName("menubar")
        self.menuKelimeler = QtWidgets.QMenu(self.menubar)
        self.menuKelimeler.setObjectName("menuKelimeler")
        self.menuKategoriler = QtWidgets.QMenu(self.menubar)
        self.menuKategoriler.setObjectName("menuKategoriler")
        self.menuS_nav = QtWidgets.QMenu(self.menubar)
        self.menuS_nav.setObjectName("menuS_nav")
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
        self.menuKelimeler.addAction(self.actionKelime_Ekle)
        self.menuKelimeler.addAction(self.actionKelime_D_zenle)
        self.menuKelimeler.addAction(self.actionKelime_Sil)
        self.menuKategoriler.addAction(self.actionKategori_Ekle)
        self.menuKategoriler.addAction(self.actionKategori_D_zenle)
        self.menuKategoriler.addAction(self.actionKategori_Sil)
        self.menuS_nav.addAction(self.actionRastgele_S_nav_Yap)
        self.menubar.addAction(self.menuKelimeler.menuAction())
        self.menubar.addAction(self.menuKategoriler.menuAction())
        self.menubar.addAction(self.menuS_nav.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "İşaret Dili Sözlüğü"))
        self.menuKelimeler.setTitle(_translate("MainWindow", "Kelimeler"))
        self.menuKategoriler.setTitle(_translate("MainWindow", "Kategoriler"))
        self.menuS_nav.setTitle(_translate("MainWindow", "Sınav"))
        self.actionKelime_Ekle.setText(_translate("MainWindow", "Kelime Ekle"))
        self.actionKelime_D_zenle.setText(_translate("MainWindow", "Kelime Düzenle"))
        self.actionKelime_Sil.setText(_translate("MainWindow", "Kelime Sil"))
        self.actionKategori_Ekle.setText(_translate("MainWindow", "Kategori Ekle"))
        self.actionKategori_D_zenle.setText(_translate("MainWindow", "Kategori Düzenle"))
        self.actionKategori_Sil.setText(_translate("MainWindow", "Kategori Sil"))
        self.actionRastgele_S_nav_Yap.setText(_translate("MainWindow", "Rastgele Sınav Yap"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
