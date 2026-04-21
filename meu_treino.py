# Criamos uma lista vazia para armazenar os nomes
nomes = []
# Loop infinito (o programa só para quando o usuário escolher sair)

while True:
    
   # Exibe o menu de opções
    print("\n1 - Adicionar nome")
    print("2 - Listar nomes")
    print("3 - Buscar nome")
    print("4 - Remover nome")
    print("5 - Salvar em arquivo")
    print("6 - Carregar nomes")
    print("0 - Sair")

     # Captura a opção digitada pelo usuário
    opcao = input("Escolha uma opção: ")

     # -------------------------------
    # OPÇÃO 1 - ADICIONAR NOME
    # -------------------------------
    if opcao == "1":
        nome = input("Digite o nome: ")  # pede o nome
        nomes.append(nome)  # adiciona o nome na lista
        print("Nome adicionado com sucesso!")
         # -------------------------------
    # OPÇÃO 2 - LISTAR NOMES
    # -------------------------------
    elif opcao == "2":
        print("\nLista de nomes:")
        # verifica se a lista está vazia
        if len(nomes) == 0:
            print("Nenhum nome cadastrado.")
        else:
            # percorre a lista e mostra cada nome
            for nome in nomes:
                print(nome)
                # -------------------------------
    # OPÇÃO 3 - BUSCAR NOME
    # -------------------------------
    elif opcao == "3":
        busca = input("Digite o nome para buscar: ")

        # verifica se o nome está na lista
        if busca in nomes:
            print("Nome encontrado!")
        else:
            print("Nome não encontrado.")

    # -------------------------------
    # OPÇÃO 4 - REMOVER NOME
    # -------------------------------
    elif opcao == "4":
        remover = input("Digite o nome para remover: ")

        # verifica se o nome existe antes de remover
        if remover in nomes:
            nomes.remove(remover)  # remove o nome
            print("Nome removido com sucesso!")
        else:
            print("Nome não encontrado.")

    # -------------------------------
    # OPÇÃO 5 - SALVAR EM ARQUIVO
    # -------------------------------
    elif opcao == "5":
        # abre (ou cria) o arquivo nomes.txt no modo escrita
        with open("nomes.txt", "w") as arquivo:

            # percorre a lista e escreve cada nome no arquivo
            for nome in nomes:
                arquivo.write(nome + "\n")

        print("Nomes salvos no arquivo!")

    # -------------------------------
    # OPÇÃO 6 - CARREGAR DO ARQUIVO
    # -------------------------------
    elif opcao == "6":
        try:
            # abre o arquivo no modo leitura
            with open("nomes.txt", "r") as arquivo:

                # lê todas as linhas do arquivo
                linhas = arquivo.readlines()

                # limpa a lista antes de carregar
                nomes.clear()

                # percorre cada linha
                for linha in linhas:
                    nomes.append(linha.strip())  # remove quebra de linha

            print("Nomes carregados com sucesso!")

        except FileNotFoundError:
            # caso o arquivo não exista
            print("Arquivo não encontrado.")

    # -------------------------------
    # OPÇÃO 0 - SAIR
    # -------------------------------
    elif opcao == "0":
        print("Saindo do programa...")
        break  # encerra o loop

    # -------------------------------
    # OPÇÃO INVÁLIDA
    # -------------------------------
    else:
        print("Opção inválida, tente novamente.")