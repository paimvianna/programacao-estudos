#entrada
pri = int(input('Por favor informe o primeiro numero interiro: '))
seg = int(input('Por favor informe o segundo numero inteiro: '))
inicio = 1
limite = 0
# processamento
while pri >= inicio:
    #print(pri)
    a = pri
    #print (a)
    limite = pri +seg
    #print(limite)
    while a < limite:
        print (a, end=' ')
        a += 1
    print('')
    pri -= 1