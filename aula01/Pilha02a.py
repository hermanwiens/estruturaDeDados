class Stack:
     ''' Implementa o TAD pilha usando list como base
         A pilha é uma estrutura lógica. A lista é apenas a estrutura física.”
     '''

     def __init__(self):
         self.items = []

     def is_empty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         if self.is_empty():
             raise IndexError("Tentando remover elemento de pilha vazia")
         else:
             return self.items.pop()

     def peek(self):
         if self.is_empty():
             raise IndexError("Tentando pegar referência para objeto no topo de uma lista vazia")
         return self.items[-1]

     def size(self):
         return len(self.items)

     def print(self):
         return print(self.items)

     def __str__(self):
         return str(self.items)

pilha = Stack()

try:
    pilha.push('ARA0098')
    pilha.print()
    pilha.push('ARA0068')
    pilha.print()
    pilha.push('ARA0078')
    print(pilha)
    print('Retirando o último elemento: ', pilha.pop())
    print(pilha)
    print('Retirando o último elemento: ', pilha.pop())
    print(pilha)
    print('Retirando o último elemento: ', pilha.pop())
    print(pilha)
    print('Retirando o último elemento: ', pilha.pop())
    print(pilha)
except IndexError as e : 
    print("Erro: ", e)
