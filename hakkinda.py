# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Salih\Desktop\Python Eğitici Eğitimi\Proje\munel\is_en\ui\hakkinda.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtWidgets import QDialog, QWidget, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Hakkinda(QDialog):

    def __init__(self):

        super(Hakkinda, self).__init__()
        #self.setFixedSize(464, 327)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setupUi(self)

    def setupUi(self, Hakkinda):
        self.hakkindaYazisi="Bu proje Milli Eğitim Bakanlığı Öğretmen Yetiştirme Genel Müdürlüğü tarafından hazırlanmış hizmetiçi eğitim kapsamında " \
                            "verilen Python Eğitici Eğitimi kursu için hazırlanmıştır. " \
                            "\n \nProje Adı: İşaret Dili Sözlüğü " \
                            "\n\nProje Grubu: 497_12 İstanbul " \
                            "\nGitHub Adresi: https://github.com/munel/is_en" \
                            "\n\nProje Üyeleri: \n- Ahmet Arman Göçmez \n- Ali İhsan BİLGİÇ \n- Arda ÇAKIR \n- Aykut COŞKUN " \
                            "\n- Fulya ÖZÇELİK \n- Mustafa ÜNEL \n- Salih ŞAHİN \n- Süleyman ERCİN " \
                            "\n\nLisanslar" \
                            "\nBazı Resimler: www.freepik.com" \
                            "\nPYQT" \
                            "\nSQLite" \
                            "\nSpeechRecognition" \
                            "\nPyAudio"
        qss = "sablon.qss"
        with open(qss, "r") as fh:
            self.setStyleSheet(fh.read())
        Hakkinda.setObjectName("Hakkinda")
        Hakkinda.resize(500, 610)
        self.gridLayout = QtWidgets.QGridLayout(Hakkinda)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0,0,0,0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblUstGorunum = QtWidgets.QLabel(Hakkinda)

        self.lblUstGorunum.setMinimumSize(QtCore.QSize(0, 200))
        self.lblUstGorunum.setMaximumSize(QtCore.QSize(700, 200))
        self.lblUstGorunum.setObjectName("lblUstGorunum")
        self.verticalLayout.addWidget(self.lblUstGorunum)
        self.verticalLayoutIcerik = QtWidgets.QVBoxLayout()
        self.verticalLayoutIcerik.setContentsMargins(0,0,0,0)
        self.verticalLayoutIcerik.setObjectName("horizontalLayout_2")

        self.lblHakkinda = QtWidgets.QLabel(Hakkinda)
        self.lblHakkinda.setObjectName("lblHakkinda")
        self.lblHakkinda.setWordWrap(True)
        self.lblHakkinda.setContentsMargins(10,0,0,0)
        self.lblHakkinda.setMinimumSize(QtCore.QSize(0, 200))
        self.lblHakkinda.setMaximumSize(QtCore.QSize(700, 500))
        self.verticalLayoutIcerik.addWidget(self.lblHakkinda)

        self.btnKapat = QtWidgets.QPushButton(Hakkinda)
        self.btnKapat.setMinimumSize(QtCore.QSize(0, 35))
        self.btnKapat.setObjectName("btnDuzenle")
        self.verticalLayoutIcerik.addWidget(self.btnKapat)
        self.btnKapat.clicked.connect(self.Kapat)


        self.verticalLayout.addLayout(self.verticalLayoutIcerik)

        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.pressing = False
        # setting  the geometry of window


        # creating label


        print("loading image")
        self.pixmap = QPixmap("./resim/ust_banner.png")

        # adding image to label
        self.lblUstGorunum.setScaledContents(True)
        self.lblUstGorunum.setPixmap(self.pixmap)




        self.retranslateUi(Hakkinda)
        QtCore.QMetaObject.connectSlotsByName(Hakkinda)

    def retranslateUi(self, Hakkinda):
        _translate = QtCore.QCoreApplication.translate
        Hakkinda.setWindowTitle(_translate("Hakkinda", "Hakkında"))
        #self.lblUstGorunum.setText(_translate("Hakkinda", "Buraya üst resim gelecek."))
        self.btnKapat.setText(_translate("Hakkinda", "Kapat"))
        self.lblHakkinda.setText(_translate("Hakkinda", self.hakkindaYazisi))

    def Kapat(self):
        self.done(1)


    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.width(),
                                self.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False