import xmlrpc.client
import time
from datetime import datetime

# Conectar ao servidor
servidor = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2")

# Identificador do chapeiro (pode ser único para cada instância)

chapeiro_id = input("Informe o ID do chapeiro: ")

# Lista os métodos que podem ser chamados no servidor

# print(servidor.system.listMethods())

fila = servidor.pedidos_na_fila()
if fila:
        print("Pedidos na fila:", fila)
else:
        print("Nenhum pedido na fila!")

while True:
    # Solicitar um pedido
    pedido_id, pedido = servidor.solicitar_pedido(chapeiro_id)
    
    if pedido_id:
        print(f"\n Chapeiro {chapeiro_id} pegou o pedido {pedido_id}: {pedido}")
        for i, item in enumerate(pedido, start=1):
            inicio = datetime.now().strftime("%H:%M:%S")
            print(f" Processando item {i}/{len(pedido)}: {item} (Início: {inicio})")
            time.sleep(60)  # Cada item leva 1 minuto para ser preparado
            fim = datetime.now().strftime("%H:%M:%S")
            print(f"Item {i}/{len(pedido)}: {item} concluído (Fim: {fim})")
        
        # Informar ao servidor que o pedido foi concluído
        servidor.liberar_pedido(pedido_id)
        print(f"Pedido {pedido_id} liberado! Aguardando novo pedido...\n")
    else:
        print("Nenhum pedido na fila. Aguardando 15 segundos...")
        time.sleep(15)
