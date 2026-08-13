novo_cpf_str = input(f'Informe o CPF: ')
novo_cpf_str = novo_cpf_str.replace('.','').replace('-','')
if not isinstance(novo_cpf_str,str) or len(novo_cpf_str) != 11 or not novo_cpf_str.isdigit():
    print('1 falso')
else:
    a = 0
    cpf_inteiro = []
    for i in novo_cpf_str:
        novo_cpf = int(i)
        cpf_inteiro.append(novo_cpf)
        a+=1
    novo_cpf = cpf_inteiro
    if len(set(novo_cpf)) == 1: # aqui o set verifica que no conjunto ou seja lista cpf quantos itens tem iguais criando um conjunto que se verifica o tamanho e vejo se e igual a 1 que significa que todos os 11 elementos sao iguais.
    #if novo_cpf[0]==novo_cpf[1] and novo_cpf[1]==novo_cpf[2] and novo_cpf[2]==novo_cpf[3]
    # and novo_cpf[3] == novo_cpf[4] and novo_cpf[5]==novo_cpf[6] and novo_cpf[7]==novo_cpf[8] and novo_cpf[9]==novo_cpf[10]:
        print('falso')

    soma_a = 0
    for i in range(0, 9, 1):
        soma_a += novo_cpf[i] * (10 - i)
        #print(i,'*',(10-i),'=', soma_a) usei para verificar
        # se estava ocorrendo a multiplicação corretamente
    divisao_soma_a = soma_a // 11
    resto_a = soma_a % 11

    if (resto_a < 2) and (novo_cpf[9] == 0):
        print('1')
    elif (resto_a >= 2 and resto_a < 10) and (11 - resto_a == novo_cpf[9]):
        print('2')

    soma_b = 0
    for i in range(0, 10, 1):
        soma_b += novo_cpf[i] * (11 - i)
    divisao_soma_b = soma_b // 11
    resto_b = soma_b % 11

    if (resto_b <2) and (novo_cpf[10] == 0):
        print('3')
    elif (resto_b >= 2 and resto_b < 10) and (11 - resto_b == novo_cpf[10]):
        print('4')
'''
    if (val_1 == True or val_2 == True) and (val_3 == True or val_4 == True):
        print(f'O CPF numero: {novo_cpf} é válido!')
#self.__cpf = novo_cpf
'''