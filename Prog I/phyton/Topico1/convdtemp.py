#Entrada
h = int(input("Por favor informe as horas que marca no relogio neste momento: "))
m = int(input("Por favor informe os minutos que marca no relogio neste momento: "))
s = int(input("Por favor informe os segundos que marca no relogio neste momento: "))

#Processamento
totalseg = (h * 3600) + (m * 60) + s

#Saída
print("O valor total em segundos é: ",totalseg)