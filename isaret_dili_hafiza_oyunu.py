# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from random import random
import time
from tkinter import messagebox

class HafizaOyunu:
    def oyunuBaslat(self):
        pencere = Tk()
        hafiza = []
        self.bilinen = 0
        self.bilinenDugmeler=[]
        resimler = []
        atananlar = []
        self.oncekiBasilan = -1
        for i in range(0,28):
            resimler.append(PhotoImage(file="resim/"+ str(i) +".png", width=80, height=80))


        def cevir(a):

            if (len(hafiza) == 1 and a == self.oncekiBasilan)  or (a in self.bilinenDugmeler):
                print("aynı buton")
            else:
                if len(hafiza) == 0:
                    for i in atananlar:
                        if a == i[0]:
                            self.ilk_buton = i[2]
                            ##y = PhotoImage(file=str(i[1]) + ".png", width=50, height=50)
                            self.ilk_buton.config(text=i[1], image=resimler[int(i[1])], state="normal")

                            hafiza.append(i)
                            print(hafiza)
                else:
                    for i in atananlar:
                        if a == i[0]:
                            ikinci_buton = i[2]

                            ##k = PhotoImage(file=str(i[1]) + ".png",width=50, height=50)
                            ikinci_buton.config(text=i[1], image=resimler[int(i[1])], state="normal")

                            if i[1] == hafiza[0][1]:
                                self.bilinen = self.bilinen + 1
                                self.bilinenDugmeler.append(self.oncekiBasilan)
                                self.bilinenDugmeler.append(a)
                                hafiza.clear()
                                if self.bilinen == 18:
                                    messagebox.showinfo("hafıza oyunu",
                                                        "Tebrikler!Tüm eşleştirmeleri başarıyla gerçekleştirdiniz")
                            else:
                                self.oncekiBasilan = -1
                                ikinci_buton.after(100, lambda x=i[2]: cevirici(x))
                self.oncekiBasilan = a

        def cevirici(ikinci_buton):

            birinci_buton = hafiza[0][2]
            birinci_buton.config(text="eşimi bul", image=m, state="normal")
            ikinci_buton.config(text="eşimi bul", image=m, state="normal")
            time.sleep(0.5)
            hafiza.clear()

        icerikler = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        icerikler = icerikler * 2

        satirno = 0
        m = PhotoImage(file="resim/kapat.png", width=80, height=80)

        for satir in range(0, 6):
            sutunno = 0
            for sutun in range(0, 6):
                deger = len(icerikler)
                ilk = str(satirno) + str(sutunno)
                ikinci = int(random() * deger)
                butonx = Button(pencere, text="eşimi bul", image=m,
                                command=lambda a=ilk: cevir(a))
                atanacak = (ilk, icerikler[ikinci], butonx)
                atananlar.append(atanacak)
                icerikler.pop(ikinci)
                print(atananlar)
                butonx.grid(row=satirno, column=sutunno)
                sutunno = sutunno + 1
            satirno += 1

        w = 515
        h = 515
        ws = pencere.winfo_screenwidth()
        hs = pencere.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        pencere.geometry('%dx%d+%d+%d' % (w, h, x, y))
        pencere.title("İşaret Dili Alfabesi Hafıza Oyununa Hoşgeldiniz")
        messagebox.showinfo("hafıza oyunu",
                            "Kartların üstüne tıklayarak işaret dili harflerinin eşlerini bulabilir misin?")
        pencere.mainloop()