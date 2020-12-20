import os
import platform


def videoyuOynat(self, video):
    self.progress.hide()
    self.videoWidget.show()

    if platform.system() == 'Darwin':
        videoRp = video.replace('\\', '/')
        path = os.path.abspath(videoRp)
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile(path)))
    else:
        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile(video)))

    self.mediaPlayer.play()