class Animal:
    nr_animais = 0
    Filo = ''
    NomeComum = ''

    def __init__(self, Filo, NomeComum):
        self.Filo = Filo
        self.NomeComum = NomeComum
        Animal.nr_animais = Animal.nr_animais + 1


print("Começo do programa")

an1 = Animal('Chordata', 'Lobos-cinzento')
#an1.Classe = 'Mammalia'
#an1.NomeCientifico = 'Canis Lupus'
#an1.Peso = 31.7

an2 = Animal('Chordata', 'Cavalo')
'''
an2.Classe = 'Mammalia'
an2.NomeCientifico = 'Ursidea'
an2.Peso = 300
'''

print('==== ' + an1.NomeComum)
print('Filo:' + an1.Filo)
'''print('Classe:' + an1.Classe)
print('Nome científico: ' + an1.NomeCientifico)
print('Peso: ' + str(an1.Peso) + 'kg')'''

print('==== ' + an2.NomeComum)
print('Filo:' + an2.Filo)
'''print('Classe:' + an2.Classe)
print('Nome científico: ' + an2.NomeCientifico)
print('Peso: ' + str(an2.Peso) + 'kg')'''

print('Quantidade de animais:'+str(Animal.nr_animais)



