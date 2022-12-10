def cadastro():
    pessoas = {}
    pessoas['nome'] = str(input('Digite seu nome: '))
    pessoas['nascimento'] = int(input('Digite sua data de nascimento: '))
    pessoas['clt'] = int(input('Digite sua CLT: '))
    if pessoas['clt'] != 0:
        pessoas['contratacao'] = int(input('Digite o ano da sua primeira contratação: '))
        pessoas['salario'] = float(input('Digite sua salario: '))
        print(pessoas)
    else:
        print(pessoas)

cadastro()