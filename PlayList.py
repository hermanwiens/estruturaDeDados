from Pilha import Stack
from Musica import Musica

class PlayList:
    def __init__(self, nome):
        self.nome = nome
        self._musicas = Stack()

    def adicionar_musica(self, musica):
        if not isinstance(musica, Musica):
            raise TypeError("Apenas objetos do tipo Musica podem ser adicionados")
        self._musicas.push(musica)
        print("Adicionando ", musica)

    def tocar(self):
        if self._musicas.is_empty():
            print("Playlist vazia.")
            return

        print(f"Iniciando playlist: {self.nome}")
        
        while not self._musicas.is_empty():
            musica = self._musicas.pop()
            print(f"Tocando: {musica}")

        print("Fim da playlist.")
