#aula sobre dicionario
a = []
dicionario = {} # quando usamos chaves podemos colocar qualquer valor como indice ou seja pode se alfanumerico.

print(type(a))
print(type(dicionario))


dicionario ['Restinga'] = 50000 # vemos que aqui, temos uma chave que esta entre aspas. e o valor numerico esta na posição que esta associada a chave.
dicionario ['Rubem Berta'] = 78624
dicionario ['Sarandi'] = 60403
dicionario ['Partenon'] = 47460
dicionario ['Santa Tereza'] = 47175
dicionario ['Vila Nova'] = 33145
dicionario ['Lomba do Pinheiro'] = 30388
dicionario ['Vila São Jose'] = 28957
dicionario ['Bom Jesus'] = 28229
dicionario ['Cascata'] = 24130
dicionario ['Coronel Aparicio Borges'] = 22786

print(dicionario)

chaves = dicionario.keys() #nesta função temos uma atribuição das chaves do dicionario sera atribuida a chaves criando
# uma tubla um espaço onde armazena o dado e um indece de forma imutavel, umm lista imutavel.

print(chaves)

for k in chaves:# for ira agir de formma interada onde k ira percorrer os valor das chaves, ou seja pegando o valor do primeiro campo, em uma lista ele informa o valor dentro do campo não sendo o indece
    print (k, dicionario [k])# o que ele faz e percorre toods os valores das lista chaves imutavel ou tupla, com isso a chave k aplicada no dicionaria ira apresentar o valor da chave.


print('------')
for bairro in dicionario:
    print(bairro, dicionario[bairro])

print('-----')
dicionario_ordenado = sorted(dicionario)# neste foi ordenado por ordem alfabetica os bairro

print(dicionario_ordenado)
print(dicionario)


for k in dicionario_ordenado:
    print(k, dicionario[k])# neste foi impresso de forma ordenado por ordem alfabetica os bairro

dicionario_crescente = sorted(dicionario.items(), key = lambda item: item[1]) # podemos colocar mais especifico e onde a gente coloca em item colocamos mais subintens, colocando item [1][1]
print(dicionario_crescente)

for i in sorted(dicionario, key = dicionario.get):
    print(i,dicionario[i])