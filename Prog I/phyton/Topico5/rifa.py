#entrada
import random
print('Para finalizar o programa digite 0 no valor do bilhete.')
bilhete = int(input('informe o numero do biblete: '))
l1=[]
l2=[]
while bilhete != 0:
    #print(bilhete)
    l2.append(bilhete)
    nome = str(input('informe o nome do comprador: '))
    l1.append(nome)
    bilhete = int(input('informe o numero do biblete: '))
#random.shuffle(l2)
#print('numeros embaralhados.')
sorteado=random.choice(l2)
sortudo = l2.index(sorteado)
print(f'numero sorteado {sorteado}.')
print(f'posição na lista {sortudo}.')
print(f'nome do sortudo {l1[sortudo]}.')
#print(l1,l2,)
