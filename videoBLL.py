from entity import Video
import shutil
import os

class VideoBLL:

    @staticmethod
    def VideolariListele():
        pass

    @staticmethod
    def VideoSil(silinecekVideo=Video()):
        try:

            print("Silinecek video")
            print(silinecekVideo.secilenKelimeVideoYol)
            if os.path.exists(silinecekVideo.secilenKelimeVideoYol):
                os.remove(silinecekVideo.secilenKelimeVideoYol)
                return 1
            else:
                print("Video bulunamadığı için Silemedim.")
                return -1
        except Exception as exp:
            print("Hata oluştuğu için video silinemedi..")
            print(exp)
            return 0


    @staticmethod
    def VideoKopyala(video=Video()):
        try:
            print(video.videoKaynakYol)
            print(video.videoHedefYol)
            shutil.copy(video.videoKaynakYol, video.videoHedefYol)
            print("video kopyalandı.")
            return True
        except Exception as exp:
            print(exp)
            return False