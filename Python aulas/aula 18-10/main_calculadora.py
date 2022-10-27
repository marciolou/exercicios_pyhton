from controller import adicao, sub, multi, div

def menu():
    print('*'*25, 'Menu', '*'*25)

    cond = 'sim'
    while cond == 'sim':
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite um numero: '))

        opcao = input('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n operação:>')

        match opcao:
            case '1':
                print(f'O resultado da soma é {adicao(n1,n2)}')
            case '2':
                print(f'O resultado da subtração é {sub(n1,n2)}')
            case '3':
                print(f'O resultado da multiplicação é {multi(n1,n2)}')
            case '4':
                print(f'O resultado da divisão é {div(n1,n2)}')
            case _:
                print('Digite uma opção valida!')

        cond = str(input('Deseja continuar?\nsim\nnão\n:>'))

menu()

print('Você saiu da sua aplicação!')
