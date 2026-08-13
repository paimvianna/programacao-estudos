#entrada
e=int(input('informe o digito do competidor:'))
#processamento
pri=0
seg=0
ter=0
qua=0
qui=0
k=0
while e != 0:
    t=int(input('informe a quantidade de tijolos: '))
    if e == 1:
        pri += t
    if e == 2:
        seg += t
    if e == 3:
        ter += t
    if e == 4:
        qua += t
    if e == 5:
        qui += t
    e=int(input('informe o digito do competidor: '))
k = pri+seg+ter+qua+qui
#processamento/saida
if pri>=seg>=ter>=qua>=qui:
    l=1 
    w=pri
elif seg>pri>=ter>=qua>=qui:
    l=2 
    w=seg
elif ter>seg>pri>=qua>=qui:
    l=3
    w=ter
elif qua>ter>seg>pri>=qui:
    l=4
    w=qua
elif qui>qua>ter>seg>pri:
    l=5
    w=qua
#if e ==0:
 #   print(0)
#else:
print(f'{l} {w}')
