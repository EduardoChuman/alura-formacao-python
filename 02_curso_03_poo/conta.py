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
    
    def sacar(self, valor):
        self.__saldo -= valor
    
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