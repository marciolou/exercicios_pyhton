from model.pessoafisica import PessoaFisica
from model.pessoajuridica import PessoaJuridica
from controller.fisico import creat_psf, read_psf
from controller.juridico import creat_pj, read_pj

def menu():
    menu = 1

    while (menu != 0):
        print('='*10, 'Quero-Tudo-Que-e-Seu', '='*10)
        print('Qual é a opção desejada?')
        menu_inicial = int(input('1 - Pessoa Fisica\n2 - Pessoa Juridica\n3 - Sair do Programa\n:> '))

        match menu_inicial:
            case 1:
                print('Qual é a opção desejada?')
                menu = int(input('1 - Criar Pessoa Fisica\n2 - Listar\n:> '))

                match menu:
                    case 1:
                        pf = PessoaFisica()
                        pf.titular = str(input('Digite o nome do titular: '))
                        pf.cpf = str(input('Digite o seu CPF: '))
                        pf.saldo_inicial = float(input('Qual é o seu saldo inicial? '))

                        cond = str(input('Deseja cadastrar algum segundo titular? ')).upper()
                        if cond == 'SIM':
                            pf.segundo_titular = str(input('Qual é o nome do segundo titular? '))
                        
                        creat_psf(pf)
                    
                    case 2:
                        read_psf()
            
            case 2:
                print('Qual é a opção desejada?')
                menu = int(input('1 - Criar Pessoa Juridica\n2 - Listar\n:> '))

                match menu:
                    case 1:
                        pj = PessoaJuridica()
                        pj.titular = str(input('Digite o nome do titular: '))
                        pj.cnpj = str(input('Digite o seu CNPJ: '))
                        pj.saldo_inicial = float(input('Qual é o seu saldo inicial? '))

                        cond = str(input('Deseja cadastrar algum segundo titular? ')).upper()
                        if cond == 'SIM':
                            pj.segundo_titular = str(input('Qual é o nome do segundo titular? '))
                        
                        creat_pj(pj)
                    
                    case 2:
                        read_pj()
            
            case 3:
                break
            case _:
                print('Opção Invalida!!')
