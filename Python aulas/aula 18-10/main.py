from controller import adicao, sub, multi, div

decoracao = '='*7
print(f'{decoracao} CALCULADORA {decoracao}')

while True:
    opcaomenu = int(input('''O que você deseja fazer?
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
5 - Sair
Qual opção? '''))
    if opcaomenu == 1:
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite outro numero: '))
        print(f'A soma é {adicao(n1, n2)}')
    elif opcaomenu == 2:
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite outro numero: '))
        print(f'A subtração é {sub(n1, n2)}')
    elif opcaomenu == 3:
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite outro numero: '))
        print(f'A multiplicação é {multi(n1, n2)}')
    elif opcaomenu == 4:
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite outro numero: '))
        print(f'A divisão é {div(n1, n2)}')
    elif opcaomenu == 5:
        print('Obrigado pro utilizar a calculadora Stark!')
        break
    else:
        print('Essa opção não é valida!')
