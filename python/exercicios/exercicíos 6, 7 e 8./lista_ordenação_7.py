"""
Trabalho 7
• Objetivo:
• Desenvolver um projeto em Python para testar e comparar o
desempenho computacional de 4 algoritmos de ordenação
(BubbleSort, SelectionSort, InsertionSort e QuickSort).
• Cargas de Teste:
• Tamanhos de vetor: 1.000, 10.000, 50.000, 100.000, 500.000 e
1.000.000 de elementos gerados aleatoriamente.
• Diretrizes Metodológicas:
• Medições estritamente focadas no tempo de execução do método de
ordenação (desprezando a alocação inicial de memória).
• Utilizar exatamente o mesmo conjunto de dados de teste para garantir
justiça na comparação algorítmica.
• Entregas (para dia 23/10):
• Código modularizado, instruções de execução e relatório técnico
comparativo com gráficos ou tabelas de tempo e suas justificativas de
desempenho e comparações entre os diferentes métodos.
"""
import random
class Vetor:
    """
    Representa o meu vetor ou vetores que irei testar o metodo.
    """
    """
    ====CRIANDO VETORES====
    """

    def __init__(self,tamanho: int):
        self.vetor = [random.randint(-tamanho, tamanho) for _ in range(tamanho)]

    def  __str__(self):
        """
        Impressão do vetor. Para que eu possa ver ele inteiro, para comfirmar
        se ocorreu a geração.
        """
        return f"O vetor e constituido de tais valores: {', '.join(str(i) for i in self.vetor)}"
    #def vetor_random(self,tamanho):
    #    vetor = [random.randint(-1000000,1000000) for _ in range(tamanho)]
    #    return vetor

    """
    ====Ordenar SelectionSort====
    """

    def selection_sort(self,vetor: list[int]) -> None:

        n = len(vetor)
        # Passa por cada posição do vetor assumindo que ela receberá o menor elemento restante
        for i in range(n):
            # Assume que o elemento atual (i) é o menor da sub-lista não ordenada
            min_index = i
            # Explora o restante do vetor à direita para encontrar um elemento ainda menor
            for j in range(i + 1, n):
                if vetor[j] < vetor[min_index]:
                    # Atualiza o índice do menor elemento encontrado
                    min_index = j
            # Se o menor elemento não for o próprio elemento da posição i, faz a troca
            if min_index != i:
                vetor[i], vetor[min_index] = vetor[min_index], vetor[i]

    """
    ====Ordenar InsertionSort====
    """

    def insertion_sort(self,vetor: list[int]) -> None:
     # Começamos a iterar a partir do segundo elemento (índice 1).
        for i in range(1, len(vetor)):
            # Guarda o valor do elemento atual que será inserido na parte ordenada
            chave = vetor[i]
            # Inicializa o ponteiro 'j' para o último elemento da sub-lista ordenada à esquerda
            j = i - 1
            # Desloca os elementos da sub-lista ordenada que são maiores que a chave
            # uma posição para a direita, abrindo espaço para a inserção
            while j >= 0 and vetor[j] > chave:
                vetor[j + 1] = vetor[j]  # Deslocamento para a direita
                j -= 1  # Move o ponteiro para o elemento anterior

            # Insere a chave na sua posição correta encontrada na sub-lista ordenada
            vetor[j + 1] = chave

    """
    ====BUBBLESORT====
    """

    def bubble_sort(self,vetor: list[int]) -> None:
        fim = len(vetor)
        continua = True

        # Enquanto houver trocas E o limite for maior que 1...
        while continua and fim > 1:
            continua = False  # Assume que está ordenado nesta passada
            # Laço para levar o maior elemento encontrado para final do vetor...
            for i in range(fim - 1): # o "i" determina a janela de interação/comparação
                if vetor[i] > vetor[i + 1]:
                    # Troca os elementos de lugar (Swap)
                    vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
                    continua = True  # Houve troca, logo o vetor não estava ordenado
            # Reduz o tamanho da varredura, pois o maior elemento já foi levado para o fim
            fim -= 1

    """
    ====QUICK SORT====
    """

    def quick_sort(self,vetor: list[int], baixo: int, alto: int) -> None:
        """
        Implementação unificada e clássica do QuickSort in-place (Lomuto).
        Ordena o vetor diretamente na memória, sem criar listas auxiliares.
        """
        if baixo < alto:
            # 1. Particionamento embutido
            pivo = vetor[alto]
            i = baixo - 1

            for j in range(baixo, alto):
                if vetor[j] <= pivo:
                    i += 1
                    vetor[i], vetor[j] = vetor[j], vetor[i]

            # Coloca o pivô na sua posição definitiva
            vetor[i + 1], vetor[alto] = vetor[alto], vetor[i + 1]
            indice_pivo = i + 1

            # 2. Chamadas recursivas para as duas metades
            self.quick_sort(vetor, baixo, indice_pivo - 1)
            self.quick_sort(vetor, indice_pivo + 1, alto)