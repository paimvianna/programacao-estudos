#Entrada 
ordem1 = int(input(' '))
ordem2 = int(input(' '))
ordem3 = int(input(' '))


if(ordem1 <= ordem2 <= ordem3):
    print(ordem1, ordem2, ordem3)
else:
    if(ordem1<=ordem3<=ordem2):
        print(ordem1, ordem3, ordem2)
    else:
        if(ordem2<=ordem1<=ordem3):
            print(ordem2, ordem1, ordem3)
        else:
            if(ordem2<=ordem3<=ordem1):
                print(ordem2, ordem3, ordem1)
            else:
                if(ordem3<=ordem1<=ordem2):
                    print(ordem3, ordem1, ordem2)
                else:
                    print(ordem3, ordem2, ordem1)
