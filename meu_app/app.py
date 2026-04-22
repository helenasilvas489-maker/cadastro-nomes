import json

def salvar_dados(nomes):
    with open("nomes.json", "w", encoding="utf-8") as f:
        json.dump(nomes, f, ensure_ascii=False, indent=4)

def carregar_dados():
    try:
        with open("nomes.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def mostrar_menu():
    print("\n" + "=" * 30)
    print("   SISTEMA DE CADASTRO")
    print("=" * 30)
    print("1 - Adicionar Nome")
    print("2 - Atualizar Nome")
    print("3 - Remover Nome")
    print("4 - Ver Lista")
    print("5 - Sair")
    print("=" * 30)

def listar_nomes(nomes):
    print("\n--- LISTA DE NOMES ---")
    if nomes:
        for i, nome in enumerate(nomes):
            print(f"{i} - {nome}")
    else:
        print("⚠️ Nenhum nome cadastrado.")

nomes = carregar_dados()

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Digite o nome: ").strip()
        if nome:
            nomes.append(nome)
            salvar_dados(nomes)
            print(f"✅ {nome} adicionado!")
        else:
            print("⚠️ Nome vazio.")

    elif opcao == "2":
        if nomes:
            listar_nomes(nomes)
            try:
                indice = int(input("Índice: "))
                if 0 <= indice < len(nomes):
                    novo = input("Novo nome: ").strip()
                    nomes[indice] = novo
                    salvar_dados(nomes)
                    print("✅ Atualizado!")
                else:
                    print("⚠️ Índice inválido.")
            except:
                print("⚠️ Erro.")
        else:
            print("⚠️ Lista vazia.")

    elif opcao == "3":
        if nomes:
            listar_nomes(nomes)
            try:
                indice = int(input("Índice: "))
                if 0 <= indice < len(nomes):
                    removido = nomes.pop(indice)
                    salvar_dados(nomes)
                    print(f"🗑️ {removido} removido.")
                else:
                    print("⚠️ Índice inválido.")
            except:
                print("⚠️ Erro.")
        else:
            print("⚠️ Nada para remover.")

    elif opcao == "4":
        listar_nomes(nomes)

    elif opcao == "5":
        print("👋 Saindo...")
        break

    else:
        print("⚠️ Opção inválida.")