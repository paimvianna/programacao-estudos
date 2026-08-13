#entrada
'''
rota = int(input('informe a rota do onibus ou digite 0 para encerrar:'))
rotas = []
viagens = []
passageiros = []
while rota != 0:
    print(passageiros)
   passageiro = int(input ('informe a quantidade de passageiros: '))

    if (rota in rotas):
        a= rotas.index(rota)
        #print('b',a)
        #print('c', passageiros[a])
        viagens[a] += 1
        passageiros[a] += passageiro
    else:
        rotas.append(rota)
        passageiros.append(passageiro)
        viagens.append(1)
    rota = int(input('informe a rota do onibus ou digite 0 para encerrar:'))
b=len(rotas)
for i in range (b):
    print(f'{rotas[i]} {viagens[i]} {passageiros[i]//viagens[i]:.1f}')
'''
rota = int(input('informe a rota do onibus ou digite 0 para encerrar:'))
rotas = []
viagens = []
passageiros = []
while rota != 0:
    passageiro = int(input('informe a quantidade de passageiros: '))
    e = 0
    for i in range (len(rotas)):
        if(rotas[i]==rota):
            viagens[i] += 1
            passageiros[i] += passageiro
            e+=1
            print(viagens,)
            print('a',passageiros)
            print(rotas)
    if e==0:
        rotas.append(rota)
        passageiros.append(passageiro)
        viagens.append(1)
        print(viagens)
        print('b', passageiros)
        print(rotas)
    rota = int(input('informe a rota do onibus ou digite 0 para encerrar:'))
#print(viagens)
#print(passageiros)
#print(rotas)
b=len(rotas)
for i in range (b):
    print(f'{rotas[i]} {viagens[i]} {passageiros[i]//viagens[i]:.1f}')