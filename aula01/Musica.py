class Musica:

     def __init__(self, nome, duracao, cantor):
         self.nome = nome
         self.duracao = duracao
         self.cantor = cantor

     def getNome(self):
         return self.nome 

     def getDuracao(self):
         return self.duracao

     def getCantor(self):
         return self.cantor 

     def __str__(self):
         return f"{self.nome} - {self.cantor} ({self.duracao}s)"
