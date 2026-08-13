'''
Criar uma classe chamada Produto:
Atributos: marca, modelo, valor e estoque
    Método de informação
    Método para alterar valor
    Método pra alterar estoque
    '''

class Produto:
    def __init__(self, marca, modelo, valor, estoque):#metodo construtor que tem os parametros que se liga ao atributos seria o que o atributo recebe.
        self.marca = marca # oq eu tem self e o atributo
        self.modelo = modelo
        self.valor = valor
        self.estoque = estoque
    def info(self):
        print("+++INformações de produto")
        print(f"Marca/modelo: {self.marca}/{self.modelo}")
        print(f"Valor/estoque: R${self.valor}/{self.estoque}")
if __name__ == '__main__':
    prod1 = Produto('nike','12 mola', 500, 1000)
    prod2 = Produto('mizuno', 'prata veloz', 300, 500)
    prod3 = Produto('adidas', '3 linhas', 250, 700)

produtos=[]
produtos.append(prod1)
produtos.append(prod2)
produtos.append(prod3)
print(produtos[0])