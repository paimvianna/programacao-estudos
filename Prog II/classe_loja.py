class loja:
    def __init__(self, nome, cnpj, espaco_comercial, numero_sala,variavel5,variavel6,variavel7):
        self.nome = nome
        self.cnpj = cnpj
        self.espaco_comercial = espaco_comercial
        self.numero_sala = numero_sala
        self.variavel5 = variavel5
        self.variavel6 = variavel6
        self.variavel7 = variavel7

    def info(self):
        print(f">>>>> numero sala{self.numero_sala}")
        print(f"Nome da loja: {self.nome}")
        print(f'cnpj{self.cnpj}')
        print(f'Espaço comercial: {self.espaco_comercial}')

        print('')

    def mudancade_espaco(self, mudancade_espaco, novo_numero_sala):
        self.espaco_comercial = mudancade_espaco
        self.numero_sala = novo_numero_sala

if __name__ == '__main__':
    arquivo = open('acervo.txt', 'r' )
    lista_de_lojas =[]

    linha = arquivo.readline().replace('\n', '')
    linha_sep = linha.split(',')
    while linha:
        print(linha_sep)
        nova_loja = loja(linha_sep[0], linha_sep[1], linha_sep[2], linha[3], linha[4],linha[5],linha[6])
        lista_de_lojas.append(nova_loja)

        linha = arquivo.readline().replace('\n', '')
        linha_sep = linha.split(',')

    for loja in lista_de_lojas:
        loja.info()

#loja1 = loja('Panvel', '234', 'Barra Shopping', '137','0000','44444','555')
#lista_de_lojas.append(loja1)