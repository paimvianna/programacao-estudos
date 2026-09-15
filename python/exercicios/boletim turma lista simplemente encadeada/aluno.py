class Aluno:
    """Estou criando uma classe dos objetos neste caso aluno, aqui vou criar
       o objeto e seus metodos, como impressão dos seus dados. """
    
    def __init__(self, nome: str, codigo_inscricao:int, media: float):
        self.nome = nome
        self.codigo_inscricao = codigo_inscricao
        self.media = media

    def __str__(self):
        """
        Vou retorna aqui a representação textual do objeto para o usario.
        Ou seja nao vou inprimir um objeto ou dicionario e simos dados formatados.
        """
        return f"Aluno (matricula= {self.codigo_inscricao}, nome= {self.nome}, media= {self.media})"

    def __eq__(self, outro):
        """
        Define o criterio de matemático de igualdade entre dois objetos no Python.
        Neste caso a matricula ou media. Creio que vou usar este criterio para pegar
        medias iguais e por colocar a o objeto mais antigo na frente do mais novo.
        """
        if isinstance(outro,Aluno):
            return self.codigo_inscricao == outro.codigo_inscricao

        return self.codigo_inscricao == outro

    def __gt__(self, outro):
        """
        Define quem e o maior baseado em criterio de comparação  entre dois objetos Python.
        Neste caso sera a media. Estou usando dicas do gemini.
        """
        if isinstance(outro,Aluno):
            return self.media > outro.media

        return self.media > outro

    def __repr__(self):
        """
        Retorna a representação oficial e técnica do objeto.
        É acionada automaticamente pelo Python ao imprimir o objeto quando ele está
        guardado dentro de coleções (listas, dicionários, etc). Se não for sobrescrito,
        o Python imprime o endereço de memória hexadecimal ilegível.
        """
        return f"Aluno: {self.nome}"