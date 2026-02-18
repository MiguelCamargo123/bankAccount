class contaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self):
        valorDepositar = int(input('Digite um valor: '))
        if valorDepositar > 0:
            self.__saldo += valorDepositar
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

titular = input('Digite seu nome: ')

conta = contaBancaria(titular, 0)
conta.depositar()
conta.sacar()