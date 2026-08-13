#entrada
c=int(input('informe por favor um valor inteiro possitivo: '))
i=1
#Processamento
while i<c:
    a = 1
    p = 0
    while a <= i:
        if i%a==0:
            p+=1
        a += 1
#saida
    if p==2:
        print(i)
    i += 1