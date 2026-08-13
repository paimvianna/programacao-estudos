#entrada
inicial=float(input('informe o valor inicial da PA: '))
quantidade=int(input('informe a quantidades de termos: '))
progressao=float(input('informe o valor da Progressão ou a Razão: '))
r=inicial
'''
l=[inicial]
#Processamento
for i in range(1,quantidade):
    r += progressao
    l.append(r)
#saida
print(l)
s = sum(l)
print(s)
'''
l=[]
for i in range(quantidade):
    l.append(r)
    r += progressao
print(l)
s = sum (l)
print(s)