class Carro:
    marca = ''
    modelo = ''
    valor = 0
    def __str__(self) -> str:
        return f'{self.marca} - {self.modelo} - {self.valor}'
