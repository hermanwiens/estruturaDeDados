from Pilha import Stack
from Musica import Musica

pilha = Stack()

pilha.push(Musica("Maracatu Atômico", 284, "Chico Science"))
pilha.push(Musica("Espirito da Mata", 201, "Mestre Ambrosio"))
pilha.push(Musica("Manguetow", 159, "Paralamas do Sucesso"))

while not pilha.is_empty() :

   musica = pilha.pop()
   print("Tocando ", musica)

print("Fim da playlist")

