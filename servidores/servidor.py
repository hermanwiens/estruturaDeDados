from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading
import time
from datetime import datetime
from Fila import Queue

# Classe para tratar requisições (restrita ao caminho /RPC2)

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)

# Fila de pedidos

fila_pedidos = Queue()
proximo_id = 1
pedidos_em_processamento = {}

# Função para adicionar um pedido à fila
def adicionar_pedido(pedido):
    global proximo_id
    pedido_id = proximo_id
    proximo_id += 1
    fila_pedidos.enqueue((pedido_id, pedido))
    print(f"Pedido {pedido_id} adicionado: {pedido}")
    return pedido_id

# Função para pegar o número de pedidos na fila
def pedidos_na_fila():
    return fila_pedidos.size()

# Função para consultar a posição de um pedido na fila

def consultar_pedido(pedido_id):
    if fila_pedidos:
        for pos, (id_pedido, _) in enumerate(fila_pedidos):
            print(pos, id_pedido)
            if id_pedido == pedido_id:
                return pos + 1  # Posição na fila começa em 1
        return -1  # Pedido não encontrado
    return -1

# Função para um chapeiro solicitar um pedido

def solicitar_pedido(chapeiro_id):
    if fila_pedidos.size() > 0:
        print("Tem pedido na fila...")
        pedido_id, pedido = fila_pedidos.dequeue()
        pedidos_em_processamento[pedido_id] = {
            "chapeiro": chapeiro_id,
            "pedido": pedido,
            "inicio": datetime.now(),
            "conclusao": None
        }
        print(f"Chapeiro {chapeiro_id} pegou pedido {pedido_id}: {pedido}")
        return pedido_id, pedido
    return None, None

# Função para um chapeiro informar que concluiu um pedido

def liberar_pedido(pedido_id):
    if pedido_id in pedidos_em_processamento:
        pedidos_em_processamento[pedido_id]["conclusao"] = datetime.now()
        print(f"Pedido {pedido_id} concluído por chapeiro {pedidos_em_processamento[pedido_id]['chapeiro']}")
        return True
    return False

# Inicia o servidor XML-RPC

server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler, allow_none=True)
print("Servidor Food Truck rodando na porta 8000...")

# Registra as funções no servidor

server.register_function(adicionar_pedido, "adicionar_pedido")
server.register_function(pedidos_na_fila, "pedidos_na_fila")
server.register_function(consultar_pedido, "consultar_pedido")
server.register_function(solicitar_pedido, "solicitar_pedido")
server.register_function(liberar_pedido, "liberar_pedido")

# Inicia o loop do servidor

server.serve_forever()

