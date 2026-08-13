#criar algoritmo que armazene 10 valores
v = int(input('por favor informe os valores para lista: '))
valores = []
i = 0
while i < 4:
    valores.append(v)
    i += 1
    v = int(input('por favor informe os valores para lista: '))
valores.append(v)

b = 0
while b < 5:
    if valores[b] % 10 == 0:
        print(valores[b])
    b += 1
print(valores)