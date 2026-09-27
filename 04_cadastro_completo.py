def buscar_usuario(nome_buscado, lista_nomes, lista_idades):
    for i in range(len(lista_nomes)):
        if lista_nomes[i].lower() == nome_buscado.lower():
            print(f"\n Usuário encontrado!")
            print(f"Nome: {lista_nomes[i]}")
            print(f"Idade: {lista_idades[i]}")
            return i
            
    return -1


def remover_usuario(nome_buscado, lista_nomes, lista_idades):
    posicao = buscar_usuario(nome_buscado, lista_nomes, lista_idades)
    
    if posicao != -1:
        lista_nomes.pop(posicao)
        lista_idades.pop(posicao)
        print("Usuário removido com sucesso!")
        return True
    else:
        print("\nUsuário não encontrado. Remoção não realizada.")
        return False


limite_usuarios = int(input("Quantas pessoas serão cadastradas? "))

nome = []
idade = []

quantidadeUsuarios = 0
opcao = 0

while opcao != 3:

    print("\n===== MENU =====")
    print("1 - Cadastrar novo usuario")
    print("2 - Listar todos os usuarios")
    print("4 - Buscar usuario pelo nome")
    print("5 - Remover usuario")
    print("3 - Sair do sistema")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        if quantidadeUsuarios < limite_usuarios:
            nome.append(input("Nome: "))
            idade.append(int(input("Idade: ")))
            
            quantidadeUsuarios += 1
            print("Usuario cadastrado com sucesso!")
        else:
            print(" Limite atingido! Não há posições disponíveis para novos cadastros.")

    elif opcao == 2:
        if quantidadeUsuarios == 0:
            print("Nenhum usuario cadastrado.")
        else:
            print("\n===== USUARIOS CADASTRADOS =====")
            for i in range(quantidadeUsuarios):
                print(f"Nome: {nome[i]}")
                print(f"Idade: {idade[i]}")
                print("-------------------")

    elif opcao == 4:
        if quantidadeUsuarios == 0:
            print("Nenhum usuario cadastrado para buscar.")
        else:
            nome_pesquisa = input("Digite o nome do usuário que deseja buscar: ")
            posicao = buscar_usuario(nome_pesquisa, nome, idade)
            
            if posicao == -1:
                print("\n Usuário não encontrado na pesquisa. (Retorno: -1)")
            else:
                print(f"Retorno da função (Posição no vetor): {posicao}")

    elif opcao == 5:
        if quantidadeUsuarios == 0:
            print("Nenhum usuario cadastrado para remover.")
        else:
            nome_remover = input("Digite o nome do usuário que deseja remover: ")
            
            if remover_usuario(nome_remover, nome, idade):
                quantidadeUsuarios -= 1

    elif opcao == 3:
        print("Saindo do sistema...")

    else:
        print("Opcao invalida!")