#entreda
n=int(input('informe o primeiro valor inteiro positivo do intevalo:'))
n1=int(input('informe o segundo valor inteiro positivo do intevalo:'))
if(n<n1):
    f=1
    v1=0
    v2=1
    while(f<=n1):
        v3=v1+v2
        
        #if(n<=v1):
        #    if(v1<=n1):
        if(n<=v1<=n1):
                print(v1, end=' ')
        v1=v2
        v2=v3
        f+=1
else:
    print('valores iguais ou valor 2 menor que valor 1')