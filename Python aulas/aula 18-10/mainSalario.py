from controller import sal

print('Digite seus quatro ultimos salarios.')
sal1 = float(input('1º R$'))
sal2 = float(input('2º R$'))
sal3 = float(input('3º R$'))
sal4 = float(input('4º R$'))

decoracao = '='*9
print(decoracao,'CALCULADORA', decoracao)

print('Seu primeiro salario é R${:.2f}.\nSeu segundo salario é R${:.2f}.\nSeu terceiro salario é R${:.2f}.\nSeu quarto salario é R${:.2f}.\nA soma deles é R${:.2f}.'.format(sal1, sal2, sal3, sal4, sal(sal1, sal2, sal3, sal4)))
