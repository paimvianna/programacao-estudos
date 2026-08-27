#from lista_linear_v3_old import Aluno, ListaSequencial
from lista_linear_v3 import Aluno, ListaSequencial


def executar_sistema():
    """
    Função controladora principal do sistema interativo via terminal.
    Gerencia o menu de opções, captura as entradas do usuário, instancia objetos
    da classe Aluno e consome os métodos da ListaSequencial, lidando com
    exceções operacionais e de integridade (como capacidade cheia ou matrículas duplicadas).
    """
    print("=== SISTEMA DE GERENCIAMENTO DE LISTA SEQUENCIAL COMPLETA ===")

    # Solicita ao usuário a capacidade máxima fixa do vetor estático
    capacidade_informada = int(input("Informe a capacidade máxima da lista: "))
    lista = ListaSequencial(capacidade=capacidade_informada)
    ...

    while True:
        # Exibe o menu interativo com todas as operações disponíveis na API
        print("\n--- MENU DE OPÇÕES ---")
        print("1. Inserir no início")
        print("2. Inserir no fim")
        print("3. Inserir por posição")
        print("4. Remover do início")
        print("5. Remover do fim")
        print("6. Remover por posição")
        print("7. Remover por matrícula (objeto)")
        print("8. Buscar por matrícula")
        print("9. Consultar elemento em índice (elemento_em)")
        print("10. Listar todos os elementos")
        print("11. Exibir estado atual e status (tamanho, vazia, cheia)")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        try:
            # Opção 1: Inserção no início da lista (O(n) devido ao deslocamento/shifting)
            if opcao == "1":
                mat = int(input("Digite a matrícula: "))
                nome = input("Digite o nome: ")
                lista.adicionar_no_inicio(Aluno(mat, nome))
                print(f"Sucesso! Aluno {nome} inserido no início.")

            # Opção 2: Inserção direta no fim da lista (O(1))
            elif opcao == "2":
                mat = int(input("Digite a matrícula: "))
                nome = input("Digite o nome: ")
                lista.adicionar_fim(Aluno(mat, nome))
                print(f"Sucesso! Aluno {nome} inserido no fim.")

            # Opção 3: Inserção em uma posição intermediária específica informada pelo usuário
            elif opcao == "3":
                pos = int(input(f"Digite a posição (0 a {lista.tamanho()}): "))
                mat = int(input("Digite a matrícula: "))
                nome = input("Digite o nome: ")
                lista.inserir(pos, Aluno(mat, nome))
                print(f"Sucesso! Aluno {nome} inserido na posição {pos}.")

            # Opção 4: Remove o primeiro elemento da estrutura (O(n))
            elif opcao == "4":
                lista.remover_do_inicio()
                print("Primeiro elemento removido com sucesso!")

            # Opção 5: Remove o último elemento da estrutura em tempo O(1)
            elif opcao == "5":
                lista.remover_do_fim()
                print("Último elemento removido com sucesso!")

            # Opção 6: Remove o elemento com base em um índice/posição exata fornecida
            elif opcao == "6":
                pos = int(input(f"Digite a posição a remover (0 a {lista.tamanho() - 1}): "))
                lista.remover(pos)
                print(f"Elemento da posição {pos} removido com sucesso!")

            # Opção 7: Remove o aluno buscando primeiramente pela sua chave de negócio (matrícula)
            elif opcao == "7":
                mat = int(input("Digite a matrícula do aluno que deseja remover: "))
                lista.remover_por_objeto(mat)
                print(f"Aluno com matrícula {mat} removido com sucesso!")

            # Opção 8: Realiza busca sequencial por chave (matrícula) na estrutura
            elif opcao == "8":
                mat = int(input("Digite a matrícula que deseja buscar: "))
                indice = lista.buscar(mat)
                if indice != -1:
                    aluno_enq = lista.elemento_em(indice)
                    print(f"-> Encontrado no índice {indice}: {aluno_enq}")
                else:
                    print(f"-> Nenhum aluno encontrado com a matrícula {mat}.")

            # Opção 9: Consulta direta de um elemento pelo seu índice em O(1)
            elif opcao == "9":
                pos = int(input(f"Digite o índice (0 a {lista.tamanho() - 1}): "))
                aluno_cons = lista.elemento_em(pos)
                print(f"-> Elemento na posição {pos}: {aluno_cons}")

            # Opção 10: Retorna uma cópia limpa e exibe formatada a lista de todos os ativos
            elif opcao == "10":
                todos = lista.listar()
                print("--- LISTA DE ALUNOS ---")
                for idx, al in enumerate(todos):
                    print(f"[{idx}] -> {al}")

            # Opção 11: Exibe o estado bruto atual e os status lógicos (tamanho, vazia, cheia)
            elif opcao == "11":
                print("Estado:", lista)
                print(f"Tamanho: {lista.tamanho()} | Vazia? {lista.esta_vazia()} | Cheia? {lista.esta_cheia()}")

            # Opção 0: Encerra o loop de execução do sistema
            elif opcao == "0":
                print("Encerrando o sistema. Até logo!")
                break
            else:
                print("Opção inválida! Escolha de 0 a 11.")

        except (OverflowError, ValueError, IndexError) as e:
            # Bloco de segurança: captura estouro de capacidade (OverflowError),
            # índices inválidos (IndexError) e violações de regra de negócio/duplicidade (ValueError)
            print(f"[ERRO DE OPERAÇÃO]: {e}")


if __name__ == "__main__":
    executar_sistema()
