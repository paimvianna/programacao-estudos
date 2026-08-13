#processamento
a=0
e=0

while(a<=9):
    b=0
    while(b <= 9):
        if(e<=b<=9):
            print(b, end='')
        if (b == 9):
            print('')
            e+= 1
        b+=1
    a+=1
