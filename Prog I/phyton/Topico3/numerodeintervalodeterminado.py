#entrada
v=int(input('informe os valores a serem avaliados: '))
#processamento
c=0
while(v!=0):
    if(100<=v<=200):
        c+=1
    v=int(input('informe os valores a serem avaliados: '))
#saida
if(c!=0):
    print(c)
else:
    print(v)