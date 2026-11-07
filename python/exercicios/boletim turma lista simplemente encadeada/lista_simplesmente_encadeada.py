class Nodo:
    """
    Aqui to criando os Nós onde vou por o objeto e o ponteiro. Sendo um (conteiner)
    da lista encadeada. É a base oculta da estrutura, pela a estrutura da entender que
    o arquivo principal nunca interage diretamente com Nodo, apenas com o Dado (Aluno).
    """

    def __init__(self, elemento, proximo = None):
        """
        Construtor do Nó.
        Passos:
        1 - Recebe o dado util de domínio(neste caso objeto Aluno) e guardado em "self.elemento".
        2 - Recebe o endereço do proximo nó e guarda em "self.proximo" (padrão é None).
        """
        self.elemento = elemento
        self.proximo = proximo
       
class ListaSimplesmenteEncadeada:
    def __init__(self):
        
        """
        Inicializa as referências de controle da estrutura dinâmica.
        Passos:
        1 - Define o ponteiro Head (primeiro) apontando para o vazio (None).
        2 - Define o ponteiro Tail (ultimo) apontando para o vazio (None).
        3 - inicializa o contador logico (total_de_elementos) com 0.
        """
        self.primeiro = None
        self.ultimo = None
        self.total_de_elementos = 0

    def esta_vazia(self) -> bool:
        """
        Avalia logicamente se a estrutura possui elementos.
        Passos:
        1 - Verifica se a variável de controle total_de_elementos é exatamente igual a 0.
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

    def _posicao_valida(self, posicao: int) -> bool:
        """
        Valida se o índice informado é aceitável para INSERÇÕES.
        Passos:
        1 - Checa se o número é maior ou igual a 0.
        2 - Checa se o número é menor ou igual ao total de elementos (permitindo inserir no fim).
        3 - Retorna booleano.
        """
        return 0 <= posicao <= self.total_de_elementos

    def _posicao_ocupada(self, posicao: int) -> bool:
        """
        Valida se existe de fato um Nó habitando o índice (usado para REMOÇÃO/BUSCA).
        Passos:
        1 - Checa se o número é maior ou igual a 0.
        2 - Checa se o número é estritamente menor que o total de elementos.
        3 - Retorna booleano.
        """
        return 0 <= posicao < self.total_de_elementos

    def _pega_nodo(self, posicao: int) -> Nodo:
        """
        Navega iterativamente pelos ponteiros até alcançar o índice desejado em tempo O(n).
        Passos:
        1 - Aciona _posicao_ocupada() para validar se o índice existe (IndexError se falhar).
        2 - Cria o cursor 'atual' apontando inicialmente para o Head (self.primeiro).
        3 - Dispara um laço 'for' que se repete a quantidade exata de vezes da 'posicao'.
        4 - A cada repetição, avança o cursor para o próximo endereço (atual.proximo).
        5 - Ao fim do laço, retorna o objeto Nodo encontrado.
        """
        if not self._posicao_ocupada(posicao):
            raise IndexError("Posição inexistente na lista.")

        atual = self.primeiro

        for _ in range(posicao):
            atual = atual.proximo

        return atual

    # =========================================================================
    # INSERÇÕES (Costura de Ponteiros)
    # =========================================================================
    def adiciona_ordenado(self, valor):
        """
        Insere no início em tempo O(1), sem arrastar os outros elementos (zero shifting).
        Passos:
        1 - Chama o método buscar() para verificar duplicidade (ValueError se já existir).
        2 - Instancia um novo Nodo, já conectando seu ponteiro 'proximo' ao atual Head.
        3 - Checa se a lista estava vazia; se sim, aponta o Tail para este novo nó.
        4 - Atualiza a variável Head (self.primeiro) para assumir este novo nó.
        5 - Incrementa o contador total_de_elementos.
        """

        #verifico se o objeto aluno já foi cadastrado.
        if self.buscar(valor) != -1:
            raise ValueError("Erro de integridade: O elemento já está cadastrado!")
        
        #verifico se a lista esta vazia
        if self.esta_vazia():
            novo_nodo = Nodo(valor)
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
            self.total_de_elementos += 1
            return

        assert self.primeiro is not None # precisei consulta pq o erro no vscode ai coloquei o assert

        #testo se novo aluno tem media maior que o self.primeiro.
        if valor.__gt__(self.primeiro.elemento):
            novo_nodo = Nodo(valor, self.primeiro)
            self.primeiro = novo_nodo
            self.total_de_elementos += 1
            return

        atual = self.primeiro

        while atual.proximo is not None and not valor.__gt__(atual.proximo.elemento):
            atual = atual.proximo

        novo_nodo = Nodo(valor,atual.proximo)
        atual.proximo = novo_nodo

        if novo_nodo.proximo is None:
            self.ultimo = novo_nodo

        self.total_de_elementos += 1

    # =========================================================================
    # REMOÇÕES E CONSULTAS (Desconexões)
    # =========================================================================
    def remover_do_inicio(self):
        """
        Remove o primeiro elemento em tempo O(1).
        Passos:
        1 - Valida se a lista está vazia (IndexError se sim).
        2 - Atualiza o Head para pular o primeiro nó e apontar diretamente
        para o segundo (seu sucessor).
        3 - Decrementa o contador total_de_elementos.
        4 - Checa novamente se a lista esvaziou após a remoção; se sim, limpa
        o ponteiro Tail.
        """
        if self.esta_vazia():
            raise IndexError("A lista já está vazia!")

        self.primeiro = self.primeiro.proximo
        self.total_de_elementos -= 1

        if self.esta_vazia():
            self.ultimo = None

    def remover_do_fim(self):
        """
        Remove o último elemento (O(n) - O gargalo estrutural).
        Passos:
        1 - Valida se a lista está vazia (IndexError se sim).
        2 - Se houver apenas 1 elemento, repassa a execução para 'remover_do_inicio()'.
        3 - Aciona _pega_nodo() para varrer a corrente e estacionar no PENÚLTIMO nó.
        4 - Rompe o encadeamento definindo o 'proximo' do penúltimo nó como None.
        5 - Atualiza o ponteiro de atalho Tail recuando-o para este penúltimo nó.
        6 - Decrementa o contador total_de_elementos.
        """
        if self.esta_vazia():
            raise IndexError("A lista já está vazia!")

        if self.total_de_elementos == 1:
            self.remover_do_inicio()
        else:
            penultimo = self._pega_nodo(self.total_de_elementos - 2)
            penultimo.proximo = None
            self.ultimo = penultimo
            self.total_de_elementos -= 1

    def remover(self, posicao: int):
        """
        Remove por índice arbitrário costurando os ponteiros (O(n)).
        Passos:
        1 - Valida se a posição está ocupada com _posicao_ocupada()
        (IndexError se não).
        2 - Se a posição for 0, direciona para o 'remover_do_inicio()'.
        3 - Se a posição for o último índice, direciona para 'remover_do_fim()'.
        4 - Aciona _pega_nodo() para estacionar no nó imediatamente ANTERIOR ao alvo da exclusão.
        5 - Isola o nó alvo (que está logo à frente do anterior) numa variável temporária.
        6 - Faz o desvio: aponta o 'proximo' do nó anterior direto para o sucessor do alvo.
        7 - Decrementa o contador total_de_elementos.
        """
        if not self._posicao_ocupada(posicao):
            raise IndexError(f"Posição {posicao} inválida para remoção.")

        if posicao == 0:
            self.remover_do_inicio()
        elif posicao == self.total_de_elementos - 1:
            self.remover_do_fim()
        else:
            nodo_anterior = self._pega_nodo(posicao - 1)
            nodo_a_remover = nodo_anterior.proximo
            nodo_anterior.proximo = nodo_a_remover.proximo
            self.total_de_elementos -= 1

    def buscar(self, valor_ou_objeto) -> int:
        """
        Busca sequencial iterando pelos ponteiros em tempo O(n).
        Passos:
        1 - Inicia o cursor 'atual' no Head (self.primeiro).
        2 - Inicia o contador numérico 'posicao' em 0.
        3 - Executa laço 'while' que se repete enquanto o cursor não chegar ao fim absoluto (None).
        4 - Dentro do laço, aciona '__eq__' para checar se a carga útil atual bate com o procurado.
        5 - Se achar, interrompe tudo e retorna o número da 'posicao'.
        6 - Se não achar, avança o cursor para o próximo nó e incrementa 'posicao' em 1.
        7 - Se o laço acabar naturalmente (não encontrou o alvo), retorna -1.
        """
        atual = self.primeiro
        posicao = 0

        while atual is not None:
            if atual.elemento == valor_ou_objeto:
                return posicao
            atual = atual.proximo
            posicao += 1

        return -1

    def remover_por_objeto(self, valor_ou_chave):
        """
        Descobre o índice numérico através da busca e orquestra a remoção O(n).
        Passos:
        1 - Executa o método buscar() passando o alvo para descobrir em qual índice ele está.
        2 - Se o retorno for -1, dispara ValueError avisando que não foi encontrado.
        3 - Se for encontrado, repassa o índice válido para o método remover().
        """
        indice = self.buscar(valor_ou_chave)
        if indice == -1:
            raise ValueError("O elemento informado não foi encontrado na lista.")
        self.remover(indice)

    def elemento_em(self, indice: int):
        """
        Retorna apenas a carga útil (elemento) do nó escondendo a mecânica de contêiner.
        Passos:
        1 - Aciona _pega_nodo() passando o índice para extrair o Nodo desejado.
        2 - Acessa e retorna unicamente a variável 'elemento' (o objeto Aluno) que está dentro dele.
        """
        nodo = self._pega_nodo(indice)
        return nodo.elemento

    def listar(self) -> list:
        """
        Desmembra a estrutura dinâmica transferindo as cargas úteis para um array nativo.
        Passos:
        1 - Instancia uma lista padrão vazia do Python.
        2 - Inicia um cursor 'atual' apontando para o Head.
        3 - Dispara um laço 'while' para percorrer até o fim da corrente (None).
        4 - A cada volta, extrai a carga útil e faz um append na lista nativa.
        5 - Avança o cursor para o próximo nó.
        6 - Ao fim do laço, retorna o vetor populado.
        """
        resultado = []
        atual = self.primeiro

        while atual is not None:
            resultado.append(atual.elemento)
            atual = atual.proximo

        return resultado

    def __str__(self):
        """
        Cria o desenho hierárquico da estrutura para debug visual no terminal.
        Passos:
        1 - Se vazia, retorna mensagem curta.
        2 - Instancia a string inicial constando o tamanho atual.
        3 - Posiciona o cursor de varredura no Head e inicia contador visual em 0.
        4 - Executa laço 'while' até o fim da corrente.
        5 - Concatena na string o índice e o texto do objeto alvo (acionando seu __str__).
        6 - Avança o cursor físico e o índice visual.
        7 - Retorna a super string pronta para o print().
        """
        if self.esta_vazia():
            return "[Ocupação Dinâmica: 0 - Lista Vazia]"

        resultado = f"[Ocupação Dinâmica: {self.total_de_elementos} nodos]"
        atual = self.primeiro
        indice = 0

        while atual is not None:
            resultado += f"\n    - [{indice}] {str(atual.elemento)}"
            atual = atual.proximo
            indice += 1

        return resultado