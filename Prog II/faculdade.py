class disciplina:
    def __int__(self):
        self.alunos = []
    def __init__(self, nome, turma, professores):
        self.nome = nome
        self.turma = turma
        self.professores = professores
    def info(self):
        print(f'Nome da Disciplina: {self.nome}')
        print(f"Turma: {self.turma}")
        print(f'Professor da disciplina: {self.professores}')
        for a in self.alunos:
            print(a)
        print('')
class aluno:
    def __init__(self):
        self.disciplinas = []
    def __init__(self, matricula, nome, disciplinas):
        self.matricula = matricula
        self.nome = nome
        self.disciplina = disciplinas
    def info(self):
        print(f'Matricula do aluno: {self.matricula}')
        print(f"Turma: {self.turma}")
        for a in self.disciplinas:
            print(a)
        print('')
class professor:
    def __init__(self):
        self.disciplinas_professor = []
    def __init__(self, matricula, nome, disciplinas):
        self.matricula = matricula
        self.nome = nome
        self.disciplinas_professor = disciplinas
    def info(self):
        print(f'Matricula do aluno: {self.matricula}')
        print(f"Turma: {self.turma}")
        for a in self.disciplinas_professor:
            print(a)
        print('')
class faculdade:
    def disciplina(self):
        nome = str(input(f'Informe o nome da Disciplina:'))
