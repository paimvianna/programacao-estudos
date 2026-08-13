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
        print(f'Valor total em estoque: R${self.valor * self.quantidade_em_estoque}')
        print('')

    def info_codigo(self):
        print(f">>>>> Cod#{self.codigo}")
        print(f"Titulo/Editora: {self.titulo}/{self.editora}")
        print(f'Categoria: {self.area}')
        print(f'Ano: {self.ano}')


class Filial:
    def __init__(self, codigo_filial, nome_filial, endereco_filial, contato_filial):
        self.codigo_filial = codigo_filial
        self.nome_filial = nome_filial
        self.endereco_filial = endereco_filial
        self.contato_filial = contato_filial
        self.acervo = []

    def info(self):
        print(f">>>>> Cod_filial#{self.codigo_filial}")
        print(f"Nome da Filial: {self.nome_filial}")
        print(f'Endereço: {self.endereco_filial}')
        print(f'Contato telefonico da Filial: {self.contato_filial}')
        print('')

    def info_acervo(self):
        print(f'\n+++Estoque da Filial {self.nome_filial} {self.codigo_filial} +++\n')
        if self.acervo:
            valor_total_filial = 0
            for livro in self.acervo:
                livro.info()
                valor_total_filial += livro.valor * livro.quantidade_em_estoque
            print(f'Valor total em estoque nesta filial: R$ {valor_total_filial:.2f}\n')
        else:
            print(f'Não consta nada no estoque desta filial.\n')



class Livraria:

    def __init__(self):
        self.filial = Filial('','','','')
        self.filiais = []  # estou criando um atributo filiais, que vai ser uma lista vazia que irá
        # carregar os dados do cadastro das filiais e de acervo.txt que vai ter as filiais e seus acervos,
        # por isso que e o primeiro metodo a ser chamado.

    def cadastro_filial(self):
        codigo = int(input(f'Informe o numero da filial: '))
        codigo_filial = str(f'#FL{codigo:02d}')  # Formatando para ter sempre dois dígitos
        nome_filial = input(f'Informe o nome da Filial: ')
        endereco_filial = input(f'Informe o Endereço da Filial: ')
        contato_filial = input(f'Informe o telefone de contato da filial: ')
        print(f'|______________________________________________________________________________|')
        print('')
        nova_filial = Filial(codigo_filial, nome_filial, endereco_filial, contato_filial)
        self.filiais.append(nova_filial)

    def listar_filiais(self):
        if self.filiais:
            for filiais in self.filiais:
                filiais.info()
        else:
            print(f'A lista de filiais esta vazia.')

    def escolha_filiais(self):
        if self.filiais:
            print(f'\n+++++++++++++++Lista de Filiais+++++++++++++++\n')
            print(f'Numero//Nome Filial//Codigo\n')
            for numero, filiais in enumerate(self.filiais):
                print(f'{numero + 1:06d}//{filiais.nome_filial}//{filiais.codigo_filial}')
        else:
            print(f'\nNão temos filiais cadastradas ainda!!!\n')
        confirmacao = int(input(f'\nPor favor informe numero da filial da filial que deseja usar: \n'))
        if 1 <= confirmacao <= len(self.filiais):
            #print(len(self.filiais)) pus este print para um controle do que realmente processado pelo len.
            return self.filiais[confirmacao - 1]
        else:
            print(f'O numero informado escolhido não esta dentro do números informados.\n'
                  f'Escolha um número da lista.')


    def cadastro_livros(self):
        if not self.filiais:
            print(f'\nNão temos filiais cadastradas. Cadastre uma Filial agora para este livro.\n')
            self.cadastro_filial()
            tamanho = len(self.filiais) -1
            print(tamanho)
            filial_existente = self.filiais[tamanho]
        else:
            confirmacao = input(f'Deseja cadastra um nova filial para o livro que vai cadastrar.\n'
                                f'Digite SIM/S ou NÃO/n: ')
            if confirmacao.lower() in ['s', 'y', 'sim']:
                self.cadastro_filial()
                tamanho = len(self.filiais) - 1
                filial_existente = self.filiais[tamanho]
                #print(filial_existente)
            else:
                filial_existente = self.escolha_filiais()
                print(filial_existente)
                if not filial_existente:
                    return

        continuar_cadastro = True
        while continuar_cadastro:  # continuar variável boolena que se inicia com o true e no proxímo input e testado
            # no if e se não satisfaça a condição muda o estado para False.
            # print(continuar_cadastro) print de teste para verificar se recebia corretamente o valor do input.

            titulo = input('Informe o titulo do livro: ')
            codigo = int(input('Informe o numero do codigo do livro: '))
            editora = str(input('Informe a editora: '))
            area = str(input('Informe a area do livro: '))
            ano = int(input('Informe o ano da edição: '))
            valor = float(input('Informe o valor do livro: '))
            quantidade_em_estoque = int(input('Informe a quantidade do estoque: '))
            livro_novo = Livro(titulo, codigo, editora, area, ano, valor, quantidade_em_estoque)
            filial_existente.acervo.append(livro_novo)  # adiciona os livros na lista que e um atributo de Livraria
            for livro in self.filial.acervo:
                livro.info()
            for a in self.filiais:
                #print(a) mesma relação de controle que pus em confirmacao de escolha_filiais
                print(filial_existente.acervo) #mesma relação de controle que pus em confirmacao de escolha_filiais
                a.info()
                a.info_acervo()
                #for a in self.filial.acervo:
                 #   a.info_acervo
            confirmacao = input('Deseja continuar a inserir livros no acervo.\nDigite SIM/S ou NÃO/N: ')
            if confirmacao.lower() not in ['s', 'y', 'sim']:
                continuar_cadastro = False

    def pesquisa_nome(self):
        print(f'Você deseja busca um livro pelo nome dentro de nossas filiais?\n'
              f'Por favor, escolha baseada na lista abaixo.')
        filial_existente = self.escolha_filiais()
        busca_nome = str(input(f'\nInforme nome do livro que deseja pesquisa:\n'))
        '''
        resultados = [livro for livro in self.acervo if livro.titulo.lower() == busca_nome.lower() ] aqui faremos uma lista onde será 
        suprida com os criteria que esta dentro das chaves ou seja livro que e o objeto vai receber o que 'livro' dentro
        do 'for livro in self.acervo' self.acervo e um atributo que recebeu uma lista, para cada atributo livro.titulo que
        for igual que busca_nome ira ser guardada na lista resultados, fora passa tudo para minusculos para ficar possivel a comparação.  
        '''
        resultados = []  # lista que guarda o resultado do if
        for livro in filial_existente.acervo:  # percorre a lista do atributo self.acervo
            if livro.titulo.lower() == busca_nome.lower():  # if compara o atributo .titulo de livro em minusculo com busca_nome em minusculo sendo .lower que passa tudo para minusculo
                resultados.append(livro)  # acrescenta o objeto que passou no teste do if a resultados
        if resultados:
            if len(resultados) == 1:  # verifica se temos resultado homônimos.
                print(f'\n++++Resultado da pesquisa por nome.++++\n')
            else:
                print(f'\n++++Resultado da pesquisa possui homônimos.++++\n')
            for livro in resultados:  # print da lissta resultados
                livro.info()
        else:  # se resultado estiver vazio ira imprimir a mensagem a baixo.
            print('\nNenhum livro foi encontrado com este nome no acervo.\n')

    def acervo_livraria_codigo(self):
        '''utilizei um sistema de 'for' em cascata para buscar dentro das filiais e seus depositos,
        guardando em uma lista chamdada resultado o de qual filial esta o livro e posteriormente eu
        utilizo o 'busca_codigo_livro' para ter a referencia para chamar o '.info_codigo' posteriormente
        eu busco dentro da lista resultados as filiais e seus acervos para imprimir os dados solicitados.
        '''
        codigo = int(input(f'Por favor informe o código do livro que deseja buscar em nossas filiais: '))
        resultados = []
        for filial in self.filiais:
            resultado_filial = 0
            if filial != resultado_filial:
                #filial.info()
                for livro in filial.acervo:
                    #print(livro.codigo)
                    if livro.codigo == codigo:
                        resultado_filial = filial
                        resultados.append(resultado_filial)
                        busca_codigo_livro = livro
        #print(resultados)
        busca_codigo_livro.info_codigo()
        valor_total_filial = 0
        for filial in resultados:
            for livro in filial.acervo:
                if codigo == livro.codigo:
                    print(f'Valor: R$ {livro.valor} >>> {filial.nome_filial}, estoque: {livro.quantidade_em_estoque}')
                    valor_total_filial += livro.valor * livro.quantidade_em_estoque
        print(f'Valor total em estoque nesta filial: R$ {valor_total_filial:.2f}\n')

    def pesquisa_categoria(self):
        print(f'Você deseja buscar livros por categoria dentro de nossas filiais?\n'
              f'Por favor, escolha baseada na lista abaixo.')
        filial_existente = self.escolha_filiais()
        busca_categoria = input(f'\nInforme a categoria do livro que deseja pesquisa:\n')
        '''
        resultados = [livro for livro in self.acervo if livro.categoria.lower() == busca_categoria.lower() ] aqui faremos uma lista onde será 
        suprida com os criteria que esta dentro das chaves ou seja livro que e o objeto vai receber o que 'livro' dentro
        do 'for livro in self.acervo' self.acervo e um atributo que recebeu uma lista, para cada atributo livro.area que
        for igual que busca_categoria ira ser guardada na lista resultados, fora passa tudo para minusculos para ficar possivel a comparação.  
        '''
        resultados = []
        for livro in filial_existente.acervo:
            if livro.area.lower() == busca_categoria.lower():  # compara livro.area com em minusculo com busca_categotia em minusculo
                (resultados.
                 end(livro))  # adiciona em resultados o que passou pelo if
        if resultados:  # imprimi o que foi guardado em resultados
            print(f'\n++++Resultado da pesquisa por categoria.++++\n')
            for livro in resultados:
                livro.info()

        else:
            print('\nNenhum livro desta categoria foi encontrado no acervo.\n')

    def pesquisa_valor(self):
        print(f'Você deseja busca um livro pelo valor dentro de nossas filiais?\n'
              f'Por favor, escolha baseada na lista abaixo.')
        filial_existente = self.escolha_filiais()
        busca_valor = float(input(f'\nInforme o preço máximo do livro que deseja pesquisa:\n'))
        print('')
        '''
        resultados = [livro for livro in self.acervo if livro.valor < busca_valor] aqui faremos uma lista onde será 
        suprida com os criteria que esta dentro das chaves ou seja livro que e o objeto vai receber o que 'livro' dentro
        do 'for livro in self.acervo' self.acervo e um atributo que recebeu uma lista, para cada atributo livro.valor que
        for menor que busca_valor ira ser guardada na lista resultados.  
        '''
        resultados = []  # so se cria a lista vazia se o metodo for acionado para guarda o resultado do if
        for livro in filial_existente.acervo:
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
            # resultados_mais_caros = [a for a in self.acervo if a.valor >= busca_valor]
            resultados = []  # so se cria a lista vazia se o metodo for acionado para guarda o resultado do if
            for livro in filial_existente.acervo:
                if livro.valor >= busca_valor:
                    resultados.append(livro)
            print(f'\n++++Livros do acervo de preço acima ou igual a R${busca_valor:.2f}\n')
            # for livro in resultados_mais_caros:
            for livro in resultados:
                livro.info()

    def pesquisa_quantidade_acervo(self):
        print(f'Você deseja busca uma quantidade de minima de livro em nossas filiais?\n'
              f'Por favor, escolha baseada na lista abaixo.')
        filial_existente = self.escolha_filiais()
        busca_quantidade_estoque = int(input(f'\nInforme a quantidade mínima em estoque que deseja pesquisar: \n'))
        # resultados = [livro for livro in self.acervo if livro.quantidade_em_estoque >= busca_quantidade_estoque]
        resultados = []  # so se cria a lista vazia se o metodo for acionado para guarda o resultado do if
        for livro in filial_existente.acervo:
            if livro.quantidade_em_estoque >= busca_quantidade_estoque:
                resultados.append(livro)
        if resultados:
            for livro in resultados:
                livro.info()
        else:
            print(f'Não foram encontrados livros com valores iguais ou maiores {busca_quantidade_estoque} em estoque.')

    def pesquisa_valor_total_acervo(self):
        # busca_valor_estoque = sum (livro.valor * livro.quantidade_em_estoque for livro in self.acervo) este metodo vai fazer a soma 'sum' da multiplicação dos atributos
        # utilizei o metodo a baixo pois fica mais facil o entendimento
        # com isso tive que iniciar a variavel busca_valor_estoque com 0.
        print(f'Você deseja busca o valor total em uma de nossas filiais?\n'
              f'Por favor, escolha baseada na lista abaixo.')
        filial_existente = self.escolha_filiais()
        busca_valor_estoque = 0
        for livro in filial_existente.acervo:
            busca_valor_estoque += (livro.valor * livro.quantidade_em_estoque)
        print(f'\nO valor total de todos os livros no acervo é: R${busca_valor_estoque:.2f}\n')

    def lista_de_estoque(self):
        print(f'Por favor escolha qual filial deseja mostra a listagem do estoque.')
        filial_existente = self.escolha_filiais()
        print(filial_existente.info_acervo())

    def carregar_acervo(self):
        self.filiais = []
        #filial_atual = None
        filiais_acervo_arquivo = open('acervo.txt', 'r')  # estou atribuindo o conteudo do arquivo acervo.txt a variavel acervo_arquivo
        for linha in filiais_acervo_arquivo:
            if linha.startswith('#FL'):
                linha_sep = linha.split(',')
                if len(linha_sep) == 4:
                    nova_filial = Filial(linha_sep[0], linha_sep[1], linha_sep[2], linha_sep[3])
                    self.filiais.append(nova_filial)
                    filial_atual = nova_filial
                else:
                    print(f'Formato invalido para linha de filial: {linha}')
            elif filial_atual:
                linha_sep = linha.split(',')
                if len(linha_sep) == 7:
                    filial_atual.acervo.append(
                        Livro(linha_sep[1], int(linha_sep[0]), linha_sep[4],
                              linha_sep[3], linha_sep[2], float(linha_sep[5].replace('R$','')), int(linha_sep[6])))
                else:
                    print(f'Formato não suportado: {linha}')

        '''
        controle para ver se estava ocorrendo a correta leitura pois a forma que os elementos são lidos não e a forma 
        correta que se deve guarda na lista da filial. 
        for filial in self.filiais:
            filial.info()
            for livro in filial.acervo:
                livro.info()
        '''
    def gravar_acervo(self):
        filial_acervo_arquivo = open('acervo.txt', 'w')
        for filial in self.filiais:
            #filial_acervo_arquivo.write(f'{filial.codigo_filial},{filial.nome_filial},'
            #                           f'{filial.endereco_filial},{filial.filial_contato}')
            linha = f'{filial.codigo_filial},{filial.nome_filial},{filial.endereco_filial},{filial.filial_contato}'
            filial_acervo_arquivo.write(linha)
            for livro in filial.acervo:
                filial_acervo_arquivo.write(linha)

    def confimacao_encerramento(self):
        if opcao == 0:
            print('Deseja atualizar o arquivo do estoque?')
            resposta = input(f'SIM OU NÃo.\n').lower()
            if resposta in ['sim', 's', 'y', 'yes']:
                self.gravar_acervo()
                print('Programa encerrado, com arquivo do estoque atualizado.')
            else:
                print('Programa encerrado')

    def exibir_menu(self):
        print(f'+++Para interagir com o sistema favor digite o numero de uma da opções abaixo+++ \n'
              f'|    1 – Cadastrar nova filial                                                 |\n'
              f'|    2 – Cadastrar novo livro                                                  |\n'
              f'|    3 – Buscar livros por nome                                                |\n'
              f'|    4 - Buscar livros por código                                              |\n'
              f'|    5 – Buscar livros por categoria                                           |\n'
              f'|    6 – Buscar livros por preço                                               |\n'
              f'|    7 – Busca por quantidade em estoque                                       |\n'
              f'|    8 – Valor total no estoque                                                |\n'
              f'|    9 - Listar filiais                                                        |\n'
              f'|   10 - Listagem de estoque                                                   |\n'
              f'|   11 - Carregar estoque                                                      |\n'
              f'|   12 - Atualizar arquivo de estoque                                          |\n'              
              f'|    0 – Encerrar atividades                                                   |\n'
              f'|______________________________________________________________________________|')


if __name__ == '__main__':
    Livraria = Livraria()  # fazendo isso eu chamo o construtor __init__
    # se eu não fizer isso tenho que definir obrigatoriamento o self = Livraria.
    # dentro do parentes dos metodos para dizer que são da classe Livraria
    Livraria.exibir_menu()  # chama o metodo exibir_menu
    opcao = int(input('Por favor informe a opção desejada: '))  # variavel que recebe a escolha do menu

    while opcao != 0:
        if opcao == 1:
            Livraria.cadastro_filial()
        elif opcao == 2:
            Livraria.cadastro_livros()
        elif opcao == 3:
            Livraria.pesquisa_nome()
        elif opcao == 4:
            Livraria.acervo_livraria_codigo()
        elif opcao == 5:
            Livraria.pesquisa_categoria()
        elif opcao == 6:
            Livraria.pesquisa_valor()
        elif opcao == 7:
            Livraria.pesquisa_quantidade_acervo()
        elif opcao == 8:
            Livraria.pesquisa_valor_total_acervo()
        elif opcao == 9:
            Livraria.listar_filiais()
        elif opcao == 10:
            Livraria.lista_de_estoque()
        elif opcao == 11:
            Livraria.carregar_acervo()
        elif opcao == 12:
            Livraria.gravar_acervo()

        else:
            print('Opção não valida.')
        Livraria.exibir_menu()

        opcao = int(input('Por favor informe a opção desejada: '))

    Livraria.confimacao_encerramento()