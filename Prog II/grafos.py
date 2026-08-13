'''
grafos e sistema de cadastro de cidades, conexão, listar cidades, conexões, listar cidades vizinhas.
'''


class vertice:
    def __init__(self,nome_cidade):
        self.nome_cidade = nome_cidade
        self.vizinhanca = []
        self.conexoes = []

    def info_vertice(self):
        print(f'++++Cidade:{self.nome_cidade}++++\n')
        self.info_vizinhos()
        self.info_conexoes()

    def info_vizinhos(self):
        if not self.vizinhanca:
            print(f'Não possui vizinhos diretos.')
        else:
            cidades_ordenadas = sorted(self.vizinhanca, key=lambda obj: obj.nome_cidade.lower())
            for cidades in cidades_ordenadas:
                print(f'-{cidades.nome_cidade}')

    def info_conexoes(self):
        print(f'\n****Conexões de {self.nome_cidade}.****\n')
        cidades_ordenadas = sorted(self.conexoes, key=lambda obj: obj.distancia)
        for conexao in cidades_ordenadas:
            print(f'-{conexao}')

    def __str__(self):
        '''retorna aem string o objeto Vertice, neste caso nome_cidade.'''
        return self.nome_cidade

    def __repr__(self):
        '''representação para debug do objeto vertice.'''
        return f"vertice('{self.nome_cidade}')"

class aresta:
    def __init__(self, cidade1, cidade2, distancia:[int,float]):
        self.cidade1 = cidade1
        self.cidade2 = cidade2
        self.distancia = distancia

    def info_aresta(self):
        print(f'A distancia de {self.cidade1.nome_cidade} para {self.cidade2.nome_cidade} é de {self.distancia}.')

    def __str__(self):
        '''representação em string do objeto aresta.'''
        return f"conexão entre {self.cidade1.nome_cidade} e {self.cidade2.nome_cidade}, {self.distancia}"

class grafo:
    def __init__(self):
        self.cidades = []
        self.conexoes = []
    def buscar_cidade(self, nome_cidade: str) :
        '''metodo auxiliar para busca de objetos vertice pelo nome.'''
        for cidade_objeto in self.cidades:
            if cidade_objeto.nome_cidade.lower() == nome_cidade.lower():
                return cidade_objeto
        return None

    ''' 
    #aqui cadastro uma nova cidade (vertice) no grafo.
    nova_nome_cidade = str(input(f'Por favor informe o nome da cidade:\n')).strip() # utilizo para retirar os espaços antes e depois.
    se na der certo esta parte vai pra dentro de cadastro_cidade.
    '''
    def cadastra_cidades(self, nova_nome_cidade):
        if not nova_nome_cidade:
            print(f'Nome da cidade não pode ser vazio.')
            return
        if self.buscar_cidade(nova_nome_cidade):
            print(f'Cidade {nova_nome_cidade} já esta cadastrada no grafo.')
        else:
            novo_vertice = vertice(nova_nome_cidade)# aqui criamos o objeto vertice que atribuimos a novo_vertice
            self.cidades.append(novo_vertice)
            print(f'Cidade {nova_nome_cidade} cadastrada com sucesso.')
            return novo_vertice

    def cadastra_conexao(self,nome_cidade1,nome_cidade2,distancia):
        '''vou cadastra uma aresta (conexão) entre duas cidades existentes, fazendo assim a atualização das cidades (vertices) da conexão.'''


        cidade_objeto1 = self.buscar_cidade(nome_cidade1)
        cidade_objeto2 = self.buscar_cidade(nome_cidade2)

        if not cidade_objeto1: #se busca_cidade retorna None 'nenhum' ou vazio significa que não foi cadastrado.
            print(f'Cidade {nome_cidade1} não encontrada no Grafo. Por favor, cadastre a cidade primeiro.')
            return
        if not cidade_objeto2:
            print(f'Cidade {nome_cidade2} não encontrada no Grafo. Por favor, cadastre a cidade primeiro.')
            return
        if cidade_objeto1 == cidade_objeto2:
            print(f' Não e possivel fazer uma conexão com a mesma cidade.')
            return

        #verificarei se existe a conexão evitando duplicidade.
        for conexao in self.conexoes:
            if (conexao.cidade1 == cidade_objeto1 and conexao.cidade2 == cidade_objeto2) or (conexao.cidade1 == cidade_objeto2 and conexao.cidade2 == cidade_objeto1):
                print(f'A conexão entre {nome_cidade1} e {nome_cidade2} já existe.')
                return
        while True:
            try:
                if distancia <= 0:
                    print(f'O valor da distância deve ser positivo.')
                    continue
                break
            except ValueError:
                print('Distância inválida. Por favor, informe um número.')

        nova_aresta = aresta(cidade_objeto1, cidade_objeto2,distancia) #cria a aresta.
        self.conexoes.append(nova_aresta)# grafo adiciona a aresta à sua lista de conexões.


        if nova_aresta not in cidade_objeto1.conexoes: #atualização dos vertices (cidades)
            cidade_objeto1.conexoes.append(nova_aresta)# adicionando as arestas na lista de conexões dos vertices.
        if nova_aresta not in cidade_objeto2.conexoes: # pois cidade cidade_objetos já consta na lista cidades.
            cidade_objeto2.conexoes.append(nova_aresta)#que tinha cido cadastrado anteriormente

        if cidade_objeto1 not in cidade_objeto2.vizinhanca:#adioiona os vertices a lista de vizinhança um do outro
            cidade_objeto2.vizinhanca.append(cidade_objeto1)
        if cidade_objeto2 not in cidade_objeto1.vizinhanca:
            cidade_objeto1.vizinhanca.append(cidade_objeto2)

        print(f'A conexão entre {nome_cidade1} e {nome_cidade2} cadastrada com sucesso, a distancia eh de:{distancia}')

    def info_cidades(self):#exibe todas as cidades no grafo.
        print(f'\n*** Cidades Cadastradas ***\n')
        cidades_ordenadas =sorted(self.cidades, key=lambda obj: obj.nome_cidade.lower())
        if not self.cidades:
            print(f'Nenhuma cidade cadastrada ainda.')
        else:
            for cidades in cidades_ordenadas:
                print(f'* {cidades.nome_cidade}')

    def info_conexoes(self): # informações das conexoes.
        print(f'\n*** Conexões Cadastradas ***\n')
        if not self.conexoes:
            print(f'Nenhuma conexão cadastrada ainda.')
        else:
            for conexoes in self.conexoes:
                conexoes.info_aresta()

    def carregar_banco(self):
        self.conexoes_temporario = []
        cidades_banco = open('cidades_banco.txt', 'r') #estou atribuindo

        for linha in cidades_banco:
            if linha.startswith('•'):
                linha = linha[1:].strip()
                linha_separador = linha.split(',')
                if len(linha_separador) == 3:
                    cidade1 = linha_separador[0].strip()
                    cidade2 = linha_separador[1].strip()
                    distancia_str = linha_separador[2].replace('km','').strip()
                    distancia = float(distancia_str)
                    self.cadastra_cidades(cidade1)
                    self.cadastra_cidades(cidade2)

                else:
                    print(f'Formato invalido para aresta.')
                nome_cidade1 = cidade1.title()
                nome_cidade2 = cidade2.title()
                self.cadastra_conexao(nome_cidade1,nome_cidade2,distancia)
        for aresta in self.conexoes_temporario:
            aresta.info_aresta()
    def gravar_banco(self):
        cidades_banco = open('cidades_banco.txt', 'w')
        for aresta_pro_banco in self.conexoes:
            linha = f'•{aresta_pro_banco.cidade1},{aresta_pro_banco.cidade2},{aresta_pro_banco.distancia}km\n'
            cidades_banco.write(linha)
def menu(): # *** Menu ***
    menu_grafo = grafo()

    while True:
        print(f'\n|***************** Sistema de Grafos ********************|\n'
                f'| 1 - Cadastrar nova cidade                              |\n'
                f'| 2 - Cadastra nova conexão                              |\n'
                f'| 3 - Listar todas as cidades                            |\n'
                f'| 4 - Listar todas as conexões                           |\n'
                f'| 5 - Ver informações de uma Cidade (vizinhos e conexões)|\n'
                f'| 6 - Carregar as cidades do banco.                      |\n'
                f'| 7 - Sair                                               |\n'
                f'**********************************************************')
        opcao = input(f'Escolha uma opção: ').strip()
        if opcao == '1':
            nova_nome_cidade = str(input(
                f'Por favor informe o nome da cidade:\n')).strip().title()  # utilizo para retirar os espaços antes e depois.
            menu_grafo.cadastra_cidades(nova_nome_cidade)
        elif opcao == '2':
            print(f'Informe a conexão entre as cidades existentes.')
            nome_cidade1 = (str(input(f'1Informe o nome da primeira cidade: \n'))).title()
            nome_cidade2 = (str(input(f'2Informe o nome da segunda cidade: \n'))).title()
            distancia = float(input(f'Informe a distancia entre {nome_cidade1} e {nome_cidade2}:\n'))
            menu_grafo.cadastra_conexao(nome_cidade1,nome_cidade2,distancia)
        elif opcao == '3':
            menu_grafo.info_cidades()
        elif opcao == '4':
            menu_grafo.info_conexoes()
        elif opcao == '5':
            nome_cidade =input(f'\nInforme o nome da cidade para ver detalhes:\n').strip()
            cidade_objeto = menu_grafo.buscar_cidade(nome_cidade)
            if cidade_objeto:
                cidade_objeto.info_vertice()
            else:
                print(f'Cidade {nome_cidade} não encontrado.')
        elif opcao == '6':
            menu_grafo.carregar_banco()
        elif opcao == '7':
            print(f'Saindo do sistema. Salvando os dados no banco.\n Ate mais!')
            menu_grafo.gravar_banco()
        else:
            print(f'Opção invalida. Por favor, tente novamente.')

if __name__ == '__main__':
    menu()