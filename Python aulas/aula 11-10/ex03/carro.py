class Carro:
    def __init__(self, marca, modelo, cor, categoria) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__categoria = categoria
    
    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        self.__marca = marca
    
    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo
    
    def get_cor(self):
        return self.__cor
    def set_cor(self, cor):
        self.__cor = cor
    
    def get_categoria(self):
        return self.__categoria
    def set_categoria(self, categoria):
        self.__categoria = categoria

    def __str__(self) -> str:
        return f'O carro da marca {self.get_marca} e modelo {self.get_modelo}, com a cor {self.get_cor} da categoria {self.get_categoria}'
