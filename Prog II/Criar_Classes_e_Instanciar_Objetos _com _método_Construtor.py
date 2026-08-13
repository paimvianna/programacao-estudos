class empresa:
    def __init__(self, nome, cnpj, endereco,servico):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.servico = servico


if __name__ == '__main__':
    e1 = empresa('web', "0001",'rua da santinha numero 31','equipamento eletricos' )
    e2 = empresa('siemens', "0002", 'br 448 numero numero 16', 'inversores e equipamentos eletricos')
    e3 = empresa('trafo', "0003", 'avenida das industrias numero 13', 'venda e manutenção de transformadores' )

class remedio:
    def __init__(self, nome, tarja, valor, laboratorio, estoque):
        self.nome = nome
        self.tarja = tarja
        self.valor =valor
        self.laboratorio = laboratorio
        self.estoque = estoque


if __name__ == '__main__':
    r1 = remedio('paracetamol', 'branca',1.5, 'biriba', 1000)
    r2 = remedio('dipirona', 'branca', 2.5, 'crist', 2000)
    r3 = remedio('ritalina', 'preta', 250, 'calminho', 50)

class funcionario:
    def __init__(self, nome, sobrenome, cpf, salario, cargo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.salario = salario
        self.cargo =cargo


if __name__ == '__main__':
    f1 = funcionario('anderson', 'Paim', '123456', 1500, 'montador')
    f2 = funcionario('jose', 'santos', '234567', 1700, 'tecnico')
    f3 = funcionario('bia','rosa', '345678', 1800, 'engenheira')

class livro:
    def __init__(self, titulo,isbn, valor,autor, editora, estoque):
        self.titulo = titulo
        self.isbn = isbn
        self.valor = valor
        self.autor = autor
        self.editora = editora
        self.estoque = estoque


if __name__ == '__main__':
    l1 = livro('auto da compadecida', 1, 3.5, 'zeze','elipse',1000)
    l2 = livro('dom casmuro', 2, 4.5, 'pedro', 'letrados', 100)
    l3 = livro('amora', 3, 5, 'emicida', 'h2o', 200)

empresa = []
empresa.append(e1)
empresa.append(e2)
empresa.append(e3)

for x in range(3):
    print(empresa[x].nome, empresa[x].cnpj, empresa[x].endereco, empresa[x].servico) #forma concatenada.
    print('')

remedio = []
remedio.append(r1)
remedio.append(r2)
remedio.append(r3)

for x in range(3):
    print(remedio[x].nome, remedio[x].tarja, remedio[x].valor, remedio[x].laboratorio, remedio[x].estoque)  # forma concatenada.
    print('')

funcionario = []
funcionario.append(f1)
funcionario.append(f2)
funcionario.append(f3)

for x in range(3):
    print(funcionario[x].nome, funcionario[x].sobrenome, funcionario[x].cpf, funcionario[x].salario, funcionario[x].cargo)  # forma concatenada.
    print('')

livro = []
livro.append(l1)
livro.append(l2)
livro.append(l3)

for x in range(3):
    print(livro[x].titulo, livro[x].isbn, livro[x].valor, livro[x].autor, livro[x].editora, livro[x].estoque)  # forma concatenada.
    print('')
