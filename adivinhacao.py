import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhacao!")
    print("*********************************")

    numero_secreto = random.randrange(1, 100 + 1)
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Define o nivel: "))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print(f"Tentativa {rodada} / {total_tentativas}")
        chute = int(input("Digite um numero entre 1 e 100: "))
        print("Você digitou ", chute)

        if chute < 1 or chute > 100:
            print("Você deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print(f"Você acertou e fez {pontos} pontos")
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior que o numero secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

            if rodada == total_tentativas:
                print(f"O numero secreto era {numero_secreto}. Voce fez {pontos} pontos")

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
