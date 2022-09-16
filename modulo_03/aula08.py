from time import sleep

lista_notas = []
lista_historico_notas = []
lista_historico_media = []
nome = str(input('Digite seu nome: '))
sobreNome = str(input('Digite seu sobrenome: '))
idade = int(input('Digite sua idade: '))

situacao = 'Reprovado'

while situacao == 'Reprovado':
    for lista in range(0, 4):
        nota = int(input('Digite sua nota: '))
        lista_notas.append(nota)
    
    media = sum(lista_notas) / len(lista_notas)

    if media >= 7:
        sleep(1)
        situacao = 'Aprovado'
        lista_historico_notas.append(lista_notas)
        lista_historico_media.append(media)
    else:
        situacao = 'Reprovado'
        
    dicionario = {'Nome': nome, 'Sobrenome': sobreNome, 'Idade': idade}
    print(f'Suas notas são {lista_notas} e sua média é {media}, Você está {situacao}')
    
    if situacao == 'Reprovado':
        lista_historico_notas.append(lista_notas)
        lista_historico_media.append(media) 
        
    lista_notas = []    

print(f'Nome:{nome} {sobreNome}\nIdade: {idade} anos')     

for notas in lista_historico_notas:
    print(f'Notas: {notas}')

for med in lista_historico_media:
    print(f'Media: {med}')