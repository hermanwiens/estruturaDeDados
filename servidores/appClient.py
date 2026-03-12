import xmlrpc.client

# Conectar-se ao servidor
servidor = xmlrpc.client.ServerProxy("http://localhost:8000", allow_none=True)

def menu():
    while True:
        print("\n=== MENU FOOD TRUCK ===")
        print("1. Fazer um pedido")
        print("2. Ver fila de pedidos")
        print("3. Consultar posição do pedido")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            fazer_pedido()
        elif escolha == "2":
            ver_fila()
        elif escolha == "3":
            consultar_pedido()
        elif escolha == "4":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def fazer_pedido():
    print("Itens disponíveis: Bauru, Cachorro-quente, Hamburguer, Batata frita, X-tudo")
    itens = input("Digite os itens do pedido (separados por vírgula): ").split(',')
    pedido = [item.strip() for item in itens if item.strip()]
    
    if not pedido:
        print("Pedido inválido! Lista vazia.")
        return
    
    id_pedido = servidor.adicionar_pedido(pedido)
    print(f"Pedido {id_pedido} adicionado com sucesso!")

def ver_fila():
    fila = servidor.pedidos_na_fila()
    if fila:
        print("Pedidos na fila:", fila)
    else:
        print("Nenhum pedido na fila!")

def consultar_pedido():
    try:
        id_pedido = int(input("Digite o número do pedido: "))
        posicao = servidor.consultar_pedido(id_pedido)
        if posicao == -1:
            print(f"Pedido {id_pedido} não encontrado!")
        else:
            print(f"Pedido {id_pedido} está na posição {posicao} da fila.")
    except ValueError:
        print("Número de pedido inválido!")

if __name__ == "__main__":
    menu()

