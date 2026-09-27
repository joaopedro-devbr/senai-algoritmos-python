nome = []
idade = []

quantidadeUsuarios = 0
opcao = 0

while opcao != 3:

    print("===== MENU =====")
    print("1 - Cadastrar novo usuario")
    print("2 - Listar todos os usuarios")
    print("3 - Sair do sistema")

    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:

        nome.append(input("Nome: "))
        idade.append(int(input("Idade: ")))

        quantidadeUsuarios += 1

        print("Usuario cadastrado com sucesso!")

    elif opcao == 2:
        if quantidadeUsuarios == 0:
            print("Nenhum usuario cadastrado.")

        else:    
            print("===== USUARIOS CADASTRADOS =====")

            for i in range(quantidadeUsuarios):
                print("Nome: ", nome[i])
                print("Idade: ", idade[i])
                print("-------------------")

    elif opcao == 3:
        print("Saindo do sistema...")

    else:
        print("Opcao invalida!")   