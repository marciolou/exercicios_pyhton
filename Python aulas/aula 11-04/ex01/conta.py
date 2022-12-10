class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

conta = Conta(numero=7854, titular='Márcio Lourenço', saldo=1530.0, limite=0)

print(conta.titular, conta.numero, conta.saldo, conta.limite)
