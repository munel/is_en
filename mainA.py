import sys
import time

from PyQt5.QtCore import QUrl, QDir, QSize, Qt, QThread, pyqtSignal
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QInputDialog, QMainWindow, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QProgressBar
from formA import *
from PyQt5.QtGui import QIcon, QPixmap
import sqlite3
import os
import speech_recognition as sr
import threading


conn = sqlite3.connect('Sozluk.db')
cur = conn.cursor()
cur.execute("SELECT KELIME_ADI FROM KELIMELER")
kelimeListesiTupple = cur.fetchall()
kelimeListesi = [item[0] for item in kelimeListesiTupple]
cur.execute("SELECT GRUP_ADI FROM GRUPLAR")
kategoriListesiTupple = cur.fetchall()
kategoriListesi = [item[0] for item in kategoriListesiTupple]
kategoriListesi.insert(0,"Kategori Seçin")

seciliListe = []


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
        self.ui.comboBox.currentIndexChanged.connect(self.comboBoxSecim)
        self.ui.actionKategori_Ekle.triggered.connect(self.yeniKategoriEkle)
        self.ui.actionKategori_Sil.triggered.connect(self.kategoriSil)
        self.ui.actionKategori_D_zenle.triggered.connect(self.kategoriDuzenle)
        self.ui.actionRastgele_S_nav_Yap.triggered.connect(self.rastgeleSinav)

        self.listeyiHazirla()
        self.comboListeHazirla()



        # Video Göstericinin Kodları. layout isimli bir widgeta ekleniyor.

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()


        self.buton = KayitButonu(self)
        self.buton.setIcon(QIcon('micro.png'))
        self.buton.setIconSize(QSize(60, 60))
        self.buton.setGeometry(0, 0, 60, 60)
        self.buton.setStyleSheet('border-radius:60')
        self.buton.setFixedSize(self.buton.size())
        self.buton.setEnabled(True)
        self.buton.clicked.connect(self.butonTiklandi)

        self.uyariLbl = QtWidgets.QLabel('')


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
        hBox3.setContentsMargins(0, 0, 0, 0)
        hBox3.addWidget(self.uyariLbl)
        hBox3.setAlignment(Qt.AlignHCenter)

        vBoxLayout = QVBoxLayout()
        vBoxLayout.addLayout(hBox)
        vBoxLayout.addLayout(hBox2)
        vBoxLayout.addLayout(hBox3)
        vBoxLayout.addWidget(self.videoWidget)

        self.ui.layout.addLayout(vBoxLayout)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile("2.mp4")))
        self.mediaPlayer.play()
        self.videoWidget.hide()
        self.uyariLbl.hide()

        self.show()

    def kategoriDuzenle(self):
        item, okPressed = QInputDialog.getItem(self, "Kategori Düzenleme", "Düzenlenecek Kategori:", kategoriListesi, 0, False)
        if okPressed and item:
            if item != "Kategori Seçin":
                duzenlenmis, ok = QInputDialog.getText(self, "Kategori Düzenle", f"Düzenlenen Kategori:  {item}", QLineEdit.Normal, "")
                if ok and item:
                    # Kategoriler tablosunda düzenleme yapılacak
                    pass



    def yeniKategoriEkle(self):
        yeniKategori, okPressed = QInputDialog.getText(self, "Kategori Ekleme", "Yeni Kategori:", QLineEdit.Normal, "")
        if okPressed and yeniKategori != '':
            # kategoriler tablosuna yeni kategori eklenecek
            kategoriListesi.append(yeniKategori)
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(kategoriListesi)

    def kategoriSil(self):
        item, okPressed = QInputDialog.getItem(self, "Kategori Silme İşlemi", "Silineek Kategoriyi Silin:", kategoriListesi, 0, False)
        if okPressed and item:
            if item != "Kategori Seçin":
                # Kategori tablosundan veri silinecek
                kategoriListesi.remove(item)
                self.ui.comboBox.clear()
                self.ui.comboBox.addItems(kategoriListesi)



    def comboBoxSecim(self):

        kategori = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        if (self.ui.comboBox.currentIndex() != 0):
            try:
                cur.execute("SELECT KELIME_ADI FROM WR_GRUP_KELIMELERI WHERE GRUP_ADI=(?)", [kategori])
                sonuc = cur.fetchall()
                seciliListe = [item[0] for item in sonuc]
                self.ui.listWidget.clear()
                self.ui.listWidget.addItems(seciliListe)
            except Exception as e:
                print(e)

    def comboListeHazirla(self):
        self.ui.comboBox.addItems(kategoriListesi)

    def listeyiHazirla(self):
        self.ui.listWidget.addItems(kelimeListesi)

    def videoyuOynat(self, video):
        #self.mediaPlayer.setMedia(
         #   QMediaContent(QUrl.fromLocalFile(video)))
        self.progress.hide()
        self.videoWidget.show()
        #name = video.replace('\\', '/')
        #filename = os.path.abspath(name)
        #print(filename)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(video)))
        self.mediaPlayer.play()



    def listedeKiElemanSecildi(self):
        d = self.ui.listWidget.currentItem()
        cur.execute("SELECT KELIME_YOLU FROM KELIMELER Where KELIME_ADI=(?)", [d.text()])
        sonuc = cur.fetchone()[0]
        print(sonuc)
        self.videoyuOynat(sonuc)

    def rastgeleSinav(self):
        pass

    def aramaMetniDegistir(self):
        self.ui.listWidget.clear()
        seciliListe.clear()
        aramaMetni = self.ui.lineEdit.text()
        for v in kelimeListesi:
            if v.startswith(aramaMetni.upper()):
                seciliListe.append(v)

        self.ui.listWidget.addItems(seciliListe)

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
            self.uyariLbl.setText(response["error"])
            self.uyariLbl.show()
            self.buton.setIcon(QIcon('micro.png'))
        except:
            self.uyariLbl.setText("Bir şeyler ters gitti. Tekrar deneyin.")
            self.uyariLbl.show()
            self.buton.setIcon(QIcon('micro.png'))
        else:
            try:
                response["transcription"] = recognizer.recognize_google(audio, language='tr')
            except sr.RequestError:
                response["success"] = False
                response["error"] = "API hatası! Arayüze ulaşılamadı."
                self.uyariLbl.setText(response["error"])
                self.uyariLbl.show()
            except sr.UnknownValueError:
                response["error"] = "Konuşmanız anlaşılamadı."
                self.uyariLbl.setText(response["error"])
                self.uyariLbl.show()
        return response


    def sesleAra(self):

        self.uyariLbl.hide()

        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        guess = self.recognize_speech_from_mic(recognizer, microphone)
        if not guess["transcription"] or not guess["success"]:
            self.uyariLbl.setText("Ne dediğinizi anlayamadım.")
            self.uyariLbl.show()
        elif guess["error"]:
            self.uyariLbl.setText("ERROR: {}".format(guess["error"]))
            self.uyariLbl.show()

        else:
            conn = sqlite3.connect('../../is_en-master-OOP/Sozluk.db')
            cur = conn.cursor()
            cur.execute("SELECT KELIME_YOLU FROM KELIMELER WHERE KELIME_ADI=?", [guess["transcription"].upper()])
            data = cur.fetchone()
            if data is None:
                self.uyariLbl.setText("Aradığınız kelime sözlükte yer almamaktadır.")
                self.uyariLbl.show()
            else:
                self.videoyuOynat(data[0])

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())