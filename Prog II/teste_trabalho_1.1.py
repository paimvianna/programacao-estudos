
#criação da classe livro com seus atributos ao lado do self, e os parametro e o que está entre parenteses
acervo = []
pesquisa_nome_livros = []
pesquisa_categoria = []
pesquisa_valor_livro = []
pesquisa_mais_baratos = []
pesquisa_mais_caros = []
quantitativo = []

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
        print(f'Valor total em estoque: R$', self.quantidade_em_estoque * self.valor)
        print('')
'''def pesquisa(acervo,busca): função para pesquisa.
    for a in acervo:
        if a.titulo == busca:
            pesquisa_nome_livros.append(a)
    return pesquisa_nome_livros
'''

if __name__ == '__main__':
    livro1 = Livro("A Arte da Programação", "12345", "Editora ABC", "Computação", 2020, 99.90, 10)
    livro2 = Livro("Python para Iniciantes", "12346", "Editora XYZ", "Tecnologia", 2021, 79.90, 5)
    livro3 = Livro("Design Patterns", "12347", "Editora DEF", "Desenvolvimento de Software", 2019, 120.00, 8)
    livro4 = Livro("Inteligência Artificial", "12348", "Editora GHI", "Tecnologia", 2022, 150.00, 12)
    livro5 = Livro("Algoritmos e Estruturas de Dados", "12349", "Editora JKL", "Computação", 2018, 89.90, 15)
    livro6 = Livro("Arquitetura de Software", "12350", "Editora MNO", "Tecnologia", 2023, 135.50, 6)
    livro7 = Livro("Redes de Computadores", "12351", "Editora PQR", "Redes", 2020, 95.00, 20)
    livro8 = Livro("Machine Learning", "12352", "Editora STU", "Inteligência Artificial", 2021, 110.00, 4)
    livro9 = Livro("Desenvolvimento Web", "12353", "Editora VWX", "Desenvolvimento", 2022, 85.90, 18)
    livro10 = Livro("Segurança em Redes", "12354", "Editora YZA", "Segurança", 2023, 120.00, 3)

for i in [livro1, livro2, livro3, livro4, livro5, livro6, livro7, livro8, livro9, livro10]:
    acervo.append(i)
'''
print(i)
for i in range(len(acervo)):
    print(acervo[i].titulo, acervo[i].codigo, acervo[i].editora,acervo[i].area, acervo[i].ano, acervo[i].valor, acervo[i].quantidade_em_estoque)
usei para controle e ver se estava funcionando as funçoes
'''
i = len(acervo)
print(f'+++Para interagir com o sistema favor digite o numero de uma da opções abaixo+++ \n'
      f'|   1 – Cadastrar novo livro                                                   |\n'
      f'|   2 – Listar livros                                                          |\n'
      f'|   3 – Buscar livros por nome                                                 |\n'
      f'|   4 – Buscar livros por categoria                                            |\n'
      f'|   5 – Buscar livros por preço                                                |\n'
      f'|   6 – Busca por quantidade em estoque                                        |\n'
      f'|   7 – Valor total no estoque                                                 |\n'
      f'|   0 – Encerrar atividades                                                    |\n'
      f'|______________________________________________________________________________|')

opcao = int(input('Por favor infome a opção desejada: '))

while opcao != 0:

    if opcao == 1:
        #cadastraLivro();
        continuar_cadastro = True
        while continuar_cadastro: # continuar variável boolena que se inicia com o true e no proxímo input e testado
            # no if e se não satisfaça a condição muda o estado para False.
            print(continuar_cadastro)
            ttulo = str(input('Informe o titulo do livro: '))
            cod = int(input('Informe o numero do codigo do livro: '))
            edt = str(input('Informe a editora: '))
            area = str(input('Informe a area do livro: '))
            ano = int(input('Informe o ano da edição: '))
            vlr = float(input('Informe o valor do livro: '))
            qdd_em_stq = int(input('Informe a quantidade do estoque: '))
            i = i+1
            h = str(f'livro{i}')#produz o nome da variável onde eu contateno o texto com um contador e depois transformo
                                # numa 'string'.
            if __name__ == '__main__':
                #print(h) print para verificar o nome da variavel.
                h = Livro(ttulo, cod, edt, area, ano, vlr, qdd_em_stq)
                acervo.append(h) # faz coloca os objetos na lista
            continuar_cadastro = input('Deseja continuar a inserir livros no acervo.\nDigite SIM ou NÃO: ') # aqui tem que
                                                    # ser cetado para int se nao nao ira funcionar o controle no while
            if (continuar_cadastro.lower() !='sim'
                    and continuar_cadastro.lower() != 's'
                    and continuar_cadastro.lower() != 'yes'
                    and continuar_cadastro.lower() != 'y') :
                continuar_cadastro = False
    elif opcao == 2:
        for a in acervo:# faz a varredura da lista onde 'a' admite o valor que esta dentro da primeira a ultima possição da lista que vem a ser a posição de memoria do objeto.
            a.info() #imprime todos os dados dos elemetos do acervo
            #print(a.titulo)# imprime o valor do parametro titulo do objeto de memoria 'a' em que foi varido na lista.
        print(f'O total de obras no acervo e de {len(acervo)}')
    elif opcao == 3:
        pesquisa_nome_livros.clear()
        contador_geral_f3_f4_f5_f6 = 0
        busca = input('Informe o nome do livro que deseja:')
        print('')
        for a in acervo:
            if a.titulo == busca:
                pesquisa_nome_livros.append(a)
                contador_geral_f3_f4_f5_f6 = contador_geral_f3_f4_f5_f6 + 1
        if contador_geral_f3_f4_f5_f6 >= 1:
            for a in pesquisa_nome_livros:
                a.info() # este vai informar todos os dados do livro incluindo os  homonimos da busca.
        else:
            print('Nenhum livro foi encontrado com este nome no acervo.')
    elif opcao == 4:
        pesquisa_categoria.clear()
        contador_geral_f3_f4_f5_f6 = 0
        busca = input('Informe a categoria que deseja pesquisar no acervo:')
        for a in acervo:
            if a.area == busca:
                pesquisa_categoria.append(a)
                contador_geral_f3_f4_f5_f6 = contador_geral_f3_f4_f5_f6 + 1
        if contador_geral_f3_f4_f5_f6 != 0:
            for a in pesquisa_categoria:
                a.info()  # este vai informar todos os dados do livro da categoria incluindo os homonimos da busca.
        else:
            print('Nenhum livro foi encontrado nesta categoria.')
    elif opcao == 5:
        pesquisa_valor_livro.clear()
        pesquisa_mais_baratos.clear()
        pesquisa_mais_caros.clear()
        escolha0 = 0
        contador_geral_f3_f4_f5_f6 = 0
        busca = float(input('Informe o valor do livro que deseja: R$ '))
        print('')
        for a in acervo:
            if a.valor == busca:
                pesquisa_valor_livro.append(a)
                contador_geral_f3_f4_f5_f6 = contador_geral_f3_f4_f5_f6 + 1
            elif a.valor > busca:
                pesquisa_mais_caros.append(a)
            elif a.valor < busca:
                pesquisa_mais_baratos.append(a)

        if contador_geral_f3_f4_f5_f6 != 0:
            for a in pesquisa_valor_livro:
                a.info()  # este vai informar todos os dados do livro fora os homonimos das busca.
        else:
            print(f'Nenhum livro foi encontrado com este valor R$ {busca:003.02f}.')
        escolha0 = int(input(f'Gostaria de ver os livros que estão abaixo deste valor R$ {busca:003.02f}.\n'
                             f'Digite 1 para SIM e 2 para NÃO: '))
        print('')
        if escolha0 == 1:
            for a in pesquisa_mais_baratos:
                a.info()
        elif escolha0 == 2:
            print('')
        escolha0 = int(input(f'Gostaria de ver os livros que estão acima deste valor R$ {busca:003.02f}.\n'
                               f'Digite 1 para SIM e 2 para NÃO: '))
        print('')
        if escolha0 == 1:
            for a in pesquisa_mais_caros:
                a.info()
        elif escolha0:
            print('')
    elif opcao == 6:
        quantitativo.clear()
        escolha0 = 0
        contador_geral_f3_f4_f5_f6 = 0
        k = 0
        escolha0 = int(input('Deseja consultar o quantitativo geral ou de um Livro especifico.\n'
              'Digite 1 quantitativo do Livro ou 2 para o quantitativo do geral do acervo:\n '))
        print('')
        if escolha0 == 1:
            busca = input(f'Informe o livro que deseja o quantitativo no acervo: ')
            print('')
            for a in acervo:
                k = k + 1
                if a.titulo == busca:
                    contador_geral_f3_f4_f5_f6 = contador_geral_f3_f4_f5_f6+ 1
                    quantitativo.append(a)
                elif k == len(acervo) and contador_geral_f3_f4_f5_f6 == 0:
                    print(f'Livro não encontrado na base de dados.')
                    print('')
            if contador_geral_f3_f4_f5_f6 == 1:
                for a in quantitativo:
                    print(f'O livro {busca} tem {a.quantidade_em_estoque} exemplares em estoque.')
                    print('')
            elif contador_geral_f3_f4_f5_f6 > 1:
                print('A pesquisa resultou em livros homonimos, portanto segue os dados dos livros.')
                for a in quantitativo:
                    a.info()
        elif escolha0 == 2:
            b = 0
            for a in acervo:
                    b = b + a.quantidade_em_estoque
            if escolha0 == 2:
                print(b)
        #print('6')
    elif opcao == 7:
        b = 0
        for a in acervo:
            b = b + (a.quantidade_em_estoque * a.valor)
        print(f'o valor total em estoque e de R$ {b:.02f}.')
        print('')
    else:
        print('Opção não valida.')
    print(f'+++Para interagir com o sistema favor digite o numero de uma da opções abaixo+++ \n'
          f'|   1 – Cadastrar novo livro                                                   |\n'
          f'|   2 – Listar livros                                                          |\n'
          f'|   3 – Buscar livros por nome                                                 |\n'
          f'|   4 – Buscar livros por categoria                                            |\n'
          f'|   5 – Buscar livros por preço                                                |\n'
          f'|   6 – Busca por quantidade em estoque                                        |\n'
          f'|   7 – Valor total no estoque                                                 |\n'
          f'|   0 – Encerrar atividades                                                    |\n'
          f'|______________________________________________________________________________|')

    opcao = int(input('Por favor informe a opção desejada: '))
print('Programa encerrado.')