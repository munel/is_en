import speech_recognition as sr

def sesTanimaFunc():
    mic = sr.Microphone()
    r = sr.Recognizer()
    algilanan = ""
    with mic as source:
        print("Dinleme Başladı Konuşun.")
        try:
            ses = r.listen(source, timeout=2, phrase_time_limit=2)
            algilanan = r.recognize_google(ses, language='tr-tr')
        except sr.WaitTimeoutError:
            print("Dinleme zaman aşımına uğradı")

        except sr.UnknownValueError:
            print("Ne dediğini anlayamadım")

        except sr.RequestError:
            print("İnternete bağlanamıyorum")
        finally:
            print("Dinleme Bitti")

    return algilanan
