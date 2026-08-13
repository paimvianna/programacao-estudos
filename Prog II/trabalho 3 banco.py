'''trabalho 3, sistema bancario. Com metodos de classes e relações. '''
from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome,sobrenome,idade,cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.__cpf = cpf
        self.__contasbancarias = []

    @classmethod
    def receber_do_teclado(pessoa): #'pessoa' representa a propria classe Pessoa
        print(f'\n----Cadastro de Nova Pessoa ----\n')
        nome = str(input('Informe o nome: '))
        sobrenome = str(input('Informe o sobrenome: '))

        while True:
            try:
                idade = int(input('Digite a idade: '))
                if idade <= 0:
                    print(f'A idade deve ser um valor positivo.')
                    continue
                break
            except ValueError:
                print('Entrada invalida para a idade. Digite um numero inteiro.')

        while True:
            cpf_input = input('Informe o CPF(apenas números): ')
            if Pessoa.validar_cpf(cpf_input):
                break
            else:
                print('CPF invalido. Informe um CPF valido. Tente novamente!')
        return pessoa(nome,sobrenome,idade,cpf_input)

    '''def carrega_pessoa_txt(pessoa,linha):
        #Contruindo objeto pessoa a partir da linha do .txt
        linha'''


    def salva_dados_txt(self):
        #converto o objeto pessoa em linha no arquivo texto começando com a sua classe na frente.
        return f'Pessoa|{self.nome}|{self.sobrenome}|{self.idade}|{self.__cpf}'

    @staticmethod
    def validar_cpf(cpf_str):
        cpf_str = str(cpf_str).replace('.', '').replace('-', '')#Aqui recebo somente letras e numeros simbolos.

        if not isinstance(cpf_str, str) or len(cpf_str) != 11 or not cpf_str.isdigit(): #realizo pra ver o que tem na string e seu tamanho.
            print(f'Erro: CPF deve ter 11 dígitos numéricos.')
            return False
        else:
            cpf_inteiro = []
            for i in cpf_str:
                novo_cpf = int(i)
                cpf_inteiro.append(novo_cpf)
            novo_cpf = cpf_inteiro
            if len(set(novo_cpf)) == 1:  # aqui o set verifica que no conjunto ou seja lista cpf
                # quantos itens tem iguais criando um conjunto que se verifica o tamanho e
                # vejo se e igual a 1 que significa que todos os 11 elementos sao iguais
                # outra forma e usar um if comparando os conteudos dos endereços da lista.
                # if novo_cpf[0]==novo_cpf[1] and novo_cpf[1]==novo_cpf[2] and novo_cpf[2]==novo_cpf[3]
                # and novo_cpf[3] == novo_cpf[4] and novo_cpf[5]==novo_cpf[6] and novo_cpf[7]==novo_cpf[8] and novo_cpf[9]==novo_cpf[10]:
                print(f'Erro: Cpf não pode ter todos seus dígitos iguais é inválido.')
                return False

            #validação do primeiro digito verificador.
            soma_a = 0
            for i in range(0, 9, 1):
                soma_a += novo_cpf[i] * (10 - i)
                # print(i,'*',(10-i),'=', soma_a) usei para verificar
                # se estava ocorrendo a multiplicação corretamente
            resto_a = soma_a % 11
            digito_esperado_a = 11 - resto_a

            if (resto_a < 2) and (novo_cpf[9] == 0):
                digito_esperado_a = 0

            if (resto_a >= 2 and resto_a < 10) and (digito_esperado_a != novo_cpf[9]):
                print(f'Primeiro digito verificador {novo_cpf[9]} incorreto. Esperado: {digito_esperado_a}')
                return False

            #validação do segundo digito verificador.
            soma_b = 0
            for i in range(0, 10, 1):
                soma_b += novo_cpf[i] * (11 - i)
            resto_b = soma_b % 11
            digito_esperado_b = 11 - resto_b

            if (resto_b < 2) and (novo_cpf[10] == 0):
                digito_esperado_b = 0

            if (resto_b >= 2 and resto_b < 10) and (digito_esperado_b != novo_cpf[10]):
                print(f'Segundo digito verificador {novo_cpf[10]} incorreto. Esperado: {digito_esperado_b}')
                return False

            return True #, 'CPF válido!'

    @property #getter para o cpf
    def cpf(self):
        #rotorno o CPF formatado para exibição formatado esse e o getter,
        # através do return ele acessa os enderços da string self.__cpf que é privado
        # desta forma a princípio, sendo o meio pra acessar o cpf.
        return f'{self.__cpf[:3]}.{self.__cpf[3:6]}.{self.__cpf[6:9]}-{self.__cpf[9:]}'

    @cpf.setter
    def cpf(self,novo_cpf):
        #vou atribuir o que tem cpf_str após validação, a self__cpf.
        # Também vou colocar uma exceção se a validação falhar
        if not Pessoa.validar_cpf(novo_cpf):
            raise ValueError(f'Tentativa de atribuir um CPF inválida.')
        #Se der certo, limpa e armazena o CPF
        self.__cpf = str(novo_cpf).replace('.','').replace('-','')

    @property
    def contas_bancarias(self):
        return self.__contasbancarias

    def buscar_conta(self, numero_conta_buscar):
        #metodo para busca de contas
        for conta_objeto in self.contas_bancarias:
            if conta_objeto.numero_conta == numero_conta_buscar:
                return conta_objeto
        return None


    def adicionar_conta(self, conta):
        self.__contasbancarias.append(conta)

    def info(self):
       print(f'Nome: {self.nome} {self.sobrenome}')
       print(f'Idade: {self.idade}')
       print(f'CPF: {self.cpf}')# chama o getter formatado
       print(f'Contas  bancárias: {len(self.contas_bancarias)}')
       # Lista as contas em self.contasbancarias
       self.info_contas()
       '''
       if self.contas_bancarias:
           print(f'Detalhes das contas:')
           for conta in self.contas_bancarias:
               #tenho que criar o metodo __str__ ou info()
                print(f'- {conta.info()}')
       else:
           print(f'Não há contas associadas a esta pessoa.')
        '''
    def info_contas(self):
        print(f'contas de {self.nome} {self.sobrenome}')
        if not self.contas_bancarias:
            print(f'Não existe contas para este cliente.')
        else:
            for conta in self.contas_bancarias:
                print(f'- {conta.info()}')

class Banco:
    def __init__(self,nome,cnpj,numero_banco):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__numero_banco = numero_banco
        self.__contasbancaria_banco = []

    @classmethod
    def receber_do_teclado(banco):  # 'banco' representa a propria classe Banco
        print(f'\n----Cadastro de Novo Banco ----\n')
        nome = str(input('Informe o nome do Banco: '))
        while True:
            cnpj_input = input('Informe o CNPJ(apenas números): ')
            if Banco.validar_cnpj(cnpj_input):
                break
            else:
                print('CNPJ invalido. Informe um CNPJ valido. Tente novamente!')
                pass

        while True:
            try:
                numero_banco = int(input('Informe o numero do Banco: '))
                if numero_banco <= 0 and not isinstance(numero_banco,int):
                    print(f'O numero do banco deve ser um valor positivo, somente com dígitos numéricos.')
                    continue
                break
            except ValueError:
                print('Entrada invalida para o numero do banco. Digite um numero inteiro.')

        return banco(nome, cnpj_input, numero_banco)

    def salva_dados_txt(self):
        #converto o objeto pessoa em linha no arquivo texto começando com a sua classe na frente.
        return f'Banco|{self.__nome}|{self.__cnpj}|{self.__numero_banco}'

    @staticmethod
    def validar_cnpj(cnpj_str):
        cnpj_str = str(cnpj_str).replace('.','').replace('/','').replace('-','')

        if len(cnpj_str) != 14 and not cnpj_str.isdigit():
            print(f'Erro: O CNPJ deve conter 14 dígitos numéricos.')
            return False
        else:
            cnpj_inteiros = []
            for i in cnpj_str:
                cnpj_numero = int(i)
                cnpj_inteiros.append(cnpj_numero)
            if len(set(cnpj_inteiros)) == 1:
                print(f'Erro: O CNPJ não pode ter todos seus dígitos iguais é inválido.')
                return False

            lista_numeros_validadores_a = [5,4,3,2,9,8,7,6,5,4,3,2]
            soma_a = 0
            for i in range(0,12,1):
                soma_a += cnpj_inteiros[i] * lista_numeros_validadores_a[i]
            resto_a = soma_a % 11
            digito_esperado_a = 11 - resto_a
            if (resto_a < 2) and (cnpj_inteiros[12] == 0):
                digito_esperado_a = 0
            if (resto_a >= 2 and resto_a < 10) and (digito_esperado_a != cnpj_inteiros[12]):
                print(f'Primeiro digito verificador {cnpj_inteiros[12]} incorreto. Esperando {digito_esperado_a}.')
                return False

            lista_numeros_validadores_b = [6,5,4,3,2,9,8,7,6,5,4,3,2]
            soma_b = 0
            for i in range(0,13,1):
                soma_b += cnpj_inteiros[i] * lista_numeros_validadores_b[i]
            resto_b = soma_b % 11
            digito_esperado_b = 11 - resto_b
            if (resto_b < 2) and (cnpj_inteiros[13] == 0):
                digito_esperado_b = 0
            if (resto_a >= 2 and resto_b < 10) and (digito_esperado_b != cnpj_inteiros[13]):
                print(f'Segundo digito verificador {cnpj_inteiros[13]} incorreto. Esperando {digito_esperado_b}.')
                return False

            return True, #'CNPJ válido!'

    @property
    def nome(self):
        return f'{self.__nome}'

    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str) or len(novo_nome.strip()) == 0:
            raise ValueError('O nome do Banco não pode ser vazio.')
        self.__nome = novo_nome.strip()

    @property
    def cnpj(self):
        #Mesmo sistema que foi detalho em cpf o return vai nos exibir o CNJP formatado.
        return f'{self.__cnpj[:2]}.{self.__cnpj[2:5]}.{self.__cnpj[5:8]}/{self.__cnpj[8:12]}-{self.__cnpj[12:14]}'

    @cnpj.setter
    def cnpj(self,cnpj_inteiros):
        if not Banco.validar_cnpj(cnpj_inteiros):
            raise ValueError(f'Tentativa de atribuir um CNPJ inválida.')
        self.__cnpj = str(cnpj_inteiros).replace('.','').replace('/','').replace('-','')

    @property
    def numero_banco(self):
        return self.__numero_banco

    @numero_banco.setter
    def numero_banco(self,numero_banco):
        if not isinstance(numero_banco, int) and numero_banco <= 0:
            raise ValueError(f'O numero do banco deve ser um inteiro possitivo.')
        self.__numero_banco = numero_banco

    @property
    def contasbancaria_banco(self):
        return self.__contasbancaria_banco

    def adiciona_contasbancaria_banco(self, conta):
        self.__contasbancaria_banco.append(conta)

    def info_banco(self):
        print(f'----Informações do Banco:-----')
        print(f'Nome do banco: {self.nome}')
        print(f'CNPJ: {self.cnpj}')
        print(f'Número do Banco: {self.numero_banco}')
        print(f'Total de Contas: {len(self.contasbancaria_banco)}')
        if self.contasbancaria_banco:
            print(f'Detalhes das contas do banco {self.nome}:')
            for conta in self.contasbancaria_banco:
                print(f'-',{conta.info()})
            else:
                print(f'Não há contas cadastradas neste banco.')

        '''ver depois de criar class ContaBancaria. mas a principio terei que @classmethod'''


    def criar_conta(self,titular:'Pessoa', tipo_conta: str):
        print(f'\n ----Criando Conta no Banco{self.nome} para {titular.nome}')

        numero_conta = None
        while True:
            try:
                numero_conta = int(input(f'Informe o numero da conta: '))
                if numero_conta <= 0:
                    print(f'O numero da conta deve ser um numero positivo.')
                    continue
                break
            except ValueError:
                print(f'Entrada invalida para numero de conta. Digite um numero válido.')

        saldo_inicial = None
        while True:
            try:
                saldo_inicial = float(input(f'Informe o saldo inicial da conta: R$ '))
                if saldo_inicial < 0:
                    print(f'O saldo inicial não pode ser negativo.')
                    continue
                break
            except ValueError:
                print(f'Entrada inválida para o saldo inicial. Digite um número.')

        senha = None
        while True:
            senha = input(f'Crie uma senha para a conta (mínimo 4 caracteres): ')
            if len(senha) < 4:
                print(f'A senha deve ter no mínimo 4 dígitos.')
                continue
            break

        nova_conta = None
        if tipo_conta.lower() == 'cc':
            taxas_mensais = None
            while True:
                try:
                    taxas_mensais = float(
                        input(f'Informe as taxas mensais da conta corrente (padrão 15.00): R$ ') or '15.00')
                    if taxas_mensais < 0:
                        print(f'As taxas mensais não podem ser negativas.')
                        continue
                    break
                except ValueError:
                    print(f'Entrada inválida para taxas mensais. Digite um número.')
            nova_conta = ContaCorrente(titular, self, numero_conta, saldo_inicial, senha, taxas_mensais)

        elif tipo_conta.lower() == 'cp':
            rendimento_mensal = None
            while True:
                try:
                    rendimento_mensal = float(
                        input('Informe o rendimento mensal (ex: 0.005 para 0.5%) (padrão 0.005): ') or '0.005')
                    if rendimento_mensal < 0:
                        print('O rendimento mensal não pode ser negativo.')
                        continue
                    break
                except ValueError:
                    print('Entrada inválida para o rendimento mensal. Digite um número.')
            nova_conta = ContaPoupanca(titular, self, numero_conta, saldo_inicial, senha, rendimento_mensal)

        else:
            print("Tipo de conta inválido. Use 'cc' ou 'cp'.")
            return None  # Retorna None se o tipo for inválido

        if nova_conta:
            self.adiciona_contasbancaria_banco(nova_conta)#adiciona a conta o a lista de contas do banco
            titular.adicionar_conta(nova_conta)#adicona a conta lista de pessoa que e igual a titular
            print(f'Conta {nova_conta.numero_conta} {tipo_conta.upper()} criada com sucesso no banco {self.nome} para o {titular.nome}!')
        return nova_conta

class Conta_Bancaria(ABC):
    def __init__(self, titular:'Pessoa',banco:'Banco',numero_conta:int, saldo:float, senha:str):
        if not isinstance(titular,Pessoa):
            raise TypeError (f'O titular deve ser uma instância da classe Pessoa.')
        if not isinstance(banco, Banco):
            raise TypeError(f'O banco deve ser uma instancia da classe Banco.')
        if not isinstance(numero_conta, int) or numero_conta <= 0:
            raise TypeError (f'numero da conta deve ser um inteiro positivo.')
        if not isinstance(saldo, (int,float) or saldo < 0):
            raise TypeError (f'O saldo inicial não pode ser negativo e deve ser numérico.')
        if not isinstance(senha,str) or len(senha) < 4:
            raise TypeError (f'A senha deve ser uma string e ter menos de 4 caracteres.')

        self._titular = titular
        self._banco = banco
        self._numero_conta = int(numero_conta)
        self._saldo = saldo
        self._senha = senha

    @property
    def titular(self):
        return self._titular

    @property
    def banco(self):
        return self._banco

    @property
    def numero_conta(self):
        return self._numero_conta

    @numero_conta.setter
    def numero_conta(self,novo_numero):
        if not isinstance(novo_numero,int) or novo_numero <= 0:
            raise ValueError(f'O numero da conta deve ser um inteiro postivo.')
        self._numero_conta = novo_numero

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,novo_saldo):
        if novo_saldo < 0:
            raise ValueError(f'Saldo nao pode ser negativo.')
        self._saldo = novo_saldo

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        if not isinstance(nova_senha, str) or len(nova_senha) < 4:
            raise ValueError(f'A senha deve ser uma string e ter no minimo 4 caracteres.')
        self._senha = nova_senha

    @abstractmethod
    def deposito(self, valor: float):
        pass

    @abstractmethod
    def saque(self, valor: float):
        pass

    @abstractmethod
    def verifica_senha(self,senha_digitada: str):
        pass

    @abstractmethod
    def info(self):
        pass

class ContaCorrente(Conta_Bancaria):
    def __init__(self,titular: 'Pessoa', banco: 'Banco', numero_conta, saldo_inicial, senha: str ,taxas_mensais = 15.00):
        #taxas_mensais = 15.00
        super().__init__(titular,banco,numero_conta,saldo_inicial,senha)
        if not isinstance(taxas_mensais, (int,float)) or taxas_mensais < 0:
            raise ValueError(f'As taxas mensais devem ser um valor positivo.')
        self._taxas_mensais = taxas_mensais

    @property
    def taxas_mensais(self):
        return self._taxas_mensais
    @taxas_mensais.setter
    def taxas_mensais(self, nova_taxa:float):
        if not isinstance(nova_taxa,(int,float)) or nova_taxa < 0:
            raise ValueError(f'As taxas mensais devem ser um valor positivo.')
        self._taxas_mensais = nova_taxa

    def deposito(self,valor):
        if not isinstance(valor,(int,float)) or valor <= 0:
            print(f'Valor de deposito invalido. Informe um valor positivo.')
            return
        self.saldo += valor
        print(f'O valor depositado foi de R$ {valor:.2f}, com sucesso.'
              f'\nNovo saldo de {self.saldo:.2f}')

    def saque(self,valor):
        if not isinstance(valor,(int,float)) or valor <= 0:
            print(f'O valor a ser sacado tem que ser positivo.')
            return

        if self.saldo >= valor:
            self.saldo -= valor
            print(f'O saque de R${valor:.2f} foi atutorizado.\n'
                  f'Seu saldo após operação e de {self.saldo:.2f}.')
        else:
            print(f'Saque não autorizado: Saldo R${self.saldo:.2f} insuficiente para sacar R${valor:.2f}')

    def verifica_senha(self,senha_digitada: str):
        return senha_digitada == self._senha

    def info(self):
        print(f"\n--- Informações da Conta Corrente ---")
        print(f"Banco: {self.banco.nome}")
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Titular: {self.titular.nome} {self.titular.sobrenome} (CPF: {self.titular.cpf})")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print(f"Taxas Mensais: R$ {self.taxas_mensais:.2f}")
        print(f"------------------------------------")

    def novo_mes(self):
        if self.saldo >= self.taxas_mensais:
            self.saldo -= self.taxas_mensais
            print(f'Taxa mensal de R${self.taxas_mensais:.2f} cobrado da canta {self.numero_conta}.')
        else:
            print(f'Aviso: saldo insuficiente para cobrar a taxa mensal de R${self.taxas_mensais:.2f} da conta {self.numero_conta}.')
            print(f'Saldo atual: R$ {self.saldo:.2f}')
        print(f'Novo saldo após o mês: R$ {self.saldo:.2f}')

class ContaPoupanca(Conta_Bancaria):
    SAQUES_MAX_POR_MES = 3

    def __init__(self, titular: 'Pessoa', banco: 'Banco', numero_conta: int, saldo_inicial: float, senha: str,
                 rendimento_mensal: float = 0.005):  # 0.5%
        # Chama o construtor da classe base (Conta_Bancaria)
        super().__init__(titular, banco, numero_conta, saldo_inicial, senha)
        if not isinstance(rendimento_mensal, (int, float)) or rendimento_mensal < 0:
            raise ValueError("O rendimento mensal deve ser um valor numérico positivo ou zero.")
        self._rendimento_mensal = rendimento_mensal  # Atributo específico da Conta Poupança
        self._saques_restantes_mes = self.SAQUES_MAX_POR_MES  # Reseta saques no início

    @property
    def rendimento_mensal(self) -> float:
        return self._rendimento_mensal

    @rendimento_mensal.setter
    def rendimento_mensal(self, novo_rendimento: float):
        if not isinstance(novo_rendimento, (int, float)) or novo_rendimento < 0:
            raise ValueError("O rendimento mensal deve ser um valor numérico positivo ou zero.")
        self._rendimento_mensal = novo_rendimento

    @property
    def saques_restantes_mes(self) -> int:
        return self._saques_restantes_mes

    def deposito(self, valor: float):
        if not isinstance(valor, (int, float)) or valor <= 0:
            print("Valor de depósito inválido. Informe um valor positivo.")
            return

        self.saldo += valor  # Usa o setter de saldo da classe base
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        print(f"Novo saldo: R$ {self.saldo:.2f}")

    def saque(self, valor: float):
        if not isinstance(valor, (int, float)) or valor <= 0:
            print("Valor de saque inválido. Informe um valor positivo.")
            return

        if self.saques_restantes_mes <= 0:
            print(f"Saque não autorizado: Limite de {self.SAQUES_MAX_POR_MES} saques para o mês atingido na conta {self.numero_conta}.")
            return

        if self.saldo >= valor:
            self.saldo -= valor  # Usa o setter de saldo da classe base
            self._saques_restantes_mes -= 1  # Decrementa o contador
            print(f"Saque de R$ {valor:.2f} autorizado.")
            print(f"Saques restantes no mês: {self.saques_restantes_mes}")
            print(f"Novo saldo: R$ {self.saldo:.2f}")
        else:
            print(f"Saque não autorizado: Saldo R$ {self.saldo:.2f} insuficiente para R$ {valor:.2f}.")

    def verifica_senha(self, senha_digitada: str) -> bool:
        return senha_digitada == self._senha

    def info(self):
        print(f"\n--- Informações da Conta Poupança ---")
        print(f"Banco: {self.banco.nome}")
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Titular: {self.titular.nome} {self.titular.sobrenome} (CPF: {self.titular.cpf})")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print(f"Rendimento Mensal: {self.rendimento_mensal * 100:.2f}%")
        print(f"Saques Restantes no Mês: {self.saques_restantes_mes}")
        print(f"------------------------------------")

    # --- Método Específico da ContaPoupanca ---
    def novo_mes(self):
        """
        Simula a passagem de um mês na conta poupança, aplicando o rendimento
        e resetando a contagem de saques.
        """
        rendimento_aplicado = self.saldo * self.rendimento_mensal
        self.saldo += rendimento_aplicado
        self._saques_restantes_mes = self.SAQUES_MAX_POR_MES  # Reseta os saques
        print(f"Mês virado para a conta poupança {self.numero_conta}.")
        print(f"Rendimento de R$ {rendimento_aplicado:.2f} aplicado.")
        print(f"Saques resetados para {self.SAQUES_MAX_POR_MES}.")
        print(f"Novo saldo após o mês: R$ {self.saldo:.2f}")



def salva_dados_bancarios(pessoas, bancos):
    lista_que_vai_gravar = []
    lista_que_vai_gravar.append("[Banco]")
    for banco in bancos:
        lista_que_vai_gravar.append(banco.salva_dados_txt())

    lista_que_vai_gravar.append("[Pessoas]")
    for pessoa in pessoas:
        lista_que_vai_gravar.append(pessoa.salva_dados_txt())

    lista_que_vai_gravar.append("[Contas]")
    for pessoa in pessoas:
        for conta in pessoa.contas_bancarias:
            lista_que_vai_gravar.append(conta.salva_dados_txt())

    try:
        bancos_dados = open('dados_bancarios.txt','w')
        for dados in lista_que_vai_gravar:
            bancos_dados.write(dados+'\n')
    except IOError as e:
        print(f'Erro ao salvar dados no arquivo {banco_dados}: {e}')

def menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- Sistema Bancário ---")
    print("1. Cadastrar Nova Pessoa")
    print("2. Cadastrar Novo Banco")
    print("3. Criar Nova Conta")
    print("4. Realizar Operação em Conta Existente")
    print("5. Exibir Informações (Pessoa/Banco/Conta)")
    print("6. Simular Passagem de Mês (Aplicar taxas/rendimentos)")
    print("7. Sair")
    print("------------------------")

def encontrar_pessoa_por_cpf(cpf_str: str, lista_pessoas: list) -> Pessoa:
    """Busca uma pessoa na lista pelo CPF (formatado ou não)."""
    for pessoa in lista_pessoas:
        # Acessa o atributo privado diretamente para comparação sem formatação
        if pessoa._Pessoa__cpf == cpf_str.replace('.', '').replace('-', ''):
            return pessoa
    return None

def encontrar_banco_por_numero(numero: int, lista_bancos: list) -> Banco:
    """Busca um banco na lista pelo número do banco."""
    for banco in lista_bancos:
        if banco.numero_banco == numero:
            return banco
    return None

def encontrar_conta_por_numero(numero_conta: int, pessoa: Pessoa) -> Conta_Bancaria:

    return pessoa.buscar_conta(numero_conta)

def main():
    """Função principal que executa o sistema bancário."""
    pessoas = []
    bancos = []

    while True:
        menu()
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número.")
            continue

        if opcao == 1:  # Cadastrar Nova Pessoa
            nova_pessoa = Pessoa.receber_do_teclado()
            pessoas.append(nova_pessoa)
            print(f"Pessoa '{nova_pessoa.nome} {nova_pessoa.sobrenome}' cadastrada com sucesso!")

        elif opcao == 2:  # Cadastrar Novo Banco
            novo_banco = Banco.receber_do_teclado()
            bancos.append(novo_banco)
            print(f"Banco '{novo_banco.nome}' cadastrado com sucesso!")

        elif opcao == 3:  # Criar Nova Conta (agora via método do Banco)
            if not pessoas:
                print("Nenhuma pessoa cadastrada. Cadastre uma pessoa primeiro.")
                continue
            if not bancos:
                print("Nenhum banco cadastrado. Cadastre um banco primeiro.")
                continue

            print("\n--- Criar Nova Conta ---")
            cpf_pessoa = input("Informe o CPF do titular da conta (apenas números): ").replace('.', '').replace('-',
                                                                                                                '')
            pessoa_existente = encontrar_pessoa_por_cpf(cpf_pessoa, pessoas)

            if not pessoa_existente:
                print("Pessoa não encontrada. Verifique o CPF.")
                continue

            num_banco_str = input("Informe o número do Banco onde a conta será criada: ")
            try:
                num_banco = int(num_banco_str)
            except ValueError:
                print("Número do banco inválido.")
                continue
            banco_existente = encontrar_banco_por_numero(num_banco, bancos)

            if not banco_existente:
                print("Banco não encontrado. Verifique o número do banco.")
                continue

            tipo_conta = input("Tipo de conta (cc para Corrente, cp para Poupança): ").lower()

            # Chamada ao método criar_conta do objeto Banco
            # Este método agora coleta TODOS os dados da conta e a instancia
            banco_existente.criar_conta(pessoa_existente, tipo_conta)

        elif opcao == 4:  # Realizar Operação em Conta Existente
            if not pessoas:
                print("Nenhuma pessoa/conta cadastrada.")
                continue

            cpf_pessoa = input("Informe o CPF do titular da conta (apenas números): ").replace('.', '').replace('-',
                                                                                                                '')
            pessoa_existente = encontrar_pessoa_por_cpf(cpf_pessoa, pessoas)

            if not pessoa_existente:
                print("Pessoa não encontrada.")
                continue

            if not pessoa_existente.contas_bancarias:
                print("Esta pessoa não possui contas cadastradas.")
                continue

            num_conta_str = input("Informe o número da conta para a operação: ")
            try:
                num_conta = int(num_conta_str)
            except ValueError:
                print("Número da conta inválido.")
                continue

            conta_escolhida = encontrar_conta_por_numero(num_conta, pessoa_existente)

            if not conta_escolhida:
                print("Conta não encontrada para esta pessoa.")
                continue

            senha_digitada = input("Informe a senha da conta: ")
            if not conta_escolhida.verifica_senha(senha_digitada):
                print("Senha incorreta. Operação não autorizada.")
                continue

            print("\n--- Operações da Conta ---")
            print("a. Depositar")
            print("b. Sacar")
            print("c. Ver Saldo e Detalhes")

            op_conta = input("Escolha a operação (a/b/c): ").lower()

            if op_conta == 'a':
                try:
                    valor = float(input("Informe o valor para depósito: R$ "))
                    conta_escolhida.deposito(valor)
                except ValueError:
                    print("Valor inválido para depósito.")
            elif op_conta == 'b':
                try:
                    valor = float(input("Informe o valor para saque: R$ "))
                    conta_escolhida.saque(valor)
                except ValueError:
                    print("Valor inválido para saque.")
            elif op_conta == 'c':
                conta_escolhida.info()
            else:
                print("Opção de operação inválida.")

        elif opcao == 5:  # Exibir Informações
            print("\n--- Exibir Informações ---")
            print("1. Informações de uma Pessoa")
            print("2. Informações de um Banco")
            print("3. Informações de uma Conta Específica")

            info_opcao = input("Escolha o que deseja exibir (1/2/3): ")

            if info_opcao == '1':
                if not pessoas:
                    print("Nenhuma pessoa cadastrada.")
                    continue
                cpf_pessoa = input("Informe o CPF da pessoa (apenas números): ").replace('.', '').replace('-', '')
                pessoa_existente = encontrar_pessoa_por_cpf(cpf_pessoa, pessoas)
                if pessoa_existente:
                    pessoa_existente.info()
                else:
                    print("Pessoa não encontrada.")
            elif info_opcao == '2':
                if not bancos:
                    print("Nenhum banco cadastrado.")
                    continue
                num_banco_str = input("Informe o número do Banco: ")
                try:
                    num_banco = int(num_banco_str)
                except ValueError:
                    print("Número do banco inválido.")
                    continue
                banco_existente = encontrar_banco_por_numero(num_banco, bancos)
                if banco_existente:
                    banco_existente.info_banco()
                else:
                    print("Banco não encontrado.")
            elif info_opcao == '3':
                if not pessoas:
                    print("Nenhuma pessoa cadastrada para buscar contas.")
                    continue
                cpf_pessoa = input("Informe o CPF do titular da conta (apenas números): ").replace('.', '').replace(
                    '-', '')
                pessoa_existente = encontrar_pessoa_por_cpf(cpf_pessoa, pessoas)
                if not pessoa_existente:
                    print("Pessoa não encontrada.")
                    continue
                if not pessoa_existente.contas_bancarias:
                    print("Esta pessoa não possui contas cadastradas.")
                    continue
                num_conta_str = input("Informe o número da conta para exibir informações: ")
                try:
                    num_conta = int(num_conta_str)
                except ValueError:
                    print("Número da conta inválido.")
                    continue
                conta_escolhida = encontrar_conta_por_numero(num_conta, pessoa_existente)
                if conta_escolhida:
                    conta_escolhida.info()
                else:
                    print("Conta não encontrada para esta pessoa.")
            else:
                print("Opção de exibição inválida.")

        elif opcao == 6:  # Simular Passagem de Mês
            print("\n--- Simulação de Novo Mês ---")
            contas_processadas = 0
            for pessoa in pessoas:
                for conta in pessoa.contas_bancarias:
                    conta.novo_mes()
                    contas_processadas += 1
            if contas_processadas > 0:
                print(f"\nSimulação de mês concluída para {contas_processadas} contas.")
            else:
                print("Nenhuma conta para processar.")

        elif opcao == 7:  # Sair
            print("Salvando dados antes de sair...")
            salva_dados_bancarios(pessoas, bancos)
            print("Dados salvos com sucesso!")
            print("Saindo do Sistema Bancário. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 7.")

# Executa o programa principal
if __name__ == "__main__":
    main()