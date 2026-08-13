#Entrada
n1=int(input('Por favor informe o primeiro numero: '))
n2=int(input('Por favor informe o segundo numero: '))
#Processamento
if(n1>=n2):
    m=n1%n2
    if(m==0):
        print('sim')
    else:
        print('não')
else:
    m=n2%n1
    if(m==0):
        print('sim')
    else:
        print('não')