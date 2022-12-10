class Carro:
    def __init__(self, marca, modelo, cor, categoria) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__categoria = categoria

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, marca):
        self.__marca = marca
    
    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
    
    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self, cor):
        self.__cor = cor
    
    @property
    def categoria(self):
        return self.__categoria
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria
    
    def __str__(self) -> str:
        return f'O Carro é da marca: {self.marca}\nModelo: {self.modelo}\nCor: {self.cor}\nCategoria: {self.categoria}'
