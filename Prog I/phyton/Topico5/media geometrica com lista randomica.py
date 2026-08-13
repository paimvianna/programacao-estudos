#entrada
from random import randrange
n = int(input('informe o numero de elementos da lista desde que seja maior que 1: '))
l=[]
produto = 1
#processamento
if n > 1:
    for i in range (n):
        l.append(randrange(1,5+1,1))
        produto *= l[i]
    #print(l)
    #print(produto)
    resultado = produto **(1/2)
#saida
print(f'{resultado:.2f}')