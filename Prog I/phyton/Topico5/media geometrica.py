#entrada
n = int(input('informe o um valor inteiro: '))
#processamento
max=min=n
l=[]
while n != 0:
    l.append(n)
    n = int(input('informe o um valor inteiro: '))
for i in range(len(l)):
    if max < l[i]:
        max = l[i]
    if min > l[i]:
        min = l[i]
mg = (min * max) ** (1/2)
#print(max)
#print(min)
#saida
print(f'{mg:.2f}')