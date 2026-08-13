#entrada
n = int(input('informe os valores de entrada, para sair informe 0:'))
l=[]
l2=[]
while n != 0:
    if n % 2 == 0:
        l.append(n)
    else:
        l2.append(n)
    n = int(input('informe os valores de entrada, para sair informe 0:'))
print(l)
print(l2)