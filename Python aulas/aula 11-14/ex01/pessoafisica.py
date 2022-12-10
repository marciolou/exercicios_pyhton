from conta import Conta
class PessoaFisica(Conta):
    __segundo_titular = ''
    def __init__(self, titular, cpf, saldo_inicial) -> None:
        super().__init__(8574, 'Conta Corrente')
        self.titular = titular
        self.cpf = cpf
        self.saldo_inicial = saldo_inicial
        print('Passando pelo construtor da classe PessoaFisica')
    
    @property
    def segundo_titular(self):
        return self.__segundo_titular
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular
    
    def __str__(self) -> str:
        return f'{super().__str__()}\nTitular da conta: {self.titular}\nCpf: {self.cpf}\nSaldo Inicial: {self.saldo_inicial}\nSegundo Titular: {self.segundo_titular}'
