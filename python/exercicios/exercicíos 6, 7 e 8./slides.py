

# busca linear...

# def busca_linear(vetor: list[int], elemento: int) -> int:
#     """
#     Percorre o vetor sequencialmente comparando cada elemento.
#     Retorna o índice do elemento se encontrado, ou -1 caso contrário.
#     """
#     for i in range(len(vetor)):
#         if vetor[i] == elemento:
#             return i
#     return -1


# busca ordenada...

# def busca_linear_ordenada(vetor: list[int], elemento: int) -> int:
#     """
#     Recebe um vetor ordenado e o elemento pesquisado.
#     Retorna o índice se encontrado, ou -1 se não encontrar ou ultrapassar o valor.
#     """
#     for i in range(len(vetor)):
#         if vetor[i] == elemento:
#             return i
#         elif vetor[i] > elemento:
#             # Parada antecipada: elementos futuros serão ainda maiores
#             break
#     return -1


# bubbleSort

# def bubble_sort(vetor: list[int]) -> None:
#     fim = len(vetor)
#     continua = True
#
#     # Enquanto houver trocas E o limite for maior que 1...
#     while continua and fim > 1:
#         continua = False  # Assume que está ordenado nesta passada
#         # Laço para levar o maior elemento encontrado para final do vetor...
#         for i in range(fim - 1): # o "i" determina a janela de interação/comparação
#             if vetor[i] > vetor[i + 1]:
#                 # Troca os elementos de lugar (Swap)
#                 vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
#                 continua = True  # Houve troca, logo o vetor não estava ordenado
#         # Reduz o tamanho da varredura, pois o maior elemento já foi levado para o fim
#         fim -= 1

# busca binária

# def busca_binaria(vetor: list[int], elemento: int) -> int:
#     """
#     Realiza a busca binária iterativa em um vetor ordenado.
#     Retorna o índice do elemento ou -1 se não encontrado.
#     """
#     inicio = 0
#     fim = len(vetor) - 1
#
#     while inicio <= fim:
#         meio = (inicio + fim) // 2
#
#         if vetor[meio] == elemento:
#             return meio
#         elif elemento < vetor[meio]:
#             fim = meio - 1  # Descarta metade direita
#         else:
#             inicio = meio + 1  # Descarta metade esquerda
#
#     return -1


# selection sort

# def selection_sort(vetor: list[int]) -> None:
#
#     n = len(vetor)
#     # Passa por cada posição do vetor assumindo que ela receberá o menor elemento restante
#     for i in range(n):
#         # Assume que o elemento atual (i) é o menor da sub-lista não ordenada
#         min_index = i
#         # Explora o restante do vetor à direita para encontrar um elemento ainda menor
#         for j in range(i + 1, n):
#             if vetor[j] < vetor[min_index]:
#                 # Atualiza o índice do menor elemento encontrado
#                 min_index = j
#         # Se o menor elemento não for o próprio elemento da posição i, faz a troca
#         if min_index != i:
#             vetor[i], vetor[min_index] = vetor[min_index], vetor[i]


# insertion sort

# def insertion_sort(vetor: list[int]) -> None:
#     # Começamos a iterar a partir do segundo elemento (índice 1).
#     for i in range(1, len(vetor)):
#         # Guarda o valor do elemento atual que será inserido na parte ordenada
#         chave = vetor[i]
#         # Inicializa o ponteiro 'j' para o último elemento da sub-lista ordenada à esquerda
#         j = i - 1
#         # Desloca os elementos da sub-lista ordenada que são maiores que a chave
#         # uma posição para a direita, abrindo espaço para a inserção
#         while j >= 0 and vetor[j] > chave:
#             vetor[j + 1] = vetor[j]  # Deslocamento para a direita
#             j -= 1  # Move o ponteiro para o elemento anterior
#
#         # Insere a chave na sua posição correta encontrada na sub-lista ordenada
#         vetor[j + 1] = chave


# quick sort (com list comprehensions)

# def quick_sort(vetor: list[int]) -> list[int]:
#     # Caso base da recursão: vetores com 0 ou 1 elemento já estão ordenados
#     if len(vetor) <= 1:
#         return vetor
#
#     # Escolha do pivô: pegamos o elemento central do vetor atual
#     pivo = vetor[len(vetor) // 2]
#     # Particionamento utilizando List Comprehensions do Python:
#     # 1. Cria uma lista apenas com os elementos menores que o pivô
#     menores = [x for x in vetor if x < pivo]
#     # 2. Cria uma lista com os elementos iguais ao pivô (trata duplicatas corretamente)
#     iguais = [x for x in vetor if x == pivo]
#     # 3. Cria uma lista apenas com os elementos maiores que o pivô
#     maiores = [x for x in vetor if x > pivo]
#
#     # Chamada recursiva combinando as partes menores ordenadas, os iguais,
#     # e as partes maiores ordenadas
#     return quick_sort(menores) + iguais + quick_sort(maiores)


# quick sort clássico com a função particionar...


# def quick_sort_classico(vetor: list[int], baixo: int, alto: int) -> None:
#     """
#     Função principal recursiva do QuickSort.
#     Ordena o vetor 'in-place' (sem criar novas listas), focando apenas
#     nos índices de 'baixo' até 'alto'.
#     """
#     if baixo < alto:
#         # 1. Particionamento: O pivô é colocado em seu lugar definitivo,
#         # e o vetor é dividido em duas partes (esquerda e direita).
#         indice_pivo = particionar(vetor, baixo, alto)
#         # 2. Chamada recursiva para a metade da esquerda (elementos menores que o pivô)
#         quick_sort_classico(vetor, baixo, indice_pivo - 1)
#         # 3. Chamada recursiva para a metade da direita (elementos maiores que o pivô)
#         quick_sort_classico(vetor, indice_pivo + 1, alto)

# def particionar(vetor: list[int], baixo: int, alto: int) -> int:
#     """
#     Função auxiliar que organiza os elementos em torno de um pivô.
#     Escolhemos sempre o último elemento do trecho como pivô.
#     """
#     # Escolhemos o último elemento como pivô
#     pivo = vetor[alto]
#     # 'i' marca a fronteira dos elementos menores que o pivô.
#     # Começa um passo antes do limite inferior.
#     i = baixo - 1
#     # Percorre o vetor do índice 'baixo' até o penúltimo elemento (alto - 1)
#     for j in range(baixo, alto):
#         # Se o elemento atual for MENOR ou IGUAL ao pivô, precisamos jogá-lo para o lado esquerdo
#         if vetor[j] <= pivo:
#             i += 1  # Avança a fronteira dos menores
#             # Troca o elemento da posição 'i' com o da posição 'j' (Swap)
#             vetor[i], vetor[j] = vetor[j], vetor[i]
#     # Quando o loop acaba, colocamos o pivô (que estava guardado no final 'alto')
#     # exatamente na sua posição correta, logo após o último elemento menor encontrado.
#     vetor[i + 1], vetor[alto] = vetor[alto], vetor[i + 1]
#
#     # Retorna a posição definitiva onde o pivô ficou
#     return i + 1

# --- COMO USAR NA PRÁTICA ---
# Como essa versão usa índices (baixo e alto), para ordenar um vetor inteiro você chama assim:
# meu_vetor = [10, 7, 8, 9, 1, 5]
# quick_sort_classico(meu_vetor, 0, len(meu_vetor) - 1)


# quick sort clássico sem a função particionar...

# def quick_sort(vetor: list[int], baixo: int, alto: int) -> None:
#     """
#     Implementação unificada e clássica do QuickSort in-place (Lomuto).
#     Ordena o vetor diretamente na memória, sem criar listas auxiliares.
#     """
#     if baixo < alto:
#         # 1. Particionamento embutido
#         pivo = vetor[alto]
#         i = baixo - 1
#
#         for j in range(baixo, alto):
#             if vetor[j] <= pivo:
#                 i += 1
#                 vetor[i], vetor[j] = vetor[j], vetor[i]
#
#         # Coloca o pivô na sua posição definitiva
#         vetor[i + 1], vetor[alto] = vetor[alto], vetor[i + 1]
#         indice_pivo = i + 1
#
#         # 2. Chamadas recursivas para as duas metades
#         quick_sort(vetor, baixo, indice_pivo - 1)
#         quick_sort(vetor, indice_pivo + 1, alto)
#
# # --- COMO CHAMAR NO PROGRAMA ---
# # meu_vetor = [10, 7, 8, 9, 1, 5]
# # quick_sort(meu_vetor, 0, len(meu_vetor) - 1)
