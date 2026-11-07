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
from lista_ordenação_7 import Vetor
import time 

def executar_sistema():
    """
    Controlador do sistema interativo via terminal.
    Faz a ponte entre os inputs do usuário final e os algoritmos dinâmicos da Lista.
    """
    print("=== SISTEMA DE BUSCA E ORDENAÇÃO DE LISTA ===")

    # Instanciamento limpo. Sem 'capacidade máxima'. O crescimento agora
    # depende unicamente da memória física (RAM) do sistema operacional.
    tamanho = 0
    lista = Vetor(tamanho)
    #Inicializa a variavel no escopo principal para evitar Erro
    listaOriginal1 = None
    listaOriginal2 = None
    listaOriginal3 = None
    listaOriginal4 = None

    # LAÇO PRINCIPAL DO SISTEMA (Infinite Loop Controlado):
    # Mantém o menu sendo exibido indefinidamente até que o usuário digite "0",
    # momento em que o comando 'break' destrói o laço e o programa encerra.
    while True:
        print("\n--- MENU DE OPÇÕES ---")
        print("1. Criar lista:")
        print("2. Imprimir lista.")
        print("3. Ordenar selectionsort.")
        print("4. Ordenar insertionsort.")
        print("5. Ordenar por bubblesort.")
        print("6. Ordenar por quick sort.")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        # O bloco Try captura as exceções manuais lançadas pela classe da Lista
        # impedindo que o software trave e feche na cara do usuário em caso de erro.
        try:
            if opcao == "1":
                tamanho = int(input(f"Informe o tamanho do vetor que deseja criar: "))
                lista.__init__(tamanho)
                listaOriginal1 = lista.vetor.copy()
                listaOriginal2 = lista.vetor.copy()
                listaOriginal3 = lista.vetor.copy()
                listaOriginal4 = lista.vetor.copy()

                print(f"Sucesso! O vetor com {tamanho} foi criado.")

            elif opcao == "2":
                print(lista)
    
            elif opcao == "3": 
                #Ordena por selection sort
                if listaOriginal1 is None:
                    print("[Aviso]: Crie a lista (Opão 1) antes de ordenar.")
                else:
                    inicio = time.perf_counter()
                    lista.selection_sort(listaOriginal1)
                    fim = time.perf_counter()
                    tempo_execucao_linear = fim - inicio  
                    #print(f"Tempo de execução: {tempo_execucao_linear}\n Lista Ordenada:{listaOriginal1}\n")
                    print(f"Tempo de execução: {tempo_execucao_linear}")

            elif opcao == "4":
                #Ordena por insertion sort
                if listaOriginal2 is None:
                    print("[Aviso]: Crie a lista (Opão 1) antes de ordenar.")
                else:
                    inicio = time.perf_counter()
                    lista.insertion_sort(listaOriginal2)
                    fim = time.perf_counter()
                    tempo_execucao_linear = fim - inicio
                    #print(f"Tempo de execução: {tempo_execucao_linear}\n Lista Ordenada:{listaOriginal2}\n")
                    print(f"Tempo de execução: {tempo_execucao_linear}")

            elif opcao == "5":
                #Ordenação por bubble sort
                if listaOriginal3 is None:
                    print("[Aviso]: Crie a lista (Opção 1) antes de ordenar.")
                else:
                    inicio = time.perf_counter()
                    lista.bubble_sort(listaOriginal3)
                    fim = time.perf_counter()
                    tempo_execucao_linear = fim - inicio
                    #print(f"Tempo de execução: {tempo_execucao_linear}\n Lista Ordenada:{listaOriginal3}\n")
                    print(f"Tempo de execução: {tempo_execucao_linear}")

            elif opcao == "6":
                #Ordenação por quick sort
                if listaOriginal4 is None:
                    print("[Aviso]: Crie a lista (Opão 1) antes de ordenar.")
                else:  
                    inicio = time.perf_counter()
                    lista.quick_sort(listaOriginal4,0, len(listaOriginal4)-1)
                    fim = time.perf_counter()
                    tempo_execucao_linear = fim - inicio
                    #print(f"Tempo de execução: {tempo_execucao_linear}\n Lista Ordenada:{listaOriginal4}\n")
                    print(f"Tempo de execução: {tempo_execucao_linear}")

            elif opcao == "0":
                print("Encerrando o sistema. Até logo!")
                break
            else:
                print("Opção inválida! Escolha de 0 a 7.")

        # Tratamento de exceções específicas de lógica de negócio e índices.
        # OverflowError não existe mais neste cenário dinâmico.
        except (ValueError, IndexError) as e:
            print(f"[ERRO DE OPERAÇÃO]: {e}")

if __name__ == "__main__":
    executar_sistema()