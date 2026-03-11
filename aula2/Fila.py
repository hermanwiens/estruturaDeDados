class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def peek(self):
        return self._items[0]

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

