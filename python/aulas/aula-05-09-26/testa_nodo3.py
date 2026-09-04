from aluno import Aluno
from lista_simplesmente_encadeada import Nodo

"""
Testa nodo sem saber do tail....
"""

# class Aluno:
#     def __init__(self, matricula, nome):
#         self.matricula = matricula
#         self.nome = nome
#
#     def __str__(self):
#         return f"Aluno(matricula={self.matricula}, nome='{self.nome}')"
#
#     def __repr__(self):
#         return f"Aluno: nome={self.nome}"
#
#     def __eq__(self, outro):
#         if isinstance(outro, Aluno):
#             return self.matricula == outro.matricula
#         return self.matricula == outro
#
#
# class Nodo:
#
#     def __init__(self, elemento, proximo = None):
#         self.elemento = elemento
#         self.proximo = proximo





"""
Instanciando nodos e navegando com duas variáveis de controle: atual, tamanho...
"""

#
# n1 = Nodo(Aluno(101, "Leonardo"))
# n2 = Nodo(Aluno(102, "Raquel"))
# n3 = Nodo(Aluno(103, "Maria Antônia"))
# n4 = Nodo(Aluno(104, "Trevinho"))
#
# # print(n1.elemento)
# # print(n2.elemento)
# # print(n3.elemento)
# # print(n4.elemento)
#
# """
# Criando a lista, ou seja, a cadeia de apontamentos...
# """
#
# n1.proximo = n2
# n2.proximo = n3
# n3.proximo = n4
#
#
# """
# Navegando na lista com duas variáveis de controle: atual e proximo...
# """
#
# atual = n1
# tamanho = 0
#
# print("Lendo os elementos da lista...")
# while atual is not None:
#     print(f"Nó [{tamanho}] -> {atual.elemento}")
#
#     atual = atual.proximo
#     tamanho += 1
#
# print("Varredura concluída...")
#




"""
Instanciando nodos e navegando na lista com 5 variáveis de controle: atual, proximo, 
primerio, ultimo e total_de_elementos...
"""

atual = None
tamanho = 0

primeiro = None
ultimo = None
total_de_elementos = 0

print(f"Tamanho da lista: {total_de_elementos}")
print(f"O primeiro aponta para: {primeiro}")
print(f"O ultimo aponta para: {ultimo}")

# Adicionando um nodo...
n1 = Nodo(Aluno(101, "Leonardo"))
primeiro = n1
ultimo = n1
total_de_elementos += 1

print("\nNodo inserido na lista...")
print(f"Tamanho da lista: {total_de_elementos}")
print(f"O primeiro aponta para: {primeiro.elemento}")
print(f"O ultimo aponta para: {ultimo.elemento}")


# Adicionando um nodo...
n2 = Nodo(Aluno(102, "Raquel"))
# -> Encadeamento
ultimo.proximo = n2
ultimo = n2
total_de_elementos += 1

print("\nNodo inserido na lista...")
print(f"Tamanho da lista: {total_de_elementos}")
print(f"O primeiro aponta para: {primeiro.elemento}")
print(f"O ultimo aponta para: {ultimo.elemento}")

# Adicionando um nodo...
n3 = Nodo(Aluno(103, "Maria Antonia"))
# -> Encadeamento
ultimo.proximo = n3
ultimo = n3
total_de_elementos += 1

print("\nNodo inserido na lista...")
print(f"Tamanho da lista: {total_de_elementos}")
print(f"O primeiro aponta para: {primeiro.elemento}")
print(f"O ultimo aponta para: {ultimo.elemento}")


# Adicionando um nodo...
n4 = Nodo(Aluno(104, "Trevinho"))
# -> Encadeamento
ultimo.proximo = n4
ultimo = n4
total_de_elementos += 1

print("\nNodo inserido na lista...")
print(f"Tamanho da lista: {total_de_elementos}")
print(f"O primeiro aponta para: {primeiro.elemento}")
print(f"O ultimo aponta para: {ultimo.elemento}")


"""
Navegando na lista com duas variáveis de controle: atual e proximo...
"""

atual = primeiro
tamanho = 0

print("\nLendo os elementos da lista...\n")

while atual is not None:
    print(f"Nó [{tamanho}] -> {atual.elemento}")
    atual = atual.proximo
    tamanho += 1

print("\nVarredura concluída...")


"""
Fazendo uma varreduda reversa...
"""


pilha_auxiliar = []
atual = primeiro

# Adiciona itens na pilha...para reorganziar a memória
while atual is not None:
    pilha_auxiliar.append(atual)
    atual = atual.proximo

# for indice, nodo in enumerate(pilha_auxiliar):
#     print(f"Nodo{[indice]}: {nodo.elemento}")

contador_reverso = total_de_elementos - 1

print("\nLendo os elementos da lista de forma reversa...\n")

while len(pilha_auxiliar) > 0:
    nodo_recuperado = pilha_auxiliar.pop()
    print(f"Nó [{contador_reverso}] -> {nodo_recuperado.elemento}")
    contador_reverso -= 1

print("\nVarredura concluída...")















