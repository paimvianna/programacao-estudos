#Entrada
dia=int(input('Por favor, informe o dia: '))
mes=int(input('Por favor, informe o mes: '))

#Processamento
if(28>=dia>0 and mes==2):
    print('sim')
else:
    if(31>=dia>0 and 12>=mes>0):
        if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
            print('sim')
        else:
            if(30>=dia>0 and 12>=mes>0):
                if(mes==4 or mes==6 or mes==9 or mes==11):
                    print('sim')
                else:
                    print('não')
            else:
                print('não')
    else:
        print('não')
