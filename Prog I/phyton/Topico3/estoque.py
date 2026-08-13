#entrada
e=int(input('informe o digito do grão a ser recebido:\nLegenda:\n1 trigo.\n2 arroz.\n3 cevada.\n4 milho.\n0 para sair.\n'))
#processamento
t=0
a=0
c=0
m=0
k=0
while(e!=0):
    q=int(input('informe a quantidade em tonelas a ser recebida:'))
    if ( e==1):
        t += q
    if (e == 2):
        a += q
    if (e == 3):
        c += q
    if (e == 4):
        m += q
    k += q
    e=int(input('informe o digito do grão a ser recebido: '))
#processamento/saida
l=1
while(l<=4):
    if(l==1):
        y = l
        w = t
        x = (t / k) * 100
    if(l==2):
        y = l
        w = a
        x = (a / k) * 100
    if(l==3):
        y = l
        w = c
        x = (c / k) * 100
    if(l==4):
        y = l
        w = m
        x = (m / k) * 100
    print(f'{l} {w} {x:.2f}')
    l+=1
#saida
#print(f'{k}\n1 {t} {(t/k)*100:.2f}\n2 {a} {(a/k)*100:.2f}\n3 {c} {(c/k)*100:.2f}\n4 {m} {(m/k)*100:.2f}\n')
