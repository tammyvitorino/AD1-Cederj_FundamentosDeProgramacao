# CEDERJ - Sistemas da Computação • Pólo Saquarema
# Aluna: Tamara da Silva Teixeira Vitorino - Matrícula 16213050208

def soma(x):
    y = 0
    for i in range(1,x):
       if x%i == 0:
            y = y + i
    if y == x:
        return True
    return False

qtdeTestes = int(input())
numeros = [None] * qtdeTestes

for i in range(0,qtdeTestes):
    numeros[i] = int(input())

for j in range(0,len(numeros)):
    resultado = soma(numeros[j])
    if resultado == True:
        print(numeros[j], "é perfeito")
    else:
        print(numeros[j], "não é perfeito")