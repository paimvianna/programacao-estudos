#entrada
n = int (input('informe um numero primo: '))
#Processamento
l=[]
for i in range (n):
    a = int(input('informe um valor inteiro: '))
    l.append(a)
pontocentral = n //2
numerocentral = l[pontocentral]
'''
f=numerocentral
for i in range(numerocentral-1,0,-1):
   f *= i
'''
f=1
for i in range (numerocentral,0,-1):
    f *= i
#saida
#print(numerocentral)
print(f)