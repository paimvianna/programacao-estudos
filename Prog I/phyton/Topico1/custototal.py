#Entrada
autu= float(input("Por favor informe a altura da parede: "))
larg = float(input("Por favor informe a largura da parede: "))
preço = float(input("Por favor informe o valor do litro da tinta: "))
cobertura = 1.75 #OBS nao tinha observador que usei virgula e tava dando erro.
#Processamento
custo = ((autu * larg)/cobertura) * preço

#Saída
print (F"Ocusto total da pintura {custo:.2f}")
#OBS Reaproveitando codigo do custo de viagem.