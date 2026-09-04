def fatorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fatorial(n-1)

numero = int(input(f'Informe o numero que deseja fatorar: '))
print(fatorial(numero))