#estrutura de decisão

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua primeira nota: "))

media = (n1 + n2) / 2

print(f"Sua média é: {media}")
if media >= 7:
    print("Você atingiu a média")

else:
    print("Você não atingiu a média")