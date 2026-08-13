#Entrada obs: versão 3 do exercico creio que convertendo pra mesma base sera necessario so 1 teste.
h1=int(input('informe a hora de inicio:'))
m1=int(input('informe o minuto de inicio:'))
h2=int(input('informe a hora de termino:'))
m2=int(input('informe o minuto de termino:'))

#Processamento
tempo= (h2*60+m2)-(h1*60+m1)
if(tempo<=0):
    tempo+=1440
    
th=tempo//60
tm=tempo%60

    
#Saída
print('{:02d}:{:02d}'.format(th,tm))
#hora=h2-h1
#minutos=m2-m1
#if(minutos<0):
#   minutos+=60
#  hora-=1
#if(hora<0):
#    hora+=24
#if(hora==0 and minutos==0):
#    hora+=24
#saída
#print('{:02d}:{:02d}'.format(hora,minutos))