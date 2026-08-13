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
        print(f'>>>>> Cod#{self.codigo}')
        print(f'Titulo/Editora: {self.titulo}/{self.editora}')
        print(f'Categoria: {self.area}')
        print(f'Ano: {self.ano}')
        print(f'Valor: R$ {self.valor}')
        print(f'Estoque: {self.quantidade_em_estoque}')
        print(f'Valor total em estoque: R${self.valor*self.quantidade_em_estoque}')
        print('')

class Filial:

    def __init__(self, codigo_filial, nome_filial, endereco_filial, contato_filial):
        self.codigo_filial = codigo_filial
        self.nome_filial = nome_filial
        self.endereco_filial = endereco_filial
        self.contato_filial = contato_filial
        self.estoque = []  # Cada filial terá sua própria lista de livros

    def info(self):
        print(f">>>>> Cod_filial#{self.codigo_filial}")
        print(f"Nome da Filial: {self.nome_filial}")
        print(f'Endereço: {self.endereco_filial}')
        print(f'Contato telefonico da Filial: {self.contato_filial}')
        print('')

    def info_estoque(self):
        print(f"\n+++++ Estoque da Filial {self.nome_filial} ({self.codigo_filial}) +++++\n")
        if self.estoque:
            valor_total_filial = 0
            for livro in self.estoque:
                livro.info()
                valor_total_filial += livro.valor * livro.quantidade_em_estoque
            print(f"Valor total em estoque nesta filial: R$ {valor_total_filial:.2f}\n")
        else:
            print("O estoque desta filial está vazio.\n")



    class Livraria:

        def __init__(self):
            self.filiais = []  # Lista para armazenar os objetos Filial

        '''
        def cadastrar_filial(self):
            nova_filial = Filial('', '', '', '').cadastro_filial()
            self.filiais.append(nova_filial)
            print(f'Filial {nova_filial.nome_filial} ({nova_filial.codigo_filial}) cadastrada com sucesso!')

        def listar_filiais(self):
            if self.filiais:
                print("\n+++++ Filiais Cadastradas +++++\n")
                for filial in self.filiais:
                    filial.info()
            else:
                print("\nAinda não há filiais cadastradas.\n")
        '''

        def cadastro_filial(self):
            codigo = int(input(f'Informe o numero da filial: '))
            codigo_filial = str(f'#FL{codigo:02d}')  # Formatando para ter sempre dois dígitos
            nome_filial = input(f'Informe o nome da Filial: ')
            endereco_filial = input(f'Informe o Endereço da Filial: ')
            contato_filial = input(f'Informe o telefone de contato da filial: ')
            print(f'|______________________________________________________________________________|')
            print('')
            nova_filial = Filial(codigo_filial, nome_filial, endereco_filial, contato_filial)
            return nova_filial

        def listar_filiais(self):
            if self.filiais:
                print("\n+++++ Filiais Cadastradas +++++\n")
                for filial in self.filiais:
                    filial.info()
            else:
                print("\nAinda não há filiais cadastradas.\n")

        def selecionar_filial(self):
            if not self.filiais:
                print("\nAinda não há filiais cadastradas. Cadastre uma primeiro.\n")
                return None

            print("\n+++++ Filiais Disponíveis +++++\n")
            for i, filial in enumerate(self.filiais):
                print(f"{i + 1} - {filial.nome_filial} ({filial.codigo_filial})")

            while True:
                try:
                    opcao = int(input("Selecione o número da filial desejada: "))
                    if 1 <= opcao <= len(self.filiais):
                        return self.filiais[opcao - 1]
                    else:
                        print("Opção inválida. Por favor, selecione um número da lista.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")

        def cadastro_livros(self):
            filial_selecionada = self.selecionar_filial()
            if not filial_selecionada:
                return

            continuar_cadastro = True
            while continuar_cadastro:
                titulo = input('Informe o titulo do livro: ')
                codigo = int(input('Informe o numero do codigo do livro: '))
                editora = str(input('Informe a editora: '))
                area = str(input('Informe a area do livro: '))
                ano = int(input('Informe o ano da edição: '))
                valor = float(input('Informe o valor do livro: '))
                quantidade_em_estoque = int(input('Informe a quantidade do estoque: '))
                livro_novo = Livro(titulo, codigo, editora, area, ano, valor, quantidade_em_estoque)
                filial_selecionada.estoque.append(livro_novo)  # Adiciona o livro ao estoque da filial
                print(f'|______________________________________________________________________________|')
                print('')
                confirmacao = input('Deseja continuar a inserir livros nesta filial?\nDigite SIM/S ou NÃO/N: ')
                if confirmacao.lower() not in ['s', 'y', 'sim', 'yes']:
                    continuar_cadastro = False

        def listagem_estoque(self):
            filial_para_listar = self.selecionar_filial()
            if filial_para_listar:
                filial_para_listar.info_estoque()

        def pesquisa_nome(self):
            filial_para_buscar = self.selecionar_filial()
            if not filial_para_buscar:
                return

            busca_nome = str(
                input(f'\nInforme nome do livro que deseja pesquisar na filial {filial_para_buscar.nome_filial}:\n'))
            resultados = [livro for livro in filial_para_buscar.estoque if livro.titulo.lower() == busca_nome.lower()]
            if resultados:
                print(f'\n++++Resultado da pesquisa por nome na Filial {filial_para_buscar.nome_filial}++++\n')
                for livro in resultados:
                    livro.info()
            else:
                print(
                    f'\nNenhum livro com este nome foi encontrado no acervo da Filial {filial_para_buscar.nome_filial}.\n')

        def pesquisa_categoria(self):
            filial_para_buscar = self.selecionar_filial()
            if not filial_para_buscar:
                return

            busca_categoria = input(
                f'\nInforme a categoria do livro que deseja pesquisar na filial {filial_para_buscar.nome_filial}:\n')
            resultados = [livro for livro in filial_para_buscar.estoque if
                          livro.area.lower() == busca_categoria.lower()]
            if resultados:
                print(f'\n++++Resultado da pesquisa por categoria na Filial {filial_para_buscar.nome_filial}++++\n')
                for livro in resultados:
                    livro.info()
            else:
                print(
                    f'\nNenhum livro desta categoria foi encontrado no acervo da Filial {filial_para_buscar.nome_filial}.\n')

        def pesquisa_valor(self):
            filial_para_buscar = self.selecionar_filial()
            if not filial_para_buscar:
                return

            busca_valor = float(input(
                f'\nInforme o preço máximo do livro que deseja pesquisar na filial {filial_para_buscar.nome_filial}:\n'))
            resultados = [livro for livro in filial_para_buscar.estoque if livro.valor <= busca_valor]
            if resultados:
                print(
                    f'\n++++Livros com preço até R$ {busca_valor:.2f} na Filial {filial_para_buscar.nome_filial}++++\n')
                for livro in resultados:
                    livro.info()
            else:
                print(
                    f'\nNenhum livro com preço até R$ {busca_valor:.2f} encontrado na Filial {filial_para_buscar.nome_filial}.\n')

            confirmacao = input(
                f'\nGostaria de ver os livros de Preço igual ou maior que R$ {busca_valor:.2f} na Filial {filial_para_buscar.nome_filial}?\nDigite Sim/S ou NÃO/N.\n').lower()
            if confirmacao in ['sim', 's', 'y', 'yes']:
                resultados_mais_caros = [livro for livro in filial_para_buscar.estoque if livro.valor >= busca_valor]
                if resultados_mais_caros:
                    print(
                        f'\n++++Livros com preço acima ou igual a R${busca_valor:.2f} na Filial {filial_para_buscar.nome_filial}++++\n')
                    for livro in resultados_mais_caros:
                        livro.info()
                else:
                    print(
                        f'\nNenhum livro com preço acima ou igual a R${busca_valor:.2f} encontrado na Filial {filial_para_buscar.nome_filial}.\n')
            else:
                print(f'\nConsulta encerrada para a Filial {filial_para_buscar.nome_filial}.\n')

        def pesquisa_quantidade_acervo(self):
            filial_para_buscar = self.selecionar_filial()
            if not filial_para_buscar:
                return

            busca_quantidade_estoque = int(input(
                f'\nInforme a quantidade mínima em estoque que deseja pesquisar na filial {filial_para_buscar.nome_filial}: \n'))
            resultados = [livro for livro in filial_para_buscar.estoque if
                          livro.quantidade_em_estoque >= busca_quantidade_estoque]
            if resultados:
                print(
                    f'\n++++Livros com estoque igual ou superior a {busca_quantidade_estoque} na Filial {filial_para_buscar.nome_filial}++++\n')
                for livro in resultados:
                    livro.info()
            else:
                print(
                    f'Não foram encontrados livros com quantidade igual ou maior que {busca_quantidade_estoque} em estoque na Filial {filial_para_buscar.nome_filial}.')

        def pesquisa_codigo(self):
            busca_codigo = int(input(f'\nInforme o código do livro que deseja pesquisar em todas as filiais:\n'))
            encontrados = False
            print(f'\n+++++ Resultados da Busca por Código #{busca_codigo} +++++\n')
            for filial in self.filiais:
                resultados = [livro for livro in filial.estoque if livro.codigo == busca_codigo]
                if resultados:
                    encontrados = True
                    for livro in resultados:
                        print(f">>>>> Cod#{livro.codigo}")
                        print(f"Titulo/Editora: {livro.titulo}/{livro.editora}")
                        print(f'Categoria: {livro.area}')
                        print(f'Ano: {livro.ano}')
                        print(
                            f'Valor: R$ {livro.valor} >>> Filial {filial.nome_filial} ({filial.codigo_filial}), estoque: {livro.quantidade_em_estoque} unidades')
            if not encontrados:
                print(f'\nNenhum livro com o código #{busca_codigo} foi encontrado em nenhuma filial.\n')
            print('')

        def carregar_acervo(self):
            try:
                with open('acervo.txt', 'r') as arquivo:
                    linhas = arquivo.readlines()
                    filial_atual = None
                    for linha in linhas:
                        linha = linha.strip()
                        if linha.startswith('#FL'):
                            codigo, nome, endereco, contato = linha.split(',')
                            nova_filial = Filial(codigo, nome, endereco, contato)
                            self.filiais.append(nova_filial)
                            filial_atual = nova_filial
                        elif linha and filial_atual:
                            codigo, titulo, ano, area, editora, valor, quantidade = linha.split(',')
                            livro = Livro(titulo, int(codigo), editora, area, int(ano), float(valor.replace('R$', '')),
                                          int(quantidade))
                            filial_atual.estoque.append(livro)
            except FileNotFoundError:
                print("Arquivo acervo.txt não encontrado. Iniciando com um acervo vazio.")

        def gravar_acervo(self):
            with open('acervo.txt', 'w') as arquivo:
                for filial in self.filiais:
                    arquivo.write(
                        f'{filial.codigo_filial},{filial.nome_filial},{filial.endereco_filial},{filial.contato_filial}\n')
                    for livro in filial.estoque:
                        arquivo.write(
                            f'{livro.codigo},{livro.titulo},{livro.ano},{livro.area},{livro.editora},R${livro.valor:.2f},{livro.quantidade_em_estoque}\n')

        def confimacao_encerramento(self, opcao):
            if opcao == 0:
                print('Deseja atualizar o arquivo do estoque?')
                resposta = input(f'SIM OU NÃO.\n').lower()
                if resposta in ['sim', 's', 'y', 'yes']:
                    self.gravar_acervo()
                    print('Programa encerrado, com arquivo do estoque atualizado.')
                else:
                    print('Programa encerrado.')

        def exibir_menu(self):
            print(f'+++Para interagir com o sistema favor digite o numero de uma da opções abaixo+++ \n'
                  f'|   1 – Cadastrar nova filial                                                |\n'
                  f'|   2 – Listar filiais                                                       |\n'
                  f'|   3 – Cadastrar novo livro na filial                                       |\n'
                  f'|   4 – Listagem de estoque por filial                                       |\n'
                  f'|   5 – Buscar livros por nome na filial                                     |\n'
                  f'|   6 – Buscar livros por categoria na filial                                |\n'
                  f'|   7 – Buscar livros por preço na filial                                    |\n'
                  f'|   8 – Busca por quantidade em estoque na filial                           |\n'
                  f'|   9 – Buscar livro por código em todas as filiais                          |\n'
                  f'|  10 - Carregar estoque                                                      |\n'
                  f'|  11 - Atualizar arquivo de estoque                                          |\n'
                  f'|   0 – Encerrar atividades                                                   |\n'
                  f'|______________________________________________________________________________|')

    if __name__ == '__main__':
        livraria = Livraria()
        livraria.carregar_acervo()  # Carrega os dados no início

        while True:
            livraria.exibir_menu()
            try:
                opcao = int(input('Por favor informe a opção desejada: '))
                if opcao == 1:
                    livraria.cadastrar_filial()
                elif opcao == 2:
                    livraria.listar_filiais()
                elif opcao == 3:
                    livraria.cadastro_livros()
                elif opcao == 4:
                    livraria.listagem_estoque()
                elif opcao == 5:
                    livraria.pesquisa_nome()
                elif opcao == 6:
                    livraria.pesquisa_categoria()
                elif opcao == 7:
                    livraria.pesquisa_valor()
                elif opcao == 8:
                    livraria.pesquisa_quantidade_acervo()
                elif opcao == 9:
                    livraria.pesquisa_codigo()
                elif opcao == 10:  # Não precisamos chamar carregar_acervo() aqui, pois já é chamado no início
                    print("O acervo já foi carregado ao iniciar o programa.")
                elif opcao == 11:
                    livraria.gravar_acervo()
                elif opcao == 0:
                    livraria.confimacao_encerramento(opcao)
                    break  # Sai do loop while True
                else:
                    print('Opção inválida. Por favor, digite um número de 0 a 11.')
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro para a opção.")