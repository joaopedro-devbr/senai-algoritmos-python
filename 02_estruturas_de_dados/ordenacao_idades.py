pessoas = []

while True:
    print("\n--- CADASTRO DE PESSOA ---")
    nome = input("Digite o nome da pessoa: ").strip()
    idade = int(input("Digite a idade: "))

    pessoa = {"nome": nome, "idade": idade}
    pessoas.append(pessoa)

    opcao = input("Deseja cadastrar mais uma pessoa? (s/n): ").strip().lower()
    if opcao != 's':
        break

pessoas.sort(key=lambda pessoa: pessoa["idade"], reverse=True)

print("\n===== LISTA ORDENADA (Mais velho -> Mais novo) =====")
for i, p in enumerate(pessoas, start=1):
    print(f"{i} - {p['nome']}: {p['idade']} anos")