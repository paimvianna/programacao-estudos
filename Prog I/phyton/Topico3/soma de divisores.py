#entrada
n=int(input('por favor informe um numero:'))
c=0
p=0
while(c<=n):
    c+=1
    if((n%c)==0):
        p+=c

print(p)
