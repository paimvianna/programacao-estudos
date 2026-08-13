#Entrada
tempo = input("Insira o horario em segundos: ")
temperatura = float(input("Insira a temperatura: "))

#Processamento
segundos = tempo % 60
min = int(tempo / 60)
hora = min // 60

if min >= 60:
    min = min % 60

#print(F"Horário: {hora:2}:{min:2}:{segundos:2})
print ("Horário: ",hora,":",min,":",segundos)
print("Temperatura : ",temperatura,"graus") 