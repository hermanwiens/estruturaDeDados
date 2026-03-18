from Fila import Queue  
from Livro import Livro

class livroFila:
    def __init__(self):
        self.fila = Queue()
        self.livros_lidos = []

    def adicionar_livro(self, livro):
        if not isinstance(livro, Livro):
            raise TypeError("Apenas objetos do tipo Livro podem ser adicionados")
        self.fila.enqueue(livro)
        print("Adicionando ", livro)
 
    def marcarLivroLido(self):
        if self.fila.is_empty():
            print("Não há livros na fila para marcar como lido.")
            return
        livro_lido = self.fila.dequeue()
        print("Livro marcado como lido: ", livro_lido)

    def mostraLivros(self):
        if self.fila.is_empty():
            print("Não há livros na fila.")
            return
        print("Livros na fila:")
        for livro in self.fila._itens:
            print(livro)

