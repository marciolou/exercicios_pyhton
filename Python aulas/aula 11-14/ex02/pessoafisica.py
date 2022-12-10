from conta import Conta
class PessoaFisica(Conta):
    __segundo_titular = ''
    def __init__(self, titular, cpf, saldo_inicial) -> None:
        super().__init__(7854, 5023, 'Conta Corrente')
        self.__titular = titular
        self.__cpf = cpf
        self.__saldo_inicial = saldo_inicial
        print('Passando pelo construtor da classe PessoaFisica')

    @property
    def segundo_titular(self):
        return self.__segundo_titular
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular
    
    def __str__(self) -> str:
        return f'{super().__str__()}\nTitular: {self.__titular}\nCPF: {self.__cpf}\nSaldo Inicial: {self.__saldo_inicial}\nSegundo Titular: {self.segundo_titular}'
