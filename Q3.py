# CEDERJ - Sistemas da Computação • Pólo Saquarema
# Aluna: Tamara da Silva Teixeira Vitorino - Matrícula 16213050208

# Subprogramas
def matriz(y, x):
    from random import sample
    valores = []
    for j in range(0, y):
        linhas = sample(range(10, 99), x)
        valores.append(linhas)

    for j in range(0, y):
        print(*valores[j], sep=' ')

    for j in range(1, y - 1):
        for i in range(1, x - 1):
            if valores[j][i] < valores[j][i - 1] and valores[j][i] < valores[j][i + 1]:
                if valores[j][i] < valores[j - 1][i - 1] and valores[j][i] < valores[j - 1][i] and valores[j][i] < valores[j - 1][i + 1]:
                    if valores[j][i] < valores[j + 1][i - 1] and valores[j][i] < valores[j + 1][i] and valores[j][i] < valores[j + 1][i + 1]:
                        submatriz = [valores[j - 1][i - 1:i + 2], valores[j][i - 1:i + 2], valores[j + 1][i - 1:i + 2]]
                        print()
                        print(*submatriz[0], sep=' ')
                        print(*submatriz[1], sep=' ')
                        print(*submatriz[2], sep=' ')


# Programa Principal
dimensoes = input().split()
l = int(dimensoes[0])
c = int(dimensoes[1])

matriz(l, c)
