class Queue:
    def __init__(self):
        self._itens = []
    
    def is_empty(self):
        return len(self._itens) == 0
    
    def enqueue(self, item):#enqueue append acressenta um item no final da lista
        self._itens.append(item)
    
    def dequeue(self):#dequeue pop tira da fila 
        if not self.is_empty():
            return self._itens.pop(0)
        else:
            raise IndexError("A fila está vazia.")
    
    def size(self):
        return len(self._itens)
    
    def peek(self):
        if not self.is_empty():
            return self._itens[0]
        else:
            raise IndexError("A fila está vazia.")
    
    def __str__(self):
        return str(self._itens)