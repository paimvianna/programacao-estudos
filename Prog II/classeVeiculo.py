class Veiculo:
    def __init__(self, placa, proprietario):
        self.placa = placa
        self.proprietario = proprietario
        self.posX = 0
        self.posY = 0

    def emplacamento(self, novaPlaca, novoProprietario):
        self.placa = novaPlaca
        self.proprietario = novoProprietario

    def movimento(self, incX, incY):
        self.posX += incX
        self.posY += incY

    def info(self):
        print(f'Testando OVERRIDE')

class Carro(Veiculo):
    def __init__(self, placa, proprietario, nr_ocupantes):
        super().__init__(placa, proprietario)
        self.nr_ocupantes = nr_ocupantes

    def info(self):
        super().info()
        print(f'Informações de Carro')
        print(f'Placa: {self.placa}')
        print(f'Proprietario: {self.proprietario}')
        print(f'Nr de ocupantes: {self.nr_ocupantes}')
        print(f'X/Y: {self.posX}/{self.posY}\n')

if __name__ == '__main__':
    c1 = Carro("123j", "Zé", "4")
    c1.info()
    c1.movimento(30, 40)
    c1.emplacamento("123j", "Celso")
    c1.info()

