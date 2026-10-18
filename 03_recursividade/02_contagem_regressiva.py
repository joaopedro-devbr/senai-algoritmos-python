# Função recursiva que recebe um inteiro positivo N, imprime a contagem regressiva até 0 e exibe "Decolar!" no final.

def contagem_regressiva(n):
    if n < 0:
        print("Decolar!")
        return

    print(n)

    contagem_regressiva(n - 1)

n = 5
contagem_regressiva(n)
