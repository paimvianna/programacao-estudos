#criação da classe livro,1 seus atributos ao lado do self, e os parametro e o que está entre parenteses
acervo = []
pesquisa_nome_livros = []
pesquisa_categoria = []
pesquisa_preco_livro = []


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
        #i +=1 # soma 1 no tamanho da lista.
        h = str(f'livro{len(acervo)+1}')  # produz o nome da variável onde eu contateno o texto com tamanho o tamanho da lista + 1 e converto em uma string'.
        if __name__ == '__main__':
            h = Livro(titulo, codigo, editora, area, ano, valor, quantidade_em_estoque)
            acervo.append(h)  #coloca os objetos na lista
        continuar_cadastro = input('Deseja continuar a inserir livros no acervo.\nDigite SIM ou NÃO: ') # aqui estou
                                                                                                        # usando booleano na varivel continuar_cadastro, mas se fosse usar um numeral teria que infomar mque tanto o input
                                                                                                        # variavel tem que ser inteiro.
        if (continuar_cadastro.lower() != 'sim' # faz a verificação se a resposta para a continuação do cadastro e valida
                and continuar_cadastro.lower() != 's'
                and continuar_cadastro.lower() != 'yes'
                and continuar_cadastro.lower() != 'y'):
            continuar_cadastro = False
def acervo_biblioteca():
    for a in acervo:  # faz a varredura da lista onde 'a' admite o valor que esta dentro da primeira à última posição
        # da lista que vem a ser a posição de memoria do objeto.
        a.info()
        # print(a.titulo)# imprime o valor do parametro titulo do objeto de memoria 'a' em que foi varido na lista.

def pesquisa(acervo):
    pesquisa_nome_livros.clear()
    busca = input(f'Informe nome do livro que deseja pesquisa:')
    print('')
    for a in acervo:
        if a.titulo.lower() == busca.lower():
            pesquisa_nome_livros.append(a)
    if pesquisa_nome_livros:
        for a in pesquisa_nome_livros:
            a.info()  # este vai informar todos os dados do livro incluindo os  homonimos da busca.
    else:
        print('Nenhum livro foi encontrado com este nome no acervo.')

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
opcao = int(input('Por favor infome a opção desejada: '))

while opcao != 0:
    if opcao == 1:
       cadastro_livros()
    elif opcao == 2:
        acervo_biblioteca()
    elif opcao == 3:
       # pesquisa(acervo)
        print(3)
    elif opcao == 4:
        busca = input('Informe o nome do livro que deseja:')
        for a in acervo:
            if busca == a.titulo:  # aqui feito o comparativo entre a variavel busca e a lista titulo.
                pesquisa.append(busca)  # neste eu guardo os positivos do comparativos na lista para posterior impressão, pois pode haver livros homônimos.
                j = +1
            else:
                print('Livro nao encontrado na base de dados.')
        print('4')
    elif opcao == 5:
        print('5')
    elif opcao == 6:
        print('6')
    elif opcao == 7:
        print('7')
    else:
        print('Opção não valida.')
    exibir_menu()

    opcao = int(input('Por favor informe a opção desejada: '))
for x in range(i):
    print(acervo[x].titulo, acervo[x].codigo, acervo[x].editora, acervo[x].area, acervo[x].ano, acervo[x].valor,acervo[x].quantidade_em_estoque) #forma concatenada de impressão dos atributos do objeto.
    print('')
print(acervo)# vai imprimir os endereços dos objetos.
print('Programa encerrado.')