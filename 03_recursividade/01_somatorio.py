# Função recursiva que recebe um inteiro positivo N e calcula o somatório de todos os números de 1 até N.

def somatorio(n):
    if n <= 1:
        return n
    return n + somatorio(n - 1)

n = 5
resultado = somatorio(n)
print(f"O somatório de 1 até {n} é: {resultado}")
