import json
import hashlib
from typing import Any


class Conta:
    def __init__(self, titular: str, senha: str) -> None:
        self.titular: str = titular
        self.senha: str = hashlib.sha256(senha.encode()).hexdigest()
        self.arquivo_historico: list[dict[str, Any]] = (
            f'historico{self.titular.lower().replace(" ", "_")}.json'
        )
        self.__saldo: float = 0.0
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


def main():
    banco = Banco()

    try:
        senha = input('Digite sua senha: ')
        nome = str(input('Digite o nome do titular da conta: '))
        sucesso, conta = banco.verificar_se_conta_certa(nome, senha)
    except ValueError:
        print(
            'Por favor, digite o nome (um texto) no campo de digitar o nome do titular, não um número!!!'
        )
        return

    if sucesso:
        while True:
            fazer_oque = input(
                'Você deseja [D]epositar um valor, [S]acar um valor, [V]er o seu saldo ou ver seu [H]istórico? '
            ).upper()

            match fazer_oque:
                case 'D':
                    try:
                        valor = int(input('Digite um valor para depositar: '))
                        conta.depositar(valor)
                    except ValueError:
                        print(
                            'Digite um valor (um número) para depositar na sua conta!!!'
                        )
