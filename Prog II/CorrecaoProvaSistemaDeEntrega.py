class Pessoa:
    def __init__(self, nomeCompleto, cpf, telefone, email):
        self.nomeCompleto = nomeCompleto
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def AlterarContatos(self, NovoTelefone, NovoEmail):
        self.telefone = NovoTelefone
        self.email = NovoEmail
        
class Cliente(Pessoa):
    def __init__(self, nomeCompleto, cpf, telefone, email, cep, enderecoCompleto):
        super().__init__(nomeCompleto, cpf, telefone, email)
        self.cep = cep
        self.enderecoCompleto = enderecoCompleto

    def Info(self):
        print("--- Informações de CLIENTE --- CPF: {}".format(self.cpf))
        print("Nome do Cliente: {}".format(self.nomeCompleto))
        print("Endereço: CEP {} - {}".format(self.cep, self.enderecoCompleto))
        print("Contatos: {}/{}".format(self.telefone, self.email))

    def AlterarEndereco(self, novoCep, novoEndereco):
        self.enderecoCompleto = novoEndereco
        self.cep = novoCep

class Entregador(Pessoa):
    def __init__(self, nomeCompleto, cpf, telefone, empresa):
        super().__init__(nomeCompleto, cpf, telefone, None)
        self.email = nomeCompleto + "@" + empresa + ".com.br"
        self.email = self.email.replace(" ", "_")
        self.email = self.email.lower()
        self.empresa = empresa
        self.listaDeEntregas = []

    def Info(self):
        print("--- Dados do Entregador --- CPF: {}".format(self.cpf))
        print("Nome: {}".format(self.nomeCompleto))
        print("Empresa: {}".format(self.empresa))
        print("Contatos: {}/{}".format(self.telefone, self.email))

        print("+++++++++ Lista de entregas")
        self.InfoDeEntregas()

    def InfoDeEntregas(self):
        for entrega in self.listaDeEntregas:
            entrega.InfoParaEntregador()

    def AlocarEntrega(self, novaEntrega):
        self.listaDeEntregas.append(novaEntrega)

class Entrega:
    def __init__(self, cod, entregador, cliente):
        self.__cod = cod
        self.__entregador = entregador
        self.__entregador.AlocarEntrega(self)
        self.__cliente = cliente
        self.__situacao = "a caminho"

    def Info(self):
        print("--- Dados da Entrega --- nº{}".format(self.__cod))
        print("Situação: {}".format(self.__situacao))
        print("Entregador: {}/{}".format(self.__entregador.nomeCompleto, self.__entregador.empresa))
        print("Endereço: CEP {}/{}".format(self.__cliente.cep, self.__cliente.enderecoCompleto))
        print("Cliente: {}/{}".format(self.__cliente.nomeCompleto, self.__cliente.telefone))

    def InfoParaEntregador(self):
        print("+++++ Dados da Entrega --- nº{}".format(self.__cod))
        print("++ Situação: {}".format(self.__situacao))
        print("++ Endereço: CEP {}/{}".format(self.__cliente.cep, self.__cliente.enderecoCompleto))
        print("++ Cliente: {}/{}".format(self.__cliente.nomeCompleto, self.__cliente.telefone))

    def AlterarSituaca(self, novaSituacao):
        self.__situacao = novaSituacao

if __name__ == '__main__':
    c1 = Cliente("iuri gomes", "112233", "99889988", "iuri@email.com", "123", "Rua X 778")
    c1.Info()
    c1.AlterarContatos("321654987", "iag@email.com")
    c1.AlterarEndereco("456987", "Rua Y 987")
    c1.Info()

    ent1 = Entregador("Andre Gomes", "123654", "99887744", "BrasCom")
    ent1.Info()

    entrega1 = Entrega(123, ent1, c1)
    entrega1.Info()
    entrega1.AlterarSituaca("entregue")
    entrega1.Info()

    entrega2 = Entrega(663, ent1, c1)
    entrega3 = Entrega(236, ent1, c1)
    ent1.Info()
