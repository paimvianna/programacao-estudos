from aluno import Aluno
from lista_simplesmente_encadeada import ListaSimplesmenteEncadeada

if __name__ == "__main__":

    # =========================================================================
    # 1. INICIALIZAÇÃO DA ESTRUTURA
    # =========================================================================
    print("=== 1. INICIALIZAÇÃO DA ESTRUTURA DINÂMICA ===")

    # A estrutura nasce baseada puramente em ponteiros apontando para None.
    # O conceito de "lista.esta_cheia()" foi extinto, pois o limite de alocação
    # de nodos físicos dita o ritmo sob demanda do hardware.
    lista = ListaSimplesmenteEncadeada()

    print("Lista criada vazia:", lista)
    print(f"Está vazia? {lista.esta_vazia()}")
    print("-" * 50)

    # =========================================================================
    # 2. TESTANDO INSERÇÕES E A NOVA REGRA DE UNICIDADE (DUPLICIDADE)
    # =========================================================================
    print("=== 2. TESTANDO INSERÇÕES E VALIDAÇÃO DE DUPLICIDADE ===")

    a1 = Aluno(201, "Lucas")
    a2 = Aluno(202, "Mariana")
    a3 = Aluno(203, "Gabriel")
    a4 = Aluno(204, "Juliana")
    a5 = Aluno(205, "Leonardo")

    # Adiciona no final quando vazia:
    # O Nó 'a1' vira automaticamente o primeiro e o último (Head e Tail apontam para ele).
    lista.adicionar_fim(a1)
    print("Após adicionar no fim (Lucas) [Operação O(1)]:", lista)

    # Testando o bloqueio implementado pelo polimorfismo do '__eq__' da classe Aluno.
    # A lista tenta comparar o int 201 com os objetos Alunos já instanciados
    # percorrendo a lista com o laço while do método buscar().
    print("\n[TESTE DE SEGURANÇA]: Tentando inserir aluno com matrícula duplicada (201)...")
    try:
        lista.adicionar_fim(Aluno(201, "Lucas Duplicado"))
    except ValueError as e:
        print(f"Bloqueio bem-sucedido -> {e}")
    print(f"Estado da lista após tentativa duplicada: {lista}\n")

    # Inserção no início: Cria nó, costura ponteiro para frente, ajusta o Head. Sem shifting O(1).
    lista.adicionar_no_inicio(a2)
    print("Após adicionar no início (Mariana) [Operação O(1)]:", lista)

    # Inserção no meio: A função dispara o laço for dentro de _pega_nodo para achar o elo anterior O(n).
    lista.inserir(1, a3)
    print("Após inserir Gabriel na posição 1 [Operação O(n)]:", lista)

    # Provando a escalabilidade dinâmica:
    # Em um vetor estático com capacidade 4, a quinta inserção estouraria o OverflowError.
    # Aqui, a RAM do sistema apenas aloca um novo bloco dinamicamente.
    lista.adicionar_fim(a4)
    lista.adicionar_fim(a5)
    print("Após adicionar Juliana e Leonardo (Ultrapassou limiar arbitrário):", lista)
    print("-" * 50)

    # =========================================================================
    # 3. TESTANDO ACESSOS DIRETOS E BUSCAS
    # =========================================================================
    print("=== 3. TESTANDO ACESSOS E BUSCAS ===")

    # Atenção técnica: Não há indexação física de vetores [0][1][2].
    # Para chegar no índice 2, o laço for em _pega_nodo executou: Head -> Nó 0 -> Nó 1 -> Nó 2.
    print(f"Elemento no índice 2 [Navegação O(n)]: {lista.elemento_em(2)}")

    # Busca linear padrão: Pula ponteiro a ponteiro checando a igualdade (__eq__).
    pos = lista.buscar(203)
    print(f"Busca pelo aluno com matrícula 203 [O(n)]: Encontrado no índice {pos}")

    # Coleta de todos os Nodos em um Array Python nativo para exportação iterando com um while
    print(f"Listagem bruta gerada por listar(): {lista.listar()}")
    print("-" * 50)

    # =========================================================================
    # 4. TESTANDO REMOÇÕES
    # =========================================================================
    print("=== 4. TESTANDO REMOÇÕES ===")

    # Exclusão instantânea: Atualiza a rota (Head) e abandona o nó antigo.
    lista.remover_do_inicio()
    print("Após remover do início (Mariana) [O(1)]:", lista)

    # O Calcanhar de Aquiles: Aciona o laço for para varrer a lista toda só para quebrar a última referência O(n).
    lista.remover_do_fim()
    print("Após remover do fim (Leonardo) [O(n)]:", lista)

    # Descoberta O(n) pelo laço do buscar() + Desvio O(n) pelo laço do _pega_nodo.
    lista.remover_por_objeto(203)
    print("Após remover por objeto (matrícula 203 - Gabriel) [O(n)]:", lista)
    print("-" * 50)

    # =========================================================================
    # 5. TESTANDO EXCEÇÕES E LIMITES LÓGICOS
    # =========================================================================
    print("=== 5. TESTANDO EXCEÇÕES E LIMITES ===")

    try:
        # A navegação _pega_nodo verifica a barreira lógica _posicao_ocupada
        # impedindo que o laço tente iterar para além do tamanho real da corrente.
        lista.elemento_em(10)
    except IndexError as e:
        print(f"Proteção lógica capturada com sucesso -> {e}")

    print("\nEstado final da Lista Encadeada no fim da rotina de testes:")
    print(lista)