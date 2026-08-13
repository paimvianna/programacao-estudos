
#criação da classe livro, seus atributos ao lado do self, e os parametro e o que está entre parenteses
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
def cadastro_livros ():
    # cadastraLivro();
    continuar_atividade = True
    while continuar_atividade:  # continuar variável boolena que se inicia com o true e no proxímo input e testado
        # no if e se não satisfaça a condição muda o estado para False.
        #print(continuar_cadastro) print de teste para verificar se recebia corretamente o valor do input.
        titulo = str(input('Informe o titulo do livro: '))
        codigo = int(input('Informe o numero do codigo do livro: '))
        editora = str(input('Informe a editora: '))
        area= str(input('Informe a area do livro: '))
        ano = int(input('Informe o ano da edição: '))
        valor = float(input('Informe o valor do livro: '))
        quantidade_em_estoque = int(input('Informe a quantidade do estoque: '))
        #i +=1 # soma 1 no tamanho da lista.
        h = str(f'livro{len(acervo)+1}')  # produz o nome da variável onde eu contateno o texto com tamanho o tamanho da lista + 1 e converto em uma string'.
        if __name__ == '__main__':
            h = Livro(titulo, codigo, editora, area, ano, valor, quantidade_em_estoque)
            acervo.append(h)  #coloca os objetos na lista
        continuar_atividade = input('Deseja continuar a inserir livros no acervo.\nDigite SIM ou NÃO: ') # aqui estou
                                                                                                        # usando booleano na varivel continuar_cadastro, mas se fosse usar um numeral teria que infomar mque tanto o input
                                                                                                        # variavel tem que ser inteiro.
        if (continuar_atividade.lower() != 'sim' # faz a verificação se a resposta para a continuação do cadastro e valida
                and continuar_atividade.lower() != 's'
                and continuar_atividade.lower() != 'yes'
                and continuar_atividade.lower() != 'y'):
            continuar_atividade = False

def acervo_biblioteca():
    for a in acervo:  # faz a varredura da lista onde 'a' admite o valor que esta dentro da primeira à última posição
        # da lista que vem a ser a posição de memoria do objeto.
        a.info()
        # print(a.titulo)# imprime o valor do parametro titulo do objeto de memoria 'a' em que foi varido na lista.

def pesquisa_nome(acervo): #pesquisa_nome(lista_de_livros)
    for a in acervo:
        if a.titulo.lower() == busca.lower():
            pesquisa_nome_livros.append(a)
    if pesquisa_nome_livros:
        for a in pesquisa_nome_livros:
            a.info()  # este vai informar todos os dados do livro incluindo os  homonimos da busca.
    else:
        print('Nenhum livro foi encontrado com este nome no acervo.')

def pesquisa_nome_categoria(acervo):
    for a in acervo:
        if a.area.lower() == busca.lower():
            print(a.area)
            pesquisa_categoria.append(a)
    if pesquisa_categoria:
        for a in pesquisa_categoria:
            a.info()  # este vai informar todos os dados do livro da categoria incluindo os homonimos da busca.
    else:
        print('Nenhum livro foi encontrado nesta categoria.')

def pesquisa_preco(acervo):
    for a in acervo:
        if a.valor == busca:
            pesquisa_valor_livro.append(a)
        elif a.valor > busca:
            pesquisa_mais_caros.append(a)
        elif a.valor < busca:
            pesquisa_mais_baratos.append(a)

    if pesquisa_valor_livro:
        for a in pesquisa_valor_livro:
            a.info()  # este vai informar todos os livros dentro do valor que se deseja.
    else:
        print(f'Nenhum livro foi encontrado com este valor R$ {busca:003.02f}.')

    continuar_pesquisa_preco = str(input(f'Gostaria de ver os livros que estão abaixo deste valor R$ {busca:003.02f}.\n'
                         f'Digite SIM ou NÃO.'))
    print('')
    print(continuar_pesquisa_preco,'1')
    if (continuar_pesquisa_preco.lower() == 'sim'  # faz a verificação se a resposta para a continuação do cadastro e valida
        or continuar_pesquisa_preco.lower() == 's'
        or continuar_pesquisa_preco.lower() == 'yes'
        or continuar_pesquisa_preco.lower() == 'y'):
        for a in pesquisa_mais_baratos:
            a.info()
    elif (continuar_pesquisa_preco.lower() == 'não' # faz a verificação se a resposta para a continuação do cadastro e valida
          or continuar_pesquisa_preco.lower() == 'n'
          or continuar_pesquisa_preco.lower() == 'no'
          or continuar_pesquisa_preco.lower() == 'n'):
        print('')

    continuar_pesquisa_preco = str(input(f'Gostaria de ver os livros que estão acima deste valor R$ {busca:003.02f}.\n'
                                f'Digite SIM ou NÃO. '))
    print('')

    if (continuar_pesquisa_preco.lower() == 'sim'  # faz a verificação se a resposta para a continuação do cadastro e valida
        or continuar_pesquisa_preco.lower() == 's'
        or continuar_pesquisa_preco.lower() == 'yes'
        or continuar_pesquisa_preco.lower() == 'y'):
        for a in pesquisa_mais_caros:
            a.info()
    elif (continuar_pesquisa_preco.lower() == 'não'  # faz a verificação se a resposta para a continuação do cadastro e valida
        or continuar_pesquisa_preco.lower() == 'n'
        or continuar_pesquisa_preco.lower() == 'no'):
        print('')

def quantidade():
    '''continuar_atividade = input('Deseja consultar o quantitativo geral, ou de um Livro especifico.\n'
                         'Digite Livro quantitativo de um Livro, ou acervo para o quantitativo do geral do Acervo:\n ')'''
    print('')
    if (continuar_atividade == 'livro'
        or continuar_atividade == 'Livro'):
        busca = input(f'Informe o livro que deseja o quantitativo no acervo: ')
        print('')
        for a in acervo:
            if a.titulo.lower() == busca.lower():
                quantitativo.append(a)
        if len(quantitativo) == 1:
            for a in quantitativo:
                print(f'O livro {busca} tem {a.quantidade_em_estoque} exemplares em estoque.')
                print('')
        elif len(quantitativo) > 1:
            for a in pesquisa_nome_livros:
                a.info()  # este vai informar todos os dados do livro incluindo os  homonimos da busca
            for a in quantitativo:
                a.info()
    elif (continuar_atividade == 'Acervo'
          or continuar_atividade == 'acervo') :
            acervo_total = 0
            for a in acervo:
                acervo_total += a.quantidade_em_estoque
            print(acervo_total)
        # print('6')

def valor_estoque():
    b = 0
    for a in acervo:
        b = b + (a.quantidade_em_estoque * a.valor)
    print(f'o valor total em estoque e de R$ {b:.02f}.')
    print('')

def exibir_menu():
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

exibir_menu()
opcao = int(input('Por favor informe a opção desejada: '))

while opcao != 0:
    if opcao == 1:
       cadastro_livros()
    elif opcao == 2:
        acervo_biblioteca()
    elif opcao == 3:
        busca = input(f'Informe do livro que deseja pesquisa:')
        print('')
        pesquisa_nome(acervo)

    elif opcao == 4:
        busca = input('Informe a categoria que deseja pesquisar no acervo:')
        print('')
        pesquisa_nome_categoria(acervo) # em um dado momento o nome da função estava se confundindo com o nome da lesta.

    elif opcao == 5:
        busca = float(input('Informe o valor do livro que deseja: R$ '))
        print('')
        pesquisa_preco(acervo)

    elif opcao == 6:
        continuar_atividade = input('Deseja consultar o quantitativo geral, ou de um Livro especifico.\n'
                                    'Digite Livro quantitativo de um Livro, ou acervo para o quantitativo do geral do Acervo:\n ')
        print('')
        quantidade()

    elif opcao == 7:
        valor_estoque()
    else:
        print('Opção não valida.')
    exibir_menu()

    opcao = int(input('Por favor informe a opção desejada: '))

print('Programa encerrado.')