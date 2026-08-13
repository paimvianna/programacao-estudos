k=0
c=9
while(k<=c):
    a=0
    while(a <= c):
        if(a%2!=0):
            print(a, end='')
        if (a == c):
            print('')
            c -= 1
        a += 1
    b=0
    while(b <= c):
        if(b%2==0):
            print(b, end='')
        if (b == c):
            print('')
            c -= 1
        b += 1
k+=1