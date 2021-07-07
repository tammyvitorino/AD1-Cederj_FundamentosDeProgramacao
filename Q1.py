# CEDERJ - Sistemas da Computação • Pólo Saquarema
# Aluna: Tamara da Silva Teixeira Vitorino - Matrícula 16213050208

valores = input().split()
x = float(valores[0])  # primeiro valor
y = float(valores[1])  # segundo valor

if x == 0 and y == 0:
    print("Não existem pontos!")

else:
    a, b = [], []
    while x != 0 or y != 0:
        a.append(x)
        b.append(y)
        valores = input().split()
        x = float(valores[0])  # primeiro valor
        y = float(valores[1])  # segundo valor

    somaa, somab = 0, 0

    for i in range(0, len(a)):
        somaa = somaa + a[i]
        somab = somab + b[i]

    print("%1.2f" % (somaa / len(a)), "%1.2f" % (somab / len(b)))
