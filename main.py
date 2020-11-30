import sys

from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from mainform2 import *

class Kelime:
    def __init__(self,kelime,video):
        self.kelime = kelime
        self.video = video
    def getKelime(self):
        return self.kelime
    def getVideoName(self):
        return self.video

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        ##self.ui.pushButton.clicked.connect(self.butonTiklandi)
        ##self.ui.lineEdit.textChanged.connect(self.aramaMetniDegistir)
        ##self.ui.listWidget.itemClicked.connect(self.listedeKiElemanSecildi)

        # Video Göstericinin Kodları. layout isimli bir widgeta ekleniyor.
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.ui.layout.addWidget(videoWidget)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile("2.mp4")))
        self.mediaPlayer.play()

        self.show()


    def listedeKiElemanSecildi(self):
        d = self.ui.listWidget.currentItem()
        print(d.text())


    def butonTiklandi(self):
        self.ui.listWidget.addItem(self.ui.lineEdit.text())

    def aramaMetniDegistir(self):
        print(self.ui.lineEdit.text())


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
