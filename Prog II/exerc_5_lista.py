#criar vetor com 5 posições e escreva os numeros impares, indique em quais posições eles se encontram.
v = int(input('por favor informe os valores para lista: '))
valores = []
primos = []
indices = []
i = 0
while i < 4:
    valores.append(v)
    i += 1
    v = int(input('por favor informe os valores para lista: '))
valores.append(v)

b = 0
while b < 5:
    p = 0
    c = valores[b]
    while c > 0:
        if valores[b] % c == 0:
            p += 1
        c -= 1
    if p == 2:
        primos.append(valores[b])
        #indices.index(valores[b])
        indices.append(b)
    b += 1
for i in range(len(primos)):
    print(primos[i], indices[i])
#print(valores)
#print(primos)
#print(indices)