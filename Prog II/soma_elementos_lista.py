#soma todos os elementos de uma lista
def soma_lista(lista):
    soma = 0
    for x in lista:
        soma = soma + x
    return soma
print(soma_lista([1,2,3]))
print(soma_lista([1,1,1,1,1]))