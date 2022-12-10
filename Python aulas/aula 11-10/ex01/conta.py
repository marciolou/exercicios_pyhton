class Conta:
    def __init__(self, titular, numero, saldo, limite) -> None:
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite

    def get_titular(self):
        return self.__titular
    def set_titular(self, titular):
        self.__titular = titular

    def get_numero(self):
        return self.__numero
    def set_numero(self, numero):
        self.__numero = numero
    
    def get_saldo(self):
        return self.__saldo
    def set_saldo(self, saldo):
        self.__saldo = saldo
    
    def get_limite(self):
        return self.__limite
    def set_limite(self, limite):
        self.__limite = limite
    
    def __str__(self) -> str:
        return f'Nome do titular: {self.get_titular()}, número da sua conta {self.get_numero()}, seu saldo R${self.get_saldo()} e limite e de R${self.get_limite()}'
