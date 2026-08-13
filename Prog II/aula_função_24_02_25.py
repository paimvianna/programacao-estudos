#funções sao estilo de blocos ou caixas pretas que pode ter entradas ou saidas aas entradas seram os argumentos e as saidas o ou os retorno
def soma2 (x1,x2):
    soma = x1 + x2
    return soma
def sub2 (x1,x2):
    sub = x1 - x2
    print(sub)
def mult2():
    print("OP de MULT")
    x1 = input("Qual valor de x1? ")
    x2 = input("Qual o valor de x2? ")
    return (int(x1)*int(x2))
def podeBeber(idade):
    if idade >= 18:
        return True
    else:
        return False
idade = 5
if podeBeber(idade): # podemos usar o 'not' antes da função que vai nega a saida da função. ja o '== True' se for igual a verdade entao ira ocorre confirmação.
    print('Pode beber!')
else:
    print('Não pode beber: ')

soma = soma2(x1=2, x2=3)

print(soma)

print(soma2(x1=5, x2=5))

x = sub2 (x1=10, x2=3)
print(mult2())