import random

numero_aleatorio = random.randint(1,100)


tentativa = None


while tentativa != numero_aleatorio:

    try:
        tentativa = int(input("Insira um número: "))

        if tentativa == numero_aleatorio:
            print(f"parabéns, o número secreto era {numero_aleatorio}. Você acertou!!!")
            break

        else: 
            print("Você errou. Tente novamente!")

    except ValueError:
        print("Por favor Insira um número inteiro")
    