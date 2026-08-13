#Entrada
numero1=float(input('Informe primeiro n°: '))
numero2=float(input('Informe segundo n°: '))

#Processamento
if(numero1>numero2):
    print('primeiro')
else:
    if(numero1<numero2):
        print('segundo')
    else:
        print('iguais')