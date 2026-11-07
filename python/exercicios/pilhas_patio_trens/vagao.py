class Vagao:
    """
    Representa o registro de um vagão no sistema do Patio.
    Funciona como o "Payload" (Dado útil) que será encapsulado dentro de um Nó
    na estrutura da Lista Simplesmente Encadeada.
    """

    def __init__(self, id_vagao: int, tipo_carga: str):
        """
        Construtor da classe Vagão.
        Inicializa os atributos de instância que definem a identidade do vagão.
        """
        self.id_vagao = id_vagao
        self.tipo_carga = tipo_carga

    def __str__(self):
        """
        Retorna a representação textual voltada para o usuário final.
        É acionada automaticamente quando fazemos um print() direto do objeto.
        """
        return f"Vagão (matricula={self.id_vagao}, tipo carga='{self.tipo_carga}')"

    def __eq__(self, outro):
        """
        Define o critério matemático de igualdade entre dois objetos no Python.
        """
        # Certo: O Python detecta que a variável "outro" também é um objeto da classe Vagao.
        # Compara a matrícula do objeto atual (self) com a matrícula do objeto recebido.
        if isinstance(outro, Vagao):
            return self.id_vagao == outro.id_vagao

        # Fallback (Plano B): O Python detecta que "outro" não é um Aluno, mas sim um
        # valor primitivo (como um número inteiro ex: 201).
        # Compara a matrícula do objeto atual diretamente com esse número.
        return self.id_vagao == outro

    def __repr__(self):
        """
        Retorna a representação oficial e técnica do objeto.
        É acionada automaticamente pelo Python ao imprimir o objeto quando ele está
        guardado dentro de coleções (listas, dicionários, etc). Se não for sobrescrito,
        o Python imprime o endereço de memória hexadecimal ilegível.
        """
        return f"Vagão: matricula {self.id_vagao}"




if __name__ == "__main__":
    """
    Códigos para testar a classe e seus métodos...
    """

    # Cria 4 objetos, sendo dois repetidos...
    a1 = Vagao(201, "Grão")
    a2 = Vagao(202, "Cimento")
    a3 = Vagao(203, "Combustivel")
    a4 = Vagao(201, "Carne")
    a5 = Vagao(202, "Grão")

    # Testa método "__eq__" para determinar objetos iguais...
    iguais = a1 == a4
    print(iguais)
    iguais = a1 == a2
    print(iguais)

    # Testa método __str__
    print(a1)

    # Testa método "__repr__"

    # --> usando diretamente a função repr() que chama o __repr__ diretamente
    print(repr(a1))

    # Ou usando uma lista
    vagoes = [a1, a2, a3, a4, a5]
    print(vagoes)