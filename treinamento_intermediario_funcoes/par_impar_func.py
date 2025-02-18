import os

os.system('cls')

def imparPar(x):
    resultado = x % 2
    if resultado == 0:
        return "par"
    return "impar"
    

def entrada(mensagem):
    while True:
        try:
            msg = int(input(mensagem))
            return msg
        except ValueError:
            print("Por favor insira um número inteiro")
            break


num = entrada("Insira um número para verificação: ")

print(imparPar(num))