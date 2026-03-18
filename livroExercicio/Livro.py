class Livro:
    def __init__(self, titulo, autor, ano_publicacao, paginas):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self._qtd_paginas = qtd_paginas

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor   

    def getAnoPublicacao(self):
        return self.ano_publicacao
    
    def getQtdPaginas(self):
        return self._qtd_paginas
    
    def __str__(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}, Quantidade de Páginas: {self._qtd_paginas}"
        
        