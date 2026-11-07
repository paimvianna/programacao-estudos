from vagao import Vagao
from pilha_dinamica import PilhaDinamica


def executar_sistema():
    """
    Controlador do sistema interativo via terminal voltado estritamente
    para o comportamento LIFO (Pilha).
    """
    print("=== SISTEMA DE GERENCIAMENTO: PILHA DINÂMICA (LIFO) ===")

    # Instanciamento limpo do contêiner de controle.
    pilha = PilhaDinamica()

    # LAÇO PRINCIPAL DO SISTEMA (Infinite Loop Controlado)
    while True:
        print("\n" + "=" * 45)
        print("--- MENU DE OPÇÕES (PILHA) ---")
        print("1. Empilhar Vagões (Push)       [O(1)]")
        print("2. Desempilhar Vagões (Pop)     [O(1)]")
        print("3. Inspecionar Topo (Peek)     [O(1)]")
        print("4. Exibir Desenho da Memória   [O(n) - Apenas Visual]")
        print("5. Exterminar todos os Nodos   [O(1) - GC Action]")
        print("6. Retirar Vagão Defeituoso [0(n) - Remove e Depois Imprime Novamente]")
        print("0. Sair do Sistema")
        print("=" * 45)

        opcao = input("Escolha a operação lógica desejada: ")

        # Bloco de proteção contínua para evitar interrupções abruptas do software.
        try:
            if opcao == "1":
                matricula_vagao = int(input("Digite a matrícula do Vagão: "))
                tipo_carga = input("Digite o tipo de carga: ")
                pilha.push(Vagao(matricula_vagao, tipo_carga))
                print(f"[SUCESSO] -> Vagão '{matricula_vagao}' adicionado ao TOPO da pilha.")

            elif opcao == "2":
                removido = pilha.pop()
                print(f"[SUCESSO] -> O Vagão '{removido.id_vagao}' foi desempilhado e entregue.")

            elif opcao == "3":
                topo = pilha.peek()
                print(f"[INSPEÇÃO] -> O elemento na agulha para sair é:\n   {topo}")

            elif opcao == "4":
                print("\n[ MAPA ESTRUTURAL DA MEMÓRIA RAM ]")
                print(pilha)

            elif opcao == "5":
                confirmar = input("Atenção: Isso destruirá todos os dados. Continuar? (s/n): ")
                if confirmar.lower() == 's':
                    pilha.esvaziar()
                    print("[ALERTA] -> Todos os ponteiros foram rompidos. Memória liberada.")
                else:
                    print("Ação cancelada.")

            elif opcao == "6":
                vagao_defeituoso = int(input("Informe o vagão que deseja excluir: "))
                topo = pilha.peek()
                pilha_aux = []
                while(vagao_defeituoso != topo.id_vagao):
                    pilha_aux.append(topo)
                    topo = pilha.pop()

                for i in range((len(pilha_aux)-1), 0, -1):
                    pilha.push(pilha_aux[i])
                
                print(pilha)
                print(f"[SUCESSO] -> O Vagão '{vagao_defeituoso}' foi desempilhado e entregue.")
                
            elif opcao == "0":
                print("Encerrando a interface LIFO. Até logo!")
                break

            else:
                print("[ERRO] -> Opção inválida! Escolha um número de 0 a 5.")

        # Captura erros estruturais (ex: tentar fazer POP no vazio)
        # e erros de tipo (ex: digitar letra onde espera-se a matrícula int)
        except (IndexError, ValueError) as e:
            print(f"\n[FALHA NA OPERAÇÃO]: {e}")


if __name__ == "__main__":
    executar_sistema()