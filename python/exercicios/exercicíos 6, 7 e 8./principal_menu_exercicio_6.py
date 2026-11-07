from lista_exercicio_6 import Vetor
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
    listaOriginal = None

    # LAÇO PRINCIPAL DO SISTEMA (Infinite Loop Controlado):
    # Mantém o menu sendo exibido indefinidamente até que o usuário digite "0",
    # momento em que o comando 'break' destrói o laço e o programa encerra.
    while True:
        print("\n--- MENU DE OPÇÕES ---")
        print("1. Criar lista:")
        print("2. Imprimir lista.")
        print("3. Busca linear.")
        print("4. Busca linear ordenada.")
        print("5. Busca binaria.")
        print("6. Ordenar por bubblesort.")
        print("7. Ordenar por quick sort.")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        # O bloco Try captura as exceções manuais lançadas pela classe da Lista
        # impedindo que o software trave e feche na cara do usuário em caso de erro.
        try:
            if opcao == "1":
                tamanho = int(input(f"Informe o tamanho do vetor que deseja criar: "))
                lista.__init__(tamanho)
                listaOriginal = lista.vetor.copy()
                print(f"Sucesso! O vetor com {tamanho} foi criado.")

            elif opcao == "2":
                print(lista)
    
            elif opcao == "3": 
                elemento = int(input(f"Informe o numero inteiro que deseja procurar no vetor:"))
                inicio = time.perf_counter()
                resultado = lista.busca_linear(lista.vetor, elemento)
                fim = time.perf_counter()
                tempo_execucao_linear = fim - inicio
                print(f"Elemento {elemento} encontrado no indice: {resultado}.\nTempo de busca: {tempo_execucao_linear}")
            
            elif opcao == "4":
                elemento = int(input(f"Informe o numero inteiro que deseja procurar no vetor:"))
                inicio = time.perf_counter()
                resultado = lista.busca_linear_ordenada(lista.vetor, elemento)
                fim = time.perf_counter()
                tempo_execucao_linear = fim - inicio
                print(f"Elemento {elemento} encontrado no indice: {resultado}\nTempo de busca: {tempo_execucao_linear}")

            elif opcao == "5":
                elemento = int(input(f"Informe o numero inteiro que deseja procurar no vetor:"))
                inicio = time.perf_counter()
                resultado = lista.busca_binaria(lista.vetor,elemento)
                fim = time.perf_counter()
                tempo_execucao_linear = fim - inicio
                print(f"Elemento {elemento} encontrado no indice: {resultado}\nTempo de busca: {tempo_execucao_linear}")

            elif opcao == "6":
                if listaOriginal is None:
                    print("[Aviso]: Crie a lista (Opão 1) antes de ordenar.")
                else:
                    print("Ordenamento usando Bubblesort\n")
                    print(f"\nLista sem ordenar:\n {', '.join(str(i) for i in listaOriginal)}")
                    print(f"\nA lista ordenada:\n ")
                    lista.bubble_sort(lista.vetor)
                    print(lista)

            elif opcao == "7":
                #Ordenação por po quick sort
                if listaOriginal is None:
                    print("[Aviso]: Crie a lista (Opão 1) antes de ordenar.")
                else:  
                    print("Ordenamento usando Quick Sort\n")
                    print(f"\nLista sem ordenar:\n {', '.join(str(i) for i in listaOriginal)}")
                    print(f"\nA lista ordenada:\n ")
                    lista.quick_sort(lista.vetor, 0, len(lista.vetor)-1)
                    print(lista)

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