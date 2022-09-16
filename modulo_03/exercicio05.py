'''
Usando o conceito de importação otimizada  importe a biblioteca que tem a capacidade de gerar um delay na impressão.

Crie uma variável recebendo o conceito de polimorfismo com o sinal de igual.

Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string cabeçalho adicione quebra de linha, ao final.

Usando o conceito de contagem regressiva crie um laco de repeticao que exiba cada número do índice até 20, gere um delay de 2 segundos e imprima uma mensagem de Feliz dia do programador na sua aplicação console.

Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string utilize como rodapé, definindo o fim do laco de repetição.
'''
#Importando a função sleep da lib time
from time import sleep

#Variável de Polimorfismo
var = "="*20

#Função de impressão do cabeçalho
print(f"\n {var} CABEÇALHO {var} \n")

#Laço de Repetição com contagem regressiva
for indice in range(20, 0, -1):
    #Função para delay de 1seg
    sleep(1)
    #função para o indice
    print(indice)

#Função para delay de 2seg
sleep(2)
print("FELIZ DIA DO PROGRAMADOR")

#Função de impressão do rodapé
print(f"\n {var} RODAPÉ {var} \n")