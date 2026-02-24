class contaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
        self.historico = []

    def depositar(self):
        valorDepositar = int(input('Digite um valor: '))
        if valorDepositar > 0:
            self.__saldo += valorDepositar
            self.historico.append({
                'Tipo': 'depósito',
                'Valor': valorDepositar,
                'Saldo Após': self.__saldo
            })
        else:
            print('Digite um valor acima de zero')


    def sacar(self):
        valorSacar = int(input('Digite um valor para sacar: '))
        if valorSacar <= 0:
            print('Digite um valor maior que zero para poder sacar')
        elif valorSacar >= self.__saldo:
            print('Digite um valor menor que seu saldo')

        else:
            self.__saldo -= valorSacar
            print('Valor sacado com sucesso')
            self.historico.append({
                'Tipo': 'saque',
                'Valor': valorSacar,
                'Saldo Após': self.__saldo
            })


    def verSaldo(self):
        print(f'O seu saldo atual é de {self.__saldo}')

    def verHistorico(self):
        for transacao in self.historico:
            print(transacao)

titular = input('Digite seu nome: ')

conta = contaBancaria(titular, 0)
conta.depositar()
conta.sacar()
conta.verSaldo()