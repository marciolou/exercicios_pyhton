nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

total = (nota1+nota2) / 2

print('='*5, 'RESULTADO FINAL', '='*5, '\n\nSua primeira nota é: {}\nSua segunda nota é: {}\nSua média é: {}'.format(nota1, nota2, total))

if total > 7:
    print("Você está acima da média")
elif total == 7:
    print('Você está na média')
elif total > 5 < 7:
    print('Você pode solicitar a recuperação')
elif total >= 4 == 5:
    print('Você deve procurar o professor')
else:
    print('Você não atingiu a média')