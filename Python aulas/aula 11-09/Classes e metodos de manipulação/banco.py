class Banco:
    #metodo contendo informações das contas
    def __init__(self, titular, numero, saldo, limite) -> None:
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'O titular {self.titular}, tem a conta {self.numero}, com o saldo total de R${self.saldo}')
    
    def depositar(self, valor):
        self.saldo += valor
        return valor
    
    def sacar(self, valor):
        self.saldo -= valor
        return valor
    
    def transferir(self, valor, origem, destino):
        origem.sacar(valor)
        destino.depositar(valor)
