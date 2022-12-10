from carro import Carro

print('*'*10, 'CARRO 01', '*'*10)
carro1 = Carro()
carro1.marca = str(input('Qual é a marca do carro? '))
carro1.modelo = str(input('Qual é o modelo do carro? '))
carro1.valor = int(input('Qual é o ano do carro? '))

print('*'*10, 'CARRO 02', '*'*10)
carro2 = Carro()
carro2.marca = str(input('Qual é a marca do carro? '))
carro2.modelo = str(input('Qual é o modelo do carro? '))
carro2.valor = int(input('Qual é o ano do carro? '))

print('*'*10, 'CARRO 03', '*'*10)
carro3 = Carro()
carro3.marca = str(input('Qual é a marca do carro? '))
carro3.modelo = str(input('Qual é o modelo do carro? '))
carro3.valor = int(input('Qual é o ano do carro? '))

print(carro1)
print(carro2)
print(carro3)
