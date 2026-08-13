x = [0,1,2,3,4]
x.append('teste')
y = [3,4,5]


print(type(x))
print(x)
print('x0:' + str(x[0])) # o mais é uma concatenação.
print(x+y) #concatena dois vetores
print(x[1:3])# nao pega o ultimo valores somente os anteriores ao 3 e a partir do 1
print(x[:-2])# nao imprime os dois ultimos a direita
print(x[-2:])# imprime os dois ultimos
print(x[-1])# imprimi o ultimo da lista
print(len(x))# me da o tamanho da lista
for i in range (len(x)): # aqui ivai percorre de zero ate o tamanho da lista menos 1
    print(x[i]) # aqui ira imprimir os valores em cada indice de memoria de 0 ao tamanho total da lista
for i in x: # neste caso i ira aponta o conteudo de cada indice da lista ou seja ira passar por todos os endereços das lista apontando seus conteudos.
    print (x[i]) # imprimi os valores internos de memoria que os indices estao indicano.
