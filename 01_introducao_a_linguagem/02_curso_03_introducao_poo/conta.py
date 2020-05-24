from decimal import *

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero     = numero
        self.__titular    = titular
        self.__saldo      = saldo
        self.__limite     = limite
    
    def emitir_extrato(self):
        print(f"O saldo da conta {self.__numero} em nome de {self.__titular} é de R$ {Decimal(self.__saldo).quantize(Decimal('.01'))}")
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor_saque):
        limite_disponivel = self.__saldo + self.__limite
        return valor_saque <= limite_disponivel
    
    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f"O valor de R$ {Decimal(valor).quantize(Decimal('.01'))} ultrapassou o limite disponível.")
    
    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
    
    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}