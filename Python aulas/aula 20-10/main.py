from controller import checkin, procurar, relatorio, checkout
from datetime import datetime

def menu():

    hora = datetime.today().strftime('%H:%M')
    saudacao = ''

    if hora > ('06:00') and hora < ('12:00'):
        saudacao = 'Bom dia!'
    elif hora > ('12:00') and hora < ('18:00'):
        saudacao = 'Boa tarde!'
    else: 
        saudacao = 'Boa noite!'
    
    while True:
        print('{}, são exatamente {}.\nHOTEL DO SATANAS!'.format(saudacao, hora))
        opcao = int(input('O que você deseja fazer?\n1-> Fazer Check-in\n2-> Relatório de Hospedes\n3-> Procurar Hospedes\n4-> Fazer Check-out\n5-> Finalizar Atendimento\n:> '))
        match opcao:
            case 1:
                cliente = {}
                cliente['nome'] = str(input('Digite seu nome: '))
                cliente['sobrenome'] = str(input('Digite seu sobrenome:'))
                cliente['idade'] = int(input('Digite sua idade: '))
                checkin(cliente)
            case 2:
                relatorio()
            case 3:
                achar=str(input('Quem deseja procurar? '))
                procurar(achar)
            case 4:
                remover=str(input('Quem você deseja remover? '))
                checkout(remover)
        
menu()
