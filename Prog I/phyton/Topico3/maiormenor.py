#Entrada
v = int(input('informe um valor: '))
minimo = maxima = v

#processamento
while(v != 0):
    
    if (v> maxima):
        maxima=v
        
    if(v<minimo):
        minimo=v
    v=int(input('informe um valor: '))
print(f'{minimo:} {maxima}')