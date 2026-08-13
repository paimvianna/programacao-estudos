#processamento
a=0
c=9
while(a<=9):
    b = 0
    while(b <= c):
        print(b, end='')
        if (b == c):
            print('')
            c -= 1
        b += 1
    a+=1
