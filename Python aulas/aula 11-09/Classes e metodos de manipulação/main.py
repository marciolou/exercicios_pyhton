from banco import Banco

print('$'*10, 'Banco Quero todo que é Seu', '$'*10)

cliente1 = Banco(titular = str(input('Qual é o nome do titular? ')),
numero = int(input('Qual é o número da conta? ')),
saldo = float(input('De quanto é o seu saldo? ')),
limite = float(input('De quanto é o seu limite?')))

cliente1.extrato()
