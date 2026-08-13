#entrada
c=int(input('informe por favor um valor inteiro positivo: '))
i=1
#Processamento
while c >= i:
    a = 1
    p = 0
    while a <= c:
        if c%a ==0:
            print (f'{a} ', end='')
        a += 1
    print()
    c -= 1
