import sys
from random import seed
from random import randint
from PyQt5.QtCore import QUrl, QDir
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QInputDialog, QMainWindow, QLineEdit,QHBoxLayout, QButtonGroup
from Form_Sinav_coktan_secme import *
import sqlite3



conn = sqlite3.connect('Sozluk.db')
cur = conn.cursor()
cur.execute("SELECT KELIME_ADI FROM KELIMELER")
cur = conn.cursor()
cur.execute("SELECT KELIME_ADI,KELIME_YOLU  FROM KELIMELER")
Tum_sorular = cur.fetchall()
secilen_sorular=[[]] * 2
tum_siklar =[]
current_soru=0
seciliListe = []
Soru_Cevap_listesi= []
Dogru_yanlis_listesi =[]


class Sinav_coktan_secme(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.Btn_ileri.clicked.connect(self.sonraki_video)
        self.ui.Btn_Geri.clicked.connect(self.onceki_video)
        self.ui.BtnTekrarOynat.clicked.connect(self.Tekrar_oynat)
        self.ui.BtnBaslat.clicked.connect(self.sinav_olustur)
        self.ui.group = QButtonGroup()
        self.ui.group.addButton(self.ui.Rb1)
        self.ui.group.addButton(self.ui.Rb2)
        self.ui.group.addButton(self.ui.Rb3)
        self.ui.group.addButton(self.ui.Rb4)
        self.ui.group.addButton(self.ui.Rb5)
        self.ui.group.setExclusive(False)
        self.ui.Rb1.toggled.connect(self.cevap)
        self.ui.Rb2.toggled.connect(self.cevap)
        self.ui.Rb3.toggled.connect(self.cevap)
        self.ui.Rb4.toggled.connect(self.cevap)
        self.ui.Rb5.toggled.connect(self.cevap)
        self.ui.frm_sonuc.hide()
        self.ui.frm_soru.hide()
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.ui.layout.addWidget(videoWidget)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile("2.mp4")))
        self.mediaPlayer.play()
        self.show()




    def soruları_olustur(self,soru_sayisi):
        global Soru_Cevap_listesi
        global current_soru
        current_soru = 0
        secilen_sorular.clear()
        Soru_Cevap_listesi.clear()
        self.ui.frm_sonuc.hide()
        Soru_Cevap_listesi = [['BOŞ BIRAKILMIŞ' for i in range(2)] for j in range(soru_sayisi)]
        cur.execute("SELECT COUNT(0) CNT FROM KELIMELER ")
        max_sayi = cur.fetchone()[0]
        if soru_sayisi>max_sayi:
            soru_sayisi = max_sayi
        i = 1
        while i <= soru_sayisi:
            value = randint(0, max_sayi-1)
            if Tum_sorular[value] not in secilen_sorular:
                secilen_sorular.append(Tum_sorular[value])
                Soru_Cevap_listesi[i-1][0]=Tum_sorular[value][0]
                i += 1


    def cevaplari_olustur(self):
       ## secilen_sorular.clear()
       tum_siklar.clear()
       cur.execute("SELECT COUNT(0) CNT FROM KELIMELER ")
       max_sayi = cur.fetchone()[0]
       secilen_cevaplar = []
       cnt=0
       for lst in  secilen_sorular:
           secilen_cevaplar.clear()
           i = 0
           while i <= 3:
             value = randint(0, max_sayi-1)
             if Tum_sorular[value][0] not in secilen_cevaplar:
                i += 1
                secilen_cevaplar.append(Tum_sorular[value][0])
           secilen_cevaplar.insert(randint(0, 4),lst[0])
           cnt += 1
           tum_siklar.append(tuple(secilen_cevaplar))


    def sinav_olustur(self):
        self.soruları_olustur(self.ui.spnbox.value())
        self.cevaplari_olustur()
        self.ui.frm_soru.show()
        self.ui.frm_Giris.hide()
        self.ui.frm_sonuc.hide()
        self.sonraki_video()

    def Soru_goster(self):
        global current_soru
        self.ui.lblSoru.setText(str(current_soru) + "/" + str(self.ui.spnbox.value()) + ". SORU ")
        cur.execute("SELECT KELIME_YOLU FROM KELIMELER Where KELIME_ADI=(?)", [secilen_sorular[current_soru - 1][0]])
        sonuc = cur.fetchone()[0]
        self.videoyuOynat(sonuc)
        self.ui.Btn_Geri.show()
        self.ui.lblSoru.setText(str(current_soru) + "/" + str(self.ui.spnbox.value()) + ". SORU ")
        self.ui.Rb1.setText(tum_siklar[current_soru - 1][0])
        self.ui.Rb2.setText(tum_siklar[current_soru - 1][1])
        self.ui.Rb3.setText(tum_siklar[current_soru - 1][2])
        self.ui.Rb4.setText(tum_siklar[current_soru - 1][3])
        self.ui.Rb5.setText(tum_siklar[current_soru - 1][4])
        self.ui.group.setExclusive(False)
        self.ui.Rb1.setChecked(Soru_Cevap_listesi[current_soru - 1][1] == self.ui.Rb1.text())
        self.ui.Rb2.setChecked(Soru_Cevap_listesi[current_soru - 1][1] == self.ui.Rb2.text())
        self.ui.Rb3.setChecked(Soru_Cevap_listesi[current_soru - 1][1] == self.ui.Rb3.text())
        self.ui.Rb4.setChecked(Soru_Cevap_listesi[current_soru - 1][1] == self.ui.Rb4.text())
        self.ui.Rb5.setChecked(Soru_Cevap_listesi[current_soru - 1][1] == self.ui.Rb5.text())
        self.ui.group.setExclusive(True)

    def sonraki_video(self):
        global current_soru
        current_soru = current_soru+1
        if current_soru<self.ui.spnbox.value():
            self.Soru_goster()
        elif current_soru>self.ui.spnbox.value():
            self.ui.frm_soru.hide()
            self.ui.frm_sonuc.show()
            self.listeyiHazirla()
        else:
            self.ui.Btn_ileri.setText('Bitir')
            self.Soru_goster()
    def onceki_video(self):
        global current_soru
        current_soru = current_soru - 1
        self.Soru_goster()
        if current_soru==1:
            self.ui.Btn_Geri.hide()


    def Tekrar_oynat(self):
        global current_soru
        cur.execute("SELECT KELIME_YOLU FROM KELIMELER Where KELIME_ADI=(?)", [secilen_sorular[current_soru-1][0]])
        sonuc = cur.fetchone()[0]
        ## print(sonuc)
        self.videoyuOynat(sonuc)

    def cevap(self):
        global current_soru
        rbtn = self.sender()
        if rbtn.isChecked()==True:
           Soru_Cevap_listesi[current_soru-1][1] =rbtn.text()
           print(Soru_Cevap_listesi)


    def listeyiHazirla(self):
        Dogru_yanlis_listesi.clear()
        toplam_Yanlis=0
        for i in range(self.ui.spnbox.value()):
            if Soru_Cevap_listesi[i][0]!=Soru_Cevap_listesi[i][1]:
                Dogru_yanlis_listesi.append(str(i+1)+'.Soru :'+Soru_Cevap_listesi[i][0].ljust(20, ' ')+'Cevap :'+Soru_Cevap_listesi[i][1])
                toplam_Yanlis+=1
        self.ui.listWidget.addItems(Dogru_yanlis_listesi)
        self.ui.lbl_Tpl_Soru.setText(str(self.ui.spnbox.value()))
        self.ui.lbl_tpl_dgr.setText(str(self.ui.spnbox.value()-toplam_Yanlis))

    def videoyuOynat(self, video):
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile(video)))
        self.mediaPlayer.play()




