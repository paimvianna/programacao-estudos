#criar algoritmo que armazene 10 nomes
n = input('por favor informe o nome para lista: ')
nomes = []
for i in range(9):
    nomes.append(n)
    n = input('por favor informe o nome para lista: ')
nomes.append(n)
#print(nomes)