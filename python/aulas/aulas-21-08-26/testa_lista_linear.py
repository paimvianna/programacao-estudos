from lista_linear_v3 import Aluno, ListaSequencial

if __name__ == "__main__":

    # =========================================================================
    # 1. INICIALIZAÇÃO DA ESTRUTURA
    # =========================================================================
    print("=== 1. INICIALIZAÇÃO DA ESTRUTURA ===")

    # Instancia a lista sequencial com capacidade máxima estática igual a 4
    lista = ListaSequencial(4)
    print("Lista criada vazia:", lista)
    print(f"Está vazia? {lista.esta_vazia()}")
    print(f"Está cheia? {lista.esta_cheia()}")
    print("-" * 50)





    # =========================================================================
    # 2. TESTANDO INSERÇÕES E A NOVA REGRA DE UNICIDADE (DUPLICIDADE)
    # =========================================================================
    print("=== 2. TESTANDO INSERÇÕES E VALIDAÇÃO DE DUPLICIDADE ===")

    a1 = Aluno(201, "Lucas")
    a2 = Aluno(202, "Mariana")
    a3 = Aluno(203, "Gabriel")
    a4 = Aluno(204, "Juliana")

    # Adiciona o primeiro elemento no fim da lista
    lista.adicionar_fim(a1)
    print("Após adicionar no fim (Lucas):", lista)

    # Testando o bloqueio de duplicidade: tenta inserir aluno com matrícula já existente (201)
    print("\n[TESTE DE SEGURANÇA]: Tentando inserir aluno com matrícula duplicada (201)...")
    try:
        lista.adicionar_fim(Aluno(201, "Lucas Duplicado"))
    except ValueError as e:
        print(f"Bloqueio bem-sucedido -> {e}")
    print(f"Estado da lista após tentativa duplicada: {lista}\n")

    try:
        lista.adicionar_no_inicio(Aluno(201, "Lucas Duplicado"))
    except ValueError as e:
        print(f"Tentativa bloqueada com sucesso: {e}\n")


    # Adiciona um elemento no início da lista
    lista.adicionar_no_inicio(a2)
    print("Após adicionar no início (Mariana):", lista)

    # Inserindo por posição arbitrária (índice 1)
    lista.inserir(1, a3)
    print("Após inserir Gabriel na posição 1:", lista)

    # Preenche o último espaço disponível
    lista.adicionar_fim(a4)
    print("Após preencher o último espaço com Juliana:", lista)
    print(f"Lista cheia agora? {lista.esta_cheia()}")
    print("-" * 50)

    # =========================================================================
    # 3. TESTANDO ACESSOS DIRETOS E BUSCAS
    # =========================================================================
    print("=== 3. TESTANDO ACESSOS E BUSCAS ===")

    # Acesso direto a um índice O(1)
    print(f"Elemento no índice 2 (O(1)): {lista.elemento_em(2)}")

    # Busca sequencial por chave O(n)
    pos = lista.buscar(203)
    print(f"Busca pelo aluno com matrícula 203 (O(n)): Encontrado no índice {pos}")

    # Listagem bruta convertida para array nativo
    print(f"Listagem bruta gerada por listar(): {lista.listar()}")
    print("-" * 50)

    # =========================================================================
    # 4. TESTANDO REMOÇÕES
    # =========================================================================
    print("=== 4. TESTANDO REMOÇÕES ===")

    lista.remover_do_inicio()
    print("Após remover do início:", lista)

    lista.remover_do_fim()
    print("Após remover do fim:", lista)

    # Re-inserindo um novo aluno para validar a remoção por chave/objeto
    lista.adicionar_fim(Aluno(205, "Fernanda"))
    print("Após adicionar Fernanda:", lista)

    lista.remover_por_objeto(203)
    print("Após remover por objeto (matrícula 203 - Gabriel):", lista)
    print("-" * 50)

    # =========================================================================
    # 5. TESTANDO EXCEÇÕES, LIMITES E ESTOURO DE CAPACIDADE
    # =========================================================================
    print("=== 5. TESTANDO EXCEÇÕES E LIMITES ===")

    try:
        # Tentando acessar um índice inválido ou fora do escopo útil
        lista.elemento_em(10)
    except IndexError as e:
        print(f"Capturado com sucesso -> {e}")

    print("\nEstado final da Lista:", lista)