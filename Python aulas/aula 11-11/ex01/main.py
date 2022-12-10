from animal import Animal

def menu():
    print('Animais Sinistros e Onde Habitam\n')

    print('='*5, 'Animal Sinistro 1', '='*5)
    animal1 = Animal(str(input('Qual é a espécie? ')), str(input('Qual é a raça? ')), str(input('Qual é a porte? ')), str(input('Qual é a cor? ')))
    print(animal1)

    print('='*5, 'Animal Sinistro 2', '='*5)
    animal2 = Animal(str(input('Qual é a espécie? ')), str(input('Qual é a raça? ')), str(input('Qual é a porte? ')), str(input('Qual é a cor? ')))
    print(animal2)

menu()
