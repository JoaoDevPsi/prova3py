numero_secreto = 7
tentativas = 3

while tentativas > 0:
    chute = int(input("Digite o seu chute: "))
    tentativas -= 1

    if chute == numero_secreto:
        print("Parabéns! Você acertou.")
        break
    else:
        print("Você errou! Tente novamente.")

if tentativas == 0:
    print(f"Suas tentativas acabaram. O número secreto era: {numero_secreto}")