# Entrada
passageiro = int(input('Porfavor informe quantos elementos tem no grupo com o motorista: '))
van=0
carro=0
carro1=0
# Processamento
if (passageiro <= 66):
        if(passageiro>=9):
            van = passageiro // 9
            if (van > 4):
                 van = 4
            carro1 = (passageiro - (van * 9)) // 5 # não sei pq com o numero 14 nao funciona
            if (((passageiro - van * 9) % 5) != 0):
                carro1 += 1
            print('{:0d}-{0d}'.format(van,carro1))


        if (passageiro <= 30):
            carro = passageiro // 5
            carro1 = passageiro % 5
            if (carro1 != 0):
                carro += 1
            print('0-{:0d}'.format(carro))

        if (passageiro <= 36):
            van = passageiro // 9
            van1 = passageiro % 9
            if (van1 != 0):
                van += 1
            print('{:0d}-0'.format(van))

else:
    print('-')