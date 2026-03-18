class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self._qtd_paginas = paginas

    def getTitulo(self):
        return self.titulo

    def getQtdPaginas(self):
        return self._qtd_paginas
    
    def __str__(self):
        return f"Livro: {self.titulo}, Quantidade de Páginas: {self._qtd_paginas}"
        
        