def alunos():
    nome = str(input('Digite seu nome: '))
    n1 = float(input('Digite sua primeira nota: '))
    n2 = float(input('Digite sua segunda nota: '))
    n3 = float(input('Digite sua terceira nota: '))
    media = (n1 + n2 + n3) / 3
    if media >= 7:
        print(f'{nome}, você teve as notas {n1}, {n2}, {n3} e sua média é {media}, com isso você esta aprovado')
    else:
        print(f'{nome}, você teve as notas {n1}, {n2}, {n3} e sua média é {media}, com isso você esta reprovado')

alunos()