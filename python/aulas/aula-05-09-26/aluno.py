class Aluno:
    """
    Representa o registro de um aluno no sistema acadêmico.
    Funciona como o "Payload" (Dado útil) que será encapsulado dentro de um Nó
    na estrutura da Lista Simplesmente Encadeada.
    """

    def __init__(self, matricula: int, nome: str):
        """
        Construtor da classe Aluno.
        Inicializa os atributos de instância que definem a identidade do aluno.
        """
        self.matricula = matricula
        self.nome = nome

    def __str__(self):
        """
        Retorna a representação textual voltada para o usuário final.
        É acionada automaticamente quando fazemos um print() direto do objeto.
        """
        return f"Aluno(matricula={self.matricula}, nome='{self.nome}')"

    def __eq__(self, outro):
        """
        Define o critério matemático de igualdade entre dois objetos no Python.
        """
        # Certo: O Python detecta que a variável "outro" também é um objeto da classe Aluno.
        # Compara a matrícula do objeto atual (self) com a matrícula do objeto recebido.
        if isinstance(outro, Aluno):
            return self.matricula == outro.matricula

        # Fallback (Plano B): O Python detecta que "outro" não é um Aluno, mas sim um
        # valor primitivo (como um número inteiro ex: 201).
        # Compara a matrícula do objeto atual diretamente com esse número.
        return self.matricula == outro

    def __repr__(self):
        """
        Retorna a representação oficial e técnica do objeto.
        É acionada automaticamente pelo Python ao imprimir o objeto quando ele está
        guardado dentro de coleções (listas, dicionários, etc). Se não for sobrescrito,
        o Python imprime o endereço de memória hexadecimal ilegível.
        """
        return f"Aluno: {self.nome}"

