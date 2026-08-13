#Entrada
km = float(input("Por favor informe a distância a ser percorrida: "))
auto = float(input("Por favor informe o consumo médio do veiculo: "))
preço = float(input("Por favor informe o valor do combustivel: "))

#Processamento
custo = (km/auto) * preço

#Saída
print (F"Ocusto total da viagem {custo:.2f}")