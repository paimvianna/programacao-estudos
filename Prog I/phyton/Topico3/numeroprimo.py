#entrada
n=int(input('por favor informe um numero:'))
c=0
p=0
while(c<=n):
    c+=1
    if((n%c)==0):
        #print(c,end=' ')
        p+=1
        #print('e divisor.')
if(p==2):
    #print(f'{n:02d} é primo')
    print('sim')
else:
    #print(f'{n:02d} não e primo')
    print('não')