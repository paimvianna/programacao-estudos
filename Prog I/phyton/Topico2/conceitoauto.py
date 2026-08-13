#entrada
n1=float(input('Por favor informe a N1: '))
n2=float(input('Por favor informe a N2: '))
n3=float(input('Por favor informe a N3: '))
p1=1
p2=2
p3=3
#Processamento
m=((p1*n1)+(n2*p2)+(n3*p3))/(p1+p2+p3)
if(m<4):
    print('{:.2f} Reprovado' .format(m))
elif(4<m<7):
    print('{:.2f} Exame' .format(m))
elif(m>=7):
    print('{:.2f} Aprovado' .format(m))