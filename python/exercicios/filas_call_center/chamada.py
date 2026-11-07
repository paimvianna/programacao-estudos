class Chamada:
    """
    Classe que representa uma chamada telefonica, onde cada chamada tem
    um número de telefone e um status que indica se a chamada foi atendida ou não.
    Funcionando como um "Playload"(Dado útil)que vai ser encapsulado dentro de um Nó
    na estrutura da lista Simplesmente Encadeada 
    """
    def __init__(self, numero: int):
        """
        Construtor da classe Aluno.
        Inicializa o atributo de chamada.
        """
        self.numero = numero

    def __str__(self):
        """
        Retorna a representação chamada, podendo ser em lista dos obj nela 
        ou o numero que foi atendido.
        """
        return f"Chamada (numero = {self.numero})."

    def __eq__(self, outro):
        """
        Aqui verifico se vamos fazer a comparação pra buscar o numero de telefone especifico. 
        """