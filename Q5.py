# CEDERJ - Sistemas da Computação • Pólo Saquarema
# Aluna: Tamara da Silva Teixeira Vitorino - Matrícula 16213050208

# Subprogramas
def saida(x, y, anteriores):
    anteriores.append(str(x) + "," + str(y))
    if (not (0 <= x < int(dimensao[0]))) or (not (0 <= y < int(dimensao[1]))) or (anteriores.count(str(x) + "," + str(y)) != 1):
        print("Esse mapa não leva a lugar algum")
        exit()
    return i

def coord(x, y, mapa):
    if i != "saida encontrada":
        ponto = mapa[y][x]
        return ponto

# ProgramaPrincipal
dimensao = input().split()
mapa = [None] * int(dimensao[1])
validos = ['>', '<', 'v', '^', '.', '*']

for i in range(0, int(dimensao[1])):
    area = [None] * int(dimensao[0])
    x = input()
    for j in range(0, int(dimensao[0])):
        if x[j] in validos:
            area[j] = x[j]
        else:
            exit()
    mapa[i] = area

verificaBau = 0
for i in range(0, len(mapa)):
    verificaBau = verificaBau + mapa[i].count('*')

if verificaBau != 1 or ((mapa[0][0] != 'v') and (mapa[0][0] != '>')):
    print("Esse mapa não leva a lugar algum")
else:
    x, y = 0, 0
    ponto = mapa[y][x]
    anteriores = ['0,0']
    while i != "saida encontrada":
        if ponto == '>':
            while ponto == '>' or ponto == '.':
                x = x + 1
                i = saida(x, y, anteriores)
                ponto = coord(x, y, mapa)
        elif ponto == '<':
            while ponto == '<' or ponto == '.':
                x = x - 1
                i = saida(x, y, anteriores)
                ponto = coord(x, y, mapa)
        elif ponto == 'v':
            while ponto == 'v' or ponto == '.':
                y = y + 1
                i = saida(x, y, anteriores)
                ponto = coord(x, y, mapa)
        elif ponto == '^':
            while ponto == '^' or ponto == '.':
                y = y - 1
                i = saida(x, y, anteriores)
                ponto = coord(x, y, mapa)
        elif ponto == '*':
            print("Esse mapa leva ao tesouro")
            i = "saida encontrada"