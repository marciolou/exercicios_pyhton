from random import choice

n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
n4 = str(input('Digite um nome: '))

lista = [n1, n2, n3, n4]

sorteio = choice(lista)

print('='*5, 'RESULTADO DO SORTEIO', '='*5, f'\n\nO nome sorteado foi: {sorteio}')

if sorteio == n1:
    print('Foi o primeiro nome digitado')
elif sorteio == n2:
    print('Foi o segundo nome digitado')
elif sorteio == n3:
    print('Foi o terceiro nome digitado')
else:
    print('Foi o quarto nome digitado')