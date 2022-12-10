from pessoa import Pessoa

print('='*5, 'Registro 1', '='*5)

pessoa1 = Pessoa(str(input('Digite seu nome: ')), str(input('Digite seu CPF: ')), int(input('Digite a sua idade: ')), float(input('Qual é a sua altura? ')))

print(pessoa1)

print('='*5, 'Registro 2', '='*5)

pessoa2 = Pessoa(str(input('Digite seu nome: ')), str(input('Digite seu CPF: ')), int(input('Digite a sua idade: ')), float(input('Qual é a sua altura? ')))

print(pessoa2)
