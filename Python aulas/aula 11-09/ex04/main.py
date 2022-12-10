from animal import Animal

print('$'*10, 'Animal 1', '$'*10)
animal1 = Animal()
animal1.especie = str(input('Qual é a espécie do animal? '))
animal1.cor = str(input('Qual é a cor do animal? '))
animal1.raca = str(input('Qual é a raça do animal? '))

print('$'*10, 'Animal 2', '$'*10)
animal2 = Animal()
animal2.especie = str(input('Qual é a espécie do animal? '))
animal2.cor = str(input('Qual é a cor do animal? '))
animal2.raca = str(input('Qual é a raça do animal? '))

print('$'*10, 'Animal 3', '$'*10)
animal3 = Animal()
animal3.especie = str(input('Qual é a espécie do animal? '))
animal3.cor = str(input('Qual é a cor do animal? '))
animal3.raca = str(input('Qual é a raça do animal? '))

print(animal1)
print(animal2)
print(animal3)
