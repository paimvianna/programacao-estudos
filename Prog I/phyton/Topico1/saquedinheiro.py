#Entrada
valor = int(input("Por favor informe o valor que desja: "))

#Processamento; peguei orirnetações do cap. estruturas de repetição a partir pag. 84 e outro problema foi a indentação dos while, tive que fazer aospoucos pra ver o que estava errado.

cont100 = 0
while valor >= 100: # Faltou o bendito ':'
    valor -= 100
    cont100 += 1
else: 
    print (cont100," de 100")
    cont20=0
    while valor >= 20:  # Faltou o bendito ':'
        valor -= 20
        cont20 += 1
    else:
        print (cont20," de 20")
        cont5=0
        while valor >= 5:  # Faltou o bendito ':'
             valor -= 5
             cont5 += 1
        else:
            print (cont5," de 5")
            cont1=0
            while valor >= 1:   # Faltou o bendito ':'
                  valor -= 1
                  cont1 += 1
            else:
                print (cont1," de 1")


#Saída nao consegui fazer com que funciona com os prints junto.
#print (cont100," de 100")
#print (cont20," de 20")
#print (cont5," de 5")
#print (cont1," de 1")