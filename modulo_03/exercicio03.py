'''
Crie uma variável do tipo inteiro solicitando dados.
Crie uma variável recebendo o conceito de polimorfismo com o sinal de igual.
Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string cabeçalho adicione quebra de linha, ao final.
Crie um laco de repetição que execute o índice de contagem crescente até o número digitado pelo usuário.
Crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois do string utilize como rodapé.
'''
#Variável Inteira
num = int(input("Digite um número: "))

#Variável de Polimorfismo
var = "="*20

#Função de impressão do cabeçalho
print(f"\n {var} CABEÇALHO {var} \n")

#Laço de Repetição
for n in range(0, num + 1):
    print(n)

#Função de impressão do rodapé
print(f"\n {var} RODAPÉ {var} \n")