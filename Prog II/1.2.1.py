'''
criação da classe livro, seus
 atributos ao lado do self,
 e os parametro e o que está entre parenteses
 '''
class Livro:
    def __init__(self, titulo, codigo, editora, area, ano, valor, quantidade_em_estoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.quantidade_em_estoque = quantidade_em_estoque

    def info(self):
        print(f">>>>> Cod#{self.codigo}")
        print(f"Titulo/Editora: {self.titulo}/{self.editora}")
        print(f'Categoria: {self.area}')
        print(f'Ano: {self.ano}')
        print(f'Valor: R$ {self.valor}')
        print(f'Estoque: {self.quantidade_em_estoque}')
        print(f'Valor total em estoque: R${self.valor*self.quantidade_em_estoque}')
        print('')

class Livraria:

    def __init__(self):
        self.acervo = [] #estou criando um atributo acervo, que vai ser uma lista vazia que irá
        # carregar os dados do cadastro de livros e de acervo.txt, por isso que e o primeiro metodo
        # a ser chamado.

    def cadastro_livros (self):
        continuar_cadastro = True
        while continuar_cadastro:  # continuar variável boolena que se inicia com o true e no proxímo input e testado
                                   # no if e se não satisfaça a condição muda o estado para False.
                                   #print(continuar_cadastro) print de teste para verificar se recebia corretamente o valor do input.
            titulo = input('Informe o titulo do livro: ')
            codigo = int(input('Informe o numero do codigo do livro: '))
            editora = str(input('Informe a editora: '))
            area= str(input('Informe a area do livro: '))
            ano = int(input('Informe o ano da edição: '))
            valor = float(input('Informe o valor do livro: '))
            quantidade_em_estoque = int(input('Informe a quantidade do estoque: '))
            livro_novo = Livro(titulo, codigo, editora, area, ano, valor, quantidade_em_estoque)
            self.acervo.append(livro_novo)#adiciona os livros na lista que e um atributo de Livraria
            confirmacao = input('Deseja continuar a inserir livros no acervo.\nDigite SIM/S ou NÃO/N: ')
            if confirmacao.lower() not in ['s','y','sim']:
                continuar_cadastro = False

    def acervo_livraria(self):
        if self.acervo: #self referencia a classe Livraria e acervo a lista se ela a lista estiver vazia passa pro else
            print(f'\n+++++ Listagem do Acervo da Livraria +++++\n')
            for livro in self.acervo:
                livro.info()
        else:
            print('\nO acervo da livraria está vazio.\n')

    def pesquisa_nome(self):
        busca_nome = str(input(f'\nInforme nome do livro que deseja pesquisa:\n'))
        '''
        resultados = [livro for livro in self.acervo if livro.titulo.lower() == busca_nome.lower() ] aqui faremos uma lista onde será 
        suprida com os criteria que esta dentro das chaves ou seja livro que e o objeto vai receber o que 'livro' dentro
        do 'for livro in self.acervo' self.acervo e um atributo que recebeu uma lista, para cada atributo livro.titulo que
        for igual que busca_nome ira ser guardada na lista resultados, fora passa tudo para minusculos para ficar possivel a comparação.  
        '''
        resultados = [] #lista que guarda o resultado do if
        for livro in self.acervo: # percorre a lista do atributo self.acervo
            if livro.titulo.lower() == busca_nome.lower(): #if compara o atributo .titulo de livro em minusculo com busca_nome em minusculo sendo .lower que passa tudo para minusculo
                resultados.append(livro) # acrescenta o objeto que passou no teste do if a resultados
        if resultados:
            if len(resultados) == 1: #verifica se temos resultado homônimos.
                print(f'\n++++Resultado da pesquisa por nome.++++\n')
            else:
                print(f'\n++++Resultado da pesquisa possui homônimos.++++\n')
            for livro in resultados: #print da lissta resultados
                livro.info()
        else: #se resultado estiver vazio ira imprimir a mensagem a baixo.
            print('\nNenhum livro foi encontrado com este nome no acervo.\n')

    def pesquisa_categoria(self):
        busca_categoria = input(f'\nInforme a categoria do livro que deseja pesquisa:\n')
        '''
        resultados = [livro for livro in self.acervo if livro.categoria.lower() == busca_categoria.lower() ] aqui faremos uma lista onde será 
        suprida com os criteria que esta dentro das chaves ou seja livro que e o objeto vai receber o que 'livro' dentro
        do 'for livro in self.acervo' self.acervo e um atributo que recebeu uma lista, para cada atributo livro.area que
        for igual que busca_categoria ira ser guardada na lista resultados, fora passa tudo para minusculos para ficar possivel a comparação.  
        '''
        resultados = []
        for livro in self.acervo:
            if livro.area.lower() == busca_categoria.lower():#compara livro.area com em minusculo com busca_categotia em minusculo
                resultados.append(livro) #adiciona em resultados o que passou pelo if
        if resultados: #imprimi o que foi guardado em resultados
            print(f'\n++++Resultado da pesquisa por categoria.++++\n')
            for livro in resultados:
                livro.info()

        else:
            print('\nNenhum livro desta categoria foi encontrado no acervo.\n')

    def pesquisa_valor(self):
        busca_valor = float(input(f'\nInforme o preço máximo do livro que deseja pesquisa:\n'))
        print('')
        '''
        resultados = [livro for livro in self.acervo if livro.valor < busca_valor] aqui faremos uma lista onde será 
        suprida com os criteria que esta dentro das chaves ou seja livro que e o objeto vai receber o que 'livro' dentro
        do 'for livro in self.acervo' self.acervo e um atributo que recebeu uma lista, para cada atributo livro.valor que
        for menor que busca_valor ira ser guardada na lista resultados.  
        '''
        resultados = []  # so se cria a lista vazia se o metodo for acionado para guarda o resultado do if
        for livro in self.acervo:
            if livro.valor < busca_valor:
                resultados.append(livro)
        if resultados:
            print(f'\n++++Livros do acervos de preço até R$ {busca_valor:.2f}.++++\n')
            for livro in resultados:
                livro.info()
        else:
            print('\nNenhum livro desta categoria foi encontrado no acervo.\n')

        print(f'\nGostaria de ver os livros de Preço igual ou maior que R$ {busca_valor:.2f}.\n')
        confirmacao = input(f'Digite Sim/S ou NÃO/N.\n').lower()
        if confirmacao not in ['sim', 's', 'y', 'yes']:
            print(f'\nConsulta encerrada.\n')
        else:
            #resultados_mais_caros = [a for a in self.acervo if a.valor >= busca_valor]
            resultados = []  # so se cria a lista vazia se o metodo for acionado para guarda o resultado do if
            for livro in self.acervo:
                if livro.valor >= busca_valor:
                    resultados.append(livro)
            print(f'\n++++Livros do acervo de preço acima ou igual a R${busca_valor:.2f}\n')
            #for livro in resultados_mais_caros:
            for livro in resultados:
                livro.info()

    def pesquisa_quantidade_acervo(self):
        busca_quantidade_estoque = int(input(f'\nInforme a quantidade mínima em estoque que deseja pesquisar: \n'))
        #resultados = [livro for livro in self.acervo if livro.quantidade_em_estoque >= busca_quantidade_estoque]
        resultados = []  # so se cria a lista vazia se o metodo for acionado para guarda o resultado do if
        for livro in self.acervo:
            if livro.quantidade_em_estoque >=busca_quantidade_estoque:
                resultados.append(livro)
        if resultados:
            for livro in resultados:
                livro.info()
        else:
            print(f'Não foram encontrados livros com valores iguais ou maiores {busca_quantidade_estoque} em estoque.')

    def pesquisa_valor_total_acervo(self):
        #busca_valor_estoque = sum (livro.valor * livro.quantidade_em_estoque for livro in self.acervo) este metodo vai fazer a soma 'sum' da multiplicação dos atributos
        # utilizei o metodo a baixo pois fica mais facil o entendimento
        #com isso tive que iniciar a variavel busca_valor_estoque com 0.
        busca_valor_estoque = 0
        for livro in self.acervo:
            busca_valor_estoque += (livro.valor * livro.quantidade_em_estoque)
        print(f'\nO valor total de todos os livros no acervo é: R$ {busca_valor_estoque:.2f}\n')

    def carregar_acervo(self):
        acervo_arquivo = open('acervo.txt', 'r')#estou atribuindo o conteudo do arquivo acervo.txt a variavel acervo_arquivo
        linha = acervo_arquivo.readline().replace('\n', '')# estou atribuindo a linha os paramentros para a
        # leitura de acervo_arquivo que e o readline() leitura de linha
        # ja replace o
        linha_sep = linha.split(',')
        while linha:
            self.acervo.append(Livro(linha_sep[0],linha_sep[1], linha_sep[2], linha_sep[3], linha_sep[4], float(linha_sep[5]), int(linha_sep[6])))
            linha = acervo_arquivo.readline().replace('\n', '')
            linha_sep = linha.split(',')
        for livro in self.acervo:
            livro.info()

    def gravar_acervo(self):
        acervo_arquivo = open('acervo.txt', 'w')
        for livro in self.acervo:
            linha = f'{livro.titulo},{livro.codigo},{livro.editora},{livro.area},{livro.ano},{livro.valor},{livro.quantidade_em_estoque}\n'
            acervo_arquivo.write(linha)

    def confimacao_encerramento(self):
        if opcao == 0:
            print('Deseja atualizar o arquivo do estoque?')
            resposta = input(f'SIM OU NÃo.\n').lower()
            if resposta in ['sim','s','y','yes']:
                self.gravar_acervo()
                print('Programa encerrado, com arquivo do estoque atualizado.')
            else:
                print('Programa encerrado')

    def exibir_menu(self):
        print(f'+++Para interagir com o sistema favor digite o numero de uma da opções abaixo+++ \n'
              f'|   1 – Cadastrar novo livro                                                   |\n'
              f'|   2 – Listar livros                                                          |\n'
              f'|   3 – Buscar livros por nome                                                 |\n'
              f'|   4 – Buscar livros por categoria                                            |\n'
              f'|   5 – Buscar livros por preço                                                |\n'
              f'|   6 – Busca por quantidade em estoque                                        |\n'
              f'|   7 – Valor total no estoque                                                 |\n'
              f'|   8 - Carregar estoque                                                       |\n'
              f'|   9 - Atualizar arquivo de estoque                                           |\n'
              f'|   0 – Encerrar atividades                                                    |\n'
              f'|______________________________________________________________________________|')

if __name__=='__main__':
    Livraria = Livraria() # fazendo isso eu chamo o construtor __init__
    # se eu não fizer isso tenho que definir obrigatoriamento o self = Livraria.
    # dentro do parentes dos metodos para dizer que são da classe Livraria
    Livraria.exibir_menu() # chama o metodo exibir_menu
    opcao = int(input('Por favor informe a opção desejada: ')) #variavel que recebe a escolha do menu

    while opcao != 0:
        if opcao == 1:
            Livraria.cadastro_livros()
        elif opcao == 2:
            Livraria.acervo_livraria()
        elif opcao == 3:
            Livraria.pesquisa_nome()
        elif opcao == 4:
            Livraria.pesquisa_categoria()
        elif opcao == 5:
            Livraria.pesquisa_valor()
        elif opcao == 6:
            Livraria.pesquisa_quantidade_acervo()
        elif opcao == 7:
            Livraria.pesquisa_valor_total_acervo()
        elif opcao == 8:
            Livraria.carregar_acervo()
        elif opcao == 9:
            Livraria.gravar_acervo()
        else:
            print('Opção não valida.')
        Livraria.exibir_menu()

        opcao = int(input('Por favor informe a opção desejada: '))

    Livraria.confimacao_encerramento()