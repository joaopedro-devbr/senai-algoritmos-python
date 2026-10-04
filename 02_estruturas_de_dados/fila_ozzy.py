def vazia(fila):
    return len(fila) == 0

def adicionar(fila, nome, limite=25):
    if len(fila) < limite:
        fila.append(nome)
        print(f"'{nome}' foi adicionado ao final da fila!")
    else:
        print("Erro: A fila está cheia! Estouro evitado (limite de 25 posições).")

def remover(fila):
    if not vazia(fila):
        nome_removido = fila.pop(0)
        print(f"'{nome_removido}' foi removido do início da fila.")
        return nome_removido
    else:
        print("Erro: A fila está vazia! Nenhum elemento para remover.")
        return None

def limpar(fila):
    fila.clear()
    print("A fila foi limpa com sucesso!")

def listar(fila):
    if vazia(fila):
        print("A fila está vazia.")
    else:
        print("\n===== ELEMENTOS NA FILA (Início -> Fim) =====")
        for i, nome in enumerate(fila):
            print(f"Posição {i}: {nome}")
        print("---------------------------------------------")

fila_nomes = []
LIMITE_FILA = 25
opcao = 0

while opcao != 6:
    print("\n===== OZZY - SISTEMA DE FILA =====")
    print("1 - Adicionar nome (Final)")
    print("2 - Remover nome (Início)")
    print("3 - Listar fila")
    print("4 - Verificar se a fila está vazia")
    print("5 - Limpar fila")
    print("6 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, introduza um número válido.")
        continue

    if opcao == 1:
        nome_input = input("Digite o nome para adicionar à fila: ").strip()
        if nome_input:
            adicionar(fila_nomes, nome_input, LIMITE_FILA)
        else:
            print("Nome não pode ser vazio!")

    elif opcao == 2:
        remover(fila_nomes)

    elif opcao == 3:
        listar(fila_nomes)

    elif opcao == 4:
        if vazia(fila_nomes):
            print("A fila está VAZIA.")
        else:
            print(f"A fila NÃO está vazia. Possui {len(fila_nomes)} elemento(s).")

    elif opcao == 5:
        limpar(fila_nomes)

    elif opcao == 6:
        print("A encerrar o sistema da Ozzy...")

    else:
        print("Opção inválida! Tente novamente.")