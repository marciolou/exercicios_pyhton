from conta import Conta

def create(conta):
    contas = open('arquivo.txt', 'a')
    contas.write(str(conta)+ '\n')
    contas.close

def read():
    lista_contas = []
    contas = open('arquivo.txt', 'r')
    for conta in contas:
        conta = conta.strip()
        conta__objeto = conta.split(' ')
        
        conta = Conta()
        conta.titular = conta__objeto[0]
        conta.numero = conta__objeto[1]
        conta.saldo = conta__objeto[2]
        lista_contas.append(conta)
        contas.close
    return lista_contas

def update(conta_update:Conta):
    lista_contas = []
    contas = open('arquivo.txt', 'r')

    for conta in contas:
        conta_limpa = conta.strip()
        conta_objeto = conta_limpa.split()

        if conta_update.numero == int(conta_objeto[1]):
            lista_contas.append(str(conta_objeto) + '\n')
        else:
            lista_contas.append(conta)
    
    contas.close()
    contas = open('arquivo.txt', 'r')
    contas.writelines(lista_contas)
    contas.close()

def delete(numero_conta:Conta):
    lista_contas = []
    contas = open('arquivo.txt', 'r')

    for conta in contas:
        conta_limpa = conta.strip()
        conta_objeto = conta_limpa.split()

        if numero_conta.numero == int(conta_objeto[1]):
            lista_contas.append(str(conta_objeto) + '\n')
        else:
            lista_contas.append(conta)
