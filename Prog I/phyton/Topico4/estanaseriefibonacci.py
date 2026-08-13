#entrada
n = int(input('Informe um numero inteiro positivo: '))
pri = 0
seg = 1
ter = 0
#print(pri)
while pri < n:
    #print (pri)
    ter = pri + seg
    pri = seg
    seg = ter
#print(pri)
if pri == n:
    print ('sim')
else:
    print('não')