#entrada
v=int(input('Por favor informe um inteiro positivo: '))

n1=0
n2=0
c=1
#processamento
while(c<=v):
    n1=v%c
    if(n1==0 and c<v):
        n2+=c
    c+=1
#saida
if(n2==v):
    print('sim')
else:
    print('não')