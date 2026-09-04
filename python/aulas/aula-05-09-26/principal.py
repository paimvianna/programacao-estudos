from aluno import Aluno
from lista_simplesmente_encadeada import ListaSimplesmenteEncadeada

def executar_sistema():
    """
    Controlador do sistema interativo via terminal.
    Faz a ponte entre os inputs do usuário final e os algoritmos dinâmicos da Lista.
    """
    print("=== SISTEMA DE GERENCIAMENTO DE LISTA SIMPLESMENTE ENCADEADA ===")

    # Instanciamento limpo. Sem 'capacidade máxima'. O crescimento agora
    # depende unicamente da memória física (RAM) do sistema operacional.
    lista = ListaSimplesmenteEncadeada()

    # LAÇO PRINCIPAL DO SISTEMA (Infinite Loop Controlado):
    # Mantém o menu sendo exibido indefinidamente até que o usuário digite "0",
    # momento em que o comando 'break' destrói o laço e o programa encerra.
    while True:
        print("\n--- MENU DE OPÇÕES ---")
        print("1. Inserir no início (O(1) - Instantâneo)")
        print("2. Inserir no fim (O(1) - Via atalho Tail)")
        print("3. Inserir por posição (O(n) - Exige varredura)")
        print("4. Remover do início (O(1) - Pulo de Head)")
        print("5. Remover do fim (O(n) - Gargalo estrutural)")
        print("6. Remover por posição (O(n))")
        print("7. Remover por matrícula/objeto")
        print("8. Buscar por matrícula")
        print("9. Consultar elemento em índice (elemento_em)")
        print("10. Listar todos os elementos")
        print("11. Exibir estado atual e status")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        # O bloco Try captura as exceções manuais lançadas pela classe da Lista
        # impedindo que o software trave e feche na cara do usuário em caso de erro.
        try:
            if opcao == "1":
                mat = int(input("Digite a matrícula: "))
                nome = input("Digite o nome: ")
                lista.adicionar_no_inicio(Aluno(mat, nome))
                print(f"Sucesso! Aluno {nome} inserido no início.")

            elif opcao == "2":
                mat = int(input("Digite a matrícula: "))
                nome = input("Digite o nome: ")
                lista.adicionar_fim(Aluno(mat, nome))
                print(f"Sucesso! Aluno {nome} inserido no fim.")

            elif opcao == "3":
                pos = int(input(f"Digite a posição (0 a {lista.tamanho()}): "))
                mat = int(input("Digite a matrícula: "))
                nome = input("Digite o nome: ")
                lista.inserir(pos, Aluno(mat, nome))
                print(f"Sucesso! Aluno {nome} inserido na posição {pos}.")

            elif opcao == "4":
                lista.remover_do_inicio()
                print("Primeiro elemento removido com sucesso!")

            elif opcao == "5":
                lista.remover_do_fim()
                print("Último elemento removido com sucesso!")

            elif opcao == "6":
                pos = int(input(f"Digite a posição a remover (0 a {lista.tamanho() - 1}): "))
                lista.remover(pos)
                print(f"Elemento da posição {pos} removido com sucesso!")

            elif opcao == "7":
                mat = int(input("Digite a matrícula do aluno que deseja remover: "))
                lista.remover_por_objeto(mat)
                print(f"Aluno com matrícula {mat} removido com sucesso!")

            elif opcao == "8":
                mat = int(input("Digite a matrícula que deseja buscar: "))
                indice = lista.buscar(mat)
                if indice != -1:
                    aluno_enq = lista.elemento_em(indice)
                    print(f"-> Encontrado no índice {indice}: {aluno_enq}")
                else:
                    print(f"-> Nenhum aluno encontrado com a matrícula {mat}.")

            elif opcao == "9":
                pos = int(input(f"Digite o índice (0 a {lista.tamanho() - 1}): "))
                aluno_cons = lista.elemento_em(pos)
                print(f"-> Elemento na posição {pos}: {aluno_cons}")

            elif opcao == "10":
                todos = lista.listar()
                print("--- LISTA DE ALUNOS ---")
                # LAÇO DE EXIBIÇÃO:
                # O enumerate() percorre o array nativo retornado e injeta um contador (idx)
                # ao lado do objeto (al), automatizando a visualização com posições.
                for idx, al in enumerate(todos):
                    print(f"[{idx}] -> {al}")

            elif opcao == "11":
                # O comando print() chama o método __str__ da nossa ListaSimplesmenteEncadeada
                # que internamente fará um laço while varrendo todos os ponteiros da memória.
                print("Estado:\n", lista)
                print(f"\nTamanho atual: {lista.tamanho()} nodos lógicos.")
                print(f"A lista está completamente vazia? {lista.esta_vazia()}")

            elif opcao == "0":
                print("Encerrando o sistema. Até logo!")
                break
            else:
                print("Opção inválida! Escolha de 0 a 11.")

        # Tratamento de exceções específicas de lógica de negócio e índices.
        # OverflowError não existe mais neste cenário dinâmico.
        except (ValueError, IndexError) as e:
            print(f"[ERRO DE OPERAÇÃO]: {e}")

if __name__ == "__main__":
    executar_sistema()