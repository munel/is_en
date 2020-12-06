class Helper:

    @staticmethod
    def KucukHarfleriBuyukYap(sozcuk):
        # https://www.pythontr.com/makale/python-turkce-karakterleri-buyuk-harfe-kucuk-55 teşekkürler..
        yeniSozcuk = ""
        trKucuk = ''
        trBuyuk=''
        TRHarfler = [
            ('i', 'İ'), ('ğ', 'Ğ'), ('ü', 'Ü'), ('ş', 'Ş'), ('ö', 'Ö'), ('ç', 'Ç'),
            ('ı', 'I')
        ]
        for trKucuk, trBuyuk in TRHarfler:
            sozcuk = sozcuk.replace(trKucuk, trBuyuk)
        yeniSozcuk = sozcuk.upper()
        return yeniSozcuk

        #print(Helper.KucukHarfleriBuyukYap("qwertyuıopğüasdfghjklşizxcvbnmöç"))
        #print("QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ")