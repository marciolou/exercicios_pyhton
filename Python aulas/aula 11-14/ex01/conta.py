class Conta:
    def __init__(self, numero, tipo) -> None:
        self.numero = numero
        self.tipo = tipo
        print('Passando pelo construtor da classe Conta')
    
    def __str__(self) -> str:
        return f'Número da conta: {self.tipo}\nTipo de conta: {self.numero}'
