#criação da classe livro,1 seus atributos ao lado do self, e os parametro e o que está entre parenteses
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
        quantidade_em_estoque_int = int(self.quantidade_em_estoque)
        valor_float = float(self.valor)
        print(f'Valor total em estoque: R${quantidade_em_estoque_int * valor_float}')
        print('')
class Livraria:
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, Livro):
        self.acervo.append(Livro)

    def cadastro_livros (self):
        continuar_cadastro = True
        while continuar_cadastro:  # continuar variável boolena que se inicia com o true e no proxímo input e testado
            # no if e se não satisfaça a condição muda o estado para False.
            #print(continuar_cadastro) print de teste para verificar se recebia corretamente o valor do input.
            titulo = str(input('Informe o titulo do livro: '))
            codigo = int(input('Informe o numero do codigo do livro: '))
            editora = str(input('Informe a editora: '))
            area= str(input('Informe a area do livro: '))
            ano = int(input('Informe o ano da edição: '))
            valor = float(input('Informe o valor do livro: '))
            quantidade_em_estoque = int(input('Informe a quantidade do estoque: '))
            livro_novo = Livro(titulo, codigo, editora, area, ano, valor, quantidade_em_estoque)
            self.adicionar_livro(livro_novo)#coloca os objetos na lista
            confirmacao = input('Deseja continuar a inserir livros no acervo.\nDigite SIM/S ou NÃO/N: ')
            if confirmacao.lower() not in ['s','y','sim']:
                continuar_cadastro = False

    def acervo_livraria(self):
        if self.acervo: #self referencia a classe Livraria
            print(f'\n+++++ Listagem do Acervo da Livraria +++++\n')
            for livro in self.acervo:
                livro.info()
        else:
            print('\nO acervo da livraria está vazio.\n')

    def pesquisa_nome(self):
        busca_nome = input(f'\nInforme nome do livro que deseja pesquisa:\n')
        resultados = [livro for livro in self.acervo if livro.titulo.lower() == busca_nome.lower() ]
        if resultados:
            if len(resultados) == 1:
                print(f'\n++++Resultado da pesquisa por nome.++++\n')
            else:
                print(f'\n++++Resultado da pesquisa possui homônimos.')
            for livro in resultados:
                livro.info()
        else:
            print('\nNenhum livro foi encontrado com este nome no acervo.\n')

    def pesquisa_categoria(self):
        busca_categoria = input(f'\nInforme a categoria do livro que deseja pesquisa:\n')
        resultados = [livro for livro in self.acervo if livro.area.lower() == busca_categoria.lower()]
        if resultados:
            print(f'\n++++Resultado da pesquisa por categoria.++++\n')
            for livro in resultados:
                livro.info()

        else:
            print('\nNenhum livro desta categoria foi encontrado no acervo.\n')

    def pesquisa_valor(self):
        busca_valor = float(input(f'\nInforme o preço máximo do livro que deseja pesquisa:\n'))
        print('')
        resultados = [livro for livro in self.acervo if livro.valor < busca_valor]  # aqui faremos uma lista onde será suprida com os criteria que esta dentro das chaves
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
            resultados_mais_caros = [a for a in self.acervo if a.valor >= busca_valor]
            print(f'\n++++Livros do acervo de preço acima ou igual a R${busca_valor:.2f}\n')
            for livro in resultados_mais_caros:
                livro.info()

    def pesquisa_quantidade_acervo(self):
        busca_quantidade_estoque = int(input(f'\nInforme a quantidade mínima em estoque que deseja pesquisar: \n'))
        resultados = [livro for livro in self.acervo if livro.quantidade_em_estoque >= busca_quantidade_estoque]
        if resultados:
            for livro in resultados:
                livro.info()
        else:
            print(f'Não foram encontrados livros com valores iguais ou maiores {busca_quantidade_estoque} em estoque.')

    def pesquisa_valor_total_acervo(self):
        busca_valor_estoque = sum (livro.valor * livro.quantidade_em_estoque for livro in self.acervo)
        print(f'\nO valor total de todos os livros no acervo é: R$ {busca_valor_estoque:.2f}\n')

    def carregar_acervo(self):
        acervo = open('acervo.txt', 'r')
        linha = acervo.readline().replace('\n', '')
        linha_sep = linha.split(',')
        while linha:
            self.adicionar_livro(Livro(linha_sep[0],linha_sep[1], linha_sep[2], linha_sep[3], linha_sep[4], linha_sep[5], linha_sep[6]))
            linha = acervo.readline().replace('\n', '')
            linha_sep = linha.split(',')
        for livro in self.acervo:
            livro.info()

    def gravar_acervo(self):
        acervo = open('acervo.txt', 'w')
        for livro in self.acervo:
            linha = f'{livro.titulo},{livro.codigo},{livro.editora},{livro.area},{livro.ano},{livro.valor},{livro.quantidade_em_estoque}\n'
            acervo.write(linha)

    def confimação_encerramento(self):
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
    Livraria = Livraria()
    Livraria.exibir_menu()
    opcao = int(input('Por favor informe a opção desejada: '))

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

    Livraria.confimação_encerramento()
    #print('Programa encerrado.')