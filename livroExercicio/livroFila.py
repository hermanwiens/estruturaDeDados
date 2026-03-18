from Fila import Queue  
from Livro import Livro

class livroFila:
    def __init__(self):
        self.fila = Queue()
        self.livros = Livro()
        
print("*** Criando uma fila")
fila = Queue()

print("*** Está vazia?", fila.is_empty())
print(fila)

def adicionar_livro(self, livro):
        if not isinstance(livro, Livro):
            raise TypeError("Apenas objetos do tipo Livro podem ser adicionados")
        self.fila.enqueue(livro)
        print("Adicionando ", livro)
 
#print("*** Adicionando elementos à fila")
#fila.enqueue("Dovahkiin", 385)
#fila.enqueue("O Senhor dos Anéis", 1178)
#fila.enqueue("Harry Potter e a Pedra Filosofal", 223)
#print(fila)


