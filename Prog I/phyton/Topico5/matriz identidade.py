#entrada
from random import randrange
linhas = int(input('informe o numero de linhas da matriz: '))
colunas = int(input('informe o numero de colunas da matriz: '))
d = 0
soma = 0
m=[]
#processamento
if linhas > 1 and colunas > 1 :
    for l in range (linhas):
        k=[]
        for c in range (colunas):
            valor = int(input('informe o valor da unidade: '))
            k.append(valor)
        m.append(k)

    #saida
    for i in range (linhas):
        for j in range (colunas):
            if linhas == colunas and (i == j and m[i][j] == 1 or i != j and m[i][j] == 0):
                d += 1
            soma += m[i][j]
        print(m[i])
    print(d) #contador que verifica quantos testes foram realizados e validados.
    if soma != 0:
        if d == linhas * colunas:
            print('E uma matriz identidade, não nula.')
        else:
            print('Não é uma matriz identidade, mas é uma matriz não nula2.')
    else:
        print('Esta e uma matriz nula.')
else:
    print('valores de linhas e colunas não formam uma matriz.')