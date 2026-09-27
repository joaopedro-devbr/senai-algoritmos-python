def vazia(pilha):
    return len(pilha) == 0

def empilhar(pilha, nome, limite=20):
    if len(pilha) < limite:
        pilha.append(nome)
        print(f"'{nome}' empilhado com sucesso!")
    else:
        print("Erro: A pilha está cheia! Estouro de pilha evitado (limite de 20 posições).")

def desempilhar(pilha):
    if not vazia(pilha):
        nome_removido = pilha.pop()
        print(f"'{nome_removido}' foi removido do topo da pilha.")
        return nome_removido
    else:
        print("Erro: A pilha está vazia! Nenhum elemento para desempilhar.")
        return None

def limpar(pilha):
    pilha.clear()
    print("A pilha foi limpa com sucesso!")

def listar(pilha):
    if vazia(pilha):
        print("A pilha está vazia.")
    else:
        print("\n===== ELEMENTOS NA PILHA (Topo -> Base) =====")
        for i in range(len(pilha) - 1, -1, -1):
            print(f"Posição {i}: {pilha[i]}")
        print("---------------------------------------------")


pilha_nomes = []
LIMITE_PILHA = 20
opcao = 0

while opcao != 6:
    print("\n===== OZZE - SISTEMA DE PILHA =====")
    print("1 - Empilhar nome")
    print("2 - Desempilhar nome")
    print("3 - Listar pilha")
    print("4 - Verificar se a pilha está vazia")
    print("5 - Limpar pilha")
    print("6 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, introduza um número válido.")
        continue

    if opcao == 1:
        nome_input = input("Digite o nome para empilhar: ").strip()
        if nome_input:
            empilhar(pilha_nomes, nome_input, LIMITE_PILHA)
        else:
            print("Nome não pode ser vazio!")

    elif opcao == 2:
        desempilhar(pilha_nomes)

    elif opcao == 3:
        listar(pilha_nomes)

    elif opcao == 4:
        if vazia(pilha_nomes):
            print("A pilha está VAZIA.")
        else:
            print(f"A pilha NÃO está vazia. Possui {len(pilha_nomes)} elemento(s).")

    elif opcao == 5:
        limpar(pilha_nomes)

    elif opcao == 6:
        print("A encerrar o sistema da Ozzy...")

    else:
        print("Opção inválida! Tente novamente.")
