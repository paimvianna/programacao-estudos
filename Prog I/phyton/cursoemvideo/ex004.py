#Entrada
n=input('digite algo:')

#Processamento
print('O tipo primitivo desse valor é', type(n))
print('So tem espaço?', n.isspace())
print('E um numero? ', n.isnumeric())
print('E um alfanumerico? ', n.isalnum())
print('E alfabético? ', n.isalpha())
print('Está em maiuscula?',n.isupper())
print('Está em minuscula?',n.islower())
print('Está capitalizada?',n.istitle())