matriz = [] #esta e a declaração de uma lista
matriz.append([0,1,2,3])# em cada indice da lista foi posto uma lista que vem a ser o conteudo do append
matriz.append([0,1,2,3,4,5])
matriz.append([0,1,2])
print(matriz) # da matriz conforme uma lista onde tem tres indices com um lista cada
print(matriz[0]) # impressão do conteudo do indice 0
print(matriz[0][1])# impressão do conteudo do indice 0 e 1
for i in range(3): # for que ira percorrer de 0 a 3 sendo que 3 não sera considerado.
    print(matriz[i]) # impressão dos indices em forma de coluna, ordenando em forma de matriz