class contaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.historico.append({
                'Tipo': 'depósito',
                'Valor': valor,
                'Saldo Após': self.__saldo
            })
        else:
            print('Digite um valor acima de zero')


    def sacar(self, valor):
        if valor <= 0:
            print('Digite um valor maior que zero para poder sacar')
        elif valor >= self.__saldo:
            print('Digite um valor menor que seu saldo')

        else:
            self.__saldo -= valor
            print('Valor sacado com sucesso')
            self.historico.append({
                'Tipo': 'saque',
                'Valor': valor,
                'Saldo Após': self.__saldo
            })


    def verSaldo(self):
        print(f'O seu saldo atual é de {self.__saldo}')

    def verHistorico(self):
        for transacao in self.historico:
            print(transacao)

titular = input('Digite seu nome: ')

conta = contaBancaria(titular, 0)

def main():
    while True:
        pergunta = input(f'Ola {conta.titular}, voce deseja [S]acar, [D]epositar, dar uma olhada no [H]istórico de transações ou [V]seu saldo?').upper()

        if pergunta == 'S':
            try:
                valorSacar = int(input('Digite um valor para sacar: '))
                conta.sacar(valorSacar)
            except ValueError:
                print('Digite um número não um texto')

        elif pergunta == 'D':
            try:
                valorDeposito = int(input('Digite um valor para depositar: '))
                conta.depositar(valorDeposito)
            except ValueError:
                print('Digite um número não um texto')

        elif pergunta == 'H':
            conta.verHistorico()

        elif pergunta == 'V':
            conta.verSaldo()

        else:
            print('Digite uma das letras dentro das chaves para fazer uma ação')

        perguntaSair = input('Você deseja sair de dentro de nosso sistema? (S/N) ').upper()

        if perguntaSair == 'S':
            print('Você saiu do nosso sistema')
            break

if __name__ == '__main__':
    main()