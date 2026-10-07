pessoas = []

while True:
    print("\n--- CADASTRO DE PESSOA ---")
    nome = input("Digite o nome da pessoa: ").strip()
    peso = float(input("Digite o peso (em kg): "))

    pessoa = {"nome": nome, "peso": peso}

    pessoas.append(pessoa)

    opcao = input("Deseja cadastrar mais uma pessoa: (s/n): ").strip().lower()
    if opcao != 's':
        break

pessoas.sort(key=lambda pessoa: pessoa["peso"])

print("\n===== LISTA ORDENADA (Mais leve -> Mais pesado) =====")
for i, p in enumerate (pessoas, start=1):
    print(f"{i} - {p['nome']}: {p['peso']} kg")