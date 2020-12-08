import sqlite3
from helper import Helper


def yolDondur(kelime):
    conn = sqlite3.connect('Sozluk.db')
    cur = conn.cursor()
    cur.execute("SELECT KELIME_YOLU FROM KELIMELER WHERE KELIME_ADI=?",
                [Helper.KucukHarfleriBuyukYap(kelime)])
    data = cur.fetchone()
    return data[0]

