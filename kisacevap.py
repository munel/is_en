# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kisacevap.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(662, 348)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 40, 171, 241))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 17, 161, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 290, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 310, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_Puan = QtWidgets.QLabel(Dialog)
        self.label_Puan.setGeometry(QtCore.QRect(110, 294, 47, 13))
        self.label_Puan.setObjectName("label_Puan")
        self.label_Yanlis = QtWidgets.QLabel(Dialog)
        self.label_Yanlis.setGeometry(QtCore.QRect(110, 312, 47, 13))
        self.label_Yanlis.setObjectName("label_Yanlis")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 20, 421, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setObjectName("layout")
        self.sonraButon = QtWidgets.QPushButton(Dialog)
        self.sonraButon.setGeometry(QtCore.QRect(530, 290, 101, 31))
        self.sonraButon.setObjectName("sonraButon")
        self.tahminButton = QtWidgets.QPushButton(Dialog)
        self.tahminButton.setGeometry(QtCore.QRect(400, 290, 101, 31))
        self.tahminButton.setObjectName("tahminButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 290, 151, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "CEVAPLANAN KELİMELER"))
        self.label_2.setText(_translate("Dialog", "Doğru Sayısı :"))
        self.label_3.setText(_translate("Dialog", "Yanlış Sayısı :"))
        self.label_Puan.setText(_translate("Dialog", "0"))
        self.label_Yanlis.setText(_translate("Dialog", "0"))
        self.sonraButon.setText(_translate("Dialog", "SONRAKİ SORU"))
        self.tahminButton.setText(_translate("Dialog", "Cevabı Kontrol Et"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())