from pessoa import Pessoa

print('='*10, 'Individuo 1', '='*10)
pessoa1 = Pessoa()
pessoa1.nome = str(input('Insira seu nome: '))
pessoa1.cpf = str(input('Insira seu cpf: '))
pessoa1.idade = int(input('Insra sua idade: '))

print('='*10, 'Individuo 2', '='*10)
pessoa2 = Pessoa()
pessoa2.nome = str(input('Insira seu nome: '))
pessoa2.cpf = str(input('Insira seu cpf: '))
pessoa2.idade = int(input('Insra sua idade: '))

print('='*10, 'Individuo 3', '='*10)
pessoa3 = Pessoa()
pessoa3.nome = str(input('Insira seu nome: '))
pessoa3.cpf = str(input('Insira seu cpf: '))
pessoa3.idade = int(input('Insra sua idade: '))

print(pessoa1)
print(pessoa2)
print(pessoa3)
