from random import shuffle

t1 = str(input("Digite o nome do grupo: "))
t2 = str(input("Digite o nome do grupo: "))
t3 = str(input("Digite o nome do grupo: "))
t4 = str(input("Digite o nome do grupo: "))

lista = [t1, t2, t3, t4]

shuffle(lista)

print('='*5,"ORDEM DOS GRUPOS",'='*5,"\n\nA ordem dos grupos é: {}".format(lista))