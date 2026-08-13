#Entrada
n1 = float(input("Por favor informe o valor de N1: "))
p1 = float(input("Por favor informe o peso de N1: "))
n2 = float(input("Por favor informe o valor de N2: "))
p2 = float(input("Por favor informe o peso de N2: "))
n3 = float(input("Por favor informe o valor de N3: "))
p3 = float(input("Por favor informe o peso de N3: "))

#Processamento
nota = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3)

#Saída
print (F"Nota final {nota:.2f}")
#Não entendi pq no ultimo exemplo do exercicio deu 7.06 em vez de 7.07