#Importando a ListaMedia
from lista_alunos_media import Aluno, ListaMedias

def executar_sistema():
    """
    Função de Controle do sistema interativo do terminal.
    """
    print ("----sISTEMA DE GERENCIAMENTO DE LISTA SEQUENCIAL COM MEDIA DOS ALUNOS----")

    """Solicitando a quantidade dos alunos."""
    quantidade_alunos = int(input("Informe o tamanho da turma: "))
    lista = ListaMedias(capacidade = quantidade_alunos)
    ...

    while True:
        #Exibir Menu Interativo.
        print("\n--- MENU DE OPÇÕES ---")
        print("1. Inserir aluno")
        print("2. Buscar por matricula")
        print("3. Remover por matricula")
        print("4. Listar")
        print("5. Sair")

        opcao = input ("Escolha uma opção: ")
        try:
            #Opção 1: inserir de forma ordenada os alunos baseado na media.
            if opcao == "1":
                nome = input("Digite o nome do Aluno: ")
                codigo_inscricao = int (input("Informe o numero da Matricula: "))
                media = float(input("Informe a Media do Aluno: "))
                lista.inserir_ordenado(Aluno(nome,codigo_inscricao,media))
                print(f"Sucesso! Aluno {nome} inserido com sucesso.")

            elif opcao == "2":
                codigo_inscricao = int (input("Digite a Matrícula que deseja buscar: "))
                indice = lista.buscar(codigo_inscricao)
                if indice !=-1:
                    aluno_enq = lista.elemento_em(indice)
                    print(f"->Encontrado no indice {indice}: {aluno_enq}")
                else:
                    print(f"->Nenhum aluno encontrado com a matricula {codigo_inscricao}")

            elif opcao == "3":
                codigo_inscricao = int (input("Digite a Matrícula  do aluno que deseja remover: "))
                lista.remover_por_objeto(codigo_inscricao)
                print(f"Aluno com matrícula {codigo_inscricao} removido com sucesso!")

            elif opcao == "4":
                todos = lista.listar()
                print(todos)
                print("---LLISTA DE ALUNOS---")
                for idx, al in enumerate(todos):
                    print(f"[{idx}] -> {al}")

            elif opcao == "5":
                print("Encerrando o sistema. Até logo!")
                break
            else:
                print("Opção invalida! Escola de 1 a 5.")

        except (OverflowError, ValueError, IndexError) as e:
            # Bloco de segurança: captura estouro de capacidade (OverflowError),
            # índices inválidos (IndexError) e violações de regra de negócio/duplicidade (ValueError)
            print(f"[ERRO DE OPERAÇÃO]: {e}")

if __name__=="__main__":
    executar_sistema()
