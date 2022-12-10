from conta import Conta
class PessoaJuridica(Conta):
    __segundo_titular = ''
    def __init__(self, titular, cnpj, saldo_inicial) -> None:
        super().__init__(9865, 'Conta Poupança')
        self.titular = titular
        self.cnpj = cnpj
        self.saldo_inicial = saldo_inicial
        print('Passando pelo construtor da classe PessoaJuridica')
    
    @property
    def segundo_titular(self):
        return self.__segundo_titular
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular
    
    def __str__(self) -> str:
        return f'{super().__str__()}\nTitular da conta: {self.titular}\nCNPJ: {self.cnpj}\nSaldo Inicial: {self.saldo_inicial}\nSegundo Titular: {self.segundo_titular}'
