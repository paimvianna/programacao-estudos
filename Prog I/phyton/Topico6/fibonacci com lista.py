#entrada
n = int (input('informe um numero N maior que 1: '))
#Processamento
l=[0,1]
for i in range (n-2):# tenho que ver que este e o
                    # numero de repetições, entao na primeira rodada
                    # ja terie 3 então portantopela definição padrão
                    # ja tenho um a mais no fim portanto tenho que terminar antes.
    a = l[i] + l[i+1]
    l.append(a)
#saida
for i in range (n):
    print(l[i])
