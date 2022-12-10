from carro import Carro

def menu():
    print('Relampago Marquinhos Ltda.\n')

    print('='*5, 'Carro 1', '='*5)
    carro1 = Carro(str(input('Qual é a Marca? ')), str(input('Qual é o Modelo? ')), str(input('Qual é a Cor? ')), str(input('Qual é a categoria? ')))
    print(carro1)

    print('='*5, 'Carro 2', '='*5)
    carro2 = Carro(str(input('Qual é a Marca? ')), str(input('Qual é o Modelo? ')), str(input('Qual é a Cor? ')), str(input('Qual é a categoria? ')))
    print(carro2)

menu()
