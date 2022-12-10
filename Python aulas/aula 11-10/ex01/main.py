from conta import Conta

print('$'*5, 'Banco Bancoso', '$'*5)

print('*'*5, 'Titular 1', '*'*5)
usuario = Conta(str(input('Digite o nome do titular: ')), int(input('Qual é o número da conta? ')), float(input('Qual é o seu saldo atual? ')), float(input('De quanto é o seu limite? ')))

print(usuario)

print('*'*5, 'Titular 2', '*'*5)

usuario2 = Conta(str(input('Digite o nome do titular: ')), int(input('Qual é o número da conta? ')), float(input('Qual é o seu saldo atual? ')), float(input('De quanto é o seu limite? ')))

print(usuario2)
