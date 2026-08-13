'''programa que gerencia notas de alunos de uma turma'''
nome = []
media = 0
nota = []
matricula = []
total_de_alunos = 0
print('Olá, por favor selecione uma das opções da legenda: \n'
      'F.1- Cadastro de Alunos. \n'
      'F.2- Informações de Alunos. \n'
      'F.3- Modificar nota. \n'
      'F.4- Média de notas. \n'
      'F.0- Sair: sair do sistema. \n')
f = int(input('Informe a função desejada, 1, 2, 3, 4, 0: '))
while f != 0: #or f == 1 or f == 2 or f == 3 or f ==4:
    if f == 1:
        n = input('Por favor informe o nome do aluno: ')
        nome.append(n)
        #sobrenome = input('Por favor informe o sobrenome do aluno: ')
        nt = float(input('Informe a nota do aluno: '))
        nota.append(nt)
        #print('teste1')
    elif f == 2:
        total_de_alunos = len(nome)
        if total_de_alunos == 0:
            print('')
            print('Não à alunos cadastrados.')
            print('')
        for i in range (total_de_alunos):
            mt= nome.index(nome[i]) + 1
            matricula.append(mt)
            print(f'{nome[i]} {nota[i]} {matricula[i]}')
        #print('teste2')
    elif f == 3:
        mt = int(input('informe a matricula do aluno: ')) - 1
        #total_de_alunos = len(nome)
        '''
        for i in range(len(nome)):
            if nome.index(nome[i]) == mt:
                n = int(input('Informe a nova nota do aluno: '))
                nota[i] = n
            else:
                print('Aluno não encontrado.')
        '''
        k = 0
        while i < len(nome) and k == 0:
            if nome.index(nome[i]) == mt:
                n = int(input('Informe a nova nota do aluno: '))
                k += 1
            elif i == len(nome):
                print('Aluno não encontrado.')
            i += 1
        #print('teste3')
    elif f == 4:
        for i in range(len(nome)):
            media += nota[i]
        print(media)
    else:
        s = int(input('Por favor informe um valor valido dentre as funções.\n'
                  'Informe a função desejada, 1, 2, 3, 4, 0: '))
    print('Olá, por favor selecione uma das opções da legenda: \n'
          'F.1- Cadastro de Alunos. \n'
          'F.2- Informações de Alunos. \n'
          'F.3- Modificar nota. \n'
          'F.4- Média de notas. \n'
          'F.0- Sair: sair do sistema. \n')
    f = int(input('Informe a função desejada, 1, 2, 3, 4, 0: '))
if f == 0:
    print('Sistema foi fechado')
