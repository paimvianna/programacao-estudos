import random
"""
Trabalho 6
• Objetivo:
    • Medir e comparar o desempenho prático de execução dos 3 algoritmos de
    busca estudados (“Busca Linear”, “Busca Linear Ordenada” e “Busca Binária”)
    utilizando o módulo time (time.perf_counter()).
• Cargas de Teste:
    • Tamanhos de vetor: 1.000, 5.000, 10.000, 50.000, 100.000, 500.000 e
    1.000.000 de elementos.
• Diretrizes Metodológicas:
    • As medições de tempo devem isolar estritamente a chamada da função
    de busca (desprezando a geração de números e a ordenação prévia).
    • Reutilizar exatamente o mesmo conjunto de dados gerado para todos os
    algoritmos na mesma rodada de testes.
• Entregas (para dia 23/10):
    • Código-fonte documentado, instruções claras de execução e relatório analítico
    de desempenho
"""

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
    ====BUSCA LINEAR====
    """

    def busca_linear(self,vetor: list[int], elemento: int) -> int:
        """
        Percorre o vetor sequencialmente comparando cada elemento.
        Retorna o índice do elemento se encontrado, ou -1 caso contrário.
        """
        for i in range(len(vetor)):
            if vetor[i] == elemento:
                return i
        return -1
    """
    ====BUSCA ORDENADA
    """

    def busca_linear_ordenada(self,vetor: list[int], elemento: int) -> int:
        """
        Recebe um vetor ordenado e o elemento pesquisado.
        Retorna o índice se encontrado, ou -1 se não encontrar ou ultrapassar o valor.
        """
        for i in range(len(vetor)):
            if vetor[i] == elemento:
                return i
            elif vetor[i] > elemento:
                # Parada antecipada: elementos futuros serão ainda maiores
                break
        return -1

    """
    ====BUSCA BINARIA====
    """

    def busca_binaria(self,vetor: list[int], elemento: int) -> int:
        """
        Realiza a busca binária iterativa em um vetor ordenado.
        Retorna o índice do elemento ou -1 se não encontrado.
        """
        inicio = 0
        fim = len(vetor) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2

            if vetor[meio] == elemento:
                return meio
            elif elemento < vetor[meio]:
                fim = meio - 1  # Descarta metade direita
            else:
                inicio = meio + 1  # Descarta metade esquerda

        return -1

    """
    BUBBLESORT
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
    ====QUICK SORT
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