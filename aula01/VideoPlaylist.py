import webbrowser
import time
from Pilha import Stack

class Video:
    def __init__(self, titulo, url):
        self.titulo = titulo
        self.url = url

    def __str__(self):
        return f"{self.titulo}"


class PlayListVideos:
    def __init__(self, nome):
        self.nome = nome
        self._videos = Stack()

    def adicionar_video(self, video):
        self._videos.push(video)

    def tocar(self):
        if self._videos.is_empty():
            print("Playlist vazia.")
            return

        print(f"Iniciando playlist: {self.nome}")

        while not self._videos.is_empty():
            video = self._videos.pop()
            input(f"Pressione ENTER para tocar: {video}")
            webbrowser.open(video.url, new=0)
            time.sleep(10)

        print("Fim da playlist.")
