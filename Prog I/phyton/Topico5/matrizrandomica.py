#entrada
from random import randrange
linhas = int(input('informe o numero de linhas da matriz: '))
colunas = int(input('informe o numero de colunas da matriz: '))
soma = 0
m=[]
#processamento

for l in range (linhas):
    k=[]
    for c in range (colunas):
        k.append(randrange(0,1+1,1))
    m.append(k)
    soma + = m.append(k)
    #saida
for i in range (linhas):
    print(m[i])
