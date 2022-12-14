from model.pessoafisica import PessoaFisica

def creat_psf(conta):
    contas = open('pessoafisica.txt', 'w')
    contas.write(str(conta) + '\n')
    contas.close

def read_psf():
    lista_contas = []
    contas = open('pessoafisica.txt', 'r')

    for conta in contas:
        conta = conta.strip()
        conta_objeto = conta.split()
        print(conta_objeto)
        
        pessoaFisica = PessoaFisica()

        pessoaFisica.agencia = conta_objeto[0]
        pessoaFisica.numero_agencia = conta_objeto[1]
        
        pessoaFisica.titular = conta_objeto[2]
        pessoaFisica.cpf = conta_objeto[3]
        pessoaFisica.saldo_inicial = conta_objeto[4]
        pessoaFisica.segundo_titular = conta_objeto[5]

        lista_contas.append(pessoaFisica)
        contas.close
    return lista_contas
