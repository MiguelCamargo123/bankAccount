import json
import hashlib


class Conta:
    def __init__(self, titular, senha):
        self.titular = titular
        self.senha = hashlib.sha256(senha.encode()).hexdigest()
        self.historico = []
        self.__saldo = 0
        self.__carregar()

    def __carregar(self):
        try:
            with open('historico.json', 'r', encoding='utf-8') as f:
                self.historico = json.load(f)
        except FileNotFoundError:
            self.historico = []

    def __salvar(self):
        with open('historico.json', 'w', encoding='utf-8') as h:
            json.dump(self.historico, h, ensure_ascii=False, indent=4)

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.historico.append(
                {'Tipo': 'depósito', 'Valor': valor, 'Saldo Após': self.__saldo}
            )
        else:
            print('Digite um valor acima de zero')
        self.__salvar()

    def sacar(self, valor):
        if valor <= 0:
            print('Digite um valor maior que zero para poder sacar')
        elif valor >= self.__saldo:
            print('Digite um valor menor que seu saldo')
        else:
            self.__saldo -= valor
            print('Valor sacado com sucesso')
            self.historico.append(
                {'Tipo': 'saque', 'Valor': valor, 'Saldo Após': self.__saldo}
            )
        self.__salvar()

    def verSaldo(self):
        print(f'O seu saldo atual é de {self.__saldo}')

    def verHistorico(self):
        for transacao in self.historico:
            print(transacao)


class Banco:
    def __init__(self, pessoa):
        self.contas = []
        self.pessoa = pessoa
