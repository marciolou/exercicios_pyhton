from conta import Conta
from controler import create, read

def menu():
    conta = Conta()
    conta.titular = str(input('Digite seu nome: '))
    conta.numero = int(input('Digite o número da conta: '))
    conta.saldo = float(input('Digite o saldo inicial: '))
    create(conta)
    
    lista_contas = read()

    for c in lista_contas:
        print(c)

menu()
