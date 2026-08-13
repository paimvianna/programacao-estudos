# Entrada
v = float(input('favor informe o valor a ser tributado: '))

# Processamento
if(v > 5000.00):
    print('{:.2f}'.format(((v-5000)*.5)+1000*.4+1000*.3+1000*.2+1000*.1))
else:
     if(5000.00>v>4000.00):
        print('{:.2f}'.format(((v-4000)*.4)+1000*.3+1000*.2+1000*.1))

     else:
         if(4000.00>v>3000.00):
            print('{:.2f}'.format(((v-3000)*.3)+1000*.2+1000*.1))
         else:
             if(3000.00>v>2000.00): 
                print('{:.2f}'.format((((v-2000)*.2)+1000*.1)))
             else: 
                 if(2000.00>v>1000.00):
                    print(' {:.2f}'.format((v-1000)*.1))
                 else:
                    print(' {:.2f}'.format(0))