import random

t1 = str(input("Digite um número: "))
t2 = str(input("Digite um número: "))
t3 = str(input("Digite um número: "))
t4 = str(input("Digite um número: "))

lista = [t1, t2, t3, t4]

sorteio = random.choice(lista)

print('='*5,"SORTEIO PREMIADO",'='*5,f"\n\nO número sorteado foi: {sorteio}")