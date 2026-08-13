l=[]
a=0
b=1
for i in range(3):
    c = []
    for j in range(3):
       n = int(input('informe os valores da matris:'))
       c.append(n)
    l.append(c)
h=[]
k=2
m=2
for i in range(2,0,-1):
    f=[]
    for j in range (2,0,-1):
        print (j)
        f.append(c[j])
        #print (j)
        #print('a',c[j])
        #print ('b',f[j])
    h.append(l[i])
    #print('a',l[i])
    print('b',h[i] )
