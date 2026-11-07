class Nodo:
    """
    Representa o bloco de memória individual (o contêiner) da Pilha.
    O usuário final nunca interage diretamente com o Nodo, apenas
    com a carga útil (o Aluno).
    """

    def __init__(self, elemento, proximo=None):
        """
        Construtor do Nó.
        Passos:
        1 - Recebe o dado útil de domínio (ex: objeto Aluno) e guarda em 'self.elemento'.
        2 - Recebe o endereço do próximo nó e guarda em 'self.proximo' (padrão é None).
        """
        self.elemento = elemento
        self.proximo = proximo


class PilhaDinamica:
    """
    Implementa uma Pilha (Stack) baseada em alocação dinâmica de nós.
    Aplica rigorosamente a regra LIFO (Last-In, First-Out).
    Garante tempo de processamento O(1) para todas as operações estruturais.
    """

    def __init__(self):
        """
        Inicializa as referências de controle da estrutura restritiva.
        Atenção Arquitetural: O ponteiro Tail (ultimo) foi extinto!
        Como não podemos inserir ou remover do fundo da Pilha, rastrear
        o fim da estrutura seria um desperdício imperdoável de memória RAM.

        Passos:
        1 - Define o ponteiro Head (agora chamado de 'topo') apontando para o vazio (None).
        2 - Inicializa o contador lógico (total_de_elementos) com 0.
        """
        self.topo = None
        self.total_de_elementos = 0



    def esta_vazia(self) -> bool:
        """
        Avalia logicamente se a estrutura possui elementos.
        Passos:
        1 - Verifica se a variável de controle total_de_elementos é igual a 0.
        2 - Retorna True se for 0, ou False caso contrário.
        """
        return self.total_de_elementos == 0

    def tamanho(self) -> int:
        """
        Devolve a contagem de nós.
        Passos:
        1 - Acessa e retorna diretamente o atributo total_de_elementos em tempo O(1).
        """
        return self.total_de_elementos

    # =========================================================================
    # INSERÇÃO (Empilhamento O(1))
    # =========================================================================
    def push(self, valor):
        """
        Operação PUSH: Adiciona um novo elemento obrigatoriamente no topo.
        Equivale ao 'adicionar_no_inicio' da lista encadeada, garantindo O(1).

        Passos:
        1 - Instancia o novo Nodo. Na própria criação, seu ponteiro 'proximo'
            já é engatado para apontar para quem ocupa atualmente o 'topo'.
        2 - A variável de controle 'topo' é atualizada e assume este novo nó
            como o nodo absoluto da estrutura.
        3 - Incrementa o contador total_de_elementos.
        """
        novo_nodo = Nodo(valor, self.topo)
        self.topo = novo_nodo
        self.total_de_elementos += 1

    # =========================================================================
    # REMOÇÃO E CONSULTA (Desempilhamento O(1))
    # =========================================================================
    def pop(self):
        """
        Operação POP: Remove e devolve o elemento que está no topo.
        Equivale ao 'remover_do_inicio', operando no tempo estrito de O(1).

        Passos:
        1 - Valida se a pilha está vazia. Se sim, dispara IndexError (Underflow).
        2 - Isola a carga útil (o Aluno) que está dentro do nó do topo em uma
            variável temporária, pois o Nodo será destruído.
        3 - O ponteiro 'topo' abandona o nó atual e escorrega para o nó de baixo
            (acessado através de 'self.topo.proximo').
        4 - Decrementa o contador total_de_elementos.
        5 - Retorna a carga útil resgatada no passo 2. O antigo nó do topo
            agora é considerado órfão e a RAM é limpa pelo Garbage Collector.
        """
        if self.esta_vazia():
            raise IndexError("Erro de Underflow: Impossível fazer pop() em pilha vazia!")

        valor_resgatado = self.topo.elemento
        self.topo = self.topo.proximo
        self.total_de_elementos -= 1

        return valor_resgatado

    def peek(self):
        """
        Operação PEEK: "Espia" o elemento do topo sem mexer na estrutura.
        Crucial para analisar o próximo da fila sem gastar o dado. Tempo O(1).

        Passos:
        1 - Valida se a pilha está vazia (IndexError se sim).
        2 - Retorna exclusivamente a variável 'elemento' do nó que está no topo,
            mantendo todos os ponteiros físicos intocados.
        """
        if self.esta_vazia():
            raise IndexError("Pilha vazia! Não há topo para inspecionar.")

        return self.topo.elemento

    def esvaziar(self):
        """
        Destrói toda a corrente de dados instantaneamente em tempo O(1).

        Passos:
        1 - Rompe a referência principal do 'topo' (apontando para None).
        2 - Sem a âncora do topo, todos os nós subsequentes ficam inacessíveis
            e o Garbage Collector extermina a lista inteira da RAM.
        3 - Zera o contador lógico.
        """
        self.topo = None
        self.total_de_elementos = 0

    def __str__(self):
        """
        Cria o desenho hierárquico (vertical) da Pilha para debug visual.
        Mostra explicitamente quem bloqueia a saída de quem.
        """
        if self.esta_vazia():
            return "[ Pilha Física Vazia - 0 Nodos ]"

        resultado = f"--- TOPO (Tamanho: {self.total_de_elementos}) ---\n"
        atual = self.topo

        while atual is not None:
            # Formata a string alinhando o texto ao centro com 40 espaços
            resultado += f"| {str(atual.elemento):^40} |\n"
            atual = atual.proximo

        resultado += "-" * 44
        return resultado