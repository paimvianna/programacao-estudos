#Entrada
amostras=int(input('informe quantas temperaturas de amostragem: '))
minimo=maxima=int(input('informe a temperatura: '))
cont=1
#processamento
while(cont<amostras):
    temperatura1 = int(input('informe a temperatura: '))
    if (temperatura1 > maxima):
        maxima=temperatura1
        
    if(temperatura1<minimo):
        minimo=temperatura1
    cont+=1
print(f'{minimo:}/{maxima}')