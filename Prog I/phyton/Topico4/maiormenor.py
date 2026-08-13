#entrada
numero = int(input('Informe um numero inteiro: '))
maior = menor = numero

#processamento
while numero != 0:
    numero = int(input('Informe um numero inteiro: '))
    if maior < numero:
        maior = numero
    if menor > numero and numero != 0:
        menor = numero
    #print (f'maior {maior}')
    #print (f'menor {menor}')
print (menor, maior)