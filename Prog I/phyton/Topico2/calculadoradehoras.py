#Entrada
h1=int(input('informe a hora de inicio:'))
h2=int(input('informe a hora de termino:'))

#Processamento
#if(h1==h2): OBS: a linhas comentadas abaixo não alteram sao superfulas.
#   print('24')
#else:
if(h1<h2):
        hora=h2-h1
        #print(hora)
else:
        hora= 24-h1+h2

print('{:02d}'.format(hora))