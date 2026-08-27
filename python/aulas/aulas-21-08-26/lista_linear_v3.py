class Aluno:
    """
    Representa o registro de um aluno no sistema acadêmico.
    Funciona como um exemplo de tipo de elemento específico armazenado na lista sequencial.
    """

    def __init__(self, matricula: int, nome: str):
        """Construtor da classe Aluno: inicializa a matrícula e o nome."""
        self.matricula = matricula
        self.nome = nome

    def __str__(self):
        """Retorna a representação textual legível do objeto Aluno."""
        return f"Aluno(matricula={self.matricula}, nome='{self.nome}')"

    def __eq__(self, outro):
        """
        Define o critério de igualdade entre dois objetos Aluno.
        Duas instâncias são consideradas iguais se possuírem a mesma matrícula.
        Permite que a lista sequencial busque e valide duplicatas de forma genérica.
        """
        if isinstance(outro, Aluno):
            return self.matricula == outro.matricula
        # Se for comparado diretamente com um valor primitivo (ex: uma chave de busca ou ID)
        return self.matricula == outro

    def __repr__(self):
        """
        Retorna a representação oficial e técnica do objeto Aluno.
        Este método é chamado automaticamente pelo Python ao imprimir coleções
        como listas ou dicionários) que contêm este objeto, ou durante a depuração
        (debug). Ele substitui a exibição padrão do endereço de memória hexadecimal
        por uma string clara que identifica o estado do objeto.
        """
        return f"Aluno: {self.nome}"  # ou qualquer formato que preferir


class ListaSequencial:
    """
    Implementa uma Lista Linear Sequencial baseada em vetor estático (alocação contígua).
    Totalmente polimórfica: gerencia qualquer tipo de objeto de domínio desde que
    ele implemente os métodos de comparação adequados (__eq__).
    """

    def __init__(self, capacidade: int = 10):
        """
        Construtor da ListaSequencial: aloca o vetor estático com tamanho máximo fixo
        e inicializa o contador de elementos ativos.
        """
        self.capacidade = capacidade
        self.elementos = [None] * capacidade  # Vetor físico estático preenchido com None
        self.total_de_elementos = 0  # Controla quantos elementos válidos existem na lista

    def esta_vazia(self) -> bool:
        """Retorna True se a lista não possui nenhum elemento armazenado, caso contrário False."""
        return self.total_de_elementos == 0

    def esta_cheia(self) -> bool:
        """Retorna True se o número de elementos atingiu a capacidade máxima estipulada."""
        return self.total_de_elementos == self.capacidade

    def tamanho(self) -> int:
        """Retorna o número atual de elementos válidos armazenados na lista."""
        return self.total_de_elementos

    def posicao_valida(self, posicao: int) -> bool:
        """Verifica se uma posição está dentro do intervalo útil aceitável para inserções (0 até total)."""
        return 0 <= posicao <= self.total_de_elementos

    def posicao_ocupada(self, posicao: int) -> bool:
        """Verifica se uma posição específica possui um elemento válido cadastrado (0 até total - 1)."""
        return 0 <= posicao < self.total_de_elementos

    def elemento_em(self, indice: int):
        """
        Retorna o elemento de uma determinada posição em tempo constante O(1).
        Lança uma exceção se o índice for inválido ou apontar para um espaço vazio.
        """
        if not self.posicao_ocupada(indice):
            raise IndexError(f"Índice {indice} inválido ou posição vazia.")
        return self.elementos[indice]

    def buscar(self, valor_ou_objeto) -> int:
        """
        Realiza uma busca sequencial O(n) percorrendo os elementos
        ativos. Utiliza o operador de igualdade (== / __eq__), permitindo
        buscar tanto pelo objeto nteiro quanto por uma chave de negócio (ex: matrícula,
        código, ID) dependendo de como o __eq__ da classe de domínio foi implementado.
        Retorna o índice onde o elemento se encontra, ou -1 se não achar.
        """
        for i in range(self.total_de_elementos):
            if self.elementos[i] == valor_ou_objeto:
                return i
        return -1

    def inserir(self, posicao: int, valor):
        """
        Insere um elemento em uma posição arbitrária específica em tempo O(n).
        Valida a capacidade, a posição e a unicidade do objeto antes de
        deslocar os elementos.
        """
        # Verifica se o vetor estático já atingiu o limite de capacidade física
        if self.esta_cheia():
            raise OverflowError("A lista sequencial está cheia! "
                                "Capacidade esgotada.")

        # Valida se a posição solicitada está no intervalo permitido
        if not self.posicao_valida(posicao):
            raise ValueError(f"Posição {posicao} inválida para inserção.")

        # Regra de negócio polimórfica: Impede cadastros duplicados
        # baseando-se no __eq__
        if self.buscar(valor) != -1:
            raise ValueError(f"Erro de integridade: O elemento informado já "
                             f"está cadastrado na lista!")

        # Deslocamento (shifting) dos elementos da direita para a frente,
        # abrindo a vaga
        for i in range(self.total_de_elementos - 1, posicao - 1, -1):
            self.elementos[i + 1] = self.elementos[i]

        # Insere o novo elemento na gaveta liberada e incrementa a contagem
        self.elementos[posicao] = valor
        self.total_de_elementos += 1

    def adicionar_fim(self, valor):
        """
        Insere um novo elemento diretamente no final da lista em tempo O(1).
        Valida a capacidade e a unicidade antes de inserir.
        """
        # Verifica se a lista atingiu o limite máximo
        if self.esta_cheia():
            raise OverflowError("A lista sequencial está cheia! "
                                "Capacidade esgotada.")

        # Regra de negócio polimórfica: Impede duplicatas
        if self.buscar(valor) != -1:
            raise ValueError(f"Erro de integridade: O elemento "
                             f"informado já está cadastrado na lista!")

        self.elementos[self.total_de_elementos] = valor
        self.total_de_elementos += 1

    def adicionar_no_inicio(self, valor):
        """
        Insere um novo elemento no início da lista (posição 0) em tempo O(n).
        Reaproveita o método 'inserir', herdando automaticamente as validações de unicidade e capacidade.
        """
        self.inserir(0, valor)

    def remover(self, posicao: int):
        """
        Remove o elemento de uma posição específica em tempo O(n).
        Realiza o deslocamento (shifting) dos elementos à esquerda para cobrir a lacuna.
        """
        if not self.posicao_ocupada(posicao):
            raise IndexError(f"Posição {posicao} inválida ou desocupada para remoção.")

        # Deslocamento para fechar o espaço do item removido
        for i in range(posicao, self.total_de_elementos - 1):
            self.elementos[i] = self.elementos[i + 1]

        self.total_de_elementos -= 1
        self.elementos[self.total_de_elementos] = None

    def remover_do_inicio(self):
        """Remove o primeiro elemento da lista (posição 0) em tempo O(n)."""
        if self.esta_vazia():
            raise IndexError("A lista já está vazia!")
        self.remover(0)

    def remover_do_fim(self):
        """Remove o último elemento da lista em tempo O(1) e libera
        explicitamente a referência da memória."""
        if self.esta_vazia():
            raise IndexError("A lista já está vazia!")

        # O índice do último elemento válido
        indice_ultimo = self.total_de_elementos - 1
        # Limpa explicitamente a referência para liberar o objeto
        # da memória RAM (Garbage Collector)
        self.elementos[indice_ultimo] = None
        # Decrementa o ponteiro lógico de ocupação
        self.total_de_elementos -= 1

    def remover_por_objeto(self, valor_ou_chave):
        """Busca um elemento (ou chave de identificação) e o remove da estrutura em O(n)."""
        indice = self.buscar(valor_ou_chave)
        if indice == -1:
            raise ValueError("O elemento informado não foi encontrado na lista.")
        self.remover(indice)

    def listar(self) -> list:
        """Retorna uma cópia limpa em formato de lista nativa contendo apenas os elementos ativos."""
        resultado = []
        for i in range(self.total_de_elementos):
            resultado.append(self.elementos[i])
        return resultado

    def __str__(self):
        """Define a representação textual personalizada da lista com a ocupação e os itens listados abaixo."""
        resultado = f"[Ocupação: {self.total_de_elementos}/{self.capacidade}]"
        for i in range(self.total_de_elementos):
            # resultado += f"\n    - {str(self.elementos[i])}"
            resultado += f"\n    - [{i}] {str(self.elementos[i])}"
        return resultado
