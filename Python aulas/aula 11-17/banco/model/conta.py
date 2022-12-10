class Conta():
    __agencia = 'Passo Manso'
    __numero_agencia = '5127'

    @property
    def agencia(self):
        return self.__agencia
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia
    
    @property
    def numero_agencia(self):
        return self.__numero_agencia
    @numero_agencia.setter
    def numero_agencia(self, numero_agencia):
        self.__numero_agencia = numero_agencia
    
    def __str__(self) -> str:
        return f'{self.agencia}; {self.numero_agencia};'
