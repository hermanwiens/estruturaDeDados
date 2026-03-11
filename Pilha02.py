class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         if self.items:
             return self.items.pop()
         else:
            return None;

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def print(self):
         return print(self.items)

pilha = Stack()

pilha.push('ARA0098')
pilha.print()
pilha.push('ARA0068')
pilha.print()
pilha.push('ARA0078')
pilha.print()
print('Retirando o último elemento: ', pilha.pop())
print('Retirando o último elemento: ', pilha.pop())
print('Retirando o último elemento: ', pilha.pop())
print('Retirando o último elemento: ', pilha.pop())
pilha.print()
