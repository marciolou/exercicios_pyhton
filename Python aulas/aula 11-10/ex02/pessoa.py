class Pessoa:
    def __init__(self, nome, cpf, idade, altura) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__altura = altura

    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome

    def get_cpf(self):
        return self.__cpf
    def set_cpf(self, cpf):
        self.__cpf = cpf
    
    def get_idade(self):
        return self.__idade
    def set_idade(self, idade):
        self.__idade = idade
    
    def get_altura(self):
        return self.__altura
    def set_altura(self, altura):
        self.__altura = altura
    
    def __str__(self) -> str:
        return f'Nome: {self.get_nome()}, seu CPF {self.get_cpf()}, sua idade é {self.get_idade()} e altura {self.get_altura()}'
