# CEDERJ - Sistemas da Computação • Pólo Saquarema
# Aluna: Tamara da Silva Teixeira Vitorino - Matrícula 16213050208

qtde = int(input())

if qtde > 0:
    x = [None] * qtde
    y = [None] * qtde

    for i in range(0, qtde):
        coordenada = input().split()
        x[i] = int(coordenada[0])
        y[i] = int(coordenada[1])

    # pontos dentro do retângulo
    pontos = []
    contador = 0
    for i in range(0, qtde):
        if min(x) < x[i] < max(x) // 2 and min(y) < y[i] < max(y) // 2:
            pontos.append(str(x[i]) + " " + str(y[i]))
            contador += 1

print("xMin = ", min(x))
print("yMin = ", min(y))
print("xMax = ", max(x))
print("yMax = ", max(y))
print("Pontos dentro do retângulo:")
print(*pontos, sep=' , ')
print("Total de Pontos:", contador)
