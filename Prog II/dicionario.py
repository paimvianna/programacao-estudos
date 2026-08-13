#aula sobre dicionarios

a = []
dicionario = {}

print(type(a))
print(type(dicionario))


dicionario['PoA'] = 1500000
dicionario['Pelotas'] = 100000
dicionario['Canoas'] = 1000000
dicionario['Alvorada'] = 8000
dicionario['Novo Hamburgo'] = 150000

#print(dicionario)

chaves = dicionario.keys()
print(chaves)

for k in chaves:
    print(k, dicionario[k])

print("---------")
for x in dicionario:
    print(x, dicionario[x])

dicionario_ordenado = sorted(dicionario)
print(dicionario_ordenado)
print(dicionario)

for k in dicionario_ordenado:
    print(k, dicionario[k])
print("----------")
for i in sorted(dicionario, key = dicionario.get):
    print(i, dicionario[i])
print("--------")
d = {'cachorro': [2, 2000], 'gato': [1, 3000], 'elefante': [3, 10000]}

print(d.items())
x = d.items()

x = sorted(x, key=lambda item: item[1][0])
print(x)


