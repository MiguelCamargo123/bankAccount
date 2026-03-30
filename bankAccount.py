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
    def __init__(self):
        self.contas = []
        self.__carregar_json_banco()

    def __carregar_json_banco(self):
        try:
            with open('contas.json', 'r', encoding='utf-8') as f:
                dados = json.load(f)
                for d in dados:
                    conta = Conta(d['Nome do titular'], d['Senha do titular'])
                    conta._Conta__saldo = d['Saldo do titular']
                    conta.historico = d['Historico do titular']
                    self.contas.append(conta)
        except FileNotFoundError:
            self.contas = []

    def __salvar_json_banco(self):
        dados = []
        for conta in self.contas:
            dados.append(
                {
                    'Nome do titular': conta.titular,
                    'Senha do titular': conta.senha,
                    'Saldo do titular': conta._Conta.__saldo,
                    'Historico do titular': conta.historico,
                }
            )
        with open('contas.json', 'w', encoding='utf-8') as c:
            json.dump(dados, c, ensure_ascii=False, indent=4)

    def registrar_pessoa_banco(self, titular, senha):
        pessoa = Conta(titular, senha)
        self.contas.append(pessoa)
        self.__salvar_json_banco()

    def verificar_se_conta_certa(self, nome_titular, senha_digitada):
        for conta in self.contas:
            if conta.titular == nome_titular:
                if hashlib.sha256(senha_digitada.encode()).hexdigest() == conta.senha:
                    return True, conta
                else:
                    return False, None
        return False, None
