from lista_atendimento_v1 import Fila, Ficha
"""Sistema do Menu para o atendimento.
Aplicação Prática Obrigatória: Simulador de Fila de Banco ou
Atendimento (gerenciando entradas nas pontas com prioridade).
vamos usar um sistema o sistema Deque. Onde podemos alterna 
com inseções e excluções nas pontas. Alternando entre 
FIFO - First In, First Out de uma fila ou 
LIFO - Last in First Out de uma pilha.
"""

def executar_sistema(): 
    """função de controle do sistema, com menu interativo e
      captura de entradas e manipulação de lista de dupla entrada."""

    print(f"===Sistema de chamamento de Fila de Atendimento ao Publico")

    #Solicitado ao usuario a capacidade maxima de fixas do vetor estatico
    
    minha_fila = Fila()
    gerador_fichas = Ficha()
    validacao = True
  
    while validacao:
        #Exibe o menu interativo com todas as operações disponiveis na API
        print("---MENU DE OPÇÕES---")
        print("1. FICHA COMUM")
        print("2. FICHA PRIORITARIA")
        print("3. EXCLUIR FICHA")
        print("4. ATENDER CLIENTE") 
        print("5. VISUALIZAR FILA")         
        print("6. QUANTIDADE DE CLIENTES")
        print("7. SAIR")

        opcao =  input("Escolha uma opção: ")

        try:
            if opcao == "1":
                """Opção 1: Cria e inclui Ficha Normal no fim da Fila; a direita. """
                ficha_criada = gerador_fichas.gera_ficha_normal(minha_fila)
                print (f"O numero da sua ficha e: {ficha_criada}")

            elif opcao == "2":
                    """Opção 2: Cria e inclui Ficha Preferencial no inicio da Fila; a esquerda."""
                    ficha_criada = gerador_fichas.gera_ficha_preferencial(minha_fila)
                    print (f"O numero da sua ficha e: {ficha_criada}")
                    

            elif opcao == "3":
                    """Opção 3: Exclui Ficha específica"""
                    numero_ficha = input(f'Informe a ficha que deseja excluir: ')
                    minha_fila.excluir_ficha(numero_ficha)
                    #lista.excluir_ficha
                    
            elif opcao == "4":
                    """Opção 4: Chama para atendimento a ficha que esta no inicio da fila a Esquerda."""
                    minha_fila.atender_cliente()
                    #print("Ficha (colocar o valor ou numero da ficha chamada.) " \
                    #"balcão/guiche (criar um codigo que indique o balcao ou guiche)")

            elif opcao == "5":
                    """Opção 5: Imprime todos os elementos da fila."""
                    #visualizar_fila de forma descritiva.
                    print(f"Tamanho: (colocar aqui o tamanho geral da fila) | Fichas Comuns: (colocar fichas não prioritarias) "
                            f"| Fichas Prioritaria: (colocar fichas prioritarias)"
                            f"| Fichas Disponiveis: (colocar quantas fichas temos disponivel baseado no tamanho da fila.)")
                    minha_fila.visualizar_fila()
                    
            elif opcao == "6":
                    """Opção 6: Exibe a quantidade de clientes por tipos de ficha."""
                    comum, preferencial, total = minha_fila.contar_por_tipo()
                    print(f"===QUANTIDADE DE CLIENTES===")
                    print(f'Fichas Comuns (N): {comum}')
                    print(f'Fichas Preferencial (P): {preferencial}')
                    print(f'Total  na Fila: {total}')
            elif opcao == "7":
                  """Opção 7: Sai e fecha a aplicação."""
                  print("Encerrando o sistema. Até logo!")
                  validacao = False
            else:
                  print("Opção invalida! Escolha de 1 a 7")

        except (OverflowError, ValueError,IndexError) as e:
              #Bloco de segurança: captura estouro de capacidade(OverflowError),
              #indices invalidos (IndexError) e violação de regras de negócio/duplicidade (ValueError)
              print(f"[ERRO DE OPERAÇÃO]: {e}")


if __name__=="__main__":
      executar_sistema()