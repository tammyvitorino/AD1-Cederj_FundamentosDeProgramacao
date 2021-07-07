# CEDERJ - Sistemas da Computação • Pólo Saquarema
# Aluna: Tamara da Silva Teixeira Vitorino - Matrícula 16213050208

#Subprograma
def fofoca(ambientes,n,m):
    y = 1
    while y != 0:
        k = 0
        for i in range(0,n) :
            for j in range(0,m) :
                if ambientes[i][j] == 'I' :
                    if i >= 0 and i < n - 1 :
                        if ambientes[i + 1][j] == 'F':
                            ambientes[i + 1][j] = 'I'
                            k = k + 1
                    if i > 0 and i <= n - 1:
                        if ambientes[i - 1][j] == 'F':
                            ambientes[i - 1][j] = 'I'
                            k = k + 1
                    if j >= 0 and j < m - 1:
                        if ambientes[i][j + 1] == 'F':
                            ambientes[i][j + 1] = 'I'
                            k = k + 1
                    if j > 0 and j <= m - 1:
                        if ambientes[i][j - 1] == 'F':
                            ambientes[i][j - 1] = 'I'
                            k = k + 1
        y = k
    return ambientes

#ProgramaPrincipal
tamanho = input().split()
n = int(tamanho[0]) #linhas
m = int(tamanho[1]) #colunas
ambientes = []

while n != 0 and m != 0:
    subambiente = []
    for i in range(0,n):
        temporario = [None] * m
        linha = input()
        for j in range(0,m):
            temporario[j] = linha[j]
        subambiente.append(temporario)

    subambiente = fofoca(subambiente,n,m)

    for k in range(0,len(subambiente)):
        ambientes.append(subambiente[k])
    ambientes.append("")
    tamanho = input().split()
    n = int(tamanho[0])  # linhas
    m = int(tamanho[1])  # colunas

for i in range(0,len(ambientes)):
    print(*ambientes[i],sep=' ')




