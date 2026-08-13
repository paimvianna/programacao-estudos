def soma2(x1, x2):
    soma = x1 + x2
    return soma

def sub2(x1,x2):
    sub = x1 - x2
    print(sub)

def mult2():
    print("OP de MULT")
    x1 = input("Qual valor de x1?")
    x2 = input("Qual o valor de x2?")
    return (int(x1)*int(x2))

def podeBeber(idade):
    if (idade >= 18):
        return True
    else:
        return False

def arit(x1, x2, op='+'):
    if op == "+":
        return x1+x2
    if op == "-":
        return x1-x2
    if op == '*':
        return x1*x2
    if op == '/':
        return x1/x2

def soma_lista(lista):
    soma = 0
    for x in lista:
        soma = soma + x

    return soma

def lista_alunos(turma, *args, **kwargs):
    print(args)
    print(kwargs)
    #print(prof2)

def soma_valores(*args):
    soma = 0
    for x in args:
        soma += x
    return soma

lista_alunos("ads2", "iuri", "pedro", "ana", prof1="iuri", prof2="ricardo")

print("------")
print(soma_valores(1,2,3))
print(soma_lista([1,2,3]))
print(soma_lista([1,1,1,1,1]))
print("------")
print(arit(2,10))
print(arit(op='-', x2=10, x1=5))
print(arit(2,3,"+"))
print(arit(2,3,"-"))
print(arit(2,3, "*"))
print(arit(2,3,'/'))


idade = 5
if not(podeBeber(idade)):
    print("Pode beber!")
else:
    print("Não pode beber :(")



soma = soma2(2,3)
print(soma)
print(soma2(5,5))
sub2(10,3)
#print(mult2())