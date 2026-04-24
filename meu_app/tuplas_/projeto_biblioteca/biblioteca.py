#  Sistema de Biblioteca em Python
# Aqui eu crio um sistema simples para cadastrar, listar, buscar e remover livros
# Os dados ficam salvos em um arquivo JSON

import json  # Aqui eu importo o JSON para salvar e carregar dados

#  Função para carregar os livros do arquivo
def carregar_dados():
    try:
        # Aqui eu tento abrir o arquivo JSON
        with open("livros.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)  # Aqui eu retorno os dados do arquivo
    except FileNotFoundError:
        # Se o arquivo não existir, eu começo com uma lista vazia
        return []

#  Função para salvar os livros no arquivo
def salvar_dados():
    # Aqui eu salvo a lista de livros no arquivo JSON
    with open("livros.json", "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, indent=4, ensure_ascii=False)

#  Aqui eu carrego os livros salvos ou começo vazio
livros = carregar_dados()

#  Função para listar livros
def listar_livros():
    # Aqui eu verifico se existe algum livro cadastrado
    if not livros:
        print("\n Nenhum livro cadastrado.")
        return

    print("\n Lista de livros:")
    # Aqui eu percorro todos os livros com numeração
    for i, livro in enumerate(livros, start=1):
        print(f"{i}. {livro[0]} | {livro[1]} | {livro[2]}")

#  Função para adicionar livro
def adicionar_livro():
    print("\n Cadastro de novo livro")

    # Aqui eu peço os dados ao usuário
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))

    # Aqui eu adiciono o livro como tupla dentro da lista
    livros.append((titulo, autor, ano))

    # Aqui eu salvo automaticamente no arquivo
    salvar_dados()

    print(" Livro cadastrado com sucesso!")

#  Função para buscar por autor
def buscar_por_autor():
    # Aqui eu peço o nome do autor
    autor = input("\nDigite o autor: ").lower()

    encontrados = False  # Aqui eu controlo se encontrei algum livro

    # Aqui eu percorro todos os livros
    for livro in livros:
        # Aqui eu comparo o autor ignorando maiúsculas/minúsculas
        if livro[1].lower() == autor:
            print(f" {livro[0]}")
            encontrados = True

    # Se não encontrar nenhum livro
    if not encontrados:
        print(" Nenhum livro encontrado.")

#  Função para remover livro
def remover_livro():
    # Aqui eu mostro os livros primeiro
    listar_livros()

    if not livros:
        return

    try:
        # Aqui eu peço o número do livro
        indice = int(input("\nDigite o número do livro para remover: ")) - 1

        # Aqui eu verifico se o índice é válido
        if 0 <= indice < len(livros):
            removido = livros.pop(indice)  # Aqui eu removo o livro
            salvar_dados()  # Aqui eu salvo a alteração
            print(f" Livro '{removido[0]}' removido com sucesso!")
        else:
            print(" Número inválido.")
    except ValueError:
        print(" Digite um número válido.")

#  Menu principal do sistema
def menu():
    # Aqui eu deixo o sistema rodando até o usuário sair
    while True:
        print("\n=================================")
        print(" SISTEMA DE BIBLIOTECA")
        print("=================================")
        print("1 - Listar livros")
        print("2 - Adicionar livro")
        print("3 - Buscar por autor")
        print("4 - Remover livro")
        print("0 - Sair")

        # Aqui eu recebo a opção do usuário
        opcao = input("Escolha uma opção: ")

        # Aqui eu direciono para cada função
        if opcao == "1":
            listar_livros()
        elif opcao == "2":
            adicionar_livro()
        elif opcao == "3":
            buscar_por_autor()
        elif opcao == "4":
            remover_livro()
        elif opcao == "0":
            print("👋 Saindo do sistema...")
            break
        else:
            print(" Opção inválida!")

#  Aqui eu inicio o programa
menu()#  Sistema de Biblioteca em Python
# Aqui eu crio um sistema simples para cadastrar, listar, buscar e remover livros
# Os dados ficam salvos em um arquivo JSON

import json  # Aqui eu importo o JSON para salvar e carregar dados

#  Função para carregar os livros do arquivo
def carregar_dados():
    try:
        # Aqui eu tento abrir o arquivo JSON
        with open("livros.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)  # Aqui eu retorno os dados do arquivo
    except FileNotFoundError:
        # Se o arquivo não existir, eu começo com uma lista vazia
        return []

#  Função para salvar os livros no arquivo
def salvar_dados():
    # Aqui eu salvo a lista de livros no arquivo JSON
    with open("livros.json", "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, indent=4, ensure_ascii=False)

#  Aqui eu carrego os livros salvos ou começo vazio
livros = carregar_dados()

#  Função para listar livros
def listar_livros():
    # Aqui eu verifico se existe algum livro cadastrado
    if not livros:
        print("\n Nenhum livro cadastrado.")
        return

    print("\n Lista de livros:")
    # Aqui eu percorro todos os livros com numeração
    for i, livro in enumerate(livros, start=1):
        print(f"{i}. {livro[0]} | {livro[1]} | {livro[2]}")

#  Função para adicionar livro
def adicionar_livro():
    print("\n➕ Cadastro de novo livro")

    # Aqui eu peço os dados ao usuário
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))

    # Aqui eu adiciono o livro como tupla dentro da lista
    livros.append((titulo, autor, ano))

    # Aqui eu salvo automaticamente no arquivo
    salvar_dados()

    print(" Livro cadastrado com sucesso!")

#  Função para buscar por autor
def buscar_por_autor():
    # Aqui eu peço o nome do autor
    autor = input("\nDigite o autor: ").lower()

    encontrados = False  # Aqui eu controlo se encontrei algum livro

    # Aqui eu percorro todos os livros
    for livro in livros:
        # Aqui eu comparo o autor ignorando maiúsculas/minúsculas
        if livro[1].lower() == autor:
            print(f" {livro[0]}")
            encontrados = True

    # Se não encontrar nenhum livro
    if not encontrados:
        print(" Nenhum livro encontrado.")

#  Função para remover livro
def remover_livro():
    # Aqui eu mostro os livros primeiro
    listar_livros()

    if not livros:
        return

    try:
        # Aqui eu peço o número do livro
        indice = int(input("\nDigite o número do livro para remover: ")) - 1

        # Aqui eu verifico se o índice é válido
        if 0 <= indice < len(livros):
            removido = livros.pop(indice)  # Aqui eu removo o livro
            salvar_dados()  # Aqui eu salvo a alteração
            print(f" Livro '{removido[0]}' removido com sucesso!")
        else:
            print(" Número inválido.")
    except ValueError:
        print(" Digite um número válido.")

#  Menu principal do sistema
def menu():
    # Aqui eu deixo o sistema rodando até o usuário sair
    while True:
        print("\n=================================")
        print(" SISTEMA DE BIBLIOTECA")
        print("=================================")
        print("1 - Listar livros")
        print("2 - Adicionar livro")
        print("3 - Buscar por autor")
        print("4 - Remover livro")
        print("0 - Sair")

        # Aqui eu recebo a opção do usuário
        opcao = input("Escolha uma opção: ")

        # Aqui eu direciono para cada função
        if opcao == "1":
            listar_livros()
        elif opcao == "2":
            adicionar_livro()
        elif opcao == "3":
            buscar_por_autor()
        elif opcao == "4":
            remover_livro()
        elif opcao == "0":
            print("👋 Saindo do sistema...")
            break
        else:
            print(" Opção inválida!")

# Aqui eu inicio o programa
menu()

