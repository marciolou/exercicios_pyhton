class Pessoa:
    nome = ''
    cpf = 0
    idade = 0
    def __str__(self) -> str:
        return f'{self.nome} - {self.cpf} - {self.idade}'
