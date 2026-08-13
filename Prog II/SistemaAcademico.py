class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.disciplinas = []

    def Info(self):
        print("--- Aluno")
        print(f'Matricula: {self.matricula}')
        print(f'Nome: {self.nome}')
        self.InfoDisciplinas()

    def InfoDisciplinas(self):
        if len(self.disciplinas)>0:
            for disc in self.disciplinas:
                print(disc.nome)

    def CadastraDisciplina(self, novaDisciplina):
        self.disciplinas.append(novaDisciplina)

class Professor:
    def __init__(self, nome, matricula, area):
        self.nome = nome
        self.matricula = matricula
        self.area = area
        self.disciplinas = []

    def Info(self):
        print("--- Professor")
        print(f'Matricula: {self.matricula}')
        print(f'Nome: {self.nome}')
        print(f'Area: {self.area}')
        self.InfoDisciplinas()

    def InfoDisciplinas(self):
        if len(self.disciplinas)>0:
            for disc in self.disciplinas:
                print(disc.nome)

    def CadastraDisciplina(self, novaDisciplina):
        self.disciplinas.append(novaDisciplina)

class Disciplina:
    def __init__(self, nome, curso, turma, professor = "A Definir"):
        self.nome = nome
        self.curso = curso
        self.turma = turma
        self.alunos = []
        self.professor = professor
        if type(self.professor) == Professor:
            self.professor.CadastraDisciplina(self)

    def Info(self):
        print("--- Disciplina")
        print(f'Nome: {self.nome}')
        print(f'Curso-Turma: {self.curso} - {self.turma}')
        print(f'Docente: {self.professor.nome}')
        self.ListarAlunos()

    def ListarAlunos(self):
        if len(self.alunos) > 0:
            for aluno in self.alunos:
                print(f'{aluno.matricula} - {aluno.nome}')

    def CadastraAluno(self, novoAluno):
        self.alunos.append(novoAluno)

    def CadastraProfessor(self, novoProfessor):
        self.professor = novoProfessor
        novoProfessor.disciplinas.append(self)

if __name__ == '__main__':
    a1 = Aluno("Iuri", 123)
    p1 = Professor("Jose", 321, "Computação")
    d1 = Disciplina("Programação II", "ADS", "2025-1")
    d2 = Disciplina("Engenharia de Software", "ADS", "2024-2", p1)
    d3 = Disciplina("E1", "ADS", "2024-2", p1)

    a1.CadastraDisciplina(d1)

    d1.CadastraAluno(a1)
    d1.CadastraProfessor(p1)
    a1.Info()
    p1.Info()
    d1.Info()
    d2.Info()


