l=[]
a = 0
k = 0
while a != 1:
    n = int(input('informe o numero interio maior que 1: '))
    if n % 2 == 1 and n > 1:
        a = 1
        b = n
    #print(a)
    #print(n)
for i in range(b):
    n = int(input('informe o numero interio maior que 1: '))
    l.append(n) 
#print(l)
c = b // 2
#print(c)
print (l[c])
if l[c] % 2 == 1:
    print ('impar')
    for i in range (b):
        if l[i] % 2 == 1:
            k += l[i]
            
    print(k)
else:
    print('par')
    for i in range (b):
        if l[i] % 2 == 0:
            k += l[i]
    print(k)