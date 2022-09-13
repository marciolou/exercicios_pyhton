salario1 = float(input("Digite seu salario: "))
salario2 = float(input("Digite seu salario: "))
salario3 = float(input("Digite seu salario: "))
salario4 = float(input("Digite seu salario: "))
total = salario1+salario2+salario3+salario4

print("="*5, "Calculadora", "="*5)
print("Primeiro salario {:.2f}\nSegundo salario {:.2f}\nTerceiro salario {:.2f}\nQuarto salario {:.2f}\nA soma de tudo é {:.2f}".format(salario1, salario2, salario3, salario4, total))