#entrada
nome = input('informe o nome do nadador: ')
tempo = int(input('informe o tempo do nadador'))
#Processamento
l1=[nome]
l2=[tempo]
for i in range (6):
    nome = input('informe o nome do nadador: ')
    tempo = int(input('informe o tempo do nadador'))
    l1.append(nome)
    l2.append(tempo)
piortempo= max(l2)
pior = l2.index(piortempo)
print(pior)
piornome = l1[pior]
melhortempo = min(l2)
melhor = l2.index(melhortempo)
melhornome = l1[melhor]
#saida
print(f'O nome do pior {piornome} e o tempo {piortempo} ')
print(f'O nome do melhor {melhornome} e o tempo {melhortempo} ')
s=sum(l2)/7
print(s)