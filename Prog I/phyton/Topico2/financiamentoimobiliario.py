#Entrada
vimovel=float(input('Por favor informe o valor do imovel a ser finaciado: '))
vrenda=float(input('Por favor informe a renda do comprador: '))
periodo=int(input('Por favor informe o tempo do financiamento: '))

#Processamento
trintaporcento=vrenda*.3
vlrparcela=vimovel/(periodo*12)
#print(trintaporcento)
#print(vlrparcela)
if(vlrparcela<=trintaporcento):
    print('{:.2f}'.format(vlrparcela))
else:
    print('Recusado')
#Saída
