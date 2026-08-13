#entrada
n = int(input('informe os valores de entrada, para sair informe 0:'))
#processamento
l=[]
while n != 0:
    l.append(n)
    n = int(input('informe os valores de entrada, para sair informe 0:'))
l2 = []
for i in l:
    if i not in l2:
        l2.append(i)
a=len(l2)
#saida
for i in range(a):
    print(l2[i])
'''
for i in l2:
    print (i)
'''