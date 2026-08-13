class Loja:
    def __init__(self, nome, cnpj, espaco_comercial, nr_loja):
        self.nome = nome
        self.cnpj = cnpj
        self.espaco_comercial = espaco_comercial
        self.nr_loja = nr_loja


    def info(self):
        print('---> Loja')
        print(f'Nome: {self.nome}')
        print(f'CNPJ: {self.cnpj}')
        print(f'Local: {self.espaco_comercial} - nr {self.nr_loja}')

    def mudancaDeEspaco(self, novo_local, novo_nr_loja):
        self.espaco_comercial = novo_local
        self.nr_loja = novo_nr_loja

if __name__ == '__main__':
    arquivo = open("dados_de_lojas.txt", 'r')
    lista_de_lojas = []


    linha = arquivo.readline().replace("\n", "")
    linha_sep = linha.split(",")

    while linha:
        print(linha_sep)
        nova_loja = Loja(linha_sep[0], linha_sep[1], linha_sep[2], linha_sep[3])
        lista_de_lojas.append(nova_loja)

        linha = arquivo.readline().replace("\n", "")
        linha_sep = linha.split(",")

    for loja in lista_de_lojas:
        loja.info()

    #loja1 = Loja("Panvel", "1234", "Barra Shopping", "137")
    #loja1.info()

3426,compiladores,2012,computação,pearson,135.50,50
2631,sistemas digitais,2017,computação,liber,99.90,30
9680,senhor dos aneis: a sociedade do anel,2005,fantasia,harper,35.00,120
