from time import sleep

lista_notas = []

nome = str(input('Digite seu nome: '))
sobrenome = str(input('Digite seu sonbrenome: '))
idade = int(input('Digite sua idade: '))

while lista_notas == "Reprovado":

    for lista in range(0 ,2):
        nota = int(input('Digite sua nota: '))
        lista_notas.append(nota)

    media = sum(lista_notas) / len(lista_notas)

    if media >= 7:
        for i in range(0, 2):
            sleep(2)
            print("*")
        situacao = "Aprovado"
    else:
        print("Reprovado")

    dic_alunos = {"Nome": nome, "Sobrenome": sobrenome, "Idade": idade, "Situação": situacao}
    print(f'{dic_alunos["Nome"]} - {dic_alunos["Sobrenome"]} - {dic_alunos["Idade"]} - {dic_alunos["Situação"]}')

print("Saiu")