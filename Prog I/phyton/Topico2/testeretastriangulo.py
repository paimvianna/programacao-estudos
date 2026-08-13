#Entrada
retaA = int(input('Valor da reta A: '))
retaB = int(input('Valor da reta B: '))
retaC = int(input('Valor da reta C: '))

#processamento
#teste=0
#if(retaA!=0 and retaB!=0 and retaC!=0):
#    if(retaA+retaB>retaC):
#        teste=teste+1
        #print('teste sim')
#    else:
#        print('não 2')
        
#    if(retaB+retaC>retaA):
#        #print('teste sim')
#        teste=teste+1
#    else:
#        print('nao 3')
#    if(retaA+retaC>retaB):
        #v=+1
#        print('sim')
#    else:
#       print('não 4')
#else:
#    print('não 1')

#Processamento
if(retaA!=0 and retaB!=0 and retaC!=0):
    if(retaA+retaB>retaC and retaB+retaC>retaA and retaA+retaC>retaB):
        print('sim')
    else:
        print('não') # faltou o bendito do ~ na letra a
else:
    print('não')