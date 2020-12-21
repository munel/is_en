import sys
import time
from datetime import time
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QProgressBar
from kelimeislemleri import YeniKelimeEkle
from yeniKategoriEkle import YeniKategoriEkle
from kategoriDuzenle import KategoriDuzenle
from kategoriSil import KategoriSil
from silinecekkelimeform import SilinecekKelimeForm
from duzenlenecekkelimeform import DuzenlenecekKelimeForm
from Sinav_coktan_secme import *
from isaret_dili_hafiza_oyunu import *
from kisacevapmain import KisaCevapFrom
from hakkinda import Hakkinda
from form import *
from kategoriBLL import KategoriBLL
from kelimeBLL import KelimeBLL
from entity import Kelime
from entity import Kategori
from helper import Helper
from PyQt5.QtCore import QUrl, QSize, Qt, QThread, pyqtSignal
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QCursor
from PyQt5 import QtGui, QtWidgets
import speech_recognition as sr
import threading
import seslearamavb
import webbrowser


class KayitButonu(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(KayitButonu, self).__init__(parent)
        self.setIcon(QtGui.QIcon("micro.png"))

    def mousePressEvent(self, event):
        super(KayitButonu, self).mousePressEvent(event)
        self.setIcon(QtGui.QIcon("micro.png"))

    def mouseReleaseEvent(self, event):
        super(KayitButonu, self).mouseReleaseEvent(event)
        self.setIcon(
            QtGui.QIcon("recording.png" if self.isChecked() else "recording.png")
        )
        self.setEnabled(False)


TIME_LIMIT = 0


class External(QThread):
    countChanged = pyqtSignal(int)

    def run(self):
        count = 5
        while count > TIME_LIMIT:
            count -= 1
            time.sleep(1)
            self.countChanged.emit(count)


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit.textChanged.connect(self.aramaMetniDegistir)
        self.ui.listWidget.itemClicked.connect(self.listedeKiElemanSecildi)
        self.ui.comboBox.activated.connect(self.comboBoxTiklama)
        self.ui.actionKategori_Ekle.triggered.connect(self.yeniKategoriEkle)
        self.ui.actionKategori_Sil.triggered.connect(self.kategoriSil)
        self.ui.actionKategori_Duzenle.triggered.connect(self.kategoriDuzenle)
        self.ui.actionCoktanSecmeliSinav.triggered.connect(self.sinavCoktanSecmeli)
        self.ui.actionHafizaOyunu.triggered.connect(self.hafizaOyunuAc)
        self.ui.actionKisaCevap.triggered.connect(self.kisacevapOyunuAc)

        self.ui.actionYardim.triggered.connect(self.Yardim)
        self.ui.actionHakkinda.triggered.connect(self.Hakkinda)
        self.ui.actionKelime_Ekle.triggered.connect(self.yeniKelimeEkle)
        self.ui.actionKelime_Sil.triggered.connect(self.kelimeSil)
        self.ui.actionKelime_Duzenle.triggered.connect(self.kelimeDuzenle)

        self.secilenKelime = Kelime()
        self.secilenKategori = Kategori()
        self.yeniKategori = Kategori()

        self.silinecekKategori = Kategori()
        self.kelimeListesi = []
        self.kategoriListesi = []
        self.seciliListe = []
        self.listeleriHazirla()

        self.listeyiHazirla()
        self.comboListeHazirla()

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()

        self.buton = KayitButonu(self)
        self.buton.setIcon(QIcon('micro.png'))
        self.buton.setIconSize(QSize(40, 40))
        self.buton.setGeometry(0, 0, 50, 50)
        self.buton.setStyleSheet('border-radius:60')
        self.buton.setCursor(QCursor(Qt.PointingHandCursor))
        self.buton.setFixedSize(self.buton.size())
        self.buton.setEnabled(True)
        self.buton.clicked.connect(self.butonTiklandi)

        self.progress = QProgressBar(self, minimum=0, maximum=0, objectName="RedProgressBar")
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(5)
        self.progress.setFormat('')
        self.progress.setStyleSheet("#RedProgressBar::chunk {"
                                    "background-color: #F44336;"
                                    "}")

        hBox = QHBoxLayout()
        hBox.setContentsMargins(0, 0, 0, 0)
        hBox.addWidget(self.buton)
        hBox.setAlignment(Qt.AlignHCenter)
        hBox2 = QHBoxLayout()
        hBox2.setContentsMargins(0, 0, 0, 0)
        hBox2.addWidget(self.progress)
        hBox2.setAlignment(Qt.AlignHCenter)
        hBox3 = QHBoxLayout()
        hBox3.setContentsMargins(0, 2, 0, 2)

        hBox3.setAlignment(Qt.AlignHCenter)

        vBoxLayout = QVBoxLayout()
        vBoxLayout.addLayout(hBox)
        vBoxLayout.addLayout(hBox2)
        vBoxLayout.addLayout(hBox3)
        vBoxLayout.addWidget(self.videoWidget)

        self.ui.layout.addLayout(vBoxLayout)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("VIDEOLAR\MERHABA.mp4")))
        self.progress.hide()
        self.videoWidget.show()
        self.mediaPlayer.play()
        self.videoWidget.show()
        self.show()

    def recognize_speech_from_mic(self, recognizer, microphone):
        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")
        if not isinstance(microphone, sr.Microphone):
            print('HATA 2')
            raise TypeError("`microphone` must be `Microphone` instance")

        response = {"success": True, "error": None, "transcription": None}

        try:
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=4)
        except sr.WaitTimeoutError:
            response["error"] = "Zamanında kelime söylemediniz."
            # self.uyariLbl.setText(response["error"])
            # self.uyariLbl.show()
            self.buton.setIcon(QIcon('micro.png'))

        except:
            print("Bir şeyler ters gitti. Tekrar deneyin.")
            # self.uyariLbl.show()
            self.buton.setIcon(QIcon('micro.png'))
        else:
            try:
                response["transcription"] = recognizer.recognize_google(audio, language='tr')
            except sr.RequestError:
                response["success"] = False
                response["error"] = "API hatası! Arayüze ulaşılamadı."
                # self.uyariLbl.setText(response["error"])
                # self.uyariLbl.show()
            except sr.UnknownValueError:
                response["error"] = "Konuşmanız anlaşılamadı."
                # self.uyariLbl.setText(response["error"])
                # self.uyariLbl.show()
        return response

    def sesleAra(self):

        # self.uyariLbl.hide()

        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        self.guess = self.recognize_speech_from_mic(recognizer, microphone)
        if not self.guess["transcription"] or not self.guess["success"]:
            print("anlaşılamadı")
            # self.uyariLbl.show()
        elif self.guess["error"]:
            print(self.guess["error"])
            # self.uyariLbl.show()
        else:
            try:
                yol = seslearamavb.yolDondur(self.guess["transcription"])
                self.videoyuOynat(yol)
                self.ui.listWidget.clear()
                self.ui.lineEdit.setText(self.guess["transcription"])
            except Exception as e:
                self.ui.lineEdit.setText("Sözcük Bulunamadı")


        self.buton.setIcon(QIcon('micro.png'))
        self.buton.setEnabled(True)

    def onCountChanged(self, value):
        self.progress.setValue(value)

    def onButtonClick(self):
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

    def butonTiklandi(self):
        self.progress.show()
        thread = threading.Thread(target=self.sesleAra)
        thread.start()
        self.onButtonClick()

    def listeleriHazirla(self):
        try:
            kelimeListesiTupple = KelimeBLL.KelimeleriListele()
            kategoriListesiTupple = KategoriBLL.KategorileriListele()
            self.kelimeListesi = [item[0] for item in kelimeListesiTupple]
            self.kategoriListesi = [item[0] for item in kategoriListesiTupple]
            self.kategoriListesi.insert(0, "Kategori Seçin")
        except Exception as exp:
            print(exp)

    def yeniKelimeEkle(self):
        try:
            self.yenikelimeEkle = YeniKelimeEkle()
            self.yenikelimeEkle.show()
            if self.yenikelimeEkle.close:
                print("Deneme")
        except Exception as e:
            print(e)
        donusDurumu=self.yenikelimeEkle.exec_()
        if  donusDurumu== 1:
            QMessageBox.information(self, "Yeni Kelime", "Yeni Kelime Eklendi")
        else:
            QMessageBox.warning(self, "Yeni Kelime", "Yeni kelime eklenemedi.")
        self.listeleriHazirla()
        self.comboListeHazirla()
        self.listeyiHazirla()


    def kelimeSil(self):
        try:
            self.kelimeSil = SilinecekKelimeForm()
            self.kelimeSil.show()

        except Exception as e:
            print(e)
        donusDurumu = self.kelimeSil.exec_()
        if donusDurumu == 1:
            QMessageBox.information(self, "Kelime Sil", "Kelime Silindi")
        else:
            QMessageBox.warning(self, "Kelime Sil", "Kelime Silinemedi.")

        self.listeleriHazirla()
        self.comboListeHazirla()
        self.listeyiHazirla()

    def kelimeDuzenle(self):

        print("Kelime Düzenle menü basıldı")
        try:
            self.KelimeDuzenle = DuzenlenecekKelimeForm()
            print("Kelime Düzenle yaratıldı")
            self.KelimeDuzenle.show()
            if self.KelimeDuzenle.close:
                print("Kelime Düzenle Kapatıldı")
        except Exception as e:
            print(e)

        donusDurumu= self.KelimeDuzenle.exec_()
        if donusDurumu== 1:
            QMessageBox.information(self, "Kelime Düzenle", "Kelime Düzeltildi.")
        else:
            QMessageBox.warning(self, "Kelime Düzenle", "Kelime Düzenlenemedi.")

        self.listeleriHazirla()
        self.comboListeHazirla()
        self.listeyiHazirla()

    def kategoriDuzenle(self):

        try:
            self.kategoriDuzenle = KategoriDuzenle()
            self.kategoriDuzenle.show()
            if self.kategoriDuzenle.close:
                print("Deneme")
        except Exception as e:
            print(e)

        donusDurumu = self.kategoriDuzenle.exec_()
        if donusDurumu == 1:

            QMessageBox.information(self, "Kategori Düzenle", "Kategori Düzenlendi.")
        else:
            QMessageBox.warning(self, "Kategori Düzenle", "Kategori Düzenlenemedi.")

        self.listeleriHazirla()
        self.comboListeHazirla()
        self.listeyiHazirla()


    def yeniKategoriEkle(self):
        try:
            self.yeniKategoriEkle = YeniKategoriEkle()
            self.yeniKategoriEkle.show()

            if self.yeniKategoriEkle.close:
                print("Yeni Kategori Sayfası kapatıldı.")

        except Exception as e:
            print(e)
        donusDurumu = self.yeniKategoriEkle.exec_()
        if donusDurumu == 1:
            QMessageBox.information(self, "Yeni Kelime", "Yeni Kelime Eklendi")
        else:
            QMessageBox.warning(self, "Yeni Kategori", "Yeni Kategori Eklenemedi")

        self.listeleriHazirla()
        self.listeyiHazirla()
        self.comboListeHazirla()

    def kategoriSil(self):
        try:
            self.kategoriSil = KategoriSil()
            self.kategoriSil.show()
            donusDurumu = self.kategoriSil.exec_()
            if donusDurumu == 1:
                QMessageBox.information(self, "Kategori Sil", "Kategori ve ilişileri Silindi")
            else:
                QMessageBox.warning(self, "Kategori Sil", "Kategori ve/veya ilişkileri silinemedi.")
        except Exception as e:
            print(e)

        self.listeleriHazirla()
        self.comboListeHazirla()
        self.listeyiHazirla()

    def comboBoxTiklama(self):
        print("tıklandı")
        self.secilenKategori.kategori = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())

        if (self.ui.comboBox.currentIndex() != 0):  # düzeltilmesi gerekiyor  bütün hepsinde çıkması lazım
            try:
                kelimeListesi = KategoriBLL.KategoriyeAitKelimeler(self.secilenKategori)
                self.ui.listWidget.clear()
                self.ui.listWidget.addItems(kelimeListesi)
            except Exception as e:
                print(e)
        else:
            self.listeleriHazirla()
            self.listeyiHazirla()

    def comboListeHazirla(self):
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(self.kategoriListesi)

    def listeyiHazirla(self):
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(self.kelimeListesi)

    def videoyuOynat(self, video):
        ##self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("VIDEOLAR/RAHAT.mp4")))
        self.progress.hide()
        self.videoWidget.show()
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile(video)))
        self.mediaPlayer.play()

    def listedeKiElemanSecildi(self):

        self.secilenKelime.kelime = self.ui.listWidget.currentItem().text()
        sonuc = KelimeBLL.KelimeVideoBul(self.secilenKelime)
        print(sonuc)
        self.videoyuOynat(sonuc)

    def sinavCoktanSecmeli(self):
        self.Form = QtWidgets.QWidget()
        self.Form.ui = Sinav_coktan_secme()
        self.Form.ui.show()

    def aramaMetniDegistir(self):
        self.ui.listWidget.clear()
        self.seciliListe.clear()
        aramaMetni = self.ui.lineEdit.text()
        for v in self.kelimeListesi:
            if v.startswith(Helper.KucukHarfleriBuyukYap(aramaMetni)):
                self.seciliListe.append(v)

        self.ui.listWidget.addItems(self.seciliListe)

    def hafizaOyunuAc(self):
        h = HafizaOyunu()
        h.oyunuBaslat()

    def kisacevapOyunuAc(self):
        KisaCevapFrom()

    def Hakkinda(self):
        self.hakkinda = Hakkinda()
        self.hakkinda.show()

    def Yardim(self):
        webbrowser.open('https://github.com/munel/is_en')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('resim/logo.png'))
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
