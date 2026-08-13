'''Criar uma classe chamada Aluno:

    Atributos: nomeCompleto, curso, matricula, email e notas
    O atributo email é formado da seguinte forma <matricula>@aluno.ifrs.edu.br
    O atributo notas é um dicionario onde a chave é o nome da disciplina e a nota o valor armazenado
        Pesquisar o funcionamento de dicionario
    Método de informação
    Método para alterar notas
        Recebe como parametros o nome da disciplina e a nova nota.'''
class Aluno:
    def __init__(self, nomeCompleto, curso, matricula, email, notas):
        self.nomeCompleto = nomeCompleto
        self.curso = curso
        self.matricula = matricula
        self.email = f'{self.matricula}@ifrs.edu.br'# aqui eu pego parametro contatenado com o resto do email.
        self.notas = {}
if __name__ == '__main__':
    al1 = Aluno('anderson paim', 'ADS', '0001', '@aluno.ifrs.edu.br', 10)
    al2 = Aluno('giovanna teixeira rodrigues', 'Enfermagem', '0002', '@aluno.ifrs.edu.br', 10)
    al3 = Aluno('flor teixeira' 'musica', '003', '@aluno.ifrs.edu.br', 8)
