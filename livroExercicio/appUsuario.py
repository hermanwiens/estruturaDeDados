from Livro import Livro 
from livroFila import livroFila

lf = livroFila()

while True:
    print("\nMenu:")
    print("1. Adicionar livro")
    print("2. Marcar livro como lido")
    print("3. Mostrar livros na fila")
    print("4. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        titulo = input("Digite o título do livro: ")
        paginas = int(input("Digite a quantidade de páginas: "))
        livro = Livro(titulo, paginas)
        lf.adicionar_livro(livro)
    elif escolha == '2':
        lf.marcarLivroLido()
    elif escolha == '3':
        lf.mostraLivros()
    elif escolha == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

