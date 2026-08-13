#entrada
v=int(input('Por favor informe um inteiro positivo: '))

n1=0
n2=1
c=1
#processamento
while(c<v):
    n3=n1+n2
    #na primeira versão usei print(n1,'-',n2,'-',n3,'-',end='')
    # onde eu imprimia a cada ciclo os tres valores que sendo
    # prejudicial ao codigo, pq no fim todos os valores iram passar por n1.
    print(n1,'-', end='')
    n1=n2
    n2=n3
    c+=1
#saida
print(n1)