def checkin(cliente):
    with open('hotel.txt', 'a') as arquivo:
        arquivo.write(str(cliente)+'\n')
    arquivo.close()

def relatorio():
    ler = open('hotel.txt', 'r')
    print(ler.read())

def procurar(achar):
    indice = 0
    flag = 0
    arquivo = open('hotel.txt', 'r')

    for linha in arquivo:
        indice += 1
        if achar == eval(linha)['nome']:
            chave = indice
            flag = 1
    if flag == 0:
        print('Não encontrado')
    else:
        print(f'{achar} encontrado!')
    arquivo.close()

def checkout(remover):
    index = 0
    flag = 0
    arquivo = open('hotel.txt', 'r')

    for linha in arquivo:
        index += 1
        if remover == eval(linha)['nome']:
            chave = index
            flag = 1
    arquivo.close()
    if flag == 0:
        print('Cliente não encontrado')
    else:
        try:
            with open('hotel.txt', 'r') as fr:
                linha = fr.readlines()
                ptr = 1
                with open('hotel.txt', 'r') as fw:
                    for linha in arquivo:
                        print('Deletado')
        except:
            print('Opa, deu algum erro')
