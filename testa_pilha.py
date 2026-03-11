from Pilha import Stack

pilha = Stack()

print("Está vazia?", pilha.is_empty())

pilha.push(10)
pilha.push(12)

print("Está vazia?", pilha.is_empty())

print("Qual o elemento no topo da pilha?", pilha.peek())

print(pilha)

pilha.pop()

print(pilha)

