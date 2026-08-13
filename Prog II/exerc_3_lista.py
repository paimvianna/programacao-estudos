#criar algoritmo que armazene 10 valores
v = int(input('por favor informe os valores para lista: '))
valores = []
i = 0
while i < 4:
    if 0 < v < 10:
        valores.append(v)
        i += 1
    v = int(input('por favor informe os valores para lista: '))
valores.append(v)
print(valores)