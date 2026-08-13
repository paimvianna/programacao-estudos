# Entrada
v = float(input('favor informe o valor a ser tributado: '))

# Processamento
if(v > 5000.00):

     print('{:.2f}, {:.2f}'.format((v), ((((v-5000)*.5)+4000*4+3000*.3+2000*.2+1000*.1)+v)))
else:
    if(v>4000.00):
        print('{:.2f}, {:.2f}'.format((v), ((((v-4000)*.4)+3000*.3+2000*.2+1000*.1)+v)))
    else:
        if(v>3000):
            print('{:.2f}, {:.2f}'.format((v), ((((v-3000)*.3)+2000*.2+1000*.1)+v)))
        else:
            if(v>2000):
                print('{:.2f}, {:.2f}'.format((v), ((((v-2000)*.2)+1000*.1)+v)))
            else:
                if(v>1000):
                    print('{:.2f}, {:.2f}'.format((v), ((v-1000)*.1)+v))
                else:
                    print('{:.2f}, {:.2f}'.format((v), (0)))