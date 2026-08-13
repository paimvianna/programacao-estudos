#entrada
n=float(input('por favor informe um numero:'))
k = 0
#processamento
while(n!=0):
    c = 1
    p = 0
    while(c<=n):
        if((n%c)==0):
            p+=1
        c+=1
    if(p==2):
        k+=1
    n = float(input('por favor informe um numero:'))
#saida
print(k)