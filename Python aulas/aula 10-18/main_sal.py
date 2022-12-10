from unittest import result
from controller import sal

def menu():
    print('='*15, 'CALCULADORA DE SALARIO', '='*15, '\n')
    var = 'sim'
    while var == 'sim':
        n1 = float(print('Digite seu primeiro salario: '))
        n2 = float(print('Digite seu segundo salario: '))
        n3 = float(print('Digite seu terceiro salario: '))
        n4 = float(print('Digite seu quarto salario: '))

        resultado = sal(n1, n2, n3, n4)
        print('A soma dos salarios é {:.2f}'.format(resultado))

        var = input('Você deseja continuar? \nsim \nnão\n:>')

menu()
print('Você saiu do programa')
