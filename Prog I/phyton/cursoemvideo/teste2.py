# Entrada
v = float(input('favor informe o valor a ser tributado: '))

# Processamento
if(v > 2000.00):
#    m = (v - 2000) * .2
#    m = m + 1000 * .1
#    print(m)
     print('{:.2f}'.format((((v-2000)*.2)+1000*.1)+v))
else:
    if(v>1000.00):
       print('{:.2f}'.format(((v-1000) * .1)+v))
#      m = (v - 1000) * .1
#      print(m)
#      print('{:.2f}, {:.2f}'.format((v), (v*1.2)))
    else:
        print('{:.2f}'.format((v+0))