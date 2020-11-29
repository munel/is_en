import sys

from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from form import *
listem = []
class Kelime:
    def __init__(self,kelime="",video=""):
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
        self.ui.pushButton.clicked.connect(self.butonTiklandi)
        self.ui.lineEdit.textChanged.connect(self.aramaMetniDegistir)
        self.ui.listWidget.itemClicked.connect(self.listedeKiElemanSecildi)

        # Video Göstericinin Kodları. layout isimli bir widgeta ekleniyor.
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.ui.layout.addWidget(videoWidget)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile("2.mp4")))
        self.mediaPlayer.play()
        self.listeyiHazirla()

        self.show()
    def listeyiHazirla(self):
        for i in range(5):
            listem.append(Kelime(kelime="Kelime"+str(i),video=str(i)+".mp4"))
        for v in listem:
            self.ui.listWidget.addItem(v.kelime)



    def listedeKiElemanSecildi(self):
        d = self.ui.listWidget.currentItem()

        k = Kelime()
        for l in listem:
            print(l.kelime)
            if d.text() == l.kelime:
                k = l
                break
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile(k.video)))
        self.mediaPlayer.play()


    def butonTiklandi(self):
        self.ui.listWidget.addItem(self.ui.lineEdit.text())

    def aramaMetniDegistir(self):
        print(self.ui.lineEdit.text())


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
