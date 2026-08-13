'''class Pessoa:
    def __init__(self):
        nome=''
        sobrenome=''
        idade=''

if __name__ == '__main__':
    p1 = Pessoa()
    print(p1)
    p1.nome = "Iuri"
    print(p1.nome)
    p1.sobrenome = "Albandes"
    print(p1.sobrenome)
    p1.idade = 37
    print(p1.idade)
    p2 = Pessoa()
    print(p2)
    p2.nome = "Anderson"
    print(p2.nome)
    p2.sobrenome = "Paim"
    print(p2.sobrenome)
    p2.idade = 39
    print(p2.idade)
    p3 = Pessoa
    print(p3)
    p3.nome = 'Fernando'
    print(p3.nome)
    p3.sobronome = 'Vianna'
    print(p3.sobronome)
    p3.idade = 36
    print(p3.idade)
'''
class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

if __name__ == '__main__':
    p1 = Pessoa('Iuri', 'Albanes', 37)
    '''
    print(p1.nome, p1.sobrenome, p1.idade)
    p1.sobrenome = "Albandes"
    print(p1.sobrenome)
    p1.idade = 37
    print(p1.idade)
    '''
    p2 = Pessoa('Anderson', 'Paim', 39)
    '''
    print(p2)
    print(p2.nome)
    print(p2.sobrenome)
    print(p2.idade)
    '''
lista_pessoa = []
lista_pessoa.append(p1)
lista_pessoa.append(p2)
for x in range(2):
    print(lista_pessoa[x].nome, lista_pessoa[x].sobrenome, lista_pessoa[x].idade) #forma concatenada.


