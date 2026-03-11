from Fila import Queue

print("*** Criando uma fila")
fila = Queue()

print("*** Está vazia?", fila.is_empty())
print(fila)

print("*** Adicionando elementos à fila")

fila.enqueue("Dovahkiin")
print(fila)

fila.enqueue("Ulfric Stormcloak")
print(fila)

fila.enqueue("Arngeir")
print(fila)

fila.enqueue("Alduin")
print(fila)

fila.enqueue("Paarthurnax")
print(fila)

fila.enqueue("Delphine")
print(fila)

fila.enqueue("Esbern")
print(fila)

fila.enqueue("Astrid")
print(fila)

fila.enqueue("Brynjolf")
print(fila)

fila.enqueue("Arquimago Savos Aren")
print(fila)

fila.enqueue("General Tullius")
print(fila)

fila.enqueue("Kodlak Whitemane")
print("*** Está vazia?", fila.is_empty())

print(fila)

print("**** Removendo elementos da fila")

while not fila.is_empty():
    print(f"*** Saindo da fila > {fila.dequeue()}");
    print(f"Fila atual: {fila}\n")

