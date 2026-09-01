#fazer analise da memoria como no primeiro dia
from collections import deque

class Fila:
    
    def __init__(self):
        """
        Implementando uma lista sequencial
        """
        self.fila = deque()

    def inserir_ficha_normal(self,ficha_normal):
        self.fila.append(ficha_normal)

    def inserir_ficha_preferencial(self,ficha_preferencial):
            self.fila.appendleft(ficha_preferencial)

    def excluir_ficha(self,numero_ficha):
        if numero_ficha  in self.fila:
            self.fila.remove(numero_ficha)      
            print(f'Ficha {numero_ficha} removido com sucesso!')
        else:
            raise ValueError(f'Ficha {numero_ficha} nao encontrada na nnfila.')

    def atender_cliente(self):
        if not self.fila:
            raise ValueError(f'Não a cliente na fila para atender.')
        print(f'Ficha {self.fila.popleft()}')
         #return self.fila.popleft()

    def visualizar_fila(self):
        print(f'Fila atual:{list(self.fila)}')
        # return list(self.fila)

    def contar_por_tipo(self):
        comum = 0
        preferencial = 0
        for ficha in self.fila:
            if ficha.startswith("N"):
                comum += 1
            else:
                preferencial += 1
        total = len(self.fila)
        return comum, preferencial, total
class Ficha:
    """
    Aqui vou cria o objeto ficha, que podera ter normal e prioritaria neste caso.
    """
    def __init__(self):
        self.numero = 0
        self.numero_preferencial = 0

    def gera_ficha_normal(self,minha_fila):
        self.numero += 1
        ficha_normal = f"N{self.numero}"
        #minha_fila.fila.append(ficha_normal)
        minha_fila.inserir_ficha_normal(ficha_normal)
        return ficha_normal

    def gera_ficha_preferencial(self, minha_fila):
        self.numero_preferencial += 1
        ficha_preferencial = f"P{self.numero_preferencial}"
        #minha_fila.fila.append(ficha_preferencial)
        minha_fila.inserir_ficha_preferencial(ficha_preferencial)
        return ficha_preferencial
