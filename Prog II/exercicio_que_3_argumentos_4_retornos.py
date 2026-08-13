#nos retorn tenho que usar uma variavel por operação ou atividade.
'''def operacoes_basicas(x1,x2,x3):
  if x3 == 'soma':
    soma = (x1 + x2)
    return soma
  if x3 == 'sub':
    sub = (x1 - x2)
    return sub
  if x3 == 'div':
    div = (float(x1) / float(x2))
    return div
  if x3 == 'mult':
    mult = (x1 * x2)
    return mult'''
def operacoes_basicas(x1,x2,x3):#podemos definir uma entrada com valor padrao ex: def operacoes_basicas(x1,x2,x3='soma') neste caso x3 esta com valor padrao de 'soma'
  if x3 == 'soma':
    return x1 + x2
  if x3 == 'sub':
    return x1 - x2
  if x3 == 'div':
    return x1/x2
  if x3 == 'mult':
    return x1 * x2

print (operacoes_basicas(x1 = 2, x2 = 3, x3 = 'mult'))
print (operacoes_basicas(x1 = 2, x2 = 3)) # como x3 nao esta declarado ele assume o valor padrao que e a soma

