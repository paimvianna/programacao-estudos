#entrada
t=int(input('informe o total de votantes: '))
v=int(input('informe o seu voto: '))
a=0
b=0
c=0
d=0
e=0
i=1
k=0
m=0
while(i<t):

    if(v==1):
        a+=1
    if(v==2):
        b+=1
    if(v==3):
        c+=1
    if(v==4):
        d+=1
    if(v==5):
        e+=1
    i += 1
    v=int(input('informe o seu voto: '))
if(v==1):
    a+=1
if(v==2):
    b+=1
if(v==3):
    c+=1
if(v==4):
    d+=1
if(v==5):
    e+=1

k=a+b+c+d+e

if(e>a and e>b and a>c and e>d):
    m = 5
    n = 'venceu'
elif(a>b and a>c and a>d and a>e):
    m=1
    n='venceu!'
elif(b>a and b>c and b>d and b>e):
    m=2
    n='venceu'
elif(c>a and c>b and c>d and c>e):
    m=3
    n='venceu'
elif(d>a and d>b and d>c and d>e):
    m=4
    n='venceu'
elif(a==b or a==c or a==d or a==e or b==c or b==d or b==e or c==d or c==e or e==d):
    n='Empate!'
#print(a, b, c, d, e)
print(f'1 {a} {(a/k)*100:02.2f}%')
print(f'2 {b} {(b/k)*100:02.2f}%')
print(f'3 {c} {(c/k)*100:02.2f}%')
print(f'4 {d} {(d/k)*100:02.2f}%')
print(f'5 {e} {(e/k)*100:02.2f}%')
if(m!=0):
    print(f'{m} {n}')
else:
    print(f'{n}')