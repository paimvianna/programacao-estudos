#Entrada
h1=int(input('informe a hora de inicio:'))
m1=int(input('informe o minuto de inicio:'))
h2=int(input('informe a hora de termino:'))
m2=int(input('informe o minuto de termino:'))

#Processamento
if(h1==h2 and m1==m2):
    print('24:00')
else:
    if(h1<h2 and m1<=m2):
        hora=h2-h1
        minutos=m2-m1
        #print('{}:{}' .format (hora,minutos))
    else:
         tempo = ((24*60)-(h1*60)+m1 + (h2*60+m2))
         hora = tempo // 60
         minutos = tempo%60
    print('{:2}:{:2}'.format(hora, minutos))