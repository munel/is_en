# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from random import random
import time
from tkinter import messagebox

pencere = Tk()
hafiza = []
global bilinen
resimler=[]
atananlar = []



class HafizaOyunu:
    def oyunuBaslat(self):
        bilinen = 0
        pencere.title("İşaret Dili Alfabesi Hafıza Oyununa Hoşgeldiniz")
        Res_1 = PhotoImage(file="resim/0.png", width=80, height=80)
        Res_2 = PhotoImage(file="resim/1.png", width=80, height=80)
        Res_3 = PhotoImage(file="resim/2.png", width=80, height=80)
        Res_4 = PhotoImage(file="resim/3.png", width=80, height=80)
        Res_5 = PhotoImage(file="resim/4.png", width=80, height=80)
        Res_6 = PhotoImage(file="resim/5.png", width=80, height=80)
        Res_7 = PhotoImage(file="resim/6.png", width=80, height=80)
        Res_8 = PhotoImage(file="resim/7.png", width=80, height=80)
        Res_9 = PhotoImage(file="resim/8.png", width=80, height=80)
        Res_10 = PhotoImage(file="resim/9.png", width=80, height=80)
        Res_11 = PhotoImage(file="resim/10.png", width=80, height=80)
        Res_12 = PhotoImage(file="resim/11.png", width=80, height=80)
        Res_13 = PhotoImage(file="resim/12.png", width=80, height=80)
        Res_14 = PhotoImage(file="resim/13.png", width=80, height=80)
        Res_15 = PhotoImage(file="resim/14.png", width=80, height=80)
        Res_16 = PhotoImage(file="resim/15.png", width=80, height=80)
        Res_17 = PhotoImage(file="resim/16.png", width=80, height=80)
        Res_18 = PhotoImage(file="resim/17.png", width=80, height=80)
        Res_19 = PhotoImage(file="resim/18.png", width=80, height=80)
        Res_20 = PhotoImage(file="resim/19.png", width=80, height=80)
        Res_21 = PhotoImage(file="resim/20.png", width=80, height=80)
        Res_22 = PhotoImage(file="resim/21.png", width=80, height=80)
        Res_23 = PhotoImage(file="resim/22.png", width=80, height=80)
        Res_24 = PhotoImage(file="resim/23.png", width=80, height=80)
        Res_25 = PhotoImage(file="resim/24.png", width=80, height=80)
        Res_26 = PhotoImage(file="resim/25.png", width=80, height=80)
        Res_27 = PhotoImage(file="resim/26.png", width=80, height=80)
        Res_28 = PhotoImage(file="resim/27.png", width=80, height=80)

        resimler.append(Res_1)
        resimler.append(Res_2)
        resimler.append(Res_3)
        resimler.append(Res_4)
        resimler.append(Res_5)
        resimler.append(Res_6)
        resimler.append(Res_7)
        resimler.append(Res_8)
        resimler.append(Res_9)
        resimler.append(Res_10)
        resimler.append(Res_11)
        resimler.append(Res_12)
        resimler.append(Res_13)
        resimler.append(Res_14)
        resimler.append(Res_15)
        resimler.append(Res_16)
        resimler.append(Res_17)
        resimler.append(Res_18)
        resimler.append(Res_19)
        resimler.append(Res_20)
        resimler.append(Res_21)
        resimler.append(Res_22)
        resimler.append(Res_23)
        resimler.append(Res_24)
        resimler.append(Res_25)
        resimler.append(Res_26)
        resimler.append(Res_27)
        resimler.append(Res_28)

        def cevir(a):
            if len(hafiza) == 0:
                for i in atananlar:
                    if a == i[0]:
                        ilk_buton = i[2]
                        ##y = PhotoImage(file=str(i[1]) + ".png", width=50, height=50)
                        ilk_buton.config(text=i[1], image=resimler[int(i[1])], state="normal")
                        hafiza.append(i)
                        print(hafiza)
            else:
                for i in atananlar:
                    if a == i[0]:
                        ikinci_buton = i[2]
                        ##k = PhotoImage(file=str(i[1]) + ".png",width=50, height=50)
                        ikinci_buton.config(text=i[1], image=resimler[int(i[1])], state="normal")
                        if i[1] == hafiza[0][1]:
                            global bilinen
                            bilinen = bilinen + 1
                            hafiza.clear()
                            if bilinen == 18:
                                messagebox.showinfo("hafıza oyunu",
                                                    "Tebrikler!Tüm eşleştirmeleri başarıyla gerçekleştirdiniz")
                        else:
                            ikinci_buton.after(100, lambda x=i[2]: cevirici(x))

        def cevirici(ikinci_buton):
            birinci_buton = hafiza[0][2]
            birinci_buton.config(text="eşimi bul", image=m, state="active")
            ikinci_buton.config(text="eşimi bul", image=m, state="active")
            time.sleep(0.5)
            hafiza.clear()

        icerikler = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        icerikler = icerikler * 2

        satirno = 0
        m = PhotoImage(file="resim/kapat.png", width=80, height=80)
        messagebox.showinfo("hafıza oyunu",
                            "Kartların üstüne tıklayarak işaret dili harflerinin eşlerini bulabilir misin?")
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
        pencere.mainloop()
