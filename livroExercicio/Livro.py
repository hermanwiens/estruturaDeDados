class Livro:
    def __init__(self, titulo, autor, ano_publicacao, paginas):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.paginas = paginas

    def getTitulo(self):
        return self.titulo
        
    def getAutor(self):
        return self.autor   

    def getAnoPublicacao(self):
        return self.ano_publicacao
    
    def getPaginas(self):
        return self.paginas
    
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano_publicacao})"