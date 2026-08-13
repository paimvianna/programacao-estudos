class carro:
    def __init__(self, placa, proprietario, posx, posy):
        self.placa = placa
        self.proprietario = proprietario
        self.posx = posx
        self.posy = posy

    def info (self):
        print(f'O numero da placa do carro: {self.placa}')
        print(f'O nome do proprietario do carro: {self.proprietario}')
        print(f'A movimentação do carro e Pos X {self.posx} Pos y{self.posy}')

    def emplacamento(self, placanova, proprietarionovo):
        placanova = input('Informe a placa do carro?')
        proprietarionovo = input('Informe o proprietario do carro?')
        self.placa = placanova
        self.proprietario = proprietarionovo

    def movimento(self, x, y):
        x = input('Informe a posição X atual: ')
        y = input('Informe a posição y atual: ')
        self.posx += x
        self.posy += y

class caminhao:
    def __init__(self, placa, proprietario, numero_eixo, carga, cap_max, posx, posy):
        self.placa = placa
        self.proprietario = proprietario
        self.numero_eixo = numero_eixo
        self.carga = carga
        self.cap_max = cap_max
        self.posx = posx
        self.posy = posy

    def info(self):
        print(f'O numero da placa do caminhão: {self.placa}')
        print(f'O nome do proprietario do caminhão: {self.proprietario}')
        print(f'O caminhao tem {self.numero_eixo} eixos.')
        print(f'A carga total do caminhão eh: {self.carga}')
        print(f'A capacidade maxima do caminhão eh: {self.cap_max}')
        print(f'A movimentação do caminhão é Pos X {self.posx} Pos y{self.posy}')


    def caminhao_emplacamento(self, placanova, proprietarionovo):
        placanova = input('Informe a placa do caminhão?')
        proprietarionovo = input('Informe o proprietario do caminhão?')
        self.placa = placanova
        self.proprietario = proprietarionovo

    def carga(self, carregamento):
        carregamento = float(input('Informe o peso que deseja carregar: '))
        if (carregamento <= self.cap_max and (carregamento + self.carga) <= self.cap_max):
            self.carga += carregamento
        else:
            print(f'O valor que deseja carregar esta acima da capacidade do caminhão.\nA capacidade Maxima dele eh de {self.cap_max}, o mesmo já esta com {self.carga} de carga.')
    def descarregar(self, descarga):
        descarga = float(input(f'Informe o valor que deseja descarregar: '))
        if (descarga <= self.carga):
            self.carga -= descarga
        else:
            print(f'O valor que deseja descarregar esta acima do valor que esta carregado que eh: {self.carga}')

    def movimento(self, x, y):
        x = input('Informe a posição X atual: ')
        y = input('Informe a posição y atual: ')
        self.posx += x
        self.posy += y