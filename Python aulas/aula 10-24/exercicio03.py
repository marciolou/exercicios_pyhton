lista = []

def pessoas():
    opcao = 'S'
    while opcao == 'S':
        dici = {}
        dici['nome'] = str(input('Digite seu nome: ')).strip()
        dici['sexo'] = str(input('Digite seu genero: ')).strip().upper()
        dici['idade'] = int(input('Digite sua idade: '))
        lista.append(dici)
        opcao = str(input('Você deseja continuar ? S/N\n '))

def mostragem():
    print(f'{len(lista)} pessoas foram cadastradas.')

def media():
    soma = 0
    for cont in lista:
        soma += cont['idade']
        medi = soma / len(lista)
    print('A média de idade é {:.0f} anos'.format(medi))

def mulheres():
    total = 0
    for ind in lista:
        total += (ind['sexo'] == 'F')
    print(f'Todas as mulheres são: {total}')

def acima_media():
    soma = 0
    for cont in lista:
        soma += cont['idade']
        medi = soma / len(lista)
        idade = (cont['idade'] > medi)
    print(f'As pessoas acima da média são {idade}')


pessoas()
mostragem()
media()
mulheres()
acima_media()